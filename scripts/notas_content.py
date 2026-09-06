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
title='Alternativas a Pixieset en español (2026) · Notas de Positiva',
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
<p>Si vives de vender copias impresas a un público internacional, Pic-Time es una gran heredera de Pixieset. Para todo lo demás — <a href="/galerias/">entregar</a> foto y vídeo con tu marca, <a href="/revision-foto/">revisar con tu cliente</a> en español y tener tu <a href="/portfolio/">portfolio</a> siempre al día, en euros y con los datos en la UE — <a href="/">Positiva</a> es la alternativa que hemos construido precisamente porque no existía. Puedes <a href="https://app.positiva.studio">probarla gratis</a> con 15&nbsp;GB y 2 galerías.</p>
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
title='Alternativas a Pic-Time en español (2026) · Notas de Positiva',
h1='Alternativas a Pic-Time en español (2026)',
desc='Alternativas a Pic-Time para fotógrafos y videógrafos: galerías de clientes en español, precios en euros, foto y vídeo en el mismo enlace y revisión online.',
lede='Pic-Time es probablemente la galería más elegante para vender impresiones. Pero si lo tuyo es entregar y revisar — y trabajar en tu idioma — hay opciones que encajan mejor. Esta es la comparación honesta.',
date_iso=D, date_h=DH,
list_names=['Positiva', 'Pixieset', 'ShootProof', 'SmugMug', 'Zenfolio'],
body="""
<p>Pic-Time se ha ganado su fama: galerías cuidadas, una tienda de impresión seria y automatizaciones de marketing que venden copias mientras duermes. Su plan habitual ronda los 230&nbsp;€ al año, con 100&nbsp;GB para fotos y 30&nbsp;GB para vídeo.</p>
<p>¿Los peros? La interfaz de trabajo está en inglés, el vídeo va limitado y aparte, no hay revisión con timecode ni portfolio web y, si tu negocio no vende impresiones, estás pagando una tienda que no usas. Estas son las alternativas a Pic-Time que valoraría en 2026.</p>
""" + VERTICALES + """
<h2>1. Positiva — entrega, revisión y portfolio, en español</h2>
<p><a href="/">Positiva</a> es una plataforma española que cubre el flujo completo. Donde Pic-Time pone el foco en vender copias, Positiva lo pone en las tres verticales del trabajo profesional: <a href="/galerias/">entregar con tu marca</a>, recoger favoritas y comentarios del cliente — <a href="/revision-foto/">foto a foto</a> y <a href="/revision-video/">fotograma a fotograma</a> — y llevártelos a Lightroom, DaVinci Resolve o Final Cut Pro, y publicar tu <a href="/portfolio/">portfolio</a> con las entregas que ya tienes.</p>
<ul>
<li><strong>A favor:</strong> las tres verticales en una sola cuota, en español y en euros (<a href="/precios/">Autor 89&nbsp;€&nbsp;+&nbsp;IVA/año con 250&nbsp;GB; Estudio 219&nbsp;€&nbsp;+&nbsp;IVA/año con 1&nbsp;TB</a>); foto y vídeo comparten almacenamiento y enlace; datos en la UE; plan gratis de 15&nbsp;GB y 2 galerías; sin comisiones.</li>
<li><strong>En contra:</strong> sin tienda de impresión integrada ni automatizaciones de venta: si Pic-Time te genera ingresos por copias, aquí no tendrás ese canal.</li>
<li><strong>Para quién:</strong> fotógrafos y videógrafos que entregan proyectos (bodas, marcas, eventos) y quieren revisión y entrega impecables en su idioma.</li>
</ul>

<h2>2. Pixieset — el estándar mundial</h2>
<p>La opción por defecto en medio mundo. Ecosistema completo: galerías, web, tienda y gestión de estudio, con planes de pago habituales de 192 a 288&nbsp;$ al año.</p>
<ul>
<li><strong>A favor:</strong> madurez, plantillas de galería icónicas, suite amplia — la entrega de foto está muy pulida y la web de portfolio existe como producto de la suite.</li>
<li><strong>En contra:</strong> en inglés y en dólares; vídeo por minutos; 15&nbsp;% de comisión en la tienda del plan gratuito; sin revisión de vídeo.</li>
<li><strong>Para quién:</strong> quien quiere el ecosistema más probado y no necesita trabajar en español.</li>
</ul>

<h2>3. ShootProof — con contratos y facturas</h2>
<p>Planes por número de fotos: 100 gratis, 1.500 por 10,99&nbsp;$/mes anual y 5.000 fotos (250&nbsp;GB) por unos 240&nbsp;$ al año.</p>
<ul>
<li><strong>A favor:</strong> contratos, facturación y pagos integrados con las galerías.</li>
<li><strong>En contra:</strong> una sola vertical (entrega de foto); orientada al mercado norteamericano, en dólares; vídeo, revisión con timecode y portfolio quedan fuera.</li>
<li><strong>Para quién:</strong> estudios de foto que quieren papeleo y entrega en la misma herramienta.</li>
</ul>

<h2>4. SmugMug — archivo ilimitado</h2>
<p>Subidas ilimitadas de foto desde 7&nbsp;$/mes; las herramientas de cliente llegan en el plan Pro, a 41,99&nbsp;$/mes (≈&nbsp;360&nbsp;$/año facturado anual).</p>
<ul>
<li><strong>A favor:</strong> almacenamiento de fotos ilimitado y buenas webs de portfolio.</li>
<li><strong>En contra:</strong> en inglés, sin plan gratuito; entrega y revisión básicas; su plan con herramientas de cliente cuesta cuatro veces el Autor de Positiva.</li>
<li><strong>Para quién:</strong> quien necesita archivar decenas de miles de fotos ante todo.</li>
</ul>

<h2>5. Zenfolio — la suite veterana</h2>
<p>Web, galerías, venta y reservas; Professional a 11,50&nbsp;$/mes anual (≈&nbsp;138&nbsp;$/año, 150&nbsp;GB).</p>
<ul>
<li><strong>A favor:</strong> producto maduro que toca entrega y portfolio.</li>
<li><strong>En contra:</strong> en inglés y en dólares, sin foco en vídeo ni revisión moderna; su plan Basic (7&nbsp;$/mes) da 15&nbsp;GB — lo que Positiva ofrece gratis.</li>
<li><strong>Para quién:</strong> fotógrafos que prefieren una suite generalista.</li>
</ul>

<h2>Comparativa: las tres verticales y el precio</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Entrega con tu marca</th><th>Revisión (foto · vídeo)</th><th>Portfolio público</th><th>Plan gratis</th><th>Precio anual aprox.</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Foto y vídeo, mismo enlace</span></td><td><span class="pv-si">Foto y vídeo · export Lightroom, DaVinci, Final Cut</span></td><td><span class="pv-si">Sí, con tus entregas</span></td><td><span class="pv-si">15 GB · 2 galerías</span></td><td><span class="pv-si">89 € + IVA (250 GB)</span></td></tr>
<tr><td>Pic-Time</td><td>Foto (vídeo limitado)</td><td>Favoritas de foto</td><td>No</td><td>3 GB</td><td>≈ 230 €</td></tr>
<tr><td>Pixieset</td><td>Foto (vídeo por minutos)</td><td>Favoritas de foto</td><td>Producto aparte de la suite</td><td>3 GB</td><td>192–288 $</td></tr>
<tr><td>ShootProof</td><td>Solo foto</td><td>Favoritas de foto</td><td>No</td><td>100 fotos</td><td>≈ 240 $ (250 GB)</td></tr>
<tr><td>SmugMug</td><td>Básica</td><td>Básica</td><td>Sí</td><td>No (prueba)</td><td>≈ 360 $ (plan Pro)</td></tr>
<tr><td>Zenfolio</td><td>Foto</td><td>Proofing de foto</td><td>Sí</td><td>No (prueba)</td><td>≈ 138 $ (150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Ninguna de las cinco cubre entrega, revisión y portfolio a la vez — y Positiva, que cubre las tres, es además la más barata a almacenamiento comparable. Tenemos la comparativa detallada en <a href="/positiva-vs-pictime-vs-pixieset/">Positiva vs Pic-Time vs Pixieset</a>.</p>

<h2>Nuestra recomendación</h2>
<p>Si la tienda de impresión es el corazón de tu negocio, quédate en Pic-Time: ahí sigue siendo la mejor. Si lo que necesitas es <a href="/galerias/">entregar</a> y <a href="/revision-foto/">revisar</a> foto y vídeo con tu marca, y un <a href="/portfolio/">portfolio</a> que se actualiza solo, en español y en euros, <a href="/">Positiva</a> está construida exactamente para eso — y puedes <a href="https://app.positiva.studio">probarla gratis</a>.</p>
""",
faq=[
('¿Hay alguna alternativa a Pic-Time en español?',
 'Sí. Positiva es una plataforma española: panel, galerías y soporte en español, precios en euros y datos en la Unión Europea, con plan gratuito de 15 GB.'),
('¿Qué pierdo al dejar Pic-Time?',
 'Principalmente la tienda de impresión y sus automatizaciones de marketing. Si no vendes copias desde la galería, no pierdes nada; si vendes, valora cuánto ingresas por esa vía antes de cambiar.'),
('¿Qué gano con la revisión de Positiva frente a Pic-Time?',
 'Además de favoritas de foto, tu cliente comenta sobre el fotograma exacto del vídeo, y tú exportas favoritas a Lightroom y comentarios como marcadores a DaVinci Resolve o Final Cut Pro.'),
('¿Cuál es la alternativa a Pic-Time más barata?',
 'A almacenamiento comparable, Positiva: 250 GB de foto y vídeo por 89 € + IVA al año, frente a los ≈230 € de Pic-Time por 100 GB de foto más 30 GB de vídeo, cubriendo además revisión de vídeo y portfolio.'),
],
),

# ══ 3 · WETRANSFER ════════════════════════════════════════════════
dict(
slug='alternativas-a-wetransfer',
title='Alternativas a WeTransfer para fotógrafos, gratis (2026) · Notas de Positiva',
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
<p>Para mover un archivo suelto, SwissTransfer o Smash resuelven gratis y rápido. Para <strong>entregar tu trabajo</strong> — que tu cliente lo vea con tu marca, lo <a href="/revision-foto/">comente</a> y no te vuelva a pedir el enlace, y que cada entrega sume a tu <a href="/portfolio/">portfolio</a> — <a href="/">Positiva</a> es gratis hasta 15&nbsp;GB y tarda cinco minutos en <a href="https://app.positiva.studio">probarse</a>.</p>
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
title='Alternativas a Frame.io en español (2026) · Notas de Positiva',
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
<p>Si tu casa es Premiere y la postproducción interna de un equipo grande, Frame.io sigue siendo la referencia. Si revisas con clientes en español y terminas en DaVinci Resolve o Final Cut Pro, <a href="/revision-video/">la revisión de vídeo de Positiva</a> hace exactamente ese recorrido — comentario del cliente → marcador en tu timeline — y de paso resuelve <a href="/galerias/">la entrega del máster</a> y tu <a href="/portfolio/">portfolio</a>, por una fracción del precio. <a href="https://app.positiva.studio">Pruébala gratis</a>.</p>
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
title='Alternativas a Arcadina (2026) · Notas de Positiva',
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
<p>Si lo que necesitas es una web con blog y tienda llave en mano y en español, Arcadina sigue teniendo sentido. Si tu problema diario es <a href="/galerias/">entregar</a> y <a href="/revision-foto/">revisar</a> foto y vídeo con tus clientes — y quieres que tu <a href="/portfolio/">portfolio</a> se actualice solo con cada entrega — <a href="/">Positiva</a> cubre las tres verticales por 89&nbsp;€&nbsp;+&nbsp;IVA al año. <a href="https://app.positiva.studio">Pruébala gratis</a> con 15&nbsp;GB y 2 galerías.</p>
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
]

# El artículo de Frame.io monta su sección de Positiva tras el intro
# (no lleva el bloque VERTICALES completo porque su ángulo es la revisión).
for _a in ARTICLES:
    if _a.get('extra_positiva'):
        _b = _a['body']
        _i = _b.index('<h2>2. ')
        _a['body'] = _b[:_i] + _a.pop('extra_positiva') + '\n' + _b[_i:]
