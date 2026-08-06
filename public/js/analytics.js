/* ──────────────────────────────────────────────────────────────
   @labbo/analytics · build ligero para la LANDING (JS plano, sin bundler)

   Esta landing es HTML estático servido por un Worker; no hay TypeScript
   ni empaquetador, así que aquí vive la versión mínima del wrapper.
   La versión completa (catálogo, propiedades, embudos) para la app está
   en /analytics como paquete portable @labbo/analytics.

   REGLA DE ORO: nunca llames a window.umami directamente desde el HTML.
   Usa siempre track() y el catálogo Events.
   ────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  // Envío de eventos. La analítica NUNCA debe romper la web: todo va en try/catch.
  function track(event, data) {
    try {
      if (typeof window === 'undefined' || !window.umami || !event) return;
      if (data && Object.keys(data).length) window.umami.track(event, data);
      else window.umami.track(event);
    } catch (_) { /* silencio deliberado */ }
  }

  // Catálogo de eventos que la LANDING puede emitir (subconjunto del paquete).
  var Events = {
    WAITLIST_SUBMITTED:     'waitlist_submitted',
    WAITLIST_INVALID_EMAIL: 'waitlist_invalid_email',
    CTA_REGISTER_CLICK:     'cta_register_click',
    COMPARISON_OPENED:      'comparison_opened',
    GALLERY_DEMO_OPENED:    'gallery_demo_opened'
  };

  // Clics declarativos: cualquier elemento con [data-ev] se registra al pulsar.
  // Propiedades opcionales con data-ev-xxx="valor"  →  { xxx: "valor" }.
  function bindClicks() {
    document.addEventListener('click', function (e) {
      var el = e.target.closest('[data-ev]');
      if (!el) return;
      var data = {};
      for (var i = 0; i < el.attributes.length; i++) {
        var a = el.attributes[i];
        if (a.name.indexOf('data-ev-') === 0) data[a.name.slice('data-ev-'.length)] = a.value;
      }
      track(el.getAttribute('data-ev'), data);
    }, { passive: true });
  }

  window.track = track;
  window.Events = Events;
  if (document.readyState !== 'loading') bindClicks();
  else document.addEventListener('DOMContentLoaded', bindClicks);
})();
