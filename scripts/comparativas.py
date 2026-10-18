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
  · Lo que en Positiva no está en todos los planes, también (p. ej. «planes Autor y Estudio»).
  · Lo no verificado: «No lo hemos encontrado en su documentación».
Datos de archivos y solicitudes verificados el 04/10/2026 en documentación
oficial (Dropbox, WeTransfer, Google, Frame.io, Vimeo, Pic-Time, Pixieset,
Arcadina). TODOS los datos de competidores revisados de nuevo el 17/10/2026
en sus webs y centros de ayuda oficiales (WeTransfer y Arcadina, edición
española; el resto, estadounidense). Las celdas de Positiva dicen el plan
cuando la función no está en todos (fuente: frontend/src/config/plans.ts).

Cada tabla: cols = [(nombre, es_positiva)], filas = [(criterio, [celdas], {índices ganadores})]
"""
import html as _html

NE = 'No lo hemos encontrado en su documentación'
POS_GUARDAR = 'Carpetas con cualquier formato y envíos con enlace (plan Estudio)'
POS_PEDIR = 'Sí, en el plan Estudio: quien sube no necesita cuenta; hasta 150 GB por archivo'
PRECIO_POS = 'Autor, 250 GB: 89 €/año + IVA (o 8,95 €/mes)'
# Funciones de Positiva que dependen del plan (plans.ts): se dice en la celda.
POS_REV = 'Favoritas y comentarios en foto; por fotograma en vídeo (planes Autor y Estudio)'
POS_GRATIS = '15 GB · 2 galerías activas'
POS_MARCA = 'Logo, colores y tipografía (planes Autor y Estudio)'
POS_COM_VIDEO = 'Por fotograma (planes Autor y Estudio)'
POS_EXPORTA = 'Marcadores a DaVinci Resolve (EDL) y Final Cut Pro (FCPXML), planes Autor y Estudio'
POS_PORTFOLIO = 'Portfolio con tus entregas (con vídeos, en Autor y Estudio)'
PIXIESET_VIDEO = '30 min de vídeo HD en Basic; en el resto, dentro del almacenamiento'
PICTIME_SUBIDA = 'Subida del cliente a la galería en Pic-Time 1.0; aún no en 2.0'
FRAME_EDITOR = 'Panel en Premiere Pro; CSV y texto; Resolve sin soporte en V4'
VIMEO_EDITOR = 'Descarga de comentarios; sin integración con editores encontrada'
REPLAY_COM = 'Sí; sincronizados al fotograma solo desde DaVinci Resolve'
REPLAY_EDITOR = 'Marcadores en Final Cut Pro y After Effects'
WT_CADUCA = 'De 3 a 7 días en Free y Starter (su ayuda y su web no coinciden); sin límite en Ultimate'
WT_PEDIR = 'Sí, desde el plan gratis; quien sube verifica su email y lo recibido caduca a los 3 días en Free y Starter'
WT_PRECIO = 'Starter 96 €/año (8 €/mes); Ultimate 276 €/año (23 €/mes); facturación mensual'

TABLAS = {

# ── Blog ─────────────────────────────────────────────────────────────────
'pixieset': dict(
  cols=[('Positiva', True), ('Pixieset', False), ('Pic-Time', False)],
  filas=[
    ('Vídeo', ['Por GB, junto a las fotos', PIXIESET_VIDEO, 'Cuota aparte: 30 GB en Professional'], {0}),
    ('Revisión', [POS_REV, 'Favoritas de foto, con notas', 'Favoritas y selección (desde Professional)'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', NE, PICTIME_SUBIDA], {0}),
    ('Web pública', [POS_PORTFOLIO, 'Website completa, módulo aparte', 'Portfolio Page embebible'], {1}),
    ('Tienda', ['No', 'Sí, módulo aparte (15 % en el plan gratis)', 'Sí, 30+ laboratorios y automatizaciones'], {2}),
    ('Gestión del negocio', ['No', 'Studio Manager, módulo aparte o en la Suite', 'No'], {1}),
    ('Plan gratis', [POS_GRATIS, '3 GB, galerías ilimitadas', '10 GB que bajan a 3 GB a los 3 meses · 1 GB de vídeo'], set()),
    ('Precio anual', [PRECIO_POS, 'Plus, 100 GB: 192 $/año (16 $/mes con facturación anual)', 'Professional, 100 GB + 30 GB de vídeo: 252 $/año (21 $/mes con facturación anual)'], {0}),
  ],
  nota='ShootProof, SmugMug y Zenfolio, en sus apartados del artículo.'),

'pic-time': dict(
  cols=[('Positiva', True), ('Pic-Time', False), ('Pixieset', False)],
  filas=[
    ('Vídeo', ['Por GB, junto a las fotos', '30 GB en Professional (ampliable desde 120 $/año, 10 $/mes con facturación anual)', PIXIESET_VIDEO], {0}),
    ('Revisión', [POS_REV, 'Favoritas y selección (desde Professional)', 'Favoritas de foto, con notas'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', PICTIME_SUBIDA, NE], {0}),
    ('Web pública', [POS_PORTFOLIO, 'Portfolio Page (escaparate de galerías, embebible)', 'Website completa, producto aparte'], {2}),
    ('Tienda', ['No', 'Sí, 30+ laboratorios y automatizaciones; 8 % en Professional si cobra Pic-Time', 'Sí (15 % de comisión en el plan gratis; 0 % en los de pago)'], {1}),
    ('Plan gratis', [POS_GRATIS, '10 GB que bajan a 3 GB a los 3 meses · 1 GB de vídeo · sin selección del cliente', '3 GB, galerías ilimitadas'], set()),
    ('Precio anual', [PRECIO_POS, 'Professional, 100 GB + 30 GB de vídeo: 252 $/año (21 $/mes con facturación anual)', 'Plus, 100 GB: 192 $/año (16 $/mes con facturación anual)'], {0}),
  ],
  nota='ShootProof, SmugMug y Zenfolio, en sus apartados del artículo.'),

'wetransfer': dict(
  cols=[('Positiva', True), ('WeTransfer', False), ('Dropbox Transfer', False), ('Google Drive', False)],
  filas=[
    ('Pensado para', ['Entregar y revisar con el cliente; también enviar y pedir archivos', 'Enviar archivos', 'Enviar desde tu Dropbox', 'Guardar y compartir carpetas'], set()),
    ('Tamaño', ['Galería: hasta tu cuota · Archivos: hasta 150 GB por archivo (Estudio)', '3 GB/30 días (Free); 300 GB/30 días (Starter); hasta 1 TB por envío (Ultimate)', '50 GB (Plus) a 250 GB (Business Plus)', 'Hasta tu cuota'], set()),
    ('Caducidad del enlace', ['No caduca', WT_CADUCA, '7 días (Plus); fecha a tu elección en planes de equipo', 'No caduca'], {0, 3}),
    ('Tu marca', [POS_MARCA, 'Página y fondos propios en Ultimate', 'Logo y fondo en planes de equipo', 'No'], {0}),
    ('Revisión', [POS_REV, 'No', 'Comentarios en archivos; al fotograma, con Replay (aparte)', 'Comentarios sobre archivos, con cuenta de Google'], {0}),
    ('Pedir archivos a terceros', [POS_PEDIR, WT_PEDIR, 'Sí, en todos los planes, sin cuenta; de 2 GB (Basic/Plus) a 250 GB por archivo', 'Solo con Forms o carpeta compartida: pide cuenta de Google'], {2}),
    ('Plan gratis', [POS_GRATIS, '10 envíos o 3 GB cada 30 días; solo uso no comercial', '2 GB', '15 GB compartidos con Gmail y Fotos'], set()),
    ('Precio', [PRECIO_POS, WT_PRECIO, 'Incluido en Dropbox (Plus, 119,88 $/año: 9,99 $/mes con facturación anual)', '15 GB gratis; Workspace desde 84 $/usuario/año (7 $/mes)'], set()),
  ],
  nota='SwissTransfer y Smash, en sus apartados del artículo.'),

'frame-io': dict(
  cols=[('Positiva', True), ('Frame.io', False), ('Vimeo', False), ('Dropbox Replay', False)],
  filas=[
    ('Comentarios en vídeo', [POS_COM_VIDEO, 'Por fotograma, por rango y anotaciones dibujadas', 'Con código de tiempo; el invitado comenta sin cuenta', REPLAY_COM], {1}),
    ('Exporta al editor', [POS_EXPORTA, FRAME_EDITOR, VIMEO_EDITOR, REPLAY_EDITOR], set()),
    ('Fotografía', ['Galerías con favoritas, comentarios y exportación a Lightroom', 'Sí, con visor y enlaces de revisión', 'No', 'No'], {0}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Cualquier archivo, hasta 5 TB, con carpetas', 'Solo vídeo', 'Tu Dropbox, con cualquier archivo'], {1}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Sin función propia', 'Solo programándolo con su API', 'Con las solicitudes de Dropbox, sin cuenta'], set()),
    ('Entrega y portfolio', ['Entrega con tu marca (Autor y Estudio) + portfolio público', 'Presentaciones con marca (desde Pro), sin portfolio', 'Showcases y portfolios de vídeo (desde Standard)', 'No'], {0}),
    ('Almacenamiento', ['250 GB (Autor) · 1 TB (Estudio)', '2 TB (Pro, +2 TB por miembro)', '4 TB (Standard)', 'El de tu Dropbox (2 TB en Plus)'], {2}),
    ('Modelo de precio', ['Por cuenta, revisores ilimitados', 'Por miembro', 'Por asiento', 'Por usuario, sobre un plan de Dropbox'], {0}),
    ('Precio de referencia', [PRECIO_POS, 'Pro: 180 $/miembro/año + impuestos (15 $/mes)', 'Standard: 300 $/asiento/año (25 $/mes)', '120 $/usuario/año (10 $/mes) + plan de Dropbox'], {0}),
  ]),

'vimeo': dict(
  cols=[('Positiva', True), ('Vimeo', False), ('Frame.io', False), ('Dropbox Replay', False)],
  filas=[
    ('Comentarios en vídeo', [POS_COM_VIDEO, 'Con código de tiempo; el invitado comenta sin cuenta', 'Por fotograma, por rango y anotaciones', REPLAY_COM], {2}),
    ('Exporta al editor', [POS_EXPORTA, VIMEO_EDITOR, FRAME_EDITOR, REPLAY_EDITOR], set()),
    ('Fotografía', ['Galerías con favoritas y comentarios', 'No', 'Sí, con visor y enlaces de revisión', 'No'], {0}),
    ('Vídeo público y directos', ['No', 'Sí: reproductor incrustable y showcases; directos en Advanced', 'No', 'No'], {1}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Solo vídeo', 'Cualquier archivo, hasta 5 TB, con carpetas', 'Tu Dropbox, con cualquier archivo'], {2}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Solo programándolo con su API', 'Sin función propia', 'Con las solicitudes de Dropbox, sin cuenta'], set()),
    ('Almacenamiento', ['250 GB (Autor) · 1 TB (Estudio)', '4 TB (Standard)', '2 TB (Pro)', 'El de tu Dropbox (2 TB en Plus)'], {1}),
    ('Modelo de precio', ['Por cuenta, revisores ilimitados', 'Por asiento', 'Por miembro', 'Por usuario, sobre un plan de Dropbox'], {0}),
    ('Precio de referencia', [PRECIO_POS, 'Standard: 300 $/asiento/año (25 $/mes)', 'Pro: 180 $/miembro/año + impuestos (15 $/mes)', '120 $/usuario/año (10 $/mes) + plan de Dropbox'], {0}),
  ]),

'dropbox-replay': dict(
  cols=[('Positiva', True), ('Dropbox Replay', False), ('Frame.io', False), ('Vimeo', False)],
  filas=[
    ('Comentarios en vídeo', [POS_COM_VIDEO, REPLAY_COM, 'Por fotograma, por rango y anotaciones', 'Con código de tiempo; el invitado comenta sin cuenta'], {2}),
    ('Audio', ['No', 'Sí, sin pérdida', 'No como producto propio', 'No'], {1}),
    ('Exporta al editor', [POS_EXPORTA, REPLAY_EDITOR, FRAME_EDITOR, VIMEO_EDITOR], set()),
    ('Entrega al cliente', ['Galería con tu marca (Autor y Estudio) + portfolio', 'No', 'Presentaciones con marca, sin portfolio', 'Showcases y portfolios de vídeo'], {0}),
    ('Guardar tus archivos', [POS_GUARDAR, 'Tu Dropbox sincronizado, con cualquier archivo', 'Cualquier archivo, hasta 5 TB', 'Solo vídeo'], {1}),
    ('Pedir archivos a terceros', [POS_PEDIR, 'Con las solicitudes de Dropbox, sin cuenta', 'Sin función propia', 'Solo programándolo con su API'], set()),
    ('Modelo de precio', ['Una cuota, revisores ilimitados', 'Por usuario + plan de Dropbox', 'Por miembro', 'Por asiento'], {0}),
    ('Precio de referencia', [PRECIO_POS, '120 $/usuario/año (10 $/mes) + plan de Dropbox', 'Pro: 180 $/miembro/año + impuestos (15 $/mes)', 'Standard: 300 $/asiento/año (25 $/mes)'], {0}),
  ]),

'arcadina': dict(
  cols=[('Positiva', True), ('Arcadina', False), ('Pixieset', False), ('Pic-Time', False)],
  filas=[
    ('Vídeo en la galería', ['Alojado, junto a las fotos', 'Enlace de YouTube o Vimeo', PIXIESET_VIDEO, 'Cuota aparte (30 GB en Professional)'], {0}),
    ('Revisión', [POS_REV, 'Favoritas + comentario en las fotos seleccionadas', 'Favoritas de foto, con notas', 'Favoritas y selección (desde Professional)'], {0}),
    ('Guardar tus archivos y pedirlos a terceros', [POS_PEDIR + '; carpetas y envíos', NE, NE, PICTIME_SUBIDA], {0}),
    ('Web pública', [POS_PORTFOLIO, 'Sí, plan Web aparte', 'Módulo aparte', 'Portfolio Page embebible'], set()),
    ('Tienda', ['No', 'Sí, sin comisión', 'Módulo aparte', 'Sí, 30+ laboratorios'], set()),
    ('Gestión del negocio', ['No', 'Sí, plan Manager aparte', 'Studio Manager, aparte', 'No'], set()),
    ('Idioma del panel', ['Español', 'Español', 'Inglés', 'Inglés, con traducción automática'], {0, 1}),
    ('Precio de referencia', [PRECIO_POS, 'Negocio, 30 GB: desde 120 €/año, IVA incl. (10 €/mes con pago anual)', 'Plus, 100 GB: 192 $/año (16 $/mes con facturación anual)', 'Professional: 252 $/año (21 $/mes con facturación anual)'], {0}),
  ],
  nota='PSPro y Zenfolio, en sus apartados del artículo.'),

# ── Páginas positiva-vs-* ────────────────────────────────────────────────
'vs-pictime-pixieset': dict(
  cols=[('Positiva Autor', True), ('Positiva Estudio', True), ('Pic-Time Professional', False), ('Pixieset Plus', False)],
  filas=[
    ('Precio', ['89 €/año + IVA (o 8,95 €/mes)', '219 €/año + IVA (o 22,95 €/mes)', '252 $/año (21 $/mes con facturación anual)', '192 $/año (16 $/mes con facturación anual)'], {0}),
    ('Espacio para fotos y vídeos', ['250 GB compartidos', '1 TB compartido', '100 GB + 30 GB de vídeo', '100 GB compartidos'], {1}),
    ('¿El vídeo tiene una cuota aparte?', ['No', 'No', 'Sí', 'No en Plus (en Basic, 30 min de HD)'], {0, 1, 3}),
    ('Selección de favoritos del cliente', ['Sí, en todos los planes', 'Sí', 'Sí (desde Professional)', 'Sí, con notas'], set()),
    ('Tu marca en la galería', ['Logo, colores y tipografía', 'Lo mismo + multimarca', 'Sí, sin la marca de Pic-Time', 'Logo y marca propios, sin la de Pixieset'], {1}),
    ('Dominio propio', ['No', 'Sí', 'Sí', 'Sí'], set()),
    ('Tus archivos y solicitudes a terceros', ['Compartir un archivo suelto con enlace', 'Carpetas, envíos y solicitudes; quien sube no necesita cuenta', PICTIME_SUBIDA, NE], {1}),
    ('Comisión si vendes copias o álbumes', ['0 % (no hay tienda)', '0 % (no hay tienda)', '8 % si cobra Pic-Time; 0 % si cobras tú', '0 % en planes de pago · 15 % en el gratis'], set()),
    ('Llevarte tus archivos al irte', ['ZIP con la estructura intacta, sin pedirlo a soporte', 'Igual', NE, NE], set()),
    ('Archivos alojados en la UE (RGPD)', ['Sí', 'Sí', 'No: servidores en la UE, EE. UU. y Australia', 'Su DPA permite transferencias fuera del EEE, sin compromiso de UE'], {0, 1}),
    ('No entrena IA con tu material', ['Nunca', 'Nunca', 'Indexa tus imágenes salvo opt-out y puede entrenar con una pequeña parte', NE], {0, 1}),
  ],
  nota='Pixieset Pro (288 $/año, 24 $/mes con facturación anual, 1 TB) sale de la tabla para que se lea entera: mismas funciones que Plus con más espacio.'),

'vs-arcadina': dict(
  cols=[('Positiva Autor', True), ('Positiva Estudio', True), ('Arcadina Exposure', False), ('Arcadina Focus', False)],
  filas=[
    ('Precio', ['89 €/año + IVA (o 8,95 €/mes)', '219 €/año + IVA (o 22,95 €/mes)', '240 €/año, imp. incl. (20 €/mes con pago anual)', '360 €/año, imp. incl. (30 €/mes con pago anual)'], {0}),
    ('Espacio para fotos y vídeos', ['250 GB compartidos', '1 TB compartido', '100 GB', '300 GB'], {1}),
    ('Revisión con comentarios (en vídeo, al fotograma)', ['Sí, exportables a DaVinci y Final Cut', 'Sí', 'Comentario en las fotos seleccionadas; en vídeo, no lo hemos encontrado', 'Igual'], {0, 1}),
    ('Selección de favoritas del cliente', ['Sí, con nombre y exportación a Lightroom, Finder, .txt y .csv', 'Sí', 'Sí', 'Sí'], set()),
    ('Diseños de entrega para vídeo', ['Estreno, Cartel, Vitrina, Montaje y Videoteca', 'Sí', 'Vídeo enlazado desde YouTube o Vimeo', 'Igual'], {0, 1}),
    ('Tu marca en la galería', ['Logo, colores y tipografía', 'Lo mismo + multimarca', 'Logo propio, sin la marca Arcadina', 'Igual'], {1}),
    ('Dominio propio', ['No', 'Sí', 'Sí, conectas tu dominio', 'Sí, conectas tu dominio'], {1, 2, 3}),
    ('Tus archivos y solicitudes a terceros', ['Compartir un archivo suelto con enlace', 'Carpetas, envíos y solicitudes; quien sube no necesita cuenta', NE, NE], {1}),
    ('Web del fotógrafo, tienda y reservas', ['Portfolio público · sin tienda ni reservas', 'Igual', 'Tienda sin comisiones · web y reservas en otros planes', 'Igual'], {2, 3}),
    ('Archivos alojados en la UE (RGPD)', ['Sí', 'Sí', 'No publica en qué país guarda los archivos', 'Ídem'], {0, 1}),
    ('No entrena IA con tu material', ['Nunca', 'Nunca', NE, 'Ídem'], {0, 1}),
  ],
  nota='Arcadina Aperture (120 €/año, 10 €/mes con pago anual, 30 GB) y Flash (600 €/año, 50 €/mes con pago anual, 1.000 GB), con impuestos incluidos, salen de la tabla para que se lea entera.'),

'vs-dropbox': dict(
  cols=[('Dropbox', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Almacenamiento y sincronización', 'Entregar y revisar fotos y vídeo con el cliente; también guardar, enviar y pedir archivos'], set()),
    ('El cliente recibe', ['Una carpeta de archivos', 'Una galería con tu marca (planes Autor y Estudio)'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['Logo y fondo en los envíos de planes de equipo; las carpetas, sin marca', 'Sí, en los planes Autor y Estudio'], {1}),
    ('El enlace caduca', ['No', 'No'], set()),
    ('El cliente elige sus favoritos', ['No', 'Sí, en todos los planes'], {1}),
    ('Comentarios sobre cada archivo', ['Sí; en vídeo, con código de tiempo solo en algunos planes (en Plus y Standard, en el segundo 0)', 'Sí: en foto, y por fotograma en vídeo (planes Autor y Estudio)'], {1}),
    ('Vídeo reproducible en la galería', ['Vista previa del archivo', 'Sí, en la galería, junto a las fotos'], {1}),
    ('Guardar tus archivos de trabajo', ['Cualquier archivo, sincronizado con tu ordenador', 'Carpetas y envíos con enlace (plan Estudio), sin sincronización'], {0}),
    ('Pedir archivos a terceros', ['Sí, en todos los planes, sin cuenta; de 2 GB a 250 GB por archivo', 'Sí, en el plan Estudio, sin cuenta; hasta 150 GB por archivo'], {0}),
    ('Portfolio / web pública', ['No', 'Sí (con vídeos, en Autor y Estudio)'], {1}),
    ('Precio de referencia', ['Plus · 2 TB · 119,88 $/año (9,99 $/mes con facturación anual)', 'Autor · 250 GB · 89 €/año + IVA (o 8,95 €/mes)'], set()),
  ]),

'vs-google-drive': dict(
  cols=[('Google Drive', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Almacenamiento en la nube', 'Entregar y revisar fotos y vídeo con el cliente; también guardar, enviar y pedir archivos'], set()),
    ('El cliente recibe', ['Una carpeta de archivos', 'Una galería con tu marca (planes Autor y Estudio)'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['No', 'Sí, en los planes Autor y Estudio'], {1}),
    ('El enlace caduca', ['No', 'No'], set()),
    ('El cliente elige sus favoritos', ['No', 'Sí, en todos los planes'], {1}),
    ('Comentarios sobre cada archivo', ['Sí, con cuenta de Google', 'Sí, sin cuenta; en vídeo, por fotograma (planes Autor y Estudio)'], {1}),
    ('Vídeo reproducible en la galería', ['Vista previa del archivo', 'Sí, en la galería, junto a las fotos'], {1}),
    ('Guardar tus archivos de trabajo', ['Cualquier archivo, sincronizado con tu ordenador', 'Carpetas y envíos con enlace (plan Estudio), sin sincronización'], {0}),
    ('Pedir archivos a terceros', ['Solo con Forms o carpeta compartida: pide cuenta de Google', 'Sí, en el plan Estudio, sin cuenta; hasta 150 GB por archivo'], {1}),
    ('Portfolio / web pública', ['No', 'Sí (con vídeos, en Autor y Estudio)'], {1}),
    ('Precio de referencia', ['15 GB gratis; Workspace Business Starter, 30 GB: 84 $/usuario/año (7 $/mes)', 'Autor · 250 GB · 89 €/año + IVA (o 8,95 €/mes)'], set()),
  ]),

'vs-wetransfer': dict(
  cols=[('WeTransfer', False), ('Positiva', True)],
  filas=[
    ('Pensado para', ['Envío de archivos', 'Entregar y revisar fotos y vídeo con el cliente; también enviar y pedir archivos'], set()),
    ('El cliente recibe', ['Un enlace de descarga', 'Una galería con tu marca (planes Autor y Estudio)'], {1}),
    ('Tu marca (logo, colores, tipografía)', ['Página y fondos propios en Ultimate', 'Sí, en los planes Autor y Estudio'], {1}),
    ('El enlace caduca', [WT_CADUCA, 'No'], {1}),
    ('Plan gratuito', ['10 envíos o 3 GB cada 30 días; solo uso no comercial', POS_GRATIS], {1}),
    ('El cliente elige sus favoritos', ['No', 'Sí, en todos los planes'], {1}),
    ('Comentarios sobre cada archivo', ['No', 'Sí: en foto, y por fotograma en vídeo (planes Autor y Estudio)'], {1}),
    ('Pedir archivos a terceros', [WT_PEDIR, 'Sí, en el plan Estudio, sin cuenta; lo recibido no caduca'], set()),
    ('Portfolio / web pública', ['No', 'Sí (con vídeos, en Autor y Estudio)'], {1}),
    ('Precio', [WT_PRECIO, 'Autor · 250 GB · 89 €/año + IVA (o 8,95 €/mes)'], set()),
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
