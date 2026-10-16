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

  // ── ATRIBUCIÓN ENTRE DOMINIOS (15/10/2026) ───────────────────────────
  // La app vive en app.positiva.studio y tiene su PROPIA propiedad de Umami,
  // con otro website-id. Al saltar de dominio se pierde el origen y un alta
  // aparece como "directa": por eso los dos registros que llegaron desde
  // ChatGPT en sep-oct hubo que deducirlos cruzando datos a mano.
  //
  // Esto añade UTM a cada enlace que va a la app. Umami los guarda en la
  // sesión de allí, así que el evento `registro` queda atribuido solo.
  // No emite ningún evento: de eso ya se encarga [data-ev] más arriba.
  function marcaDestino() {
    // Las barras se sustituyen por guiones: así el informe de Umami muestra
    // `notas-alternativas-a-pic-time` y no `notas%2Falternativas-a-pic-time`.
    var pagina = (location.pathname.replace(/^\/|\/$/g, '') || 'home').replace(/\//g, '-');
    var enlaces = document.querySelectorAll('a[href^="https://app.positiva.studio"]');
    for (var i = 0; i < enlaces.length; i++) {
      var a = enlaces[i];
      try {
        var u = new URL(a.href);
        if (u.searchParams.has('utm_source')) continue;
        // Solo entradas a la app. NUNCA una galería (/g/) ni una solicitud
        // (/s/): son enlaces que acaban en manos del cliente del fotógrafo y
        // no se les ensucia la URL con parámetros de marketing.
        if (/^\/(g|s)\//.test(u.pathname)) continue;
        u.searchParams.set('utm_source', 'landing');
        u.searchParams.set('utm_medium', 'cta');
        u.searchParams.set('utm_campaign', pagina);
        a.href = u.toString();
      } catch (_) { /* un href raro no debe romper la página */ }
    }
  }

  window.track = track;
  window.Events = Events;
  function arranca() { bindClicks(); marcaDestino(); }
  if (document.readyState !== 'loading') arranca();
  else document.addEventListener('DOMContentLoaded', arranca);
})();
