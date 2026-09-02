# -*- coding: utf-8 -*-
# Contenido de los 3 casos de uso. Lo lee casos-build.py.

# ══════════════════════ BODAS ══════════════════════
CFGS.append({
    'slug': 'bodas',
    'nombre': 'Fotografía de bodas',
    'source': 'bodas',
    'title': 'Positiva · Galerías de boda para fotógrafos y videógrafos',
    'desc': 'Entrega la boda completa — fotos y vídeo — en una galería con tu marca y un enlace que no caduca. Momentos, favoritas para el álbum y permisos distintos para la pareja y los invitados.',
    'ogdesc': 'Las fotos, el vídeo y las lágrimas, en el mismo enlace. Galerías de boda con tu marca, para siempre.',
    'captura_h2': 'La próxima boda,<br><em>entregada como merece.</em>',
    'hero': '''<header class="heroC">
  <div class="wrap heroC-inner">
    <div>
      <p class="eyebrow">Fotografía y vídeo de boda</p>
      <h1 aria-label="Las fotos, el vídeo y las lágrimas, en el mismo enlace.">
        <span class="hl"><span style="--d:.05s">Las fotos, el vídeo</span></span>
        <span class="hl"><span style="--d:.15s">y las lágrimas,</span></span>
        <span class="hl"><span style="--d:.25s"><em>en el mismo enlace.</em></span></span>
      </h1>
      <p class="lede">
        La boda entera en una galería con tu marca: las fotos por momentos, el vídeo al lado,
        y un enlace que no caduca — la pareja con los originales, los invitados solo mirando.
        Sin cuentas, sin carpetas, sin «¿me lo pasas otra vez?».
      </p>
      <div class="hero-cta">
        <a href="#lista" class="btn btn-amber" data-ev="cta_register_click" data-ev-place="hero_bodas">Regístrate</a>
        <a href="#entrega" class="btn btn-ghost">Ver cómo se entrega</a>
      </div>
      <p class="hero-note">
        Dentro de diez años, en su aniversario,<br>
        el enlace seguirá abriendo.
      </p>
    </div>
    <div class="pila" aria-hidden="true">
      <img class="atras" src="/img/galerias/slide-3-boda-grid.jpg" alt="" width="1200" height="750" loading="eager" decoding="async">
      <img class="delante" src="/img/galerias/slide-1-boda-aitana.jpg" alt="Galería de boda real entregada con Positiva" width="1200" height="750" fetchpriority="high" decoding="async">
    </div>
  </div>
</header>''',
    'secciones': '''<!-- ══ LA ENTREGA ══ -->
<section class="dark" id="entrega">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">01</span> La entrega</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">Una boda entera,<br><em>ordenada por momentos.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        Preparativos, ceremonia, cóctel, fiesta: las fotos se agrupan en momentos con nombre,
        y el vídeo vive en la misma galería — sin plataformas aparte ni espacio cobrado dos
        veces. Todo con la portada, la cuadrícula y el tema que elijas.
      </p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <em>Momentos</em>
        <h3>La boda se lee como una historia</h3>
        <p>Hasta 20 bloques con nombre, llenados arrastrando o con las teclas 1-9. La pareja
        no recorre 800 fotos: recorre su día.
        <a href="/soporte/es/momentos/">Cómo funcionan</a>.</p>
      </div>
      <div class="step reveal" style="--d:.1s">
        <em>Foto y vídeo</em>
        <h3>El mismo espacio, el mismo enlace</h3>
        <p>La película de boda se entrega junto a las fotos, con
        <a href="/galerias/#diseno">diseños pensados para vídeo</a> — y sin cobrarse
        como un producto aparte.</p>
      </div>
      <div class="step reveal" style="--d:.2s">
        <em>Con tu firma</em>
        <h3>Tu logo en la puerta</h3>
        <p>La galería lleva tu marca y se sirve desde tu subdominio — o tu dominio.
        Cuando la compartan con la familia, te están recomendando.</p>
      </div>
    </div>
    <div class="galeria-tira reveal">
      <figure><img src="/img/galerias/slide-1-boda-aitana.jpg" alt="Portada de una galería de boda real en Positiva" width="1200" height="750" loading="lazy" decoding="async"></figure>
      <figure><img src="/img/galerias/slide-6-boda-mosaico.jpg" alt="Cuadrícula en mosaico de una galería de boda en Positiva" width="1200" height="750" loading="lazy" decoding="async"></figure>
      <figure><img src="/img/galerias/slide-5-boda-alvaro.jpg" alt="Galería de boda con tema oscuro en Positiva" width="1200" height="750" loading="lazy" decoding="async"></figure>
    </div>
    <p class="tira-pie reveal"><b>Bodas reales</b> entregadas con Positiva</p>
  </div>
</section>

<!-- ══ DOS ENLACES ══ -->
<section id="enlaces">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">02</span> La pareja y los invitados</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">Dos enlaces.<br><em>Dos maneras de mirar.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        La misma galería admite varios enlaces, cada uno con su contraseña y su permiso de
        descarga: la pareja con los originales, los invitados y la familia solo viendo — o
        con la versión web para compartir. Si un enlace circula de más, lo revocas.
      </p>
    </div>
    <div class="nota-linea reveal">
      <div>
        <h3>Las favoritas hacen el álbum</h3>
        <p>La pareja marca sus favoritas en la galería y tú exportas la selección como lista
        de nombres, hoja de cálculo o etiquetas de Finder — directa a tu flujo de diseño
        de álbum. <a href="/soporte/es/favoritas-del-cliente/">Cómo se exportan</a>.</p>
      </div>
      <div>
        <h3>El ZIP de «Descargar todo»</h3>
        <p>Un archivo con lo que tú decidas — los JPEG en alta, los originales, hasta el
        contrato — detrás del botón de descarga completa, obedeciendo los permisos de
        cada enlace. <a href="/galerias/">Así funciona la entrega</a>.</p>
      </div>
    </div>
  </div>
</section>''',
    'faqs': [
        ("¿Los invitados necesitan cuenta para ver la galería?",
         "No. Abren el enlace en cualquier navegador, con la contraseña si la has puesto. Sin cuentas, sin instalaciones y sin formularios.",
         ""),
        ("¿El enlace caduca en algún momento?",
         "No. Los enlaces de Positiva no tienen fecha de caducidad: el día del aniversario seguirá abriendo la misma galería.",
         ""),
        ("¿El vídeo de boda se cobra o se guarda aparte?",
         "No. Fotos y vídeo comparten el mismo espacio de tu plan y la misma galería, con diseños propios para la pieza de vídeo.",
         ""),
        ("¿Puedo dar permisos distintos a la pareja y a los invitados?",
         "Sí. Cada enlace fija su calidad de descarga — solo ver, web o alta con originales — y su contraseña. Dos enlaces de la misma galería pueden entregar permisos distintos.",
         '<a href="/soporte/es/permisos-de-descarga/">Qué puede descargar cada uno</a>.'),
        ("¿Cómo me llevo la selección del álbum?",
         "Desde el paso Favoritas: la selección de la pareja se exporta como lista de nombres (.txt), hoja de cálculo (.csv) o etiquetas de color de Finder, generadas en tu navegador.",
         ""),
    ],
    'related': '''      <a href="/galerias/">Galerías de entrega, a fondo</a>
      <a href="/galerias/#diseno">Diseños, temas y tu marca</a>
      <a href="/revision-video/">Revisión de vídeo con la pareja</a>
      <a href="/soporte/es/momentos/">Organizar las fotos por momentos</a>
      <a href="/soporte/es/favoritas-del-cliente/">Las favoritas y el álbum</a>
      <a href="/soporte/es/enlace-de-cliente/">Crear el enlace para la pareja</a>''',
})

# ══════════════════════ AGENCIAS ══════════════════════
CFGS.append({
    'slug': 'agencias',
    'nombre': 'Agencias y marcas',
    'source': 'agencias',
    'title': 'Positiva · Entrega y revisión para agencias y marcas',
    'desc': 'Revisión con varios interlocutores — modo colaborativo o individual —, comentarios anclados al fotograma en vídeo, marca blanca y enlaces revocables con permisos por enlace. Para agencias y producto.',
    'ogdesc': 'Todos opinan. Tú entregas una sola vez. Revisión con varios interlocutores y entrega con tu marca.',
    'theme': '#0E0E0D',
    'bodyclass': ' class="hero-oscuro"',
    'captura_h2': 'El próximo proyecto,<br><em>con las rondas bajo control.</em>',
    'css': '''
/* nav sobre hero oscuro */
body.hero-oscuro nav:not(.scrolled) .logo{color:#EDECE8}
body.hero-oscuro nav:not(.scrolled) .nav-links a,
body.hero-oscuro nav:not(.scrolled) .nav-drop-btn,
body.hero-oscuro nav:not(.scrolled) .nav-login{color:#B9B8B2}
body.hero-oscuro nav:not(.scrolled) .nav-links a:hover,
body.hero-oscuro nav:not(.scrolled) .nav-drop-btn:hover,
body.hero-oscuro nav:not(.scrolled) .nav-login:hover{color:#EDECE8}
body.hero-oscuro nav:not(.scrolled) .nav-burger{background:#EDECE8}
body.hero-oscuro nav:not(.scrolled) .nav-burger span{background:var(--pv-sala)}
.heroC.dark{background:var(--pv-sala);color:#EDECE8}
.heroC.dark .lede{color:#9C9B95}
/* hilo de comentarios esquemático */
.hilo{justify-self:center;width:min(100%,470px);display:grid;gap:12px}
.hilo .msg{
  background:var(--pv-sala-2);border:1px solid var(--pv-linea-sala);border-radius:12px 12px 12px 4px;
  padding:12px 16px;font-family:var(--pv-sans);font-size:14px;line-height:1.5;color:#CFCEC8;
  max-width:88%;
}
.hilo .msg b{display:block;font-family:var(--pv-mono);font-size:9.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#5C5B56;margin-bottom:3px}
.hilo .msg.na{margin-left:auto;border-radius:12px 12px 4px 12px}
.hilo .msg.ok{border-color:rgba(201,138,43,.45)}
.hilo .msg.ok b{color:var(--pv-ambar)}
''',
    'hero': '''<header class="heroC dark">
  <div class="wrap heroC-inner">
    <div>
      <p class="eyebrow">Agencias y marcas</p>
      <h1 aria-label="Todos opinan. Tú entregas una sola vez.">
        <span class="hl"><span style="--d:.05s">Todos opinan.</span></span>
        <span class="hl"><span style="--d:.15s">Tú entregas</span></span>
        <span class="hl"><span style="--d:.25s"><em>una sola vez.</em></span></span>
      </h1>
      <p class="lede">
        Marketing, el cliente final y su jefe: cada uno comenta en la galería — en vídeo,
        sobre el fotograma exacto — y tú decides si se ven entre ellos o no. Cuando el
        trabajo se aprueba, la misma galería es la entrega, con tu marca.
      </p>
      <div class="hero-cta">
        <a href="#lista" class="btn btn-amber" data-ev="cta_register_click" data-ev-place="hero_agencias">Regístrate</a>
        <a href="#rondas" class="btn btn-ghost">Ver cómo funciona</a>
      </div>
      <p class="hero-note">
        Once correos con «cambios_v3_FINAL.mp4»<br>
        no son un flujo de revisión.
      </p>
    </div>
    <div class="hilo" aria-hidden="true">
      <div class="msg"><b>Marca · 00:12</b> El logo tiene que aguantar más en pantalla.</div>
      <div class="msg na"><b>Marketing · 00:47</b> Aquí entraría la claim nueva, no la antigua.</div>
      <div class="msg ok"><b>Tú · respuesta</b> Hecho en ambos. Versión 2 subida — mismo enlace.</div>
    </div>
  </div>
</header>''',
    'secciones': '''<!-- ══ RONDAS ══ -->
<section id="rondas">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">01</span> La revisión</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">Varios interlocutores,<br><em>cero caos.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        Cada revisor entra con su email verificado y comenta sobre la foto o el fotograma.
        Tú eliges el modo por galería: colaborativo — todos ven los comentarios de todos —
        o individual, donde cada uno solo ve los suyos. Y las rondas llegan juntas, no a
        goteo.
      </p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <em>Quién ve qué</em>
        <h3>Colaborativo o individual</h3>
        <p>Que el equipo debata sobre los mismos comentarios, o que cada departamento
        opine sin contaminarse. Se decide por galería.</p>
      </div>
      <div class="step reveal" style="--d:.1s">
        <em>Vídeo en serio</em>
        <h3>Comentarios en el fotograma</h3>
        <p>Nada de minutajes por email: cada nota cae en su momento del timeline y tú la
        exportas como marcadores a DaVinci Resolve o Final Cut.
        <a href="/revision-video/">Cómo funciona</a>.</p>
      </div>
      <div class="step reveal" style="--d:.2s">
        <em>Versiones</em>
        <h3>El mismo enlace, siempre</h3>
        <p>Subes la versión corregida y el enlace no cambia. Las versiones anteriores quedan
        guardadas con sus comentarios, por si hay que volver.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ MARCA Y CONTROL ══ -->
<section class="dark" id="marca">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">02</span> Marca y control</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">La entrega firma<br><em>por tu estudio.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        Marca blanca desde el plan Autor: tu logo, tus colores y tu dominio delante del
        cliente final — sin rastro de la herramienta. Y el control operativo que un
        proyecto con marcas exige.
      </p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <em>Permisos</em>
        <h3>Cada enlace, su alcance</h3>
        <p>Un enlace de solo visionado para la presentación, otro con descarga alta para
        el equipo de la marca. Contraseña propia en cada uno, y revocables al momento.</p>
      </div>
      <div class="step reveal" style="--d:.1s">
        <em>Analítica</em>
        <h3>Sabes si lo han abierto</h3>
        <p>Visitas, visitantes únicos, descargas y reproducciones por galería — y en
        revisión, quién ha entrado con su correo. Se acabó el «¿lo habéis podido ver?».</p>
      </div>
      <div class="step reveal" style="--d:.2s">
        <em>Un archivo suelto</em>
        <h3>También sin galería</h3>
        <p>Para el máster final o un PDF, comparte un archivo suelto con el mismo control
        de enlace — sin montar una galería entera.
        <a href="/soporte/es/compartir-un-archivo-suelto/">Cómo</a>.</p>
      </div>
    </div>
    <div class="galeria-tira reveal" style="grid-template-columns:1fr 1fr">
      <figure><img src="/img/galerias/slide-2-evento-hoka.jpg" alt="Galería de evento de marca entregada con Positiva" width="1200" height="750" loading="lazy" decoding="async"></figure>
      <figure><img src="/img/galerias/slide-4-evento-detalle.jpg" alt="Detalle de una galería de evento corporativo en Positiva" width="1200" height="750" loading="lazy" decoding="async"></figure>
    </div>
    <p class="tira-pie reveal"><b>Proyectos de marca reales</b> entregados con Positiva</p>
  </div>
</section>''',
    'faqs': [
        ("¿Cuántas personas pueden revisar un mismo proyecto?",
         "Las que necesites: cada revisor entra con su email verificado. En modo colaborativo todos ven los comentarios de todos; en individual, cada uno solo los suyos.",
         ""),
        ("¿El cliente final ve la marca de Positiva?",
         "Con marca blanca — desde el plan Autor — la galería lleva tu logo y tus colores, y con el plan Estudio se sirve desde tu propio dominio.",
         '<a href="/galerias/#diseno">Cómo funciona tu marca</a>.'),
        ("¿Cómo llegan los cambios de vídeo al editor?",
         "Los comentarios se exportan como marcadores para DaVinci Resolve o Final Cut Pro: aparecen en el timeline, en su fotograma, con el texto de cada revisor.",
         ""),
        ("¿Puedo cortar el acceso cuando termina el proyecto?",
         "Sí. Cada enlace se revoca individualmente sin tocar los demás, y puedes crear enlaces nuevos con otros permisos en cualquier momento.",
         ""),
        ("¿Sirve también para la entrega final?",
         "Sí: la misma galería de revisión se convierte en entrega sin perder contenido, o compartes el máster como archivo suelto con su propio enlace.",
         '<a href="/galerias/">La entrega, a fondo</a>.'),
    ],
    'related': '''      <a href="/revision-video/">Revisión de vídeo, a fondo</a>
      <a href="/galerias/">Galerías de entrega</a>
      <a href="/soporte/es/quien-ve-los-comentarios/">Quién ve cada comentario</a>
      <a href="/soporte/es/rondas-de-revision/">Las rondas de revisión</a>
      <a href="/soporte/es/revocar-un-enlace/">Revocar un enlace</a>
      <a href="/soporte/es/analitica/">La analítica de tus galerías</a>''',
})

# ══════════════════════ FREELANCE ══════════════════════
CFGS.append({
    'slug': 'freelance',
    'nombre': 'Freelance',
    'source': 'freelance',
    'title': 'Positiva · La herramienta única para fotógrafos y videógrafos freelance',
    'desc': 'Galerías de entrega, revisión con comentarios, envío de archivos y portfolio público en una sola herramienta y una sola cuota. Foto y vídeo en el mismo espacio, con plan gratis para empezar.',
    'ogdesc': 'Equipo de uno, herramienta de una. Entrega, revisión, envío y portfolio en una sola cuota.',
    'captura_h2': 'Una herramienta menos que pagar.<br><em>Tres, en realidad.</em>',
    'hero': '''<header class="heroC">
  <div class="wrap heroC-inner">
    <div>
      <p class="eyebrow">Freelance</p>
      <h1 aria-label="Equipo de uno, herramienta de una.">
        <span class="hl"><span style="--d:.05s">Equipo de uno,</span></span>
        <span class="hl"><span style="--d:.15s"><em>herramienta de una.</em></span></span>
      </h1>
      <p class="lede">
        Si haces foto y vídeo tú solo, no necesitas una plataforma de galerías, otra de
        transferencias, otra de revisión y una web aparte. Positiva es las cuatro: entrega,
        comentarios, archivos y portfolio, en una cuota — y con plan Gratis para empezar.
      </p>
      <div class="hero-cta">
        <a href="#lista" class="btn btn-amber" data-ev="cta_register_click" data-ev-place="hero_freelance">Regístrate</a>
        <a href="/precios/" class="btn btn-ghost">Ver precios</a>
      </div>
      <p class="hero-note">
        Los gigas se cobran una vez.<br>
        No una vez por herramienta.
      </p>
    </div>
    <div class="lista-check" aria-hidden="true">
      <b>Lo que cubre tu cuota</b>
      <span><i>✓</i> Galerías de entrega con tu marca</span>
      <span><i>✓</i> Revisión con comentarios — foto y vídeo</span>
      <span><i>✓</i> Envío de archivos y ZIP de descarga</span>
      <span><i>✓</i> Portfolio público en tu subdominio</span>
      <span><i>✓</i> Foto y vídeo en el mismo espacio</span>
      <span class="suma">Una herramienta · una cuota</span>
    </div>
  </div>
</header>''',
    'secciones': '''<!-- ══ EL FLUJO COMPLETO ══ -->
<section class="dark" id="flujo">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">01</span> El flujo completo</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">Del encargo al portfolio,<br><em>sin salir de aquí.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        Cada pieza del trabajo de un freelance tiene su sitio en Positiva, y todas se
        alimentan del mismo material: lo que subes una vez sirve para revisar, entregar
        y enseñarte.
      </p>
    </div>
    <div class="steps cuatro">
      <div class="step reveal">
        <em>01 · Revisas</em>
        <h3>Comentarios en su sitio</h3>
        <p>El cliente comenta sobre la foto o el fotograma del vídeo, y los cambios llegan
        juntos, por rondas. <a href="/revision-video/">La revisión de vídeo</a>.</p>
      </div>
      <div class="step reveal" style="--d:.08s">
        <em>02 · Entregas</em>
        <h3>Un enlace que no muere</h3>
        <p>Galería con tu marca, permisos por enlace y ZIP de descarga completa.
        <a href="/galerias/">Las galerías de entrega</a>.</p>
      </div>
      <div class="step reveal" style="--d:.16s">
        <em>03 · Firmas</em>
        <h3>Tu marca en todo</h3>
        <p>Portadas, temas, tu logo y tu subdominio — o tu dominio.
        <a href="/galerias/#diseno">El diseño de galerías</a>.</p>
      </div>
      <div class="step reveal" style="--d:.24s">
        <em>04 · Te enseñas</em>
        <h3>El portfolio se hace solo</h3>
        <p>Eliges lo mejor de lo ya subido y tu web pública queda publicada.
        <a href="/portfolio/">El portfolio público</a>.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ EL ESPACIO Y EL PRECIO ══ -->
<section id="espacio">
  <div class="wrap">
    <p class="eyebrow reveal"><span class="idx">02</span> El espacio y el precio</p>
    <div class="head2">
      <h2 class="reveal" style="--d:.05s">Gigas claros,<br><em>sin letra pequeña.</em></h2>
      <p class="lede reveal" style="--d:.15s">
        Nada de «ilimitado» que se cobra por otro lado: sabes cuántos gigas tienes y cuánto
        valen, y el vídeo comparte espacio con las fotos en lugar de facturarse como
        «horas de vídeo». Empiezas gratis y subes de plan cuando el trabajo lo pida.
      </p>
    </div>
    <div class="nota-linea reveal">
      <div>
        <h3>Para empezar, gratis</h3>
        <p>El plan Gratis incluye espacio y galerías activas suficientes para probar el flujo
        completo con encargos reales. <a href="/precios/">Los planes, en detalle</a>.</p>
      </div>
      <div>
        <h3>Tarifa fundador</h3>
        <p>Los primeros fotógrafos que entren en la beta conservan su precio para siempre.
        Es lo justo por confiar cuando la herramienta aún se estaba construyendo.</p>
      </div>
    </div>
  </div>
</section>''',
    'faqs': [
        ("¿Puedo empezar sin pagar?",
         "Sí. El plan Gratis existe para probar el flujo completo con encargos reales, y los planes de pago se contratan cuando el volumen lo pide.",
         '<a href="/precios/">Los planes, en detalle</a>.'),
        ("¿El vídeo consume un espacio aparte?",
         "No. Fotos y vídeo comparten los mismos gigas de tu plan. No hay «horas de vídeo» ni un producto separado que contratar.",
         ""),
        ("¿Sustituye a mi herramienta de transferencias?",
         "Para el trabajo con clientes, sí: los enlaces no caducan, llevan tu marca y controlan qué se descarga. También puedes compartir un archivo suelto sin montar una galería.",
         ""),
        ("¿Y la web de portfolio?",
         "Incluida en todos los planes: cuatro páginas con tu nombre en tu subdominio, montadas con el material que ya has subido.",
         '<a href="/portfolio/">Cómo funciona</a>.'),
        ("¿Qué pasa si un mes no tengo encargos?",
         "Nada: tus galerías siguen en su sitio y los enlaces entregados siguen funcionando. Tu archivo no depende de tu mes.",
         ""),
    ],
    'related': '''      <a href="/galerias/">Galerías de entrega</a>
      <a href="/revision-video/">Revisión de vídeo</a>
      <a href="/galerias/#diseno">Diseño y marca</a>
      <a href="/portfolio/">Portfolio público</a>
      <a href="/precios/">Planes y precios</a>
      <a href="/soporte/es/almacenamiento/">Cómo se calcula tu almacenamiento</a>''',
})
