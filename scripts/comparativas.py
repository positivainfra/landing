# -*- coding: utf-8 -*-
"""
Tablas comparativas del blog (/notas/alternativas-a-*) y de las páginas
positiva-vs-*. Fuente ÚNICA: gen-notas.py y scripts/new-web/gen.py las pintan
donde encuentran el marcador  <!-- @tabla clave -->.

Reglas (decididas con Rodrigo el 04/10/2026):
  · Criterios en filas, herramientas en columnas, como mucho 4 herramientas:
    lo que no cabe se queda en su apartado del artículo, no en la tabla.
  · En cada fila se marca la celda GANADORA con criterio objetivo: gana quien
    tiene el mejor dato, sea Positiva o el competidor. Empate o «depende de
    tu caso»: sin distintivo. Varias columnas de Positiva (Autor/Estudio)
    pueden ganar juntas si las dos superan al resto.
  · Archivos y solicitudes es solo del plan Estudio: se dice siempre.
  · Lo no verificado: «No lo hemos encontrado en su documentación».
Datos de archivos y solicitudes verificados el 04/10/2026 en documentación
oficial (Dropbox, WeTransfer, Google, Frame.io, Vimeo, Pic-Time, Pixieset,
Arcadina). El resto, con las fechas de cada artículo.

Cada tabla: cols = [(nombre, es_positiva)], filas = [(criterio, [celdas], {índices ganadores})]
"""
import html as _html

NE = 'No lo hemos encontrado en su documentación'
POS_GUARDAR = 'Carpetas con cualquier formato y envíos con enlace (plan Estudio)'
POS_PEDIR = 'Sí, en el plan Estudio: quien sube no necesita cuenta; hasta 150 GB por archivo'
PRECIO_POS = '89 € + IVA/año (Autor, 250 GB)'

TABLAS = {

# ── Blog ─────────────────────────────────────────────────────────────────
'pixieset': dict(
  cols=[('Positiva', True), ('Pixieset', False), ('Pic-Time', False)],
  filas=[
    ('Vídeo', ['Por GB, junto a las fotos', 'Por minutos según plan (30 min en Basic)', 'Bolsa aparte: 30 GB en Professional'], {0}),
    ('Revisión', ['Favoritas, comentarios en foto y por fotograma en vídeo', 'Favoritas de foto', 'Favoritas y selección'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', NE, 'Subida del cliente a la galería, desactivada en Pic-Time 2.0'], {0}),
    ('Web pública', ['Portfolio con tus entregas', 'Website completa, módulo aparte', 'Portfolio Page embebible'], {1}),
    ('Tienda', ['No', 'Sí, módulo aparte (15 % en el plan gratis)', 'Sí, 30+ laboratorios y automatizaciones'], {2}),
    ('Gestión del negocio', ['No', 'Studio Manager, módulo aparte', 'No'], {1}),
    ('Plan gratis', ['15 GB · 2 galerías', '3 GB', '3 GB de foto · 1 GB de vídeo'], {0}),
    ('Precio anual', [PRECIO_POS, '192 $ (Plus, 100 GB)', '252 $ (Professional, 100 GB + 30 GB de vídeo)'], {0}),
  ],
  nota='ShootProof, SmugMug y Zenfolio, en sus apartados del artículo.'),

'pic-time': dict(
  cols=[('Positiva', True), ('Pic-Time', False), ('Pixieset', False)],
  filas=[
    ('Vídeo', ['Por GB, junto a las fotos', '30 GB en Professional (ampliable desde 10 $/mes)', 'Por minutos según plan'], {0}),
    ('Revisión', ['Favoritas, comentarios en foto y por fotograma en vídeo', 'Favoritas y selección', 'Favoritas de foto'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', 'Subida del cliente a la galería, desactivada en Pic-Time 2.0', NE], {0}),
    ('Web pública', ['Portfolio con tus entregas', 'Portfolio Page (escaparate de galerías, embebible)', 'Website completa, producto aparte'], {2}),
    ('Tienda', ['No', 'Sí, 30+ laboratorios y automatizaciones', 'Sí (15 % de comisión en el plan gratis)'], {1}),
    ('Plan gratis', ['15 GB · 2 galerías', '3 GB de foto (tras 3 meses) · 1 GB de vídeo', '3 GB'], {0}),
    ('Precio anual', [PRECIO_POS, '252 $ (100 GB + 30 GB de vídeo)', '192 $ (Plus, 100 GB)'], {0}),
  ],
  nota='ShootProof, SmugMug y Zenfolio, en sus apartados del artículo.'),

'wetransfer': dict(
  cols=[('Positiva', True), ('WeTransfer', False), ('Dropbox Transfer', False), ('Google Drive', False)],
  filas=[
    ('Pensado para', ['Entregar y revisar con el cliente', 'Enviar archivos', 'Enviar desde tu Dropbox', 'Guardar y compartir carpetas'], set()),
    ('Tamaño', ['Galería: hasta tu cuota · Archivos: hasta 150 GB por archivo (Estudio)', '3 GB/30 días (Free); 1 TB por transferencia (Ultimate)', '50 GB (Plus) a 250 GB (Business Plus)', 'Hasta tu cuota'], set()),
    ('Caducidad del enlace', ['La galería no caduca', '3 días (Free y Starter); sin límite en Ultimate', '7 días (Plus); 30 en planes de empresa', 'No caduca'], {0, 3}),
    ('Tu marca', ['Logo, colores y tipografía', 'Páginas con marca en Ultimate', 'Logo y fondo en planes de empresa', 'No'], {0}),
    ('Revisión', ['Favoritas, comentarios en foto y por fotograma en vídeo', 'No', 'Con Replay, complemento aparte', 'Comentarios sobre archivos, con cuenta de Google'], {0}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Sí, desde el plan gratis; pide email verificado y lo recibido caduca a los 3 días en Free', 'Sí, en todos los planes, sin cuenta; de 2 GB (Basic/Plus) a 250 GB por archivo', 'Solo con Forms o carpeta compartida: pide cuenta de Google'], {2}),
    ('Plan gratis', ['15 GB · 2 galerías', '10 envíos o 3 GB cada 30 días', '2 GB', '15 GB compartidos con Gmail y Fotos'], set()),
    ('Precio', [PRECIO_POS, 'Starter 6,99 $/mes; Ultimate sin precio verificable', 'Incluido en Dropbox (Plus, 9,99 $/mes)', '15 GB gratis; planes según país'], set()),
  ],
  nota='SwissTransfer y Smash, en sus apartados del artículo.'),

'frame-io': dict(
  cols=[('Positiva', True), ('Frame.io', False), ('Vimeo', False), ('Dropbox Replay', False)],
  filas=[
    ('Comentarios en vídeo', ['Por fotograma', 'Por fotograma, por rango y anotaciones dibujadas', 'Con código de tiempo (desde Standard)', 'Sí; vínculo al fotograma no documentado'], {1}),
    ('Exporta al editor', ['Marcadores a DaVinci Resolve y Final Cut Pro', 'Marcadores en Premiere Pro; CSV', 'No documentado', 'No documentado'], set()),
    ('Fotografía', ['Galerías con favoritas, comentarios y exportación a Lightroom', 'Sí, con visor y enlaces de revisión', 'No', 'No'], {0}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Cualquier archivo, hasta 5 TB, con carpetas', 'Solo vídeo', 'Tu Dropbox, con cualquier archivo'], {1}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Sin función propia', 'Solo programándolo con su API', 'Con las solicitudes de Dropbox, sin cuenta'], set()),
    ('Entrega y portfolio', ['Entrega con tu marca + portfolio público', 'Presentaciones con marca, sin portfolio', 'Showcases y portfolios de vídeo', 'No'], {0}),
    ('Almacenamiento', ['250 GB (Autor) · 1 TB (Estudio)', '2 TB (Pro, +2 TB por miembro)', '4 TB (Standard)', 'El de tu Dropbox (2 TB en Plus)'], {2}),
    ('Modelo de precio', ['Por cuenta, revisores ilimitados', 'Por miembro', 'Por asiento', 'Por usuario, sobre un plan de Dropbox'], {0}),
    ('Precio de referencia', [PRECIO_POS, '15 $/miembro/mes (Pro)', '25 $/asiento/mes (Standard)', '120 $/usuario/año + Dropbox'], {0}),
  ]),

'vimeo': dict(
  cols=[('Positiva', True), ('Vimeo', False), ('Frame.io', False), ('Dropbox Replay', False)],
  filas=[
    ('Comentarios en vídeo', ['Por fotograma', 'Con código de tiempo (desde Standard)', 'Por fotograma, por rango y anotaciones', 'Sí; vínculo al fotograma no documentado'], {2}),
    ('Exporta al editor', ['Marcadores a DaVinci Resolve y Final Cut Pro', 'No documentado', 'Marcadores en Premiere Pro; CSV', 'No documentado'], set()),
    ('Fotografía', ['Galerías con favoritas y comentarios', 'No', 'Sí, con visor y enlaces de revisión', 'No'], {0}),
    ('Vídeo público y directos', ['No', 'Sí, con reproductor incrustable, showcases y directos', 'No', 'No'], {1}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Solo vídeo', 'Cualquier archivo, hasta 5 TB, con carpetas', 'Tu Dropbox, con cualquier archivo'], {2}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Solo programándolo con su API', 'Sin función propia', 'Con las solicitudes de Dropbox, sin cuenta'], set()),
    ('Almacenamiento', ['250 GB (Autor) · 1 TB (Estudio)', '4 TB (Standard)', '2 TB (Pro)', 'El de tu Dropbox (2 TB en Plus)'], {1}),
    ('Modelo de precio', ['Por cuenta, revisores ilimitados', 'Por asiento', 'Por miembro', 'Por usuario, sobre un plan de Dropbox'], {0}),
    ('Precio de referencia', [PRECIO_POS, '25 $/asiento/mes (Standard)', '15 $/miembro/mes (Pro)', '120 $/usuario/año + Dropbox'], {0}),
  ]),

'dropbox-replay': dict(
  cols=[('Positiva', True), ('Dropbox Replay', False), ('Frame.io', False), ('Vimeo', False)],
  filas=[
    ('Comentarios en vídeo', ['Por fotograma', 'Sí; vínculo al fotograma no documentado', 'Por fotograma, por rango y anotaciones', 'Con código de tiempo (desde Standard)'], {2}),
    ('Audio', ['No', 'Sí, sin pérdida', 'No como producto propio', 'No'], {1}),
    ('Exporta al editor', ['Marcadores a DaVinci Resolve y Final Cut Pro', 'No documentado', 'Marcadores en Premiere Pro; CSV', 'No documentado'], set()),
    ('Entrega al cliente', ['Galería con tu marca + portfolio', 'No', 'Presentaciones con marca, sin portfolio', 'Showcases y portfolios de vídeo'], {0}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Tu Dropbox sincronizado, con cualquier archivo', 'Cualquier archivo, hasta 5 TB', 'Solo vídeo'], {1}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Con las solicitudes de Dropbox, sin cuenta', 'Sin función propia', 'Solo programándolo con su API'], set()),
    ('Modelo de precio', ['Una cuota, revisores ilimitados', 'Por usuario + plan de Dropbox', 'Por miembro', 'Por asiento'], {0}),
    ('Precio de referencia', [PRECIO_POS, '120 $/usuario/año + Dropbox', '15 $/miembro/mes (Pro)', '25 $/asiento/mes (Standard)'], {0}),
  ]),

'arcadina': dict(
  cols=[('Positiva', True), ('Arcadina', False), ('Pixieset', False), ('Pic-Time', False)],
  filas=[
    ('Vídeo en la galería', ['Alojado, junto a las fotos', 'Enlace de YouTube o Vimeo', 'Por minutos según plan', 'Bolsa aparte (30 GB en Professional)'], {0}),
    ('Revisión', ['Favoritas, comentarios en foto y por fotograma en vídeo', 'Favoritas + comentario por imagen seleccionada', 'Favoritas de foto', 'Favoritas y selección'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', NE, NE, 'Subida del cliente a la galería, desactivada en Pic-Time 2.0'], {0}),
    ('Web pública', ['Portfolio con tus entregas', 'Sí, plan Web aparte', 'Módulo aparte', 'Portfolio Page embebible'], set()),
    ('Tienda', ['No', 'Sí, sin comisión', 'Módulo aparte', 'Sí, 30+ laboratorios'], set()),
    ('Gestión del negocio', ['No', 'Sí, plan Manager aparte', 'Studio Manager, aparte', 'No'], set()),
    ('Idioma del panel', ['Español', 'Español', 'Inglés', 'Inglés'], {0, 1}),
    ('Precio de referencia', [PRECIO_POS, 'Negocio desde 120 €/año (IVA incl., 30 GB)', '192 $/año (Plus, 100 GB)', '252 $/año (100 GB + 30 GB de vídeo)'], {0}),
  ],
  nota='PSPro y Zenfolio, en sus apartados del artículo.'),

# ── Páginas positiva-vs-* ────────────────────────────────────────────────
'vs-pictime-pixieset': dict(
  cols=[('Positiva Autor', True), ('Positiva Estudio', True), ('Pic-Time Professional', False), ('Pixieset Plus', False)],
  filas=[
    ('Precio al año', ['89 € + IVA', '219 € + IVA', '252 $ (21 $/mes anual)', '192 $ (≈ 180 €)'], {0}),
    ('Espacio para fotos y vídeos', ['250 GB compartidos', '1 TB compartido', '100 GB + 30 GB de vídeo', '100 GB de fotos + vídeo por minutos'], {1}),
    ('¿El vídeo tiene una cuota aparte?', ['No', 'No', 'Sí', 'Sí'], {0, 1}),
    ('Selección de favoritos del cliente', ['Sí, desde el plan gratis', 'Sí', 'Sí', 'Sí'], set()),
    ('Tu marca en la galería', ['Logo, colores y tipografía', 'Lo mismo + multimarca', 'Sí', 'Logo y branding'], {1}),
    ('Dominio propio', ['No', 'Sí', 'Sí', 'Sí'], set()),
    ('Tus archivos y solicitudes a terceros', ['Compartir un archivo suelto con enlace', 'Carpetas, envíos y solicitudes; quien sube no necesita cuenta', 'Subida del cliente a la galería, desactivada en Pic-Time 2.0', NE], {1}),
    ('Comisión si vendes copias o álbumes', ['0 %', '0 %', 'Comisión en su tienda integrada', '0 % en planes de pago · 15 % en el gratis'], set()),
    ('Llevarte tus archivos al irte', ['ZIP con la estructura intacta, sin pedirlo a soporte', 'Igual', 'Exportación disponible', 'Exportación disponible'], set()),
    ('Archivos alojados en la UE (RGPD)', ['Sí', 'Sí', 'No · UE, EE. UU. y Australia', 'No garantizado'], {0, 1}),
    ('No entrena IA con tu material', ['Nunca', 'Nunca', 'Indexa tus imágenes salvo opt-out', 'No en modelos generativos'], {0, 1}),
  ],
  nota='Pixieset Pro (288 $/año, 1 TB) sale de la tabla para que se lea entera: mismas funciones que Plus con más espacio.'),

'vs-arcadina': dict(
  cols=[('Positiva Autor', True), ('Positiva Estudio', True), ('Arcadina Exposure', False), ('Arcadina Focus', False)],
  filas=[
    ('Precio al año', ['89 € + IVA', '219 € + IVA', '240 € (imp. incl.)', '360 € (imp. incl.)'], {0}),
    ('Espacio para fotos y vídeos', ['250 GB compartidos', '1 TB compartido', '100 GB', '300 GB'], {1}),
    ('Revisión con comentarios (en vídeo, al fotograma)', ['Sí, exportables a DaVinci y Final Cut', 'Sí', 'Su web no lo anuncia', 'Su web no lo anuncia'], {0, 1}),
    ('Selección de favoritas del cliente', ['Sí, con nombre y exportación a Lightroom, Finder, .txt y .csv', 'Sí', 'Sí', 'Sí'], set()),
    ('Diseños de entrega para vídeo', ['Estreno, Cartel, Vitrina, Montaje y Videoteca', 'Sí', 'Su web no lo anuncia', 'Su web no lo anuncia'], {0, 1}),
    ('Tu marca en la galería', ['Logo, colores y tipografía', 'Lo mismo + multimarca', 'Logo propio', 'Logo propio'], {1}),
    ('Dominio propio', ['No', 'Sí', 'Con su Plan Web, aparte', 'Con su Plan Web, aparte'], {1}),
    ('Tus archivos y solicitudes a terceros', ['Compartir un archivo suelto con enlace', 'Carpetas, envíos y solicitudes; quien sube no necesita cuenta', 'Su web no lo anuncia', 'Su web no lo anuncia'], {1}),
    ('Web del fotógrafo, tienda y reservas', ['Portfolio público · sin tienda ni reservas', 'Igual', 'Tienda sin comisiones · web y reservas en otros planes', 'Igual'], {2, 3}),
    ('Archivos alojados en la UE (RGPD)', ['Sí', 'Sí', 'Empresa española · su web no especifica el alojamiento', 'Ídem'], {0, 1}),
    ('No entrena IA con tu material', ['Nunca', 'Nunca', 'Su web no lo especifica', 'Ídem'], {0, 1}),
  ],
  nota='Arcadina Aperture (120 €/año con impuestos, 30 GB) sale de la tabla para que se lea entera.'),

'vs-dropbox': dict(
  cols=[('Dropbox', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Almacenamiento y sincronización', 'Entregar y revisar fotos y vídeo con el cliente'], set()),
    ('El cliente recibe', ['Una carpeta de archivos', 'Una galería con tu marca'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['No', 'Sí'], {1}),
    ('El enlace caduca', ['No', 'No, nunca'], set()),
    ('El cliente elige sus favoritos', ['No', 'Sí'], {1}),
    ('Comentarios sobre cada archivo', ['No', 'Sí, en foto y por fotograma en vídeo'], {1}),
    ('Vídeo reproducible en la galería', ['No, solo descarga', 'Sí'], {1}),
    ('Guardar tus archivos de trabajo', ['Cualquier archivo, sincronizado con tu ordenador', 'Carpetas y envíos con enlace (plan Estudio), sin sincronización'], {0}),
    ('Pedir archivos a terceros', ['Sí, en todos los planes, sin cuenta; de 2 GB a 250 GB por archivo', 'Sí, en el plan Estudio, sin cuenta; hasta 150 GB por archivo'], {0}),
    ('Portfolio / web pública', ['No', 'Sí'], {1}),
    ('Precio de referencia', ['Plus · 2 TB · 9,99 $/mes', 'Autor · 250 GB · 89 €/año'], set()),
  ]),

'vs-google-drive': dict(
  cols=[('Google Drive', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Almacenamiento en la nube', 'Entregar y revisar fotos y vídeo con el cliente'], set()),
    ('El cliente recibe', ['Una carpeta de archivos', 'Una galería con tu marca'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['No', 'Sí'], {1}),
    ('El enlace caduca', ['No', 'No, nunca'], set()),
    ('El cliente elige sus favoritos', ['No', 'Sí'], {1}),
    ('Comentarios sobre cada archivo', ['Sí, con cuenta de Google', 'Sí, sin cuenta; en vídeo, por fotograma'], {1}),
    ('Vídeo reproducible en la galería', ['Vista previa del archivo', 'Sí, en la galería, junto a las fotos'], {1}),
    ('Guardar tus archivos de trabajo', ['Cualquier archivo, sincronizado con tu ordenador', 'Carpetas y envíos con enlace (plan Estudio), sin sincronización'], {0}),
    ('Pedir archivos a terceros', ['Solo con Forms o carpeta compartida: pide cuenta de Google', 'Sí, en el plan Estudio, sin cuenta; hasta 150 GB por archivo'], {1}),
    ('Portfolio / web pública', ['No', 'Sí'], {1}),
    ('Precio de referencia', ['15 GB gratis; planes de pago según país', 'Autor · 250 GB · 89 €/año'], set()),
  ]),

'vs-wetransfer': dict(
  cols=[('WeTransfer', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Envío de archivos', 'Entregar y revisar fotos y vídeo con el cliente'], set()),
    ('El cliente recibe', ['Un enlace de descarga', 'Una galería con tu marca'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['Limitada (plan de pago)', 'Sí'], {1}),
    ('El enlace caduca', ['A los 3 días (Free y Starter)', 'No, nunca'], {1}),
    ('Plan gratuito', ['10 envíos o 3 GB cada 30 días', '15 GB · 2 galerías, sin caducidad'], {1}),
    ('El cliente elige sus favoritos', ['No', 'Sí'], {1}),
    ('Comentarios sobre cada archivo', ['No', 'Sí'], {1}),
    ('Pedir archivos a terceros', ['Sí, desde el plan gratis; pide email verificado y lo recibido caduca a los 3 días en Free', 'Sí, en el plan Estudio, sin cuenta; lo recibido no caduca'], set()),
    ('Portfolio / web pública', ['No', 'Sí'], {1}),
    ('Precio', ['Starter 6,99 $/mes; Ultimate sin precio verificable', 'Autor · 250 GB · 89 €/año'], set()),
  ]),
}

CSS = """
/* .cmpx.cmpx: gana a las reglas genéricas de tabla de cada hoja (p. ej. .prosa table th) */
.cmpx.cmpx{margin:var(--pv-s5,24px) 0;border:1px solid var(--pv-linea,#DEDDD6);border-radius:16px;background:var(--pv-luz,#fff);overflow:hidden}
.cmpx.cmpx table{width:100%;border-collapse:collapse;table-layout:fixed;font-size:14.5px;line-height:1.45}
.cmpx.cmpx th,.cmpx.cmpx td{padding:12px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--pv-linea,#DEDDD6);white-space:normal !important;overflow-wrap:anywhere;font-weight:400}
.cmpx.cmpx tbody tr:last-child th,.cmpx.cmpx tbody tr:last-child td{border-bottom:0}
.cmpx.cmpx thead th{font-family:var(--pv-mono,'IBM Plex Mono',monospace);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--pv-tinta-60,#5A5852);background:var(--pv-bandeja,#E8E7E1);border-bottom:1px solid var(--pv-linea,#DEDDD6)}
.cmpx.cmpx thead th.pos{background:var(--pv-ambar-luz,#F6EAD2);color:var(--pv-ambar-ink,#8F5F15)}
.cmpx.cmpx thead th:first-child{width:24%}
.cmpx.cmpx tbody th{font-family:inherit;text-transform:none;letter-spacing:0;font-weight:600 !important;color:var(--pv-tinta,#171614);font-size:14px;background:none;border-bottom:1px solid var(--pv-linea,#DEDDD6)}
.cmpx.cmpx td{color:var(--pv-tinta-60,#5A5852)}
.cmpx.cmpx td.pos{background:color-mix(in srgb,var(--pv-ambar-luz,#F6EAD2) 35%,transparent)}
.cmpx.cmpx td.gana{background:#E6F2E8;color:#1F3B27;box-shadow:inset 3px 0 0 #2F7A45}
.cmpx.cmpx .gana-b{display:flex;width:max-content;align-items:center;gap:4px;margin-bottom:5px;font-family:var(--pv-mono,'IBM Plex Mono',monospace);font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:#2F7A45;border-radius:999px;padding:2px 8px;line-height:1.5}
.cmpx-ley{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;font-size:13px;color:var(--pv-tinta-60,#5A5852);margin:10px 0 0}
.cmpx-ley .gana-b{display:inline-flex;align-items:center;gap:4px;font-family:var(--pv-mono,'IBM Plex Mono',monospace);font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:#2F7A45;border-radius:999px;padding:2px 8px}
@media(max-width:700px){
  .cmpx.cmpx{border:0;background:none;border-radius:0;overflow:visible}
  .cmpx.cmpx table,.cmpx.cmpx tbody,.cmpx.cmpx tr,.cmpx.cmpx th,.cmpx.cmpx td{display:block;width:auto}
  .cmpx.cmpx thead{display:none}
  .cmpx.cmpx tbody tr{border:1px solid var(--pv-linea,#DEDDD6);border-radius:14px;background:var(--pv-luz,#fff);margin-bottom:10px;overflow:hidden}
  .cmpx.cmpx tbody th{background:var(--pv-bandeja,#E8E7E1);padding:10px 14px;border-bottom:1px solid var(--pv-linea,#DEDDD6)}
  .cmpx.cmpx td{display:grid;grid-template-columns:8.5em minmax(0,1fr);gap:4px 10px;padding:10px 14px}
  .cmpx.cmpx td::before{content:attr(data-h);font-family:var(--pv-mono,'IBM Plex Mono',monospace);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--pv-tinta-60,#5A5852);padding-top:3px;grid-row:1 / span 2}
  .cmpx.cmpx td.pos::before{color:var(--pv-ambar-ink,#8F5F15)}
  .cmpx.cmpx td.gana{box-shadow:inset 3px 0 0 #2F7A45}
  .cmpx.cmpx td .gana-b{grid-column:2;justify-self:start}
  .cmpx.cmpx td .v{grid-column:2}
}
"""

def tabla(clave):
    d = TABLAS[clave]
    cols = d['cols']
    e = _html.escape
    th = '<th scope="col"><span style="position:absolute;left:-9999px">Criterio</span></th>' + ''.join(
        ('<th scope="col" class="pos">' if p else '<th scope="col">') + e(n) + '</th>' for n, p in cols)
    filas = []
    for crit, celdas, gana in d['filas']:
        assert len(celdas) == len(cols), (clave, crit)
        tds = []
        for i, (c, (n, p)) in enumerate(zip(celdas, cols)):
            cls = ' '.join(x for x in ('pos' if p else '', 'gana' if i in gana else '') if x)
            badge = '<span class="gana-b" aria-label="Mejor en esta fila">✓ Mejor</span>' if i in gana else ''
            attr = ' class="%s"' % cls if cls else ''
            tds.append(f'<td data-h="{e(n)}"{attr}>{badge}<span class="v">{e(c)}</span></td>')
        filas.append(f'<tr><th scope="row">{e(crit)}</th>{"".join(tds)}</tr>')
    nota = f' {e(d["nota"])}' if d.get('nota') else ''
    return (f'<div class="cmpx"><table>\n<thead><tr>{th}</tr></thead>\n<tbody>\n' + '\n'.join(filas) +
            '\n</tbody></table></div>\n'
            f'<p class="cmpx-ley"><span class="gana-b">✓ Mejor</span><span>El mejor dato de la fila, sea de quien sea. Sin distintivo: empate o depende de tu caso.{nota}</span></p>')

def pintar(html_text):
    """Sustituye cada <!-- @tabla clave --> por su tabla."""
    import re
    return re.sub(r'<!-- @tabla ([a-z0-9-]+) -->', lambda m: tabla(m.group(1)), html_text)
