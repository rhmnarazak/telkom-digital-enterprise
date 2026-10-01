/* "How it works" tabs on capability pages: click or arrow keys switch the service */
(() => {
  const tabs = [...document.querySelectorAll('#how .tab')];
  if (!tabs.length) return;
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const select = (tab, focus) => {
    tabs.forEach(t => {
      const on = t === tab, panel = document.getElementById(t.getAttribute('aria-controls'));
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      panel.hidden = !on;
      if (on && !still) { panel.classList.remove('enter'); void panel.offsetWidth; panel.classList.add('enter'); }
    });
    if (focus) tab.focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => select(t));
    t.addEventListener('keydown', e => {
      const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (d) { e.preventDefault(); select(tabs[(i + d + tabs.length) % tabs.length], true); }
    });
  });
})();
