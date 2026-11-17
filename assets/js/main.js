// Scroll reveal
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Waveform bars behind the mission section: random timing so the bars don't move in lockstep
document.querySelector('.wave').innerHTML = Array.from({ length: 48 }, () =>
  `<i style="animation-delay:-${(Math.random() * 2.4).toFixed(2)}s;animation-duration:${(1.6 + Math.random() * 1.6).toFixed(2)}s"></i>`).join('');

// Booking form → existing Flask endpoint (backend/app.py)
const form = document.getElementById('bookingForm'), statusEl = document.getElementById('status');
form.addEventListener('submit', async e => {
  e.preventDefault();
  statusEl.textContent = 'Sending…';
  const f = form.elements;
  const payload = {
    name: f.name.value, email: f.email.value,
    subject: `Booking enquiry: ${f.event.value}${f.date.value ? ' on ' + f.date.value : ''}`,
    message: f.message.value,
  };
  try {
    const res = await fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    if (res.ok) { statusEl.textContent = 'Enquiry sent. Team JI will be in touch shortly.'; form.reset(); return; }
    const out = await res.json().catch(() => null);
    if (out && out.error) { statusEl.textContent = 'Error: ' + out.error; return; }
  } catch {}
  // No backend (e.g. GitHub Pages demo): hand the enquiry to the visitor's email app instead.
  location.href = `mailto:info@jeffreyiqbal.com?subject=${encodeURIComponent(payload.subject)}&body=${encodeURIComponent(`${payload.message}\n\n${payload.name} <${payload.email}>`)}`;
  statusEl.textContent = 'Opening your email app to send this enquiry…';
});
