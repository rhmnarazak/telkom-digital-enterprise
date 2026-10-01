/* Ecosystem stack: pointing at a service lights up the shared capabilities it uses */
(() => {
  const stack = document.querySelector('.stack');
  if (!stack) return;
  const caps = [...stack.querySelectorAll('.cap')];
  const show = svc => {
    stack.classList.toggle('focus', !!svc);
    stack.querySelectorAll('.svc').forEach(s => s.classList.toggle('on', s.dataset.svc === svc));
    caps.forEach(c => c.classList.toggle('hit', !!svc && c.dataset.in.split(' ').includes(svc)));
  };
  stack.querySelectorAll('.svc').forEach(s => {
    s.addEventListener('mouseenter', () => show(s.dataset.svc));
    s.addEventListener('focus', () => show(s.dataset.svc));
    s.addEventListener('mouseleave', () => show(null));
    s.addEventListener('blur', () => show(null));
  });
})();
