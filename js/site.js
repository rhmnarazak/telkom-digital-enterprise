/* Shared behaviour for inner pages: nav, drawer, reveal, count-up, CTA door, demo form */
(() => {
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const nav = document.querySelector('.hero > .nav');

  /* footer reuses the header logo */
  const logo = nav && nav.querySelector('.logo svg');
  if (logo) document.querySelectorAll('[data-logo]').forEach(a => a.appendChild(logo.cloneNode(true)));

  /* nav docks to the top once the page scrolls */
  if (nav) {
    const dock = () => {
      const on = scrollY > 120;
      nav.classList.toggle('stuck', on);
      document.body.classList.toggle('stuck', on);
    };
    addEventListener('scroll', dock, { passive: true }); dock();
  }

  /* mobile drawer */
  const drawer = document.getElementById('drawer');
  const menuBtn = nav && nav.querySelector('.menu');
  if (drawer && menuBtn) {
    const setMenu = open => {
      document.body.classList.toggle('menu-open', open);
      drawer.setAttribute('aria-hidden', !open);
      menuBtn.setAttribute('aria-expanded', open);
      if (open) drawer.querySelector('.drawer-close').focus();
    };
    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.addEventListener('click', () => setMenu(true));
    drawer.querySelector('.drawer-close').addEventListener('click', () => setMenu(false));
    drawer.addEventListener('click', e => { if (e.target === drawer || e.target.matches('a')) setMenu(false); });
    addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
  }

  /* count-up for figures (thousands get a separator: 6,500) */
  const fmt = (v, dec) => v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
  const count = el => {
    const to = +el.dataset.to, dec = +(el.dataset.dec || 0);
    if (still) { el.textContent = fmt(to, dec); return; }
    const t0 = performance.now(), dur = 1600;
    const tick = now => {
      const k = Math.min(1, (now - t0) / dur);
      el.textContent = fmt(to * (1 - Math.pow(1 - k, 4)), dec);
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  /* reveal on scroll */
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('on'); io.unobserve(e.target);
    e.target.querySelectorAll('.n').forEach(count);
  }), { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  /* the door opens when the CTA comes into view */
  const cta = document.querySelector('.sec.cta');
  if (cta) new IntersectionObserver(([e]) => cta.classList.toggle('on', e.isIntersecting), { threshold: .35 }).observe(cta);

  /* demo request form: inline validation, then a confirmation (no backend yet) */
  const box = document.getElementById('demo');
  if (box) {
    const form = box.querySelector('form');
    const check = el => {
      const ok = el.checkValidity() && (el.type !== 'email' || /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value.trim())) && el.value.trim() !== '';
      el.closest('.fg').classList.toggle('bad', !ok);
      el.setAttribute('aria-invalid', !ok);
      return ok;
    };
    form.querySelectorAll('input,select').forEach(el => {
      el.addEventListener('blur', () => { if (el.value) check(el); });
      el.addEventListener('input', () => { if (el.closest('.fg').classList.contains('bad')) check(el); });
      el.addEventListener('change', () => check(el));
    });
    form.addEventListener('submit', e => {
      e.preventDefault();
      const bad = [...form.querySelectorAll('input,select')].filter(el => !check(el));
      if (bad.length) { bad[0].focus(); return; }
      const btn = form.querySelector('.demo-submit');
      btn.disabled = true; btn.firstChild.textContent = 'Sending… ';
      setTimeout(() => {
        const first = form.elements.name.value.trim().split(/\s+/)[0];
        box.querySelector('.who').textContent = first ? ', ' + first : '';
        box.classList.add('sent');
      }, 700);
    });
  }
})();
