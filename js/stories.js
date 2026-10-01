/* Customer stories hub: service + capability (+ industry) filters with shareable URLs,
   "I need…" paths, and "Load more" past 12 cards. Filters only exist at 6+ stories. */
(() => {
  const grid = document.querySelector('.sc-grid');
  const box = document.querySelector('.filters');
  if (!grid) return;
  const cards = [...grid.children];
  const more = document.querySelector('.more');
  const empty = document.querySelector('.sc-empty');
  const PAGE = 12;
  let shown = PAGE;

  const state = { service: '', capability: '', industry: '' };
  const params = new URLSearchParams(location.search);
  Object.keys(state).forEach(k => { state[k] = params.get(k) || ''; });

  const childCaps = (() => {
    try { return JSON.parse(document.getElementById('child-caps').textContent); } catch { return {}; }
  })();

  const matches = c => {
    if (state.service && !c.dataset.services.split(' ').includes(state.service)) return false;
    if (state.capability) {
      const all = (c.dataset.caps + '|' + c.dataset.shared).split('|');
      if (!all.includes(state.capability)) return false;
    }
    if (state.industry && c.dataset.industry !== state.industry) return false;
    return true;
  };

  const render = () => {
    const hits = cards.filter(matches);
    cards.forEach(c => { c.hidden = true; });
    hits.slice(0, shown).forEach(c => { c.hidden = false; c.classList.add('on'); });
    if (more) more.hidden = hits.length <= shown;
    if (empty) empty.hidden = hits.length > 0;
    if (!box) return;
    box.querySelector('.fcount b').textContent = hits.length;
    box.querySelector('.fcount').lastChild.textContent = hits.length === 1 ? ' story' : ' stories';
    box.querySelectorAll('.fchip[data-f="service"]').forEach(b => b.setAttribute('aria-pressed', b.dataset.v === state.service));
    const sel = box.querySelector('select[data-f="capability"]');
    const group = sel.querySelector('optgroup[label="In this service"]');
    const kids = childCaps[state.service] || [];
    group.innerHTML = kids.map(([c, n]) => `<option value="${c}">${c} (${n})</option>`).join('');
    group.hidden = !kids.length;
    sel.value = state.capability;
    const ind = box.querySelector('select[data-f="industry"]');
    if (ind) ind.value = state.industry;
    const q = new URLSearchParams(Object.entries(state).filter(([, v]) => v));
    history.replaceState(null, '', q.toString() ? '?' + q : location.pathname);
  };

  if (box) {
    box.addEventListener('click', e => {
      const b = e.target.closest('.fchip');
      if (!b) return;
      state.service = b.dataset.v;
      state.capability = '';
      shown = PAGE; render();
    });
    box.addEventListener('change', e => {
      const s = e.target.closest('select[data-f]');
      if (!s) return;
      state[s.dataset.f] = s.value;
      shown = PAGE; render();
    });
  }
  document.querySelectorAll('.path[data-path]').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    state.service = a.dataset.path; state.capability = ''; shown = PAGE; render();
    document.getElementById('stories').scrollIntoView({ behavior: 'smooth' });
  }));
  document.querySelector('[data-reset]')?.addEventListener('click', () => {
    Object.keys(state).forEach(k => { state[k] = ''; }); shown = PAGE; render();
  });
  more?.addEventListener('click', () => { shown += PAGE; render(); });

  if (box || cards.length > PAGE) render();
})();
