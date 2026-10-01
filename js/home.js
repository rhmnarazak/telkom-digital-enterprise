/* Home only: hero mosaic (states + parallax) and the live Workspace preview.
   Shared behaviour (nav, drawer, reveal, count-up, CTA door, demo form) lives in js/site.js */
(() => {
  const hero = document.getElementById('hero');
  const mobile = matchMedia('(max-width: 640px)');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const INTERVAL = 3200;
  let i = 0, timer;

  // Desktop: A ⇄ B.  Mobile: frame 1 → frame 2 → frame 3 → frame 1 …
  const steps = () => mobile.matches ? ['a', 'b', 'c'] : ['a', 'b'];
  const next = () => { const s = steps(); i = (i + 1) % s.length; hero.dataset.state = s[i]; };
  const loop = () => { clearInterval(timer); if (!reduce) timer = setInterval(next, INTERVAL); };

  setTimeout(() => { if (!reduce) next(); loop(); }, 2000);

  document.querySelectorAll('.mosaic').forEach(m => {
    m.addEventListener('click', () => { next(); loop(); });
    m.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); next(); loop(); }
    });
  });

  mobile.addEventListener('change', () => { i = 0; hero.dataset.state = 'a'; loop(); });
  document.addEventListener('visibilitychange', () => document.hidden ? clearInterval(timer) : loop());

  // Parallax: pointer on desktop, device tilt on phones
  if (!reduce) {
    let raf;
    const setP = (x, y) => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        hero.style.setProperty('--mx', Math.max(-1, Math.min(1, x)).toFixed(3));
        hero.style.setProperty('--my', Math.max(-1, Math.min(1, y)).toFixed(3));
      });
    };
    addEventListener('pointermove', e => {
      if (e.pointerType !== 'mouse') return;
      setP(e.clientX / innerWidth * 2 - 1, e.clientY / innerHeight * 2 - 1);
    });
    document.addEventListener('mouseleave', () => setP(0, 0));
    addEventListener('deviceorientation', e => {
      if (e.gamma == null) return;
      setP(e.gamma / 25, (e.beta - 45) / 25);
    });
  }
})();

/* Platform preview: scale-to-fit, scroll tilt, live interactions and a guided demo */
(() => {
  const view = document.getElementById('ws-view');
  if (!view) return;
  const frame = document.getElementById('ws-frame');
  const ws = document.getElementById('ws');
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = s => ws.querySelector(s), $$ = s => [...ws.querySelectorAll(s)];
  const wait = ms => new Promise(r => setTimeout(r, ms));

  /* fit the 1440×800 workspace to the frame */
  const sizer = view.querySelector('.ws-sizer');
  let scale = 1, pan = false;
  const fit = () => {
    pan = view.clientWidth < 600;
    scale = pan ? .5 : view.clientWidth / 1440;
    ws.style.setProperty('--s', scale);
    view.style.height = pan ? 800 * scale + 'px' : '';
    sizer.style.width = pan ? 1440 * scale + 'px' : '';
  };
  new ResizeObserver(fit).observe(view); fit();

  /* frame tilts back and settles as it scrolls into view */
  if (!still) {
    let raf;
    const tilt = () => {
      raf = 0;
      const r = frame.getBoundingClientRect(), vh = innerHeight;
      const p = Math.max(0, Math.min(1, (r.top - vh * .18) / (vh * .7)));
      frame.style.setProperty('--p', p.toFixed(3));
    };
    addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(tilt); }, { passive: true });
    tilt();
  }

  /* ---------- interactions (work for the visitor and the guided cursor) ---------- */
  const toastEl = $('#ws-toast');
  let toastT;
  const toast = msg => {
    toastEl.textContent = msg; toastEl.classList.add('show');
    clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove('show'), 2200);
  };

  $$('.ws-mi').forEach(b => b.addEventListener('click', () => {
    $$('.ws-mi').forEach(x => x.classList.toggle('on', x === b));
  }));
  $$('.ws-qa-item').forEach(b => b.addEventListener('click', () => {
    b.classList.add('press'); setTimeout(() => b.classList.remove('press'), 180);
    toast(b.dataset.toast);
  }));

  const track = $('#ws-track');
  let slide = 0;
  const slideApps = dir => {
    slide = Math.max(0, Math.min(3, slide + dir));
    track.style.transform = `translateX(${-slide * 176}px)`;
  };
  $('.ws-apps-lead .ws-link').addEventListener('click', () => slideApps(slide >= 3 ? -3 : 1));

  const chat = $('#ws-chat'), input = $('#ws-input .txt'), answer = $('#ws-answer'), answerBody = answer.querySelector('.ws-answer-body');
  const PLACEHOLDER = 'Tanya Telkom Digital...';
  const setInput = t => { input.textContent = t || PLACEHOLDER; $('#ws-input').classList.toggle('typed', !!t); chat.classList.toggle('has-text', !!t); };
  const ask = async q => {
    const send = $('#ws-send');
    send.classList.add('press'); setTimeout(() => send.classList.remove('press'), 180);
    setInput(''); chat.classList.remove('focus');
    answerBody.innerHTML = '<span class="dots"><span></span><span></span><span></span></span>';
    answer.classList.add('show');
    await wait(1300);
    answerBody.innerHTML = q.a;
    await wait(3200);
    answer.classList.remove('show');
  };
  const QA = [
    { q: 'Ringkas laporan penjualan Agustus', a: 'Penjualan Agustus <strong>naik 12%</strong> dari Juli, didorong 3 produk teratas di Jawa Timur.' },
    { q: 'Apa aturan perjalanan dinas terbaru?', a: 'Draft peraturan terbaru membatasi uang harian <strong>maks. Rp750.000</strong> dan wajib lapor H+3.' },
    { q: 'CCTV mana yang perlu perbaikan?', a: '<strong>2 kamera</strong> offline sejak kemarin: Ruang 307 dan Lobi Timur.' }
  ];
  let qi = 0;
  $('#ws-send').addEventListener('click', () => ask(QA[qi++ % QA.length]));

  const tlist = $('#ws-tlist'), bell = $('#ws-bell'), badge = $('#ws-badge');
  let unread = 0;
  const NEW_TASKS = [
    ['task-monitor.png', 'pr-high', 'Prioritas Tinggi', 'Cek Kamera Offline Lobi Timur'],
    ['app-dim.png', 'pr-mid', 'Prioritas Sedang', 'Review Ringkasan Penjualan Agustus'],
    ['app-crm.png', 'pr-low', 'Prioritas Rendah', 'Balas Survei Kepuasan Pelanggan']
  ];
  let ni = 0;
  const addTask = () => {
    const [img, pc, pl, title] = NEW_TASKS[ni++ % NEW_TASKS.length];
    const el = document.createElement('div');
    el.className = 'ws-task new';
    el.innerHTML = `<img src="assets/workspace/${img}" alt=""><div class="ws-tmeta"><div class="ws-tline"><span class="${pc}">${pl}</span><span class="ws-chip st-todo">Belum Mulai</span></div><strong>${title}</strong></div>`;
    tlist.prepend(el);
    setTimeout(() => el.classList.remove('new'), 2600);
    while (tlist.children.length > 9) tlist.lastElementChild.remove();
    unread++; badge.textContent = unread; badge.classList.add('show');
    bell.classList.remove('ring'); void bell.offsetWidth; bell.classList.add('ring');
  };
  bell.addEventListener('click', () => { unread = 0; badge.classList.remove('show'); });
  const startTask = () => {
    const chip = tlist.querySelector('.ws-chip.st-todo');
    if (!chip) return;
    chip.classList.replace('st-todo', 'st-doing'); chip.textContent = 'Berlangsung';
    chip.classList.remove('flip'); void chip.offsetWidth; chip.classList.add('flip');
  };
  tlist.addEventListener('click', e => {
    const chip = e.target.closest('.ws-task')?.querySelector('.ws-chip');
    if (chip && chip.classList.contains('st-todo')) { chip.classList.replace('st-todo', 'st-doing'); chip.textContent = 'Berlangsung'; chip.classList.add('flip'); }
  });

  if (still) return;

  /* ---------- guided demo ---------- */
  const cursor = $('#ws-cursor');
  let userHere = false, visible = false, running = false, idleT;
  const center = el => {
    const a = ws.getBoundingClientRect(), b = el.getBoundingClientRect();
    return [(b.left - a.left + b.width / 2) / scale, (b.top - a.top + b.height / 2) / scale];
  };
  const moveTo = async (el, dx = 0, dy = 0) => {
    const [x, y] = center(el);
    if (pan) view.scrollTo({ left: (x + dx) * scale - view.clientWidth / 2, behavior: 'smooth' });
    cursor.style.setProperty('--cx', x + dx + 'px'); cursor.style.setProperty('--cy', y + dy + 'px');
    await wait(1150);
  };
  const click = async el => {
    cursor.classList.remove('click'); void cursor.offsetWidth; cursor.classList.add('click');
    el.classList.add('hot'); setTimeout(() => el.classList.remove('hot'), 400);
    el.click(); await wait(500);
  };
  const type = async text => {
    chat.classList.add('focus');
    for (let i = 1; i <= text.length; i++) { setInput(text.slice(0, i)); await wait(38 + Math.random() * 40); }
  };
  const alive = () => visible && !userHere && !document.hidden;

  const steps = [
    async () => { const b = $$('.ws-qa-item')[0]; await moveTo(b); await click(b); await wait(1400); },
    async () => { const l = $('.ws-apps-lead .ws-link'); await moveTo(l); await click(l); await wait(900); await click(l); await wait(1200); },
    async () => { const q = QA[qi % QA.length]; await moveTo($('#ws-input')); await type(q.q); await wait(350); await moveTo($('#ws-send')); cursor.classList.add('click'); qi++; await ask(q); },
    async () => { await moveTo(tlist, 0, -220); addTask(); await wait(1600); },
    async () => { const chip = tlist.querySelector('.ws-chip.st-todo'); if (chip) { await moveTo(chip); await click(chip.closest('.ws-task')); startTask(); } await wait(1400); },
    async () => { const b = $$('.ws-qa-item')[3]; await moveTo(b); await click(b); await wait(1400); if (slide) { slide = 0; track.style.transform = ''; } }
  ];
  const run = async () => {
    if (running) return;
    running = true; cursor.classList.add('show');
    let i = 0;
    while (alive()) { await steps[i++ % steps.length](); await wait(500); }
    cursor.classList.remove('show'); running = false;
  };
  const kick = () => { clearTimeout(idleT); if (alive()) idleT = setTimeout(run, 900); };

  new IntersectionObserver(([e]) => { visible = e.isIntersecting; kick(); }, { threshold: .35 }).observe(view);
  view.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') { userHere = true; view.classList.add('user'); } });
  view.addEventListener('touchstart', () => {
    userHere = true; clearTimeout(idleT);
    idleT = setTimeout(() => { userHere = false; kick(); }, 6000);
  }, { passive: true });
  view.addEventListener('pointerleave', () => { userHere = false; view.classList.remove('user'); clearTimeout(idleT); idleT = setTimeout(kick, 2500); });
  document.addEventListener('visibilitychange', kick);
})();
