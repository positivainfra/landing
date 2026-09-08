# -*- coding: utf-8 -*-
# Contenido de los artículos de /notas/. Positiva siempre en el nº 1,
# con pros y contras honestos. Arcadina solo aparece en su propio artículo.
# Enfoque editorial: las tres verticales (Entrega · Revisión · Portfolio público)
# + precio. Precios de competidores verificados en sus webs (sep 2026):
#   SmugMug smugmug.com/plans: 7/11/27/41,99 $/mes (Pro ≈360 $/año facturado anual)
#   ShootProof shootproof.com/pricing: gratis 100 fotos·5GB; 1.500 fotos 10,99$/mes anual;
#     5.000 fotos (250GB) 19,99$/mes anual ≈240$/año; ilimitado 50$/mes
#   Zenfolio zenfolio.com/plans-pricing: Basic 7$/mes anual (15GB);
#     Professional 11,50$/mes anual ≈138$/año (150GB); Advanced 20$/mes anual
#   Frame.io frame.io/pricing: Free 2 miembros·2GB; Pro 15$/usuario/mes (≈13$ anual);
#     Team 25$/usuario/mes
#   WeTransfer (reestructurado): gratis ≈3GB/mes y enlaces que caducan a los 3 días;
#     Starter ≈8$/mes; Ultimate ≈19-23$/mes

D = '2026-09-06'
DH = '6 de septiembre de 2026'

# Bloque común: las tres verticales, con enlaces a las páginas de producto.
VERTICALES = """
<h2>Las tres verticales que importan</h2>
<p>Antes de comparar herramientas, conviene tener claro qué hace falta cubrir. El flujo completo de un profesional de la imagen tiene tres patas:</p>
<ul>
<li><strong><a href="/galerias/">Entrega</a>:</strong> que tu cliente reciba fotos y vídeos en una galería con tu marca, en un enlace que no caduca — no un ZIP ni una carpeta.</li>
<li><strong>Revisión:</strong> que el cliente marque favoritas y comente <a href="/revision-foto/">foto a foto</a> o <a href="/revision-video/">sobre el fotograma exacto del vídeo</a>, y que esa selección llegue a tu editor (Lightroom, DaVinci Resolve, Final Cut Pro).</li>
<li><strong><a href="/portfolio/">Portfolio público</a>:</strong> que tu web se actualice con las entregas que ya tienes, sin montar nada aparte.</li>
</ul>
<p>Casi todas las herramientas de esta lista cubren una pata, algunas dos. Cubrir las tres — y a qué precio — es lo que separa una suscripción más de una herramienta central.</p>
"""

ARTICLES = [

# ══ 1 · PIXIESET ══════════════════════════════════════════════════
dict(
slug='alternativas-a-pixieset',
title='Alternativas a Pixieset en español (2026) · Blog de Positiva',
h1='Alternativas a Pixieset en español (2026)',
desc='Las mejores alternativas a Pixieset para entregar galerías de fotos y vídeo a clientes: opciones en español, con precios en euros y datos en la UE.',
lede='Pixieset es la galería de clientes más conocida del mundo. Pero si trabajas en España, pagas en dólares, la interfaz está en inglés y el vídeo va aparte. Estas son las alternativas que tienen sentido en 2026.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Pic-Time', 'ShootProof', 'SmugMug', 'Zenfolio'],
body="""
<p>Pixieset hizo algo muy bien: convertir la entrega de fotos en una experiencia bonita para el cliente. Por eso la usan cientos de miles de fotógrafos. Pero «la más conocida» no siempre es «la que mejor encaja»: su interfaz de trabajo está en inglés, los precios van en dólares (192&nbsp;$ o 288&nbsp;$ al año en sus planes de pago habituales), el vídeo se mide por minutos en lugar de por gigas y el plan gratuito aplica comisión del 15&nbsp;% en la tienda.</p>
<p>Si buscas una alternativa a Pixieset <strong>en español</strong>, con precios en euros y pensada para foto <em>y</em> vídeo, esta es la lista honesta.</p>
""" + VERTICALES + """
<h2>1. Positiva — las tres verticales, en español</h2>
<p><a href="/">Positiva</a> es una plataforma española construida sobre esas tres patas. La <a href="/galerias/">entrega</a>: fotos y vídeos en la misma galería y el mismo enlace, con tu marca, tus diseños y sin caducar. La revisión: tu cliente marca favoritas y comenta <a href="/revision-foto/">foto a foto</a> o <a href="/revision-video/">sobre el fotograma exacto del vídeo</a>, y tú exportas la selección a Lightroom o los comentarios como marcadores a DaVinci Resolve y Final Cut Pro. Y el <a href="/portfolio/">portfolio público</a>: seleccionas lo mejor de tus entregas y en segundos está en tu web.</p>
<ul>
<li><strong>A favor:</strong> cubre entrega, revisión y portfolio en una sola cuota, en español y en euros (<a href="/precios/">Autor, 250&nbsp;GB, 89&nbsp;€&nbsp;+&nbsp;IVA/año; Estudio, 1&nbsp;TB, 219&nbsp;€&nbsp;+&nbsp;IVA/año</a>); foto y vídeo por igual, sin contar minutos; datos alojados en la Unión Europea; plan gratis de 15&nbsp;GB y 2 galerías sin tarjeta; 0&nbsp;% de comisión.</li>
<li><strong>En contra:</strong> no tiene tienda de impresión integrada: si tu negocio vive de vender álbumes y copias desde la galería, te faltará esa pieza.</li>
<li><strong>Para quién:</strong> fotógrafos y videógrafos en España y Latinoamérica que entregan foto y vídeo y quieren revisión seria, no solo descarga.</li>
</ul>

<h2>2. Pic-Time — la más parecida a Pixieset</h2>
<p>Pic-Time juega en la misma liga que Pixieset: galerías elegantes, tienda de impresión potente y automatizaciones de marketing para vender más copias. Su plan habitual ronda los 230&nbsp;€ al año con 100&nbsp;GB de fotos más 30&nbsp;GB de vídeo.</p>
<ul>
<li><strong>A favor:</strong> diseño de galería excelente; la tienda y las campañas automáticas son de lo mejor del mercado.</li>
<li><strong>En contra:</strong> cubre una vertical (entrega de foto): sin revisión de vídeo con timecode y sin portfolio web; interfaz de trabajo en inglés; el vídeo va limitado y aparte; datos sin garantía de residencia en la UE.</li>
<li><strong>Para quién:</strong> fotógrafos centrados en venta de impresiones a mercado internacional.</li>
</ul>

<h2>3. ShootProof — galerías más gestión</h2>
<p>ShootProof añade a las galerías una capa de negocio: contratos, facturas y pagos en la misma herramienta. Sus planes van por número de fotos: 100 fotos gratis, 1.500 fotos por 10,99&nbsp;$/mes facturado anual, y el plan de 5.000 fotos (hasta 250&nbsp;GB) por 19,99&nbsp;$/mes — unos 240&nbsp;$ al año, más del doble que el plan Autor de Positiva por el mismo almacenamiento.</p>
<ul>
<li><strong>A favor:</strong> contratos y facturación integrados; sin comisión en la venta de copias.</li>
<li><strong>En contra:</strong> una sola vertical (entrega de foto): sin vídeo, sin revisión con timecode y sin portfolio; pensada para el mercado norteamericano y facturada en dólares.</li>
<li><strong>Para quién:</strong> estudios de foto que quieren contrato, factura y galería en un solo sitio y trabajan solo con imagen fija.</li>
</ul>

<h2>4. SmugMug — almacenamiento de fotos sin límite</h2>
<p>SmugMug es la veterana del grupo: portfolio, galerías y subidas ilimitadas de fotos en todos sus planes, desde 7&nbsp;$/mes. El matiz: las herramientas de cliente serias llegan en el plan Pro, a 41,99&nbsp;$/mes — unos 360&nbsp;$ al año facturado anual.</p>
<ul>
<li><strong>A favor:</strong> fotos ilimitadas; comunidad enorme; webs de portfolio sólidas — su vertical fuerte es el portfolio.</li>
<li><strong>En contra:</strong> la entrega a cliente y la revisión son básicas y quedan lejos de las herramientas nacidas para ello; en inglés y en dólares; sin plan gratuito (solo prueba de 14 días); el plan con herramientas de cliente cuesta cuatro veces el plan Autor de Positiva.</li>
<li><strong>Para quién:</strong> quien prioriza archivo y portfolio por encima del flujo de entrega.</li>
</ul>

<h2>5. Zenfolio — la clásica todo en uno</h2>
<p>Zenfolio lleva dos décadas ofreciendo web, galerías y venta para fotógrafos. Su plan Professional cuesta 11,50&nbsp;$/mes facturado anual — unos 138&nbsp;$ al año — con 150&nbsp;GB; el Basic, a 7&nbsp;$/mes, incluye 15&nbsp;GB: justo lo que Positiva da gratis.</p>
<ul>
<li><strong>A favor:</strong> madura y completa: web, galerías, venta y reservas — toca la entrega y el portfolio.</li>
<li><strong>En contra:</strong> en inglés y en dólares; el producto ha cambiado varias veces de rumbo; sin foco en vídeo ni revisión con timecode.</li>
<li><strong>Para quién:</strong> fotógrafos que quieren una suite generalista antes que la mejor pieza de cada categoría.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Entrega con tu marca</th><th>Revisión (foto · vídeo)</th><th>Portfolio público</th><th>Plan gratis</th><th>Precio anual aprox.</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Foto y vídeo, mismo enlace</span></td><td><span class="pv-si">Foto y vídeo · export Lightroom, DaVinci, Final Cut</span></td><td><span class="pv-si">Sí, con tus entregas</span></td><td><span class="pv-si">15 GB · 2 galerías</span></td><td><span class="pv-si">89 € + IVA (250 GB)</span></td></tr>
<tr><td>Pixieset</td><td>Foto (vídeo por minutos)</td><td>Favoritas de foto</td><td>Producto aparte de la suite</td><td>3 GB</td><td>192–288 $</td></tr>
<tr><td>Pic-Time</td><td>Foto (vídeo limitado)</td><td>Favoritas de foto</td><td>No</td><td>3 GB</td><td>≈ 230 €</td></tr>
<tr><td>ShootProof</td><td>Solo foto</td><td>Favoritas de foto</td><td>No</td><td>100 fotos</td><td>≈ 240 $ (250 GB)</td></tr>
<tr><td>SmugMug</td><td>Básica</td><td>Básica</td><td>Sí</td><td>No (prueba)</td><td>≈ 360 $ (plan Pro)</td></tr>
<tr><td>Zenfolio</td><td>Foto</td><td>Proofing de foto</td><td>Sí</td><td>No (prueba)</td><td>≈ 138 $ (150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Leída así, la conclusión es incómoda para casi todas: ninguna cubre las tres verticales a la vez, y las que cubren dos cuestan más que Positiva, que cubre las tres por 89&nbsp;€&nbsp;+&nbsp;IVA al año.</p>

<h2>Nuestra recomendación</h2>
<p>Si vives de vender copias impresas a un público internacional, Pic-Time es una gran heredera de Pixieset. Para todo lo demás — <a href="/galerias/">entregar</a> foto y vídeo con tu marca, <a href="/revision-foto/">revisar con tu cliente</a> en español y tener tu <a href="/portfolio/">portfolio</a> siempre al día, en euros y con los datos en la UE — <a href="/">Positiva</a> es la alternativa que hemos construido precisamente porque no existía. Puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB y 2 galerías.</p>
""",
faq=[
('¿Hay alguna alternativa a Pixieset en español?',
 'Sí. Positiva es una plataforma española con el panel, las galerías y el soporte en español, precios en euros y datos alojados en la Unión Europea. Tiene plan gratuito de 15 GB y 2 galerías.'),
('¿Qué alternativa a Pixieset maneja mejor el vídeo?',
 'Pixieset y Pic-Time miden el vídeo en minutos o lo limitan aparte. Positiva trata fotos y vídeos por igual dentro del mismo almacenamiento, en la misma galería y el mismo enlace, y añade revisión de vídeo con exportación de comentarios a DaVinci Resolve y Final Cut Pro.'),
('¿Cuál es la alternativa a Pixieset con mejor relación calidad-precio?',
 'A almacenamiento comparable, Positiva es la más barata de la lista: 250 GB por 89 € + IVA al año, cubriendo entrega, revisión y portfolio. ShootProof cobra unos 240 $ al año por 250 GB solo de foto, y SmugMug unos 360 $ al año por su plan con herramientas de cliente.'),
('¿Puedo empezar gratis y migrar después?',
 'Sí. El plan gratuito de Positiva (15 GB, 2 galerías) permite montar una entrega real con tu marca antes de decidir. Las galerías creadas se conservan al pasar a un plan de pago.'),
],
),

# ══ 2 · PIC-TIME ══════════════════════════════════════════════════
dict(
slug='alternativas-a-pic-time',
title='Alternativas a Pic-Time para fotógrafos y videógrafos (2026) · Blog de Positiva',
h1='Alternativas a Pic-Time para fotógrafos y videógrafos (2026)',
desc='Guía de alternativas a Pic-Time: qué plataforma de galerías de clientes encaja según tu caso — vídeo, contratos, almacenamiento, idioma y precio. Datos verificados.',
lede='Pic-Time combina galerías de clientes con una tienda de impresiones y automatizaciones de venta. Si estás valorando un cambio — por precio, por vídeo, por idioma o porque no vendes copias — esta guía compara las alternativas según tu caso de uso.',
date_iso='2026-09-08', date_h='8 de septiembre de 2026',
list_names=['Positiva', 'Pixieset', 'ShootProof', 'SmugMug', 'Zenfolio'],
body="""
<p>Pic-Time es una plataforma de galerías de clientes centrada en la venta de impresiones: incluye tienda conectada a más de 30 laboratorios y automatizaciones de venta en todos sus planes. Su plan Professional cuesta 21&nbsp;$/mes con facturación anual — 252&nbsp;$/año — con 100&nbsp;GB para fotos y 30&nbsp;GB para vídeo.</p>
<p>No todos los perfiles necesitan ese ecosistema. Puedes buscar una alternativa a Pic-Time si el vídeo pesa más que las copias en tu negocio, si necesitas contratos y facturación integrados, si prefieres pagar en euros y trabajar con el panel en español, o si estás pagando una tienda que no usas.</p>

<h2>Qué alternativa a Pic-Time elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Entrega y revisión de foto y vídeo</td><td><a href="/">Positiva</a></td><td>Foto y vídeo en la misma galería, con comentarios por fotograma</td></tr>
<tr><td>Tienda de impresiones y suite completa</td><td>Pixieset</td><td>Galerías, web, tienda y gestión de estudio en un ecosistema</td></tr>
<tr><td>Contratos, facturas y pagos</td><td>ShootProof</td><td>Añade la gestión administrativa a las galerías</td></tr>
<tr><td>Almacenamiento de fotos sin límite</td><td>SmugMug</td><td>Subidas ilimitadas de fotos en todos los planes</td></tr>
<tr><td>Web, galerías y venta en una suite</td><td>Zenfolio</td><td>Combina web pública, galerías y herramientas de negocio</td></tr>
<tr><td>Vender impresiones con automatizaciones</td><td>Quedarte en Pic-Time</td><td>Su tienda y sus campañas automáticas siguen siendo su punto fuerte</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Pic-Time</h2>
<p>Los motivos que más aparecen al valorar una salida de Pic-Time:</p>
<ul>
<li><strong>El vídeo va aparte y limitado.</strong> El plan Professional incluye 30&nbsp;GB de vídeo; ampliarlo cuesta desde 10&nbsp;$/mes más (facturación anual) por 100&nbsp;GB adicionales.</li>
<li><strong>La revisión se queda en la selección.</strong> El cliente puede marcar favoritas y preparar selecciones, pero no hemos encontrado en su documentación pública comentarios de vídeo vinculados al fotograma, como los que ofrecen las herramientas de revisión.</li>
<li><strong>El panel de trabajo está en inglés.</strong> Las galerías que ve el cliente pueden configurarse en otros idiomas, y Pic-Time ofrece traducir el panel de forma automática (vía Google Translate), pero el producto está pensado en inglés.</li>
<li><strong>Pagas la tienda aunque no la uses.</strong> Si no vendes copias ni álbumes desde la galería, buena parte del producto no trabaja para ti.</li>
</ul>
<p>Y el motivo para quedarte: si las ventas de impresiones son una parte importante de tus ingresos, ninguna alternativa de esta lista replica exactamente la combinación de tienda, laboratorios y automatizaciones de Pic-Time — Pixieset es lo más cercano.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios, la documentación y los centros de ayuda de cada plataforma, y las hemos comparado según los criterios que más influyen al buscar una alternativa a Pic-Time: entrega de foto, vídeo, revisión, portfolio, tienda, gestión del negocio, idioma y precio. Positiva es nuestro producto, así que señalamos también los casos en los que otra plataforma encaja mejor.</p>

<h2>Positiva: mejor para entrega y revisión de foto y vídeo</h2>
<p><a href="/">Positiva</a> es una plataforma española de <a href="/galerias/">galerías de entrega</a> y revisión. Frente a Pic-Time, la diferencia principal es el reparto de prioridades: donde Pic-Time pone la tienda, Positiva pone el vídeo y la revisión — fotos y vídeos comparten galería, enlace y almacenamiento, y el cliente comenta <a href="/revision-foto/">foto a foto</a> o <a href="/revision-video/">sobre el fotograma exacto del vídeo</a>, con exportación de favoritas a Lightroom y de comentarios como marcadores a DaVinci Resolve y Final Cut Pro. El <a href="/portfolio/">portfolio público</a> se publica desde las entregas que ya tienes.</p>
<p><strong>Mejor para:</strong> fotógrafos y videógrafos que entregan foto y vídeo y necesitan revisión, trabajando en español.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Foto y vídeo en la misma galería y el mismo enlace, sin contar minutos: el almacenamiento (250&nbsp;GB o 1&nbsp;TB) es común.</li>
<li>Revisión de foto y de vídeo con comentarios por fotograma y exportación a Lightroom, DaVinci Resolve y Final Cut Pro.</li>
<li>Panel, galerías y soporte en español; precios en euros; datos alojados en la Unión Europea.</li>
<li>Plan gratuito de 15&nbsp;GB y 2 galerías, sin tarjeta.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Sin tienda de impresiones ni automatizaciones de venta: si las copias y los álbumes son una parte importante de tu negocio, Pic-Time o Pixieset encajan mejor.</li>
<li>Sin contratos, facturación ni CRM integrados.</li>
<li>El almacenamiento va por plan; no hay opción ilimitada como en SmugMug.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB.</p>
<p><strong>No la elegiríamos si:</strong> tu prioridad es vender impresiones desde la galería.</p>

<h2>Pixieset: mejor para tienda y suite completa</h2>
<p>Pixieset es la alternativa más parecida a Pic-Time: galerías de clientes con tienda de impresiones, más una suite que añade web, tienda propia y gestión de estudio. Frente a Pic-Time tiene sentido si quieres un ecosistema más amplio que las galerías, o su plan gratuito sin límite de galerías para empezar.</p>
<p><strong>Mejor para:</strong> quien quiere galerías con tienda dentro de una suite más amplia (web, gestión de estudio).</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Galerías ilimitadas en todos los planes, incluido el gratuito (3&nbsp;GB).</li>
<li>Tienda integrada; sin comisión en los planes de pago (en el gratuito, 15&nbsp;% por venta).</li>
<li>Suite modular: Client Gallery, Website, Store y Studio Manager se contratan por separado.</li>
<li>Las galerías que ve el cliente pueden configurarse en español.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>El vídeo se mide en minutos de metraje según el plan (30 minutos en el plan Basic), no en gigas; las descargas 4K llegan solo en Pro y Ultimate.</li>
<li>La revisión se centra en favoritas de foto; no hemos encontrado comentarios de vídeo por fotograma en su documentación pública.</li>
<li>El panel del fotógrafo está en inglés.</li>
</ul>
<p><strong>Precio:</strong> Client Gallery Plus, 16&nbsp;$/mes con facturación anual — 192&nbsp;$/año — con 100&nbsp;GB; Pro, 24&nbsp;$/mes anual — 288&nbsp;$/año — con 1&nbsp;TB. Con facturación mensual, 20 y 30&nbsp;$/mes.</p>

<h2>ShootProof: mejor para contratos y facturación</h2>
<p>ShootProof puede ser una alternativa a Pic-Time si quieres combinar la entrega de galerías con la gestión administrativa del estudio: contratos, facturas y pagos dentro de la misma plataforma, algo que Pic-Time no incluye. Los planes se dimensionan por número de fotos, no por gigas.</p>
<p><strong>Mejor para:</strong> estudios de foto que quieren galerías y papeleo (contratos, facturas, pagos) en una sola herramienta.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Contratos, facturación y pagos integrados en los planes de pago.</li>
<li>Venta de copias sin comisión de la plataforma.</li>
<li>Incluye una web sencilla (portada, página «sobre mí» y contacto).</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Los planes van por número de fotos: 1.500 fotos (hasta 75&nbsp;GB) o 5.000 fotos (hasta 250&nbsp;GB) en los tramos habituales.</li>
<li>No hemos encontrado soporte de vídeo en galerías en su documentación pública.</li>
<li>Producto orientado al mercado norteamericano, en inglés y en dólares.</li>
</ul>
<p><strong>Precio:</strong> 1.500 fotos, 8,33&nbsp;$/mes con facturación anual — unos 100&nbsp;$/año; 5.000 fotos, 16,67&nbsp;$/mes anual — unos 200&nbsp;$/año. Con facturación mensual, 9,99 y 19,99&nbsp;$/mes. Plan gratuito de 100 fotos y 5&nbsp;GB.</p>

<h2>SmugMug: mejor para almacenamiento de fotos sin límite</h2>
<p>SmugMug tiene sentido frente a Pic-Time si tu problema es el volumen: todos sus planes incluyen subidas ilimitadas de fotos, con webs de portfolio personalizables. Las herramientas de venta llegan en el plan Pro y las de cliente profesional en el plan Business.</p>
<p><strong>Mejor para:</strong> archivo y portfolio de grandes volúmenes de fotos.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Subidas de fotos ilimitadas en todos los planes.</li>
<li>Webs de portfolio con control de diseño.</li>
<li>Venta de impresiones y descargas en los planes Pro y Business.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Las herramientas de cliente profesional (proofing, marca) requieren el plan Business, el más caro.</li>
<li>Sin plan gratuito: prueba de 14 días.</li>
<li>En inglés y en dólares.</li>
</ul>
<p><strong>Precio:</strong> de 7 a 41,99&nbsp;$/mes con facturación mensual según plan (Basic, Power, Pro, Business); con facturación anual el descuento va del 29 al 38&nbsp;% — el plan Business queda en unos 357&nbsp;$/año.</p>

<h2>Zenfolio: mejor para una suite generalista</h2>
<p>Zenfolio es una alternativa a Pic-Time para quien prefiere una sola herramienta generalista — web pública, galerías, venta y reservas — antes que la mejor pieza de cada categoría. Lleva más de dos décadas en el mercado.</p>
<p><strong>Mejor para:</strong> fotógrafos que quieren web, galerías y herramientas de negocio en una suite.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Web pública, galerías de clientes, proofing de foto y venta en el mismo producto.</li>
<li>Reservas y herramientas de negocio incluidas.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Sin foco en vídeo ni revisión con comentarios por fotograma.</li>
<li>En inglés y en dólares; sin plan gratuito (prueba).</li>
</ul>
<p><strong>Precio:</strong> Basic, 7&nbsp;$/mes con facturación anual (15&nbsp;GB); Professional, 11,50&nbsp;$/mes anual — unos 138&nbsp;$/año — con 150&nbsp;GB; Advanced, 20&nbsp;$/mes anual.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Vídeo</th><th>Revisión</th><th>Portfolio / web</th><th>Tienda</th><th>Plan gratis</th><th>Precio anual (fact. anual)</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Por GB, junto a las fotos</span></td><td><span class="pv-si">Favoritas + comentarios en foto + comentarios de vídeo por fotograma</span></td><td>Portfolio con tus entregas</td><td>No</td><td>15 GB · 2 galerías</td><td>89 € + IVA (250 GB)</td></tr>
<tr><td>Pic-Time</td><td>30 GB en Professional (ampliable desde 10 $/mes)</td><td>Favoritas y selección</td><td>Portfolio Page (escaparate de galerías, embebible)</td><td>Sí, 30+ laboratorios + automatizaciones</td><td>3 GB de foto (tras 3 meses) · 1 GB de vídeo</td><td>252 $ (100 GB foto + 30 GB vídeo)</td></tr>
<tr><td>Pixieset</td><td>Por minutos según plan</td><td>Favoritas de foto</td><td>Website, producto aparte de la suite</td><td>Sí (15 % comisión en plan gratis)</td><td>3 GB</td><td>192 $ (100 GB)</td></tr>
<tr><td>ShootProof</td><td>No documentado</td><td>Favoritas de foto</td><td>Web sencilla incluida</td><td>Sí, sin comisión</td><td>100 fotos · 5 GB</td><td>≈ 200 $ (5.000 fotos · 250 GB)</td></tr>
<tr><td>SmugMug</td><td>Subidas de foto ilimitadas (vídeo según plan)</td><td>Proofing en plan Business</td><td>Sí, webs personalizables</td><td>Sí (Pro y Business)</td><td>No (prueba 14 días)</td><td>≈ 357 $ (Business)</td></tr>
<tr><td>Zenfolio</td><td>—</td><td>Proofing de foto</td><td>Web incluida</td><td>Sí</td><td>No (prueba)</td><td>138 $ (Professional, 150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Tenemos una comparativa más detallada de las tres primeras en <a href="/positiva-vs-pictime-vs-pixieset/">Positiva vs Pic-Time vs Pixieset</a>.</p>

<h2>Cómo decidir</h2>
<p>Si las ventas de impresiones sostienen tu negocio, Pic-Time sigue siendo difícil de sustituir; Pixieset es la alternativa más parecida y añade una suite más amplia. Si necesitas contratos y facturación integrados, ShootProof cubre ese hueco. Si tu problema es archivar volumen, SmugMug. Positiva es nuestra recomendación para fotógrafos y videógrafos que priorizan <a href="/galerias/">entregar</a> y <a href="/revision-video/">revisar</a> foto y vídeo con su marca, quieren trabajar en español y en euros, y no necesitan tienda de impresiones — puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB antes de decidir.</p>
""",
faq=[
('¿Cuál es la alternativa más parecida a Pic-Time?',
 'Pixieset: galerías de clientes con tienda de impresiones y automatizaciones, dentro de una suite que añade web y gestión de estudio. Es la opción con el solape funcional más alto.'),
('¿Qué alternativa a Pic-Time funciona mejor con vídeo?',
 'Positiva trata fotos y vídeos por igual dentro del mismo almacenamiento y añade revisión de vídeo con comentarios por fotograma. En Pic-Time el vídeo tiene su propio límite (30 GB en el plan Professional, ampliable con un add-on desde 10 $/mes) y en Pixieset se mide en minutos según el plan.'),
('¿Qué alternativas tienen la experiencia en español?',
 'Conviene separar panel y galería. Positiva tiene panel, galerías y soporte en español. En Pic-Time y Pixieset las galerías que ve el cliente pueden configurarse en español, pero el panel de trabajo está en inglés (Pic-Time ofrece una traducción automática del panel).'),
('¿Hay alternativas a Pic-Time gratuitas?',
 'Con plan gratuito permanente: Positiva (15 GB y 2 galerías), Pixieset (3 GB, con 15 % de comisión en la tienda) y ShootProof (100 fotos, 5 GB). SmugMug y Zenfolio solo ofrecen periodo de prueba. El plan gratuito de Pic-Time queda en 3 GB de foto y 1 GB de vídeo a los 3 meses.'),
('¿Puedo migrar mis galerías desde Pic-Time?',
 'No hemos encontrado migraciones automáticas oficiales entre estas plataformas. El camino habitual es descargar los originales (o recuperarlos de tu archivo local) y volver a subirlos; las galerías nuevas no conservan favoritas ni pedidos históricos de Pic-Time.'),
('¿Qué opción es mejor si no vendo impresiones?',
 'Si tampoco necesitas contratos ni facturación, Positiva o SmugMug según tu prioridad: revisión y entrega de foto y vídeo (Positiva) o archivo ilimitado de fotos (SmugMug). Si necesitas la gestión administrativa, ShootProof.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 8 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada plataforma.</p>',
),

# ══ 3 · WETRANSFER ════════════════════════════════════════════════
dict(
slug='alternativas-a-wetransfer',
title='Alternativas a WeTransfer para fotógrafos, gratis (2026) · Blog de Positiva',
h1='Alternativas a WeTransfer para fotógrafos (2026)',
desc='Alternativas gratis a WeTransfer para entregar fotos y vídeos a clientes: enlaces que no caducan, con tu marca y sin publicidad. Comparativa honesta 2026.',
lede='WeTransfer sirve para enviar archivos. Pero una entrega profesional no es un envío: es tu marca, tu enlace que no caduca y tu cliente disfrutando el trabajo. Estas son las alternativas — varias, gratis.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'SwissTransfer', 'Smash', 'Google Drive', 'Dropbox'],
body="""
<p>Todos hemos entregado un trabajo por WeTransfer. Y todos hemos recibido el mismo mensaje una semana después: «¿me lo puedes volver a pasar?». En su plan gratuito actual los envíos van muy limitados (unos 3&nbsp;GB al mes) y los enlaces caducan a los tres días; quitarse los límites de verdad cuesta unos 19–23&nbsp;$ al mes. Y lo que el cliente ve es un ZIP gris — no tus fotos, no tu marca.</p>
<p>Para archivos sueltos, WeTransfer cumple. Para <a href="/galerias/">entregar un proyecto a un cliente</a>, estas alternativas lo hacen mejor — y varias son gratis.</p>

<h2>Enviar no es entregar</h2>
<p>La diferencia no es cosmética. Un envío mueve bytes de A a B. Una <a href="/galerias/">entrega</a> pone tu marca delante, deja que el cliente vea las fotos y reproduzca los vídeos en el navegador, le permite <a href="/revision-foto/">marcar favoritas y comentar</a>, y sigue viva dentro de seis meses. Y si la herramienta además alimenta tu <a href="/portfolio/">portfolio público</a>, cada entrega trabaja para conseguirte el siguiente encargo. Ningún servicio de envío de archivos hace nada de esto.</p>

<h2>1. Positiva — entrega profesional, gratis hasta 15 GB</h2>
<p><a href="/">Positiva</a> no envía archivos: entrega proyectos. Subes fotos y vídeos, eliges un diseño con tu logo y tus colores, y tu cliente recibe una <a href="/galerias/">galería con tu marca</a> en un enlace que no caduca. Puede verlo todo en el navegador, <a href="/revision-foto/">marcar favoritas y comentar</a> — también <a href="/revision-video/">sobre el fotograma exacto del vídeo</a> — y descargar en la calidad que tú decidas.</p>
<ul>
<li><strong>A favor:</strong> gratis hasta 15&nbsp;GB y 2 galerías — cinco veces el límite mensual gratuito de WeTransfer, sin caducidad; tu marca y tu diseño, sin publicidad; foto y vídeo en el mismo enlace; revisión y <a href="/portfolio/">portfolio</a> incluidos; en español y con los datos en la UE. Si te quedas corto, <a href="/precios/">el plan Autor da 250&nbsp;GB por 89&nbsp;€&nbsp;+&nbsp;IVA/año</a> — menos de la mitad de lo que cuesta el plan sin límites de WeTransfer, que sigue sin poner tu marca.</li>
<li><strong>En contra:</strong> pensada para foto y vídeo: si envías otro tipo de archivos (PDF, audio, proyectos), necesitarás otra herramienta para eso.</li>
<li><strong>Para quién:</strong> fotógrafos, videógrafos y productoras que entregan trabajo visual a clientes.</li>
</ul>

<h2>2. SwissTransfer — envíos grandes y gratuitos</h2>
<p>El servicio gratuito de la suiza Infomaniak permite envíos de hasta 50&nbsp;GB con caducidad de hasta 30 días.</p>
<ul>
<li><strong>A favor:</strong> 50&nbsp;GB gratis por envío, sin cuenta; empresa europea.</li>
<li><strong>En contra:</strong> sigue siendo un envío: enlace que caduca, sin marca, sin galería, sin revisión, sin portfolio.</li>
<li><strong>Para quién:</strong> mover archivos brutos muy grandes de un punto a otro, una vez.</li>
</ul>

<h2>3. Smash — sin límite de tamaño</h2>
<p>La francesa Smash no limita el tamaño en su plan gratuito (los envíos muy grandes esperan cola).</p>
<ul>
<li><strong>A favor:</strong> sin límite de tamaño; personalización básica del enlace.</li>
<li><strong>En contra:</strong> caducidad en el plan gratuito; la experiencia sigue siendo «descargar un paquete».</li>
<li><strong>Para quién:</strong> envíos puntuales enormes sin pelearse con límites.</li>
</ul>

<h2>4. Google Drive — el cajón compartido</h2>
<ul>
<li><strong>A favor:</strong> 15&nbsp;GB gratis, lo tiene todo el mundo, los enlaces no caducan; ampliar a 100&nbsp;GB cuesta unos 20&nbsp;€/año.</li>
<li><strong>En contra:</strong> los 15&nbsp;GB se comparten con Gmail y Fotos; permisos confusos; el cliente ve carpetas, no una entrega; sin marca, sin revisión, sin portfolio.</li>
<li><strong>Para quién:</strong> compartir material de trabajo interno, no entregar a un cliente. Lo contamos en detalle en <a href="/positiva-vs-google-drive/">Positiva vs Google Drive</a>.</li>
</ul>

<h2>5. Dropbox — sincronizar no es entregar</h2>
<ul>
<li><strong>A favor:</strong> sincronización impecable entre equipos; enlaces estables.</li>
<li><strong>En contra:</strong> el plan gratuito es muy pequeño (2&nbsp;GB) y el de pago (≈&nbsp;120&nbsp;€/año por 2&nbsp;TB) sigue enseñando una carpeta, no tu marca. Más en <a href="/positiva-vs-dropbox/">Positiva vs Dropbox</a>.</li>
<li><strong>Para quién:</strong> flujo interno de equipo, copias de trabajo.</li>
</ul>

<h2>Comparativa: entrega, revisión, portfolio — y precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Entrega con tu marca</th><th>Revisión</th><th>Portfolio público</th><th>Gratis</th><th>De pago</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Galería, no caduca</span></td><td><span class="pv-si">Favoritas y comentarios, foto y vídeo</span></td><td><span class="pv-si">Sí</span></td><td><span class="pv-si">15 GB · 2 galerías</span></td><td><span class="pv-si">89 € + IVA/año · 250 GB</span></td></tr>
<tr><td>WeTransfer</td><td>No · enlace caduca en días</td><td>No</td><td>No</td><td>≈ 3 GB/mes</td><td>≈ 8–23 $/mes</td></tr>
<tr><td>SwissTransfer</td><td>No · caduca en ≤ 30 días</td><td>No</td><td>No</td><td>50 GB por envío</td><td>—</td></tr>
<tr><td>Smash</td><td>No · caduca (gratuito)</td><td>No</td><td>No</td><td>Sin límite de tamaño</td><td>Planes de pago</td></tr>
<tr><td>Google Drive</td><td>No · carpetas</td><td>No</td><td>No</td><td>15 GB compartidos</td><td>≈ 20 €/año · 100 GB</td></tr>
<tr><td>Dropbox</td><td>No · carpetas</td><td>No</td><td>No</td><td>2 GB</td><td>≈ 120 €/año · 2 TB</td></tr>
</tbody>
</table>
</div>
<p>La comparativa completa está en <a href="/positiva-vs-wetransfer/">Positiva vs WeTransfer</a>.</p>

<h2>Nuestra recomendación</h2>
<p>Para mover un archivo suelto, SwissTransfer o Smash resuelven gratis y rápido. Para <strong>entregar tu trabajo</strong> — que tu cliente lo vea con tu marca, lo <a href="/revision-foto/">comente</a> y no te vuelva a pedir el enlace, y que cada entrega sume a tu <a href="/portfolio/">portfolio</a> — <a href="/">Positiva</a> es gratis hasta 15&nbsp;GB y tarda cinco minutos en <a href="https://app.positiva.studio/registro">probarse</a>.</p>
""",
faq=[
('¿Cuál es la mejor alternativa gratuita a WeTransfer para fotógrafos?',
 'Positiva ofrece 15 GB y 2 galerías gratis con enlaces que no caducan y tu marca — frente a los ~3 GB mensuales y 3 días de caducidad del plan gratuito de WeTransfer. Para envíos puntuales de archivos muy grandes, SwissTransfer permite hasta 50 GB por envío.'),
('¿Por qué no entregar las fotos por WeTransfer?',
 'Porque el enlace caduca a los pocos días, los envíos gratuitos van muy limitados y el cliente recibe un ZIP en lugar de una galería con tu marca donde pueda ver, comentar y descargar. Funciona para enviar, no para entregar.'),
('¿Puedo entregar vídeo además de fotos?',
 'Sí. En Positiva las fotos y los vídeos van en la misma galería y el mismo enlace, y el vídeo se reproduce en el navegador antes de descargarse.'),
],
),

# ══ 4 · FRAME.IO ══════════════════════════════════════════════════
dict(
slug='alternativas-a-frame-io',
title='Alternativas a Frame.io en español (2026) · Blog de Positiva',
h1='Alternativas a Frame.io en español (2026)',
desc='Alternativas a Frame.io para revisar vídeo con clientes: comentarios en el fotograma, exportación a DaVinci Resolve y Final Cut, en español y en euros.',
lede='Frame.io es la referencia en revisión de vídeo — y se nota en el precio por usuario y en que todo ocurre en inglés. Si revisas con clientes en español y editas en DaVinci o Final Cut, hay alternativas más razonables.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Vimeo', 'Dropbox Replay', 'Filestage'],
body="""
<p>Frame.io, hoy parte de Adobe, definió cómo se revisa vídeo online: comentarios anclados al timecode, versiones, integración profunda con Premiere. Si tu equipo vive dentro del ecosistema Adobe, es difícil de batir.</p>
<p>Pero para muchos videógrafos y productoras pequeñas sobra la mitad — y falta la otra mitad. Sobra: pagar por usuario (15&nbsp;$/usuario/mes el plan Pro; para un equipo de tres, unos 540&nbsp;$ al año) con la interfaz en inglés, cuando quien comenta es tu cliente. Falta: Frame.io revisa, pero no <a href="/galerias/">entrega</a> el proyecto terminado con tu marca ni te da un <a href="/portfolio/">portfolio público</a>. Estas son las alternativas en 2026.</p>

<h2>2. Vimeo — revisión dentro del ecosistema de vídeo</h2>
<ul>
<li><strong>A favor:</strong> reproductor excelente; herramientas de revisión con notas en el tiempo en sus planes de pago; marca conocida por los clientes.</li>
<li><strong>En contra:</strong> la revisión va ligada a planes por usuario y al mes; interfaz en inglés en buena parte del flujo; es alojamiento de vídeo, no entrega de proyectos de foto y vídeo ni portfolio propio.</li>
<li><strong>Para quién:</strong> quien ya aloja su portfolio de vídeo en Vimeo y quiere revisión sin salir de ahí.</li>
</ul>

<h2>3. Dropbox Replay — si ya vives en Dropbox</h2>
<ul>
<li><strong>A favor:</strong> comentarios en el fotograma sobre los archivos que ya tienes en Dropbox; incluido de serie en varios planes.</li>
<li><strong>En contra:</strong> atado al ecosistema Dropbox y a sus precios por usuario; en inglés; la entrega final sigue siendo una carpeta y el portfolio no existe.</li>
<li><strong>Para quién:</strong> equipos cuyo almacenamiento ya es Dropbox.</li>
</ul>

<h2>4. Filestage — revisión de todo tipo de archivos</h2>
<ul>
<li><strong>A favor:</strong> revisa vídeo, PDF, imágenes y webs con flujos de aprobación formales.</li>
<li><strong>En contra:</strong> precios de herramienta corporativa, por usuario; en inglés; excesiva para un estudio pequeño; solo cubre la revisión.</li>
<li><strong>Para quién:</strong> departamentos de marketing con procesos de aprobación en varios pasos.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Revisión de vídeo</th><th>Export a DaVinci / Final Cut</th><th>Entrega con tu marca</th><th>Portfolio público</th><th>Precio</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">En el fotograma, sin registro para el cliente</span></td><td><span class="pv-si">Sí · EDL y FCPXML</span></td><td><span class="pv-si">Sí, foto y vídeo</span></td><td><span class="pv-si">Sí</span></td><td><span class="pv-si">89 € + IVA/año, sin pagar por usuario</span></td></tr>
<tr><td>Frame.io</td><td>En el fotograma</td><td>Parcial (foco en Premiere)</td><td>No</td><td>No</td><td>Gratis: 2 GB · 2 miembros; Pro 15 $/usuario/mes</td></tr>
<tr><td>Vimeo</td><td>Notas en el tiempo (pago)</td><td>No</td><td>Página de vídeo</td><td>Perfil de vídeo</td><td>Por usuario/mes</td></tr>
<tr><td>Dropbox Replay</td><td>En el fotograma</td><td>No</td><td>Carpeta</td><td>No</td><td>Según plan Dropbox, por usuario</td></tr>
<tr><td>Filestage</td><td>En el fotograma</td><td>No</td><td>No</td><td>No</td><td>Por usuario, corporativo</td></tr>
</tbody>
</table>
</div>
<p>El patrón se repite: todas revisan, ninguna entrega con tu marca ni alimenta un portfolio — y todas cobran por usuario. Un equipo de tres en Frame.io Pro paga unos 540&nbsp;$ al año solo por revisar; <a href="/precios/">el plan Autor de Positiva cuesta 89&nbsp;€&nbsp;+&nbsp;IVA al año</a> y cubre revisión, entrega y portfolio sin contar asientos.</p>

<h2>Nuestra recomendación</h2>
<p>Si tu casa es Premiere y la postproducción interna de un equipo grande, Frame.io sigue siendo la referencia. Si revisas con clientes en español y terminas en DaVinci Resolve o Final Cut Pro, <a href="/revision-video/">la revisión de vídeo de Positiva</a> hace exactamente ese recorrido — comentario del cliente → marcador en tu timeline — y de paso resuelve <a href="/galerias/">la entrega del máster</a> y tu <a href="/portfolio/">portfolio</a>, por una fracción del precio. <a href="https://app.positiva.studio/registro">Pruébala gratis</a>.</p>
""",
faq=[
('¿Hay alguna alternativa a Frame.io en español?',
 'Sí. Positiva es una plataforma española: tu cliente comenta el vídeo en español sobre el fotograma exacto y tú exportas los comentarios como marcadores a DaVinci Resolve o Final Cut Pro.'),
('¿Cómo llevo los comentarios del cliente a DaVinci Resolve o Final Cut?',
 'Positiva exporta las notas de cada ronda como EDL (DaVinci Resolve) o FCPXML (Final Cut Pro); al importarlas aparecen como marcadores sobre tu timeline, en el fotograma exacto de cada comentario.'),
('¿Necesita mi cliente registrarse para comentar?',
 'No. Abre el enlace de la galería con tu marca y comenta directamente sobre el vídeo, sin crear cuenta ni instalar nada.'),
('¿Cuánto cuesta Frame.io frente a Positiva?',
 'Frame.io Pro cuesta 15 $ por usuario al mes — unos 540 $ al año para un equipo de tres. Positiva cuesta 89 € + IVA al año en total, sin pagar por usuario, e incluye además la entrega con tu marca y el portfolio.'),
],
extra_positiva="""
<h2>1. Positiva — revisión con tu cliente, y además entrega y portfolio</h2>
<p><a href="/revision-video/">Positiva</a> es una plataforma española de galerías de entrega y revisión de fotos y vídeo. Tu cliente abre un enlace con tu marca, comenta sobre el fotograma exacto — sin registrarse ni aprender nada — y tú exportas todos los comentarios como marcadores a DaVinci Resolve (EDL) o Final Cut Pro (FCPXML). Cuando la pieza se aprueba, la misma galería es <a href="/galerias/">la entrega del máster con tu marca</a>, y lo mejor de cada proyecto alimenta tu <a href="/portfolio/">portfolio público</a>.</p>
<ul>
<li><strong>A favor:</strong> pensada para el cliente final, no para editores: comentar es tan fácil como escribir; exportación nativa a DaVinci y Final Cut; rondas de revisión; las tres verticales — <a href="/galerias/">entrega</a>, revisión y <a href="/portfolio/">portfolio</a> — en una sola cuota <a href="/precios/">(Autor: 250&nbsp;GB, 89&nbsp;€&nbsp;+&nbsp;IVA/año)</a>, sin pagar por asiento; datos en la UE; plan gratis de 15&nbsp;GB.</li>
<li><strong>En contra:</strong> no tiene integración con Premiere ni panel dentro del editor, y no está pensada para postproducción interna de equipos grandes (versionado de secuencias, aprobaciones por departamento).</li>
<li><strong>Para quién:</strong> videógrafos y productoras que revisan con clientes — dirección, agencia, cliente final — y editan en DaVinci o Final Cut.</li>
</ul>
""",
),

# ══ 5 · ARCADINA ══════════════════════════════════════════════════
dict(
slug='alternativas-a-arcadina',
title='Alternativas a Arcadina (2026) · Blog de Positiva',
h1='Alternativas a Arcadina (2026)',
desc='Alternativas a Arcadina para fotógrafos: galerías de entrega y revisión de fotos y vídeo, portfolio web y precios claros. Comparativa honesta 2026.',
lede='Arcadina lleva años haciendo webs para fotógrafos en España. Si lo que buscas es web con tienda, cumple. Si tu prioridad es entregar y revisar foto y vídeo con clientes, estas alternativas encajan mejor.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Pixieset', 'Pic-Time', 'SmugMug', 'Zenfolio'],
body="""
<p>Arcadina es una empresa española centrada en crear webs para fotógrafos: plantillas, dominio, blog y tienda, con galerías de clientes como complemento. Para tener presencia online con soporte en español, es una opción razonable y veterana.</p>
<p>El matiz importante: su producto es <em>la web</em>. Si tu día a día es <a href="/galerias/">entregar proyectos</a>, recoger <a href="/revision-foto/">la selección del cliente</a> y <a href="/revision-video/">revisar vídeo</a>, necesitas una herramienta cuyo centro sea ese flujo. Estas son las alternativas a Arcadina en 2026.</p>
""" + VERTICALES + """
<h2>1. Positiva — entrega y revisión primero, también española</h2>
<p><a href="/">Positiva</a> es la otra plataforma española de la lista, y ataca el problema desde el lado contrario: primero el flujo de trabajo — <a href="/galerias/">galerías de entrega con tu marca</a>, <a href="/revision-foto/">favoritas y comentarios del cliente</a>, <a href="/revision-video/">revisión de vídeo con exportación a DaVinci Resolve y Final Cut Pro</a> — y, con tus entregas, un <a href="/portfolio/">portfolio web público</a> que se actualiza en segundos.</p>
<ul>
<li><strong>A favor:</strong> las tres verticales cubiertas — entrega (foto y vídeo en el mismo enlace), revisión de verdad (foto a foto y fotograma a fotograma, con exportación a Lightroom, DaVinci y Final Cut) y portfolio con dominios propios; en español, en euros y con los datos en la UE; plan gratis de 15&nbsp;GB y 2 galerías; <a href="/precios/">precios claros: Autor 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB) y Estudio 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>.</li>
<li><strong>En contra:</strong> el portfolio nace de tus entregas y es deliberadamente simple: si necesitas una web completa con blog y tienda de copias, Positiva no es esa herramienta.</li>
<li><strong>Para quién:</strong> fotógrafos, videógrafos y productoras cuyo cuello de botella es la entrega y la revisión, no la web.</li>
</ul>

<h2>2. Pixieset — el ecosistema más conocido</h2>
<p>Galerías, web, tienda y gestión de estudio; planes de pago habituales de 192 a 288&nbsp;$ al año.</p>
<ul>
<li><strong>A favor:</strong> galerías de referencia mundial, web y tienda en la misma suite.</li>
<li><strong>En contra:</strong> en inglés y en dólares; el vídeo se mide por minutos; sin revisión de vídeo.</li>
<li><strong>Para quién:</strong> quien quiere el estándar internacional y no necesita el idioma.</li>
</ul>

<h2>3. Pic-Time — para vender impresiones</h2>
<p>≈&nbsp;230&nbsp;€ al año con 100&nbsp;GB de foto y 30&nbsp;GB de vídeo.</p>
<ul>
<li><strong>A favor:</strong> la mejor tienda de impresión y automatizaciones de venta.</li>
<li><strong>En contra:</strong> en inglés; vídeo limitado y aparte; sin portfolio web; pensada para mercados de print maduros.</li>
<li><strong>Para quién:</strong> fotógrafos cuyo negocio son las copias y los álbumes.</li>
</ul>

<h2>4. SmugMug — archivo y portfolio</h2>
<p>Fotos ilimitadas desde 7&nbsp;$/mes; las herramientas de cliente, en el plan Pro de 41,99&nbsp;$/mes (≈&nbsp;360&nbsp;$/año facturado anual).</p>
<ul>
<li><strong>A favor:</strong> fotos ilimitadas y webs de portfolio sólidas.</li>
<li><strong>En contra:</strong> en inglés, sin plan gratis, entrega a cliente básica y sin revisión con timecode.</li>
<li><strong>Para quién:</strong> archivar mucho y mostrar bien.</li>
</ul>

<h2>5. Zenfolio — la suite generalista</h2>
<p>Professional a 11,50&nbsp;$/mes facturado anual (≈&nbsp;138&nbsp;$/año, 150&nbsp;GB); su Basic de 7&nbsp;$/mes incluye los 15&nbsp;GB que Positiva da gratis.</p>
<ul>
<li><strong>A favor:</strong> web, galerías, venta y reservas en un producto maduro.</li>
<li><strong>En contra:</strong> en inglés y en dólares; sin foco en vídeo.</li>
<li><strong>Para quién:</strong> quien prefiere una sola herramienta para todo, en inglés.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Entrega con tu marca</th><th>Revisión (foto · vídeo)</th><th>Portfolio público</th><th>En español</th><th>Precio anual aprox.</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Foto y vídeo, mismo enlace</span></td><td><span class="pv-si">Foto y vídeo · export Lightroom, DaVinci, Final Cut</span></td><td><span class="pv-si">Sí, con tus entregas</span></td><td><span class="pv-si">Sí</span></td><td><span class="pv-si">89 € + IVA (250 GB) · gratis 15 GB</span></td></tr>
<tr><td>Arcadina</td><td>Galerías como complemento</td><td>No</td><td>Web con tienda</td><td>Sí</td><td>Según plan de web</td></tr>
<tr><td>Pixieset</td><td>Foto (vídeo por minutos)</td><td>Favoritas de foto</td><td>Producto de la suite</td><td>No</td><td>192–288 $</td></tr>
<tr><td>Pic-Time</td><td>Foto (vídeo limitado)</td><td>Favoritas de foto</td><td>No</td><td>No</td><td>≈ 230 €</td></tr>
<tr><td>SmugMug</td><td>Básica</td><td>Básica</td><td>Sí</td><td>No</td><td>≈ 360 $ (plan Pro)</td></tr>
<tr><td>Zenfolio</td><td>Foto</td><td>Proofing de foto</td><td>Sí</td><td>No</td><td>≈ 138 $ (150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Tienes el análisis detallado en <a href="/positiva-vs-arcadina/">Positiva vs Arcadina</a>.</p>

<h2>Nuestra recomendación</h2>
<p>Si lo que necesitas es una web con blog y tienda llave en mano y en español, Arcadina sigue teniendo sentido. Si tu problema diario es <a href="/galerias/">entregar</a> y <a href="/revision-foto/">revisar</a> foto y vídeo con tus clientes — y quieres que tu <a href="/portfolio/">portfolio</a> se actualice solo con cada entrega — <a href="/">Positiva</a> cubre las tres verticales por 89&nbsp;€&nbsp;+&nbsp;IVA al año. <a href="https://app.positiva.studio/registro">Pruébala gratis</a> con 15&nbsp;GB y 2 galerías.</p>
""",
faq=[
('¿Cuál es la principal diferencia entre Arcadina y sus alternativas?',
 'Arcadina es ante todo un creador de webs para fotógrafos, con galerías como complemento. Alternativas como Positiva ponen el centro en la entrega y la revisión de fotos y vídeo con clientes, y generan el portfolio a partir de las entregas.'),
('¿Hay alternativas a Arcadina también españolas?',
 'Sí. Positiva es una plataforma española de galerías de entrega, revisión de fotos y vídeo y portfolio web, con los datos alojados en la Unión Europea y soporte en español.'),
('¿Puedo probar antes de cambiar?',
 'Sí. Positiva tiene un plan gratuito permanente de 15 GB y 2 galerías, sin tarjeta, suficiente para montar una entrega real con tu marca y decidir con calma.'),
],
),
# ══ 6 · VIMEO ═════════════════════════════════════════════════════
dict(
slug='alternativas-a-vimeo',
title='Alternativas a Vimeo para revisar y entregar vídeo (2026) · Blog de Positiva',
h1='Alternativas a Vimeo para revisar y entregar vídeo (2026)',
desc='Alternativas a Vimeo para videógrafos: revisión de vídeo con clientes, entrega con tu marca y portfolio, en español y sin pagar por asiento.',
lede='Vimeo sigue teniendo el mejor reproductor del sector. Pero si lo usas para revisar con clientes y entregar proyectos, pagas por asiento, por año y en inglés — por funciones que no son su centro. Estas son las alternativas.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Frame.io', 'Dropbox Replay', 'YouTube', 'Filestage'],
body="""
<p>Seamos justos con Vimeo: reproductor impecable, embeds sin publicidad y unos showcases que durante años fueron el portfolio de facto de medio sector audiovisual. Como escaparate de vídeo, sigue siendo excelente.</p>
<p>El problema aparece cuando lo estiras hacia el trabajo con clientes. Las notas con código de tiempo llegan en sus planes de pago, que se cobran por asiento y al mes (Starter 12&nbsp;$/asiento/mes facturado anual; Standard, con 2&nbsp;TB, 25&nbsp;$/asiento/mes; Advanced 75&nbsp;$/asiento/mes), los planes limitan los vídeos que subes al año, buena parte del flujo ocurre en inglés — y ni la <a href="/galerias/">entrega de un proyecto con tu marca</a> (foto incluida) ni la exportación de comentarios a tu editor existen. Estas son las alternativas en 2026.</p>

<h2>1. Positiva — revisión, entrega y portfolio, sin pagar por asiento</h2>
<p><a href="/">Positiva</a> es una plataforma española que cubre lo que un videógrafo necesita alrededor del cliente. La <a href="/revision-video/">revisión</a>: tu cliente comenta sobre el fotograma exacto sin registrarse, por rondas, y tú exportas los comentarios como marcadores a DaVinci Resolve (EDL) o Final Cut Pro (FCPXML). La <a href="/galerias/">entrega</a>: la misma galería con tu marca sirve el máster final, junto a las fotos si las hay, en un enlace que no caduca. Y el <a href="/portfolio/">portfolio público</a>: tus mejores entregas, publicadas en segundos.</p>
<ul>
<li><strong>A favor:</strong> las tres verticales en una sola cuota — <a href="/precios/">Autor: 250&nbsp;GB, 89&nbsp;€&nbsp;+&nbsp;IVA/año</a>, sin asientos ni límite de vídeos al año; en español y en euros; datos en la UE; el vídeo se reproduce en el navegador antes de descargarse; plan gratis de 15&nbsp;GB y 2 galerías.</li>
<li><strong>En contra:</strong> no es un servicio de alojamiento para incrustar vídeo en webs de terceros: si vives de los embeds de Vimeo en tu web o la de tus clientes, esa pieza no está aquí.</li>
<li><strong>Para quién:</strong> videógrafos y productoras que revisan y entregan a clientes y editan en DaVinci o Final Cut.</li>
</ul>

<h2>2. Frame.io — la referencia en postproducción</h2>
<ul>
<li><strong>A favor:</strong> comentarios en el fotograma, versiones y una integración con Premiere insuperable; plan gratuito de 2&nbsp;GB y 2 miembros.</li>
<li><strong>En contra:</strong> por usuario y al mes (Pro, 15&nbsp;$/usuario/mes), en inglés, y sin entrega con tu marca ni portfolio. Lo analizamos en <a href="/notas/alternativas-a-frame-io/">Alternativas a Frame.io</a>.</li>
<li><strong>Para quién:</strong> equipos de postproducción dentro del ecosistema Adobe.</li>
</ul>

<h2>3. Dropbox Replay — revisión sobre tu almacenamiento</h2>
<ul>
<li><strong>A favor:</strong> comentarios en el fotograma sobre archivos que ya viven en Dropbox.</li>
<li><strong>En contra:</strong> la versión completa es un add-on de 10&nbsp;$/usuario/mes sobre un plan Dropbox ya de pago — el conjunto ronda los 28&nbsp;$/usuario/mes; en inglés; la entrega sigue siendo una carpeta.</li>
<li><strong>Para quién:</strong> equipos cuyo almacenamiento ya es Dropbox.</li>
</ul>

<h2>4. YouTube — difusión, no revisión</h2>
<ul>
<li><strong>A favor:</strong> gratis, ilimitado y con el mejor alcance del planeta; los vídeos ocultos sirven para enseñar un corte rápido.</li>
<li><strong>En contra:</strong> sin comentarios con timecode privados, sin marca propia, con compresión agresiva y recomendaciones de terceros junto a tu trabajo. No es una herramienta profesional de revisión ni de entrega.</li>
<li><strong>Para quién:</strong> publicar, no trabajar.</li>
</ul>

<h2>5. Filestage — aprobaciones corporativas</h2>
<ul>
<li><strong>A favor:</strong> revisa vídeo, PDF e imágenes con flujos de aprobación formales.</li>
<li><strong>En contra:</strong> precios por usuario de herramienta corporativa, en inglés, y solo cubre la revisión.</li>
<li><strong>Para quién:</strong> departamentos de marketing con validaciones en varios pasos.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Revisión de vídeo</th><th>Entrega con tu marca</th><th>Portfolio público</th><th>Modelo de precio</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">En el fotograma · export EDL y FCPXML</span></td><td><span class="pv-si">Sí, foto y vídeo</span></td><td><span class="pv-si">Sí</span></td><td><span class="pv-si">89 € + IVA/año, sin asientos</span></td></tr>
<tr><td>Vimeo</td><td>Notas en el tiempo (planes de pago)</td><td>Página de vídeo</td><td>Showcases de vídeo</td><td>12–75 $/asiento/mes, límite de vídeos/año</td></tr>
<tr><td>Frame.io</td><td>En el fotograma</td><td>No</td><td>No</td><td>15 $/usuario/mes (Pro)</td></tr>
<tr><td>Dropbox Replay</td><td>En el fotograma</td><td>Carpeta</td><td>No</td><td>≈ 28 $/usuario/mes (plan + add-on)</td></tr>
<tr><td>YouTube</td><td>No</td><td>No</td><td>Canal público</td><td>Gratis</td></tr>
<tr><td>Filestage</td><td>En el fotograma</td><td>No</td><td>No</td><td>Por usuario, corporativo</td></tr>
</tbody>
</table>
</div>
<p>La cuenta sale rápido: un equipo de tres personas en Vimeo Standard paga unos 900&nbsp;$ al año solo por asientos; <a href="/precios/">el plan Autor de Positiva cuesta 89&nbsp;€&nbsp;+&nbsp;IVA al año</a> para todo el estudio, cubriendo revisión, entrega y portfolio.</p>

<h2>Nuestra recomendación</h2>
<p>Si tu web y las de tus clientes viven de embeds impecables, mantén Vimeo para eso: ahí sigue siendo el mejor. Para lo demás — <a href="/revision-video/">revisar con tu cliente en español</a>, <a href="/galerias/">entregar el máster con tu marca</a> y tener el <a href="/portfolio/">portfolio</a> al día — <a href="/">Positiva</a> lo cubre por una cuota anual sin asientos. <a href="https://app.positiva.studio/registro">Pruébala gratis</a> con 15&nbsp;GB.</p>
""",
faq=[
('¿Hay alguna alternativa a Vimeo en español?',
 'Sí. Positiva es una plataforma española: tu cliente revisa el vídeo en español, comenta sobre el fotograma exacto y tú exportas los comentarios a DaVinci Resolve o Final Cut Pro. El panel, las galerías y el soporte están en español.'),
('¿Qué alternativa a Vimeo no cobra por asiento?',
 'Positiva cobra por almacenamiento, no por usuarios: el plan Autor (250 GB) cuesta 89 € + IVA al año para todo el estudio, frente a los 12–75 $ por asiento y mes de los planes de pago de Vimeo.'),
('¿Puedo entregar el vídeo final además de revisarlo?',
 'En Positiva la misma galería de revisión sirve la entrega final: el máster con tu marca, junto a las fotos del proyecto si las hay, en un enlace que no caduca.'),
],
),

# ══ 7 · DROPBOX REPLAY ════════════════════════════════════════════
dict(
slug='alternativas-a-dropbox-replay',
title='Alternativas a Dropbox Replay (2026) · Blog de Positiva',
h1='Alternativas a Dropbox Replay (2026)',
desc='Alternativas a Dropbox Replay para revisar vídeo con clientes: comentarios en el fotograma, exportación a DaVinci y Final Cut, y entrega con tu marca.',
lede='Replay añade revisión de vídeo a Dropbox — pagando un add-on sobre un plan que ya pagas, y en inglés. Si revisas con clientes y entregas proyectos, hay herramientas construidas para eso. Comparación honesta.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Frame.io', 'Vimeo', 'Filestage'],
body="""
<p>Dropbox Replay tiene una lógica clara: si tu material ya vive en Dropbox, revisar ahí mismo evita mover archivos. Comentarios en el fotograma, comparación de versiones y aprobaciones, integrado con tu almacenamiento.</p>
<p>La letra pequeña: la versión completa es un add-on de 10&nbsp;$/usuario/mes (facturado anual) <em>sobre</em> un plan Dropbox de pago — el conjunto ronda los 28&nbsp;$/usuario/mes por persona del equipo. Todo en inglés, también para tu cliente. Y cuando la pieza se aprueba, lo que entregas sigue siendo una carpeta de Dropbox: sin tu marca, sin <a href="/galerias/">galería de entrega</a>, sin <a href="/portfolio/">portfolio</a>. Estas son las alternativas en 2026.</p>

<h2>1. Positiva — revisión con tu cliente, entrega con tu marca</h2>
<p><a href="/revision-video/">Positiva</a> es una plataforma española de galerías de entrega y revisión de fotos y vídeo. Tu cliente abre un enlace con tu marca y comenta sobre el fotograma exacto sin registrarse; tú trabajas por <a href="/revision-video/">rondas de revisión</a> y exportas los comentarios como marcadores a DaVinci Resolve (EDL) o Final Cut Pro (FCPXML). Aprobada la pieza, la misma galería es <a href="/galerias/">la entrega del máster</a> — y alimenta tu <a href="/portfolio/">portfolio público</a>.</p>
<ul>
<li><strong>A favor:</strong> pensada para el cliente final: comentar es tan fácil como escribir, en español; exportación nativa a DaVinci y Final Cut (Replay no exporta a editores externos); las tres verticales — revisión, entrega y portfolio — por <a href="/precios/">89&nbsp;€&nbsp;+&nbsp;IVA al año (250&nbsp;GB), sin pagar por usuario</a>; datos en la UE; plan gratis de 15&nbsp;GB.</li>
<li><strong>En contra:</strong> no sincroniza carpetas ni sustituye a Dropbox como almacenamiento de trabajo: es la capa de cliente, no tu disco en la nube.</li>
<li><strong>Para quién:</strong> videógrafos y productoras que revisan con dirección, agencia o cliente final y editan en DaVinci o Final Cut.</li>
</ul>

<h2>2. Frame.io — más profundo para postproducción</h2>
<ul>
<li><strong>A favor:</strong> la revisión más completa del mercado (versiones, comparación, integración Premiere); plan gratuito de 2&nbsp;GB y 2 miembros.</li>
<li><strong>En contra:</strong> 15&nbsp;$/usuario/mes en Pro, en inglés, y sin entrega con marca ni portfolio. Análisis completo en <a href="/notas/alternativas-a-frame-io/">Alternativas a Frame.io</a>.</li>
<li><strong>Para quién:</strong> equipos de postproducción en el ecosistema Adobe.</li>
</ul>

<h2>3. Vimeo — revisión dentro del escaparate</h2>
<ul>
<li><strong>A favor:</strong> reproductor excelente; notas en el tiempo en sus planes de pago; showcases como portfolio de vídeo.</li>
<li><strong>En contra:</strong> por asiento y con límite de vídeos al año (Standard: 25&nbsp;$/asiento/mes anual); en inglés en buena parte del flujo; sin entrega de proyectos foto+vídeo. Más en <a href="/notas/alternativas-a-vimeo/">Alternativas a Vimeo</a>.</li>
<li><strong>Para quién:</strong> quien ya aloja su vídeo en Vimeo.</li>
</ul>

<h2>4. Filestage — aprobaciones multiformato</h2>
<ul>
<li><strong>A favor:</strong> revisa vídeo, PDF, imágenes y webs con flujos de aprobación formales.</li>
<li><strong>En contra:</strong> precio corporativo por usuario, en inglés, solo revisión.</li>
<li><strong>Para quién:</strong> departamentos de marketing con procesos de validación largos.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Revisión de vídeo</th><th>Export a DaVinci / Final Cut</th><th>Entrega con tu marca</th><th>Portfolio público</th><th>Precio</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">En el fotograma, sin registro para el cliente</span></td><td><span class="pv-si">Sí · EDL y FCPXML</span></td><td><span class="pv-si">Sí, foto y vídeo</span></td><td><span class="pv-si">Sí</span></td><td><span class="pv-si">89 € + IVA/año, sin asientos</span></td></tr>
<tr><td>Dropbox Replay</td><td>En el fotograma</td><td>No</td><td>Carpeta</td><td>No</td><td>≈ 28 $/usuario/mes (plan + add-on)</td></tr>
<tr><td>Frame.io</td><td>En el fotograma</td><td>Parcial (foco en Premiere)</td><td>No</td><td>No</td><td>15 $/usuario/mes (Pro)</td></tr>
<tr><td>Vimeo</td><td>Notas en el tiempo (pago)</td><td>No</td><td>Página de vídeo</td><td>Showcases</td><td>12–75 $/asiento/mes</td></tr>
<tr><td>Filestage</td><td>En el fotograma</td><td>No</td><td>No</td><td>No</td><td>Por usuario, corporativo</td></tr>
</tbody>
</table>
</div>
<p>Tres personas con Dropbox Business + Replay pagan unos 1.000&nbsp;$ al año solo por revisar; <a href="/precios/">el plan Autor de Positiva</a> cuesta 89&nbsp;€&nbsp;+&nbsp;IVA al año para todo el estudio y añade la entrega y el portfolio. También comparamos el Dropbox «normal» en <a href="/positiva-vs-dropbox/">Positiva vs Dropbox</a>.</p>

<h2>Nuestra recomendación</h2>
<p>Si tu equipo vive dentro de Dropbox y solo necesita anotar cortes internos, Replay es cómodo. Si quien comenta es tu cliente y lo que sigue a la aprobación es una entrega, <a href="/revision-video/">la revisión de vídeo de Positiva</a> hace el recorrido completo — comentario → marcador en tu timeline → <a href="/galerias/">máster entregado con tu marca</a> — en español y sin pagar por asiento. <a href="https://app.positiva.studio/registro">Pruébala gratis</a>.</p>
""",
faq=[
('¿Cuánto cuesta Dropbox Replay frente a sus alternativas?',
 'El add-on de Replay cuesta 10 $ por usuario al mes sobre un plan Dropbox de pago: en total unos 28 $/usuario/mes. Positiva cuesta 89 € + IVA al año en total, sin pagar por usuario, e incluye además la entrega con tu marca y el portfolio.'),
('¿Puedo exportar los comentarios de la revisión a mi editor?',
 'Con Positiva sí: los comentarios de cada ronda se exportan como marcadores en EDL (DaVinci Resolve) o FCPXML (Final Cut Pro) y aparecen sobre tu timeline en el fotograma exacto. Dropbox Replay no exporta marcadores a editores externos.'),
('¿Necesita mi cliente una cuenta para comentar?',
 'En Positiva no: abre el enlace de la galería con tu marca y comenta directamente, sin registro. En Dropbox Replay el flujo vive dentro del ecosistema Dropbox.'),
],
),
]


# El artículo de Frame.io monta su sección de Positiva tras el intro
# (no lleva el bloque VERTICALES completo porque su ángulo es la revisión).
for _a in ARTICLES:
    if _a.get('extra_positiva'):
        _b = _a['body']
        _i = _b.index('<h2>2. ')
        _a['body'] = _b[:_i] + _a.pop('extra_positiva') + '\n' + _b[_i:]
