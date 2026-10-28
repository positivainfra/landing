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
    GALLERY_DEMO_OPENED:    'gallery_demo_opened',
    // Permanencia y profundidad (28/10/2026). Ver el bloque MEDIR LA LECTURA.
    TIEMPO_5S:              'tiempo_5s',
    TIEMPO_15S:             'tiempo_15s',
    TIEMPO_30S:             'tiempo_30s',
    TIEMPO_60S:             'tiempo_60s',
    TIEMPO_180S:            'tiempo_180s',
    SCROLL_50:              'scroll_50',
    SCROLL_90:              'scroll_90'
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

  // ── MEDIR LA LECTURA: PERMANENCIA Y PROFUNDIDAD (28/10/2026) ─────────
  //
  // POR QUÉ EXISTE ESTO. Umami calcula la duración de una visita como la
  // distancia entre su PRIMER y su ÚLTIMO impacto con sello de tiempo, y el
  // script estándar no manda latidos periódicos ni aviso al cerrar la pestaña.
  // Una visita de UNA sola página no tiene segundo punto con el que restar y
  // sale 0 s SIEMPRE, mida lo que mida el reloj de verdad. Eso convierte
  // "duración media" y "tasa de rebote" en el mismo dato contado dos veces.
  //
  // EL CASO QUE LO DECIDIÓ. El 27/10/2026 la landing tuvo 4 visitantes, 5
  // vistas, 100 % de rebote y 0 s de duración, y el informe diario lo leyó
  // como el peor día de la serie. La repetición de sesión de una de esas
  // visitas "de 0 segundos" dura 4 m 38 s con 621 acciones. El informe estaba
  // describiendo un agujero de medición, no a los visitantes.
  //
  // Y NO, `cta_flotante_visto` NO SIRVE DE SUSTITUTO, aunque lo parezca.
  // Mirando positiva.js, ese evento tiene cuatro puertas: solo se emite por
  // encima de 1001 px de ancho (`ancho.matches`), nunca en /soporte/, no
  // vuelve a emitirse en toda la sesión si alguien cierra el flotante, y exige
  // que no haya ningún otro botón de registro a la vista. Un móvil que lea la
  // página entera no dispara nada. Los dos de aquí abajo no tienen ninguna de
  // esas puertas: ni ancho mínimo, ni páginas excluidas, ni memoria de sesión.
  //
  // POR QUÉ EVENTOS SEPARADOS Y NO UNA PROPIEDAD CON LOS SEGUNDOS. La página
  // de Eventos de Umami cuenta por NOMBRE: así "de 5 visitas, 3 pasaron de
  // 15 s y 1 de 60 s" se lee de un vistazo y sin entrar a Properties. Con este
  // volumen —entre 5 y 50 visitantes al día— una media no dice nada y una
  // escalera sí.
  //
  // OJO CON LEER LA MEDIA DE UMAMI AUNQUE ESTO ESTÉ PUESTO. La escalera no hace
  // que la duración sea exacta: la CUANTIZA. "Duración media" pasa a ser "el
  // último umbral cruzado", así que una visita de 4 m 38 s registra 3 m 00 s.
  // Es una estimación por lo bajo, no una medida. Lo que hay que leer es la
  // escalera.
  //
  // POR QUÉ EL PRIMER PELDAÑO ES 5 s Y NO 15 s. Con este tráfico el rango que
  // importa está entre 0 y 15 s: el 27/10/2026, de 5 vistas solo UNA pasó de
  // 5 segundos. Y 5 s es además el filtro del listado de Replays de Umami, así
  // que los dos instrumentos se comprueban entre sí: si en páginas comerciales
  // `tiempo_5s` sale muy por encima del número de repeticiones grabadas, ese
  // exceso es tráfico no humano o de ventana estrecha. El coste conocido es que
  // un rastreador que retiene la página más de 5 s dispara `tiempo_5s` y la
  // pausa por visibilidad no protege de eso: un navegador sin interfaz se
  // declara visible.
  //
  // EL RELOJ SE PARA con la pestaña en segundo plano: una pestaña olvidada
  // media mañana no es una lectura de media mañana.
  //
  // AL DESPLEGAR ESTO, LA SERIE DE "DURACIÓN MEDIA" QUEDA PARTIDA EN DOS.
  // Comparar los días de después con los de antes es comparar dos formas de
  // medir. Hay que decirlo en el informe del día del despliegue.

  var UMBRALES = [[5, 'TIEMPO_5S'], [15, 'TIEMPO_15S'], [30, 'TIEMPO_30S'], [60, 'TIEMPO_60S'], [180, 'TIEMPO_180S']];

  function medirPermanencia() {
    var acumulado = 0;     // segundos ya contados con la pestaña a la vista
    var desde = null;      // inicio del tramo visible en curso, o null si pausado
    var i = 0;             // próximo umbral pendiente
    var timer = null;

    function segundos() {
      return acumulado + (desde === null ? 0 : (Date.now() - desde) / 1000);
    }
    function programa() {
      if (i >= UMBRALES.length || timer !== null || desde === null) return;
      timer = setTimeout(dispara, Math.max(0, (UMBRALES[i][0] - segundos()) * 1000));
    }
    function dispara() {
      timer = null;
      if (i >= UMBRALES.length) return;
      track(Events[UMBRALES[i][1]]);
      i++;
      programa();
    }
    function reanuda() {
      if (desde !== null) return;
      desde = Date.now();
      programa();
    }
    function pausa() {
      if (desde === null) return;
      acumulado = segundos();
      desde = null;
      if (timer !== null) { clearTimeout(timer); timer = null; }
    }
    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden') pausa(); else reanuda();
    });
    if (document.visibilityState !== 'hidden') reanuda();
  }

  // Profundidad de scroll. Solo se mide SI LA PÁGINA SE PUEDE DESPLAZAR: en una
  // que cabe entera en la ventana, el porcentaje visto es 100 desde el primer
  // instante y el dato no significaría nada.
  //
  // Y solo se evalúa AL HACER SCROLL, nunca en la carga: en las páginas de
  // soporte y del blog la etiqueta de /js/analytics.js va ANTES que la del
  // tracker (los dos son `defer`, así que respetan el orden del documento), de
  // modo que al arrancar `window.umami` puede no existir todavía y el evento se
  // perdería en silencio. Cuando alguien hace scroll ya ha cargado.
  function medirScroll() {
    var HITOS = [[50, 'SCROLL_50'], [90, 'SCROLL_90']];
    var i = 0, pedido = false;

    function alto() {
      var d = document.documentElement, b = document.body;
      return Math.max(d ? d.scrollHeight : 0, b ? b.scrollHeight : 0);
    }
    function mide() {
      pedido = false;
      var total = alto();
      if (total <= window.innerHeight + 100) return;   // no hay nada que recorrer
      var pct = ((window.scrollY + window.innerHeight) / total) * 100;
      while (i < HITOS.length && pct >= HITOS[i][0]) { track(Events[HITOS[i][1]]); i++; }
      if (i >= HITOS.length) window.removeEventListener('scroll', pide);
    }
    function pide() {
      if (pedido) return;
      pedido = true;
      // rAF hay que llamarlo sobre window: guardarlo en una variable suelta
      // rompe en navegadores que comprueban el receptor.
      if (window.requestAnimationFrame) window.requestAnimationFrame(mide);
      else setTimeout(mide, 150);
    }
    window.addEventListener('scroll', pide, { passive: true });
  }

  window.track = track;
  window.Events = Events;
  function arranca() { bindClicks(); marcaDestino(); medirPermanencia(); medirScroll(); }
  if (document.readyState !== 'loading') arranca();
  else document.addEventListener('DOMContentLoaded', arranca);
})();
