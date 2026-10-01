/* Nav mega menus (Services, Capabilities): open on click, one at a time;
   close on outside click, Escape, a second click or when focus leaves */
(() => {
  const pairs = [...document.querySelectorAll('.links-btn[aria-controls]')]
    .map(btn => [btn, document.getElementById(btn.getAttribute('aria-controls'))])
    .filter(([, menu]) => menu);
  if (!pairs.length) return;

  const set = (btn, menu, open) => {
    btn.setAttribute('aria-expanded', open);
    menu.classList.toggle('open', open);
    menu.inert = !open;
  };
  const closeAll = except => pairs.forEach(([b, m]) => { if (b !== except) set(b, m, false); });
  closeAll();

  pairs.forEach(([btn, menu]) => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const open = btn.getAttribute('aria-expanded') !== 'true';
      closeAll(btn);
      set(btn, menu, open);
      /* keyboard opens (detail 0) move focus into the menu; mouse opens do not */
      if (open && e.detail === 0) menu.querySelector('a').focus({ preventScroll: true });
    });
    menu.addEventListener('focusout', e => {
      if (!menu.contains(e.relatedTarget) && e.relatedTarget !== btn) set(btn, menu, false);
    });
  });

  document.addEventListener('click', e => { if (!pairs.some(([, m]) => m.contains(e.target))) closeAll(); });
  addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    const open = pairs.find(([b]) => b.getAttribute('aria-expanded') === 'true');
    if (open) { closeAll(); open[0].focus(); }
  });
  matchMedia('(max-width: 860px)').addEventListener('change', () => closeAll());
})();
