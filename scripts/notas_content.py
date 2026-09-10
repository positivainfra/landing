# -*- coding: utf-8 -*-
# Contenido de los artículos de /notas/ (el Blog).
# ESCRITOS SEGÚN LA GUÍA EDITORIAL «Alternativas a [competidor]»:
#   · tabla de decisión rápida al principio, antes del análisis
#   · los criterios salen del competidor y del usuario, no de Positiva
#   · nada de marcos inventados («las tres verticales» y similares: prohibidos)
#   · cada herramienta con la misma estructura: Mejor para / Ventajas /
#     Limitaciones / Precio, y al menos una limitación REAL de Positiva
#   · precios en la moneda oficial, sin convertir, con periodicidad explícita
#   · lo no verificado se dice: «no hemos encontrado en su documentación pública»
#   · metodología breve y fecha exacta de verificación al pie (extra_foot)
# Datos verificados en páginas oficiales de precios y centros de ayuda el
# 08/09/2026 (Pic-Time) y el 10/09/2026 (el resto). Al actualizar precios,
# cambiar también date_iso/date_h y la fecha del extra_foot del artículo.
ARTICLES = [

# ══ 1 · PIXIESET ══════════════════════════════════════════════════
dict(
slug='alternativas-a-pixieset',
title='Alternativas a Pixieset para fotógrafos y videógrafos (2026) · Blog de Positiva',
h1='Alternativas a Pixieset para fotógrafos y videógrafos (2026)',
desc='Guía de alternativas a Pixieset: qué plataforma de galerías encaja según tu caso — vídeo, tienda, gestión del estudio, idioma y precio. Datos verificados.',
lede='Pixieset es la galería de clientes más extendida, y su suite cubre web, tienda y gestión del estudio. Si estás buscando otra cosa — por el vídeo, por el precio, por el idioma o porque no necesitas media suite — esta guía compara las alternativas según tu caso.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'Pic-Time', 'ShootProof', 'SmugMug', 'Zenfolio'],
body="""
<p>Pixieset no es un producto, son cuatro: Client Gallery (las galerías), Website (la web pública), Store (la tienda) y Studio Manager (contratos, facturas y reservas). Cada uno se contrata por separado, y su plan de galerías más habitual, Plus, cuesta 16&nbsp;$/mes con facturación anual — 192&nbsp;$/año — con 100&nbsp;GB.</p>
<p>Puedes buscar una alternativa a Pixieset si el vídeo es una parte importante de lo que entregas, si sumar módulos te sale caro, si necesitas un flujo de revisión más allá de las favoritas o si prefieres trabajar en español y pagar en euros. Estas son las opciones que valoraría en 2026.</p>

<h2>Qué alternativa a Pixieset elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Entrega y revisión de foto y vídeo</td><td><a href="/">Positiva</a></td><td>Foto y vídeo en la misma galería, con comentarios por fotograma</td></tr>
<tr><td>Vender impresiones con automatizaciones</td><td>Pic-Time</td><td>Tienda conectada a más de 30 laboratorios y campañas de venta</td></tr>
<tr><td>Contratos, facturas y pagos</td><td>ShootProof</td><td>Galerías y gestión administrativa en la misma herramienta</td></tr>
<tr><td>Archivo de fotos sin límite</td><td>SmugMug</td><td>Subidas de fotos ilimitadas en todos sus planes</td></tr>
<tr><td>Web, galerías y venta en una suite</td><td>Zenfolio</td><td>Un solo producto en lugar de módulos por separado</td></tr>
<tr><td>El ecosistema más probado</td><td>Quedarte en Pixieset</td><td>Ninguna alternativa cubre a la vez galería, web, tienda y gestión</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Pixieset</h2>
<p>Los motivos que más pesan al valorar una salida:</p>
<ul>
<li><strong>El vídeo se mide en minutos, no en gigas.</strong> El plan Basic incluye 30 minutos de metraje, y las descargas en 4K solo llegan en Pro y Ultimate. Si entregas vídeo con regularidad, esa unidad se queda corta antes que el almacenamiento.</li>
<li><strong>La suite se paga por piezas.</strong> Galerías, web, tienda y Studio Manager son suscripciones independientes: quien las quiere todas suma cuatro cuotas.</li>
<li><strong>La revisión se queda en las favoritas.</strong> El cliente marca lo que le gusta; no hemos encontrado en su documentación pública comentarios de vídeo vinculados al fotograma.</li>
<li><strong>El panel del fotógrafo está en inglés</strong> y se factura en dólares, aunque las galerías que ve el cliente sí pueden configurarse en español.</li>
<li><strong>El plan gratuito cobra comisión.</strong> Un 15&nbsp;% sobre las ventas de la tienda, que desaparece en los planes de pago.</li>
</ul>
<p>Y el motivo para quedarse: si ya tienes montada la web, la tienda y la gestión del estudio dentro de Pixieset, ninguna alternativa de esta lista te devuelve las cuatro cosas a la vez.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios y los centros de ayuda de cada plataforma, y las hemos comparado según los criterios que más influyen al buscar una alternativa a Pixieset: entrega de foto, vídeo, revisión, portfolio, tienda, gestión del negocio, idioma y precio. Positiva es nuestro producto, así que señalamos también los casos en los que otra plataforma encaja mejor.</p>

<h2>Positiva: mejor para entrega y revisión de foto y vídeo</h2>
<p><a href="/">Positiva</a> es una plataforma española de <a href="/galerias/">galerías de entrega</a> y revisión. Frente a Pixieset, la diferencia principal es dónde está puesto el esfuerzo: no hay tienda ni gestión del estudio, y a cambio el vídeo se trata igual que la fotografía — mismo almacenamiento, misma galería, mismo enlace — y la revisión llega hasta el comentario <a href="/revision-video/">sobre el fotograma exacto</a>, que se exporta como marcadores a DaVinci Resolve y Final Cut Pro, o como selección a Lightroom.</p>
<p><strong>Mejor para:</strong> fotógrafos y videógrafos que entregan foto y vídeo y necesitan revisión, trabajando en español.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Foto y vídeo comparten galería, enlace y almacenamiento: no se cuentan minutos.</li>
<li>Favoritas y comentarios <a href="/revision-foto/">foto a foto</a> y por fotograma en vídeo, con exportación a Lightroom, DaVinci Resolve y Final Cut Pro.</li>
<li>Un enlace por tipo de acceso, cada uno con su contraseña y su calidad de descarga.</li>
<li>Panel, galerías y soporte en español; precios en euros; datos alojados en la Unión Europea.</li>
<li>Plan gratuito de 15&nbsp;GB y 2 galerías, sin tarjeta y sin comisiones.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Sin tienda de impresiones: no hay forma de vender copias ni álbumes desde la galería.</li>
<li>Sin contratos, facturación ni reservas — el equivalente a Studio Manager no existe.</li>
<li>El almacenamiento va por plan; no hay opción ilimitada.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB.</p>
<p><strong>No la elegiríamos si:</strong> vendes impresiones desde la galería o necesitas la gestión administrativa en la misma herramienta.</p>

<h2>Pic-Time: mejor para vender impresiones</h2>
<p>Pic-Time es la alternativa más parecida a Pixieset en la parte de galerías, y tiene especial sentido si las ventas de copias son una parte importante de tu negocio: su tienda está conectada a más de 30 laboratorios y las automatizaciones de venta vienen incluidas en todos los planes, también en el gratuito.</p>
<p><strong>Mejor para:</strong> fotógrafos cuyo ingreso por impresiones justifica la herramienta.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Tienda y automatizaciones de venta en todos los planes.</li>
<li>Portfolio Page: un escaparate con tus galerías, embebible en tu propia web.</li>
<li>El vídeo tiene su propia bolsa de almacenamiento, ampliable como add-on.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>El vídeo va por separado: 30&nbsp;GB en el plan Professional, y ampliarlo cuesta desde 10&nbsp;$/mes más con facturación anual.</li>
<li>El plan gratuito baja a 3&nbsp;GB de foto y 1&nbsp;GB de vídeo a los tres meses.</li>
<li>El panel está en inglés, con traducción automática opcional.</li>
</ul>
<p><strong>Precio:</strong> Professional, 21&nbsp;$/mes con facturación anual — 252&nbsp;$/año — con 100&nbsp;GB de foto y 30&nbsp;GB de vídeo. Con facturación mensual, 25&nbsp;$/mes. Beginner desde 7&nbsp;$/mes anual.</p>

<h2>ShootProof: mejor para contratos y facturación</h2>
<p>ShootProof puede sustituir a Pixieset si lo que te interesa de la suite es Studio Manager: contratos, facturas y pagos vienen con las galerías en el mismo plan, sin contratarlos aparte. Sus planes se dimensionan por número de fotografías.</p>
<p><strong>Mejor para:</strong> estudios de foto que quieren galerías y papeleo en una sola herramienta.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Contratos, facturación y pagos incluidos en los planes de pago.</li>
<li>Venta de copias sin comisión de la plataforma.</li>
<li>Incluye una web sencilla con portada, página «sobre mí» y contacto.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Los planes van por número de fotos: 1.500 (hasta 75&nbsp;GB) o 5.000 (hasta 250&nbsp;GB) en los tramos habituales.</li>
<li>No hemos encontrado soporte de vídeo en galerías en su documentación pública.</li>
<li>Producto orientado al mercado norteamericano, en inglés y en dólares.</li>
</ul>
<p><strong>Precio:</strong> 1.500 fotos, 8,33&nbsp;$/mes con facturación anual — unos 100&nbsp;$/año; 5.000 fotos, 16,67&nbsp;$/mes anual — unos 200&nbsp;$/año. Con facturación mensual, 9,99 y 19,99&nbsp;$/mes. Plan gratuito de 100 fotos y 5&nbsp;GB.</p>

<h2>SmugMug: mejor para archivo de fotos sin límite</h2>
<p>SmugMug es una alternativa a Pixieset cuando el problema es el volumen y no la venta: todos sus planes incluyen subidas de fotografías ilimitadas, con webs de portfolio personalizables. Las herramientas de venta llegan en el plan Pro y las de cliente profesional en el Business.</p>
<p><strong>Mejor para:</strong> archivo y portfolio de grandes volúmenes de fotografía.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Subidas de fotos ilimitadas en todos los planes, también en el más barato.</li>
<li>Webs de portfolio con control fino del diseño.</li>
<li>Venta de impresiones y descargas en Pro y Business.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Las herramientas de cliente profesional requieren el plan Business, el más caro de los cuatro.</li>
<li>Sin plan gratuito: solo prueba.</li>
<li>En inglés y en dólares.</li>
</ul>
<p><strong>Precio:</strong> de 7 a 41,99&nbsp;$/mes con facturación mensual según plan (Basic, Power, Pro, Business); con facturación anual el descuento va del 29 al 38&nbsp;% — el Business queda en unos 357&nbsp;$/año.</p>

<h2>Zenfolio: mejor para una suite generalista</h2>
<p>Zenfolio resuelve en un solo producto lo que Pixieset reparte en cuatro: web pública, galerías, proofing de foto, venta y reservas vienen juntos. Si la razón para irte es que sumar módulos te sale caro, es la comparación directa.</p>
<p><strong>Mejor para:</strong> fotógrafos que quieren web, galerías y negocio en una sola suscripción.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Web, galerías, proofing y venta en el mismo plan.</li>
<li>Reservas y herramientas de negocio incluidas.</li>
<li>Producto maduro, con más de dos décadas de recorrido.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Sin foco en vídeo ni revisión con comentarios por fotograma.</li>
<li>En inglés y en dólares; sin plan gratuito.</li>
<li>El plan de entrada, Basic, da 15&nbsp;GB — lo que Positiva ofrece gratis.</li>
</ul>
<p><strong>Precio:</strong> Basic, 7&nbsp;$/mes con facturación anual (15&nbsp;GB); Professional, 11,50&nbsp;$/mes anual — unos 138&nbsp;$/año — con 150&nbsp;GB; Advanced, 20&nbsp;$/mes anual.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Vídeo</th><th>Revisión</th><th>Portfolio / web</th><th>Tienda</th><th>Gestión del negocio</th><th>Plan gratis</th><th>Precio anual (fact. anual)</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Por GB, junto a las fotos</span></td><td><span class="pv-si">Favoritas + comentarios en foto + comentarios de vídeo por fotograma</span></td><td>Portfolio con tus entregas</td><td>No</td><td>No</td><td>15 GB · 2 galerías</td><td>89 € + IVA (250 GB)</td></tr>
<tr><td>Pixieset</td><td>Por minutos según plan (30 min en Basic)</td><td>Favoritas de foto</td><td>Website, módulo aparte</td><td>Sí, módulo aparte (15 % en el plan gratis)</td><td>Studio Manager, módulo aparte</td><td>3 GB</td><td>192 $ (Plus, 100 GB)</td></tr>
<tr><td>Pic-Time</td><td>30 GB en Professional, ampliable desde 10 $/mes</td><td>Favoritas y selección</td><td>Portfolio Page, embebible</td><td>Sí, 30+ laboratorios + automatizaciones</td><td>No</td><td>3 GB foto · 1 GB vídeo</td><td>252 $ (100 GB foto + 30 GB vídeo)</td></tr>
<tr><td>ShootProof</td><td>No documentado</td><td>Favoritas de foto</td><td>Web sencilla incluida</td><td>Sí, sin comisión</td><td>Contratos, facturas y pagos</td><td>100 fotos · 5 GB</td><td>≈ 200 $ (5.000 fotos · 250 GB)</td></tr>
<tr><td>SmugMug</td><td>Según plan</td><td>Proofing en el plan Business</td><td>Sí, webs personalizables</td><td>Sí (Pro y Business)</td><td>No</td><td>No (prueba)</td><td>≈ 357 $ (Business)</td></tr>
<tr><td>Zenfolio</td><td>—</td><td>Proofing de foto</td><td>Web incluida</td><td>Sí</td><td>Reservas y venta</td><td>No (prueba)</td><td>138 $ (Professional, 150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Tenemos una comparativa más detallada de las tres primeras en <a href="/positiva-vs-pictime-vs-pixieset/">Positiva vs Pic-Time vs Pixieset</a>.</p>

<h2>Cómo decidir</h2>
<p>Si tu negocio vive de las impresiones, Pic-Time es la sustituta natural de la parte de galerías. Si lo que te ata a Pixieset es Studio Manager, ShootProof lo trae de serie. Si archivas decenas de miles de fotografías, SmugMug. Si quieres dejar de pagar módulos sueltos, Zenfolio. Y Positiva es nuestra recomendación si entregas foto y vídeo, necesitas que tu cliente <a href="/revision-foto/">revise de verdad</a> y prefieres trabajar en español y en euros — puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB antes de mover nada.</p>
""",
faq=[
('¿Cuál es la alternativa más parecida a Pixieset?',
 'Pic-Time, en la parte de galerías: mismo tipo de galería de cliente con tienda de impresiones y automatizaciones. Para replicar la suite entera (galerías, web, tienda y gestión) haría falta combinar herramientas o pasar a Zenfolio.'),
('¿Qué alternativa a Pixieset funciona mejor con vídeo?',
 'Positiva, porque el vídeo comparte almacenamiento y galería con las fotografías y añade comentarios por fotograma. En Pixieset el vídeo se mide en minutos según el plan (30 minutos en Basic) y las descargas 4K llegan solo en Pro y Ultimate.'),
('¿Qué alternativas tienen la experiencia en español?',
 'Conviene separar panel y galería. Positiva tiene panel, galerías y soporte en español. En Pixieset y Pic-Time las galerías que ve el cliente pueden configurarse en español, pero el panel de trabajo está en inglés.'),
('¿Hay alternativas a Pixieset gratuitas?',
 'Con plan gratuito permanente: Positiva (15 GB y 2 galerías), Pic-Time (3 GB de foto y 1 GB de vídeo tras los tres primeros meses) y ShootProof (100 fotos, 5 GB). SmugMug y Zenfolio solo ofrecen periodo de prueba. El plan gratuito de Pixieset son 3 GB con un 15 % de comisión en la tienda.'),
('¿Puedo migrar mis galerías desde Pixieset?',
 'No hemos encontrado migraciones automáticas oficiales entre estas plataformas. El camino habitual es recuperar los originales de tu archivo local y volver a subirlos; las galerías nuevas no conservan las favoritas ni el histórico de pedidos. Si además tienes galerías en Pic-Time, escríbenos a hola@positiva.studio: con ese caso concreto podemos ayudarte.'),
('¿Qué opción es mejor si no necesito tienda?',
 'Positiva si tu prioridad es entregar y revisar foto y vídeo, o SmugMug si lo que necesitas es archivar volumen y tener portfolio. Quitar la tienda de la ecuación es justo lo que abarata el cambio.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada plataforma. Los precios en dólares son los de la edición estadounidense de cada web.</p>',
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

<aside class="nota nota-truco"><b>¿Ya tienes tus galerías en Pic-Time?</b><p>Antes de empezar a subir nada a mano, <a href="mailto:hola@positiva.studio?subject=Migrar%20desde%20Pic-Time">escríbenos</a>: llevamos un tiempo dándole vueltas a cómo traer galerías de Pic-Time a Positiva y podemos echarte una mano con la mudanza.</p></aside>

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
 'Ninguna de estas plataformas ofrece una migración automática documentada, así que el camino habitual es recuperar los originales y volver a subirlos —las galerías nuevas no conservan las favoritas ni el histórico de pedidos—. Dicho eso: si vienes de Pic-Time, escríbenos a hola@positiva.studio antes de ponerte, porque llevamos un tiempo con ello y podemos echarte una mano.'),
('¿Qué opción es mejor si no vendo impresiones?',
 'Si tampoco necesitas contratos ni facturación, Positiva o SmugMug según tu prioridad: revisión y entrega de foto y vídeo (Positiva) o archivo ilimitado de fotos (SmugMug). Si necesitas la gestión administrativa, ShootProof.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 8 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada plataforma.</p>',
),

# ══ 3 · WETRANSFER ════════════════════════════════════════════════
dict(
slug='alternativas-a-wetransfer',
title='Alternativas a WeTransfer para fotógrafos y videógrafos (2026) · Blog de Positiva',
h1='Alternativas a WeTransfer para fotógrafos y videógrafos (2026)',
desc='Guía de alternativas a WeTransfer: enlaces que no caducan, envíos grandes gratis, entrega con tu marca o revisión con el cliente. Datos verificados.',
lede='WeTransfer resuelve una cosa muy bien: mandar archivos pesados sin pensar. Los límites aparecen después — el enlace caduca, el envío tiene tope y la entrega no lleva tu marca. Esta guía compara las alternativas según lo que te esté fallando.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'SwissTransfer', 'Smash', 'Dropbox Transfer', 'Google Drive'],
body="""
<p>WeTransfer está diseñado para transferir archivos: subes, mandas, se descarga y desaparece. En su plan gratuito puedes hacer hasta 10 transferencias o 3&nbsp;GB en una ventana de 30 días, y los enlaces caducan a los tres días; los planes de pago suben el listón hasta 1&nbsp;TB por transferencia y permiten fijar tú la caducidad.</p>
<p>Buscar una alternativa suele deberse a una de estas cuatro cosas: el enlace caduca antes de que el cliente lo abra, el envío no cabe, la entrega no lleva tu marca, o necesitas que alguien comente lo que has mandado en lugar de solo descargarlo. Cada una lleva a una herramienta distinta.</p>

<h2>Qué alternativa a WeTransfer elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Entregar a un cliente con tu marca, sin caducidad</td><td><a href="/">Positiva</a></td><td>Galería con tu identidad y enlaces que no expiran</td></tr>
<tr><td>Mandar archivos grandes gratis</td><td>SwissTransfer</td><td>Hasta 50 GB por envío, sin cuenta y sin pagar</td></tr>
<tr><td>Envíos ilimitados con tu logo</td><td>Smash</td><td>Sin límite de tamaño en los planes de pago, con subdominio propio</td></tr>
<tr><td>Enviar desde donde ya guardas los archivos</td><td>Dropbox Transfer</td><td>Va incluido en el plan de Dropbox que ya pagas</td></tr>
<tr><td>Compartir carpetas de trabajo con un equipo</td><td>Google Drive</td><td>Acceso continuado y comentarios, no un envío puntual</td></tr>
<tr><td>Mandar un archivo suelto y olvidarte</td><td>Quedarte en WeTransfer</td><td>Sigue siendo lo más rápido cuando no hay nada que presentar</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde WeTransfer</h2>
<ul>
<li><strong>La caducidad.</strong> En Free y Starter los enlaces duran hasta tres días. Para una entrega que el cliente abrirá cuando pueda, eso significa reenviar.</li>
<li><strong>El tope del plan gratuito.</strong> 10 transferencias o 3&nbsp;GB en 30 días: una boda no cabe, y dos entregas seguidas tampoco.</li>
<li><strong>La entrega no se parece a ti.</strong> La marca propia — páginas con tu identidad — llega en Ultimate; en el resto, tu trabajo se presenta con la marca de otro.</li>
<li><strong>No hay conversación.</strong> WeTransfer entrega archivos; no hay favoritas, ni comentarios, ni forma de saber qué opina el cliente de la toma 3.</li>
</ul>
<p>Y el motivo para quedarse: para mandar un archivo a alguien que no es tu cliente — un proveedor, una imprenta, un colaborador — montar una galería es trabajo de más. WeTransfer y SwissTransfer siguen siendo lo más rápido cuando no hay nada que presentar.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios y los centros de ayuda de cada servicio y las hemos comparado según los criterios que decide alguien que busca una alternativa a WeTransfer: tamaño por envío, caducidad del enlace, almacenamiento, marca propia, presentación al cliente, comentarios y precio. Positiva es nuestro producto, así que señalamos también los casos en los que otra herramienta encaja mejor.</p>
<p>Un aviso sobre los precios: WeTransfer no publica actualmente una tabla de tarifas legible sin JavaScript, así que en su ficha damos los límites documentados en su centro de ayuda y no una cifra que no hemos podido verificar.</p>

<h2>Positiva: mejor para entregar a un cliente</h2>
<p><a href="/">Positiva</a> parte de una premisa distinta a la de WeTransfer: lo que mandas a un cliente no es un envío, es una entrega. En lugar de una lista de archivos con cuenta atrás, tu cliente recibe una <a href="/galerias/">galería con tu marca</a> en un enlace que no caduca, con las fotografías y los vídeos juntos, y con la posibilidad de <a href="/revision-foto/">marcar favoritas y comentar</a> — en vídeo, sobre el fotograma exacto.</p>
<p><strong>Mejor para:</strong> la entrega final a un cliente, y la revisión que viene después.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>El enlace no caduca, y puedes reemplazar archivos sin cambiarlo.</li>
<li>Tu logo, tus colores y tu tipografía en la galería; nada de marca ajena.</li>
<li>Varios enlaces por galería, cada uno con su contraseña y su calidad de descarga.</li>
<li>Favoritas y comentarios, con exportación a Lightroom, DaVinci Resolve y Final Cut Pro.</li>
<li>Analítica: sabes si la han abierto y qué se han descargado, sin preguntar.</li>
<li>Plan gratuito de 15&nbsp;GB y 2 galerías, en español y con los datos en la Unión Europea.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>No es una herramienta de envío genérico: los archivos van dentro de una galería, con su portada y su diseño. Para mandar un ZIP a un proveedor, es trabajo de más.</li>
<li>Admite JPEG y MP4; no sirve para enviar un proyecto de edición, un RAW o una carpeta cualquiera.</li>
<li>El almacenamiento va por plan, y no hay tienda ni facturación.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB y 2 galerías.</p>
<p><strong>No la elegiríamos si:</strong> lo que necesitas es mandar archivos sueltos a gente distinta cada día.</p>

<h2>SwissTransfer: mejor para mandar mucho, gratis</h2>
<p>SwissTransfer, de la suiza Infomaniak, es la alternativa directa cuando el problema es el tamaño y no quieres pagar: admite hasta 50&nbsp;GB por transferencia sin cuenta y sin coste, frente a los 3&nbsp;GB en 30 días del plan gratuito de WeTransfer.</p>
<p><strong>Mejor para:</strong> envíos grandes y puntuales sin suscripción.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Hasta 50&nbsp;GB por transferencia, gratis y sin registro.</li>
<li>Los archivos se guardan 15 días, ampliables a 30.</li>
<li>Contraseña opcional, sin coste, y límite configurable de descargas.</li>
<li>Datos en Suiza, con cifrado documentado en tránsito y en reposo.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>No hay marca propia: para logo y colores, Infomaniak remite a su producto de pago kDrive, desde 4,99&nbsp;CHF/mes con 3&nbsp;TB.</li>
<li>Sigue siendo un envío que caduca: no sirve como entrega permanente.</li>
<li>Sin comentarios, favoritas ni portfolio.</li>
<li>El envío está bloqueado desde una sesentena de países.</li>
</ul>
<p><strong>Precio:</strong> gratuito, sin planes de pago.</p>

<h2>Smash: mejor para envíos ilimitados con tu logo</h2>
<p>Smash es la alternativa a WeTransfer para quien manda mucho y quiere que el envío se parezca a su estudio: en los planes de pago no hay límite de tamaño por transferencia, y la página de descarga admite logo, fondo, mensaje y un subdominio propio.</p>
<p><strong>Mejor para:</strong> estudios que envían a diario y quieren marca propia sin montar galerías.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Sin límite de tamaño por transferencia en Pro, Team y Enterprise.</li>
<li>Logo, fondo, mensaje y subdominio propio (tunombre.fromsmash.com) desde el plan Pro.</li>
<li>Caducidad ampliable hasta 30 días en los planes de pago.</li>
<li>Aviso cuando el destinatario no ha descargado, dos días antes de que expire.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Los enlaces siguen caducando: 7 días por defecto, 30 como máximo.</li>
<li>Sin favoritas, comentarios ni portfolio: es transferencia, no entrega.</li>
<li>En el plan gratuito, lo que pase de 2&nbsp;GB se envía sin prioridad, por detrás de los envíos de pago.</li>
</ul>
<p><strong>Precio:</strong> Pro, 10&nbsp;$/mes con facturación mensual o 72&nbsp;$/año con facturación anual (sin impuestos), con 1&nbsp;TB acumulado. Team, 25&nbsp;$/mes o 180&nbsp;$/año, con 2&nbsp;TB. Plan gratuito sin almacenamiento acumulado.</p>

<h2>Dropbox Transfer: mejor si ya pagas Dropbox</h2>
<p>Si tu archivo ya vive en Dropbox, Dropbox Transfer es la alternativa a WeTransfer que no añade una suscripción más: manda hasta 100&nbsp;GB por envío en los planes de empresa desde los archivos que ya tienes sincronizados.</p>
<p><strong>Mejor para:</strong> quien ya paga Dropbox y quiere dejar de pagar también WeTransfer.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Incluido en el plan de Dropbox: 50&nbsp;GB por envío en Plus, 100&nbsp;GB en Essentials y Business, 250&nbsp;GB en Business Plus.</li>
<li>Contraseña, caducidad personalizable, logotipo y fondo propios en los planes de empresa.</li>
<li>El archivo sale de tu carpeta sincronizada: no hay que volver a subirlo.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Caduca: 7 días por defecto en Basic y Plus, 30 en los planes de empresa.</li>
<li>Es un envío, no una galería: sin favoritas ni presentación al cliente.</li>
<li>Para revisar vídeo hace falta <a href="/notas/alternativas-a-dropbox-replay/">Dropbox Replay</a>, que se paga aparte.</li>
</ul>
<p><strong>Precio:</strong> incluido en los planes de Dropbox. Plus, 9,99&nbsp;$/mes con facturación anual (2&nbsp;TB); Standard, 15&nbsp;$/usuario/mes anual; Advanced, 24&nbsp;$/usuario/mes anual.</p>

<h2>Google Drive: mejor para trabajar en equipo</h2>
<p>Google Drive no compite con WeTransfer en el mismo terreno: no es un envío que caduca, sino una carpeta compartida a la que se sigue teniendo acceso. Tiene sentido como alternativa cuando el material está vivo y varias personas entran a él más de una vez.</p>
<p><strong>Mejor para:</strong> material de trabajo compartido con un equipo o una agencia.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Sin caducidad: el acceso dura lo que tú quieras.</li>
<li>Admite cualquier tipo de archivo, también proyectos y RAW.</li>
<li>Comentarios sobre los archivos y permisos por persona.</li>
<li>15&nbsp;GB gratuitos con cualquier cuenta de Google.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>La presentación es una lista de archivos con la marca de Google, no una entrega.</li>
<li>Descargar una carpeta grande obliga al cliente a pelearse con el ZIP y con los avisos del navegador.</li>
<li>Sin favoritas, sin comentarios por fotograma y sin portfolio.</li>
</ul>
<p><strong>Precio:</strong> 15&nbsp;GB gratis con la cuenta de Google. Los planes de pago (Google One y Google Workspace) varían por país; no hemos podido verificar sus importes en la documentación oficial accesible. Google Workspace documenta 30&nbsp;GB por usuario en Business Starter, 2&nbsp;TB en Business Standard y 5&nbsp;TB en Business Plus.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Tamaño por envío</th><th>Caducidad del enlace</th><th>Marca propia</th><th>Revisión</th><th>Precio</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td>Sin envíos: subes a la galería, hasta tu cuota</td><td><span class="pv-si">No caduca</span></td><td><span class="pv-si">Logo, colores y tipografía</span></td><td><span class="pv-si">Favoritas + comentarios en foto + comentarios de vídeo por fotograma</span></td><td>89 € + IVA/año (250 GB)</td></tr>
<tr><td>WeTransfer</td><td>10 envíos o 3 GB/30 días (Free); 1 TB por transferencia (Ultimate)</td><td>3 días (Free y Starter); a tu elección en Ultimate</td><td>Páginas con marca en Ultimate</td><td>No</td><td>No publicado de forma verificable</td></tr>
<tr><td>SwissTransfer</td><td>50 GB</td><td>15 días, ampliables a 30</td><td>No</td><td>No</td><td>Gratis</td></tr>
<tr><td>Smash</td><td>Sin límite en los planes de pago</td><td>7 días por defecto, 30 máximo</td><td>Logo, fondo y subdominio (Pro)</td><td>No</td><td>72 $/año (Pro, sin impuestos)</td></tr>
<tr><td>Dropbox Transfer</td><td>50 GB (Plus) · 100 GB (Business) · 250 GB (Business Plus)</td><td>7 días (Plus); 30 en empresa</td><td>Logo y fondo en planes de empresa</td><td>Con Replay, add-on aparte</td><td>Incluido en Dropbox (desde 9,99 $/mes anual)</td></tr>
<tr><td>Google Drive</td><td>Sin envío: carpeta compartida</td><td>No caduca</td><td>No</td><td>Comentarios sobre archivos</td><td>15 GB gratis; planes según país</td></tr>
</tbody>
</table>
</div>

<h2>Cómo decidir</h2>
<p>Si lo que falla es el tamaño y no quieres pagar, SwissTransfer resuelve el problema hoy mismo. Si mandas a diario y quieres que el envío lleve tu logo, Smash. Si ya pagas Dropbox, Transfer está ahí sin coste añadido. Y si lo que estás mandando es el trabajo terminado a un cliente — la boda, la campaña, el corte final —, el problema no es el tamaño: es que un envío que caduca no es una entrega. Para eso hemos hecho <a href="/">Positiva</a>, y puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB. La comparación en detalle está en <a href="/positiva-vs-wetransfer/">Positiva vs WeTransfer</a>.</p>
""",
faq=[
('¿Hay alternativas a WeTransfer gratuitas y sin límite de tamaño?',
 'Sin límite del todo, no. La más generosa de las gratuitas es SwissTransfer, con 50 GB por transferencia sin cuenta ni pago. Positiva tiene plan gratuito de 15 GB y 2 galerías, pero es para entregar, no para enviar archivos sueltos.'),
('¿Qué alternativa a WeTransfer no caduca?',
 'Positiva y Google Drive. En Positiva el enlace de la galería no tiene fecha de caducidad y sigue funcionando aunque reemplaces archivos; en Drive el acceso dura mientras mantengas la carpeta compartida. En WeTransfer solo el plan Ultimate permite fijar la caducidad.'),
('¿Cuál permite poner mi marca en la entrega?',
 'Positiva (logo, colores y tipografía en toda la galería), Smash desde el plan Pro (logo, fondo y subdominio propio), Dropbox Transfer en los planes de empresa y WeTransfer en Ultimate. SwissTransfer y Google Drive, no.'),
('¿Alguna deja que el cliente comente lo que le mando?',
 'Positiva: favoritas y comentarios foto a foto, y comentarios sobre el fotograma exacto en vídeo, que se exportan a Lightroom, DaVinci Resolve y Final Cut Pro. Google Drive permite comentar archivos, sin timecode. El resto son servicios de transferencia y no lo contemplan.'),
('¿Puedo saber si mi cliente ha descargado los archivos?',
 'Smash avisa cuando el destinatario no ha descargado antes de que expire el envío, y WeTransfer notifica las descargas. Positiva va más allá: cada galería registra visitas, visitantes únicos, descargas y reproducciones.'),
('¿Merece la pena pagar WeTransfer si solo entrego a clientes?',
 'Depende de cuántas entregas hagas. Si la entrega es tu producto final, pagar por un enlace que caduca y no lleva tu marca resuelve el transporte pero no la presentación; una galería cuesta lo mismo o menos y hace las dos cosas.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada servicio. Los precios en dólares son los de la edición estadounidense de cada web.</p>',
),

# ══ 4 · FRAME.IO ══════════════════════════════════════════════════
dict(
slug='alternativas-a-frame-io',
title='Alternativas a Frame.io para vídeo y fotografía (2026) · Blog de Positiva',
h1='Alternativas a Frame.io para vídeo y fotografía (2026)',
desc='Guía de alternativas a Frame.io: revisión de vídeo con comentarios por fotograma, entrega al cliente, precio por usuario y idioma. Datos verificados.',
lede='Frame.io es el estándar de la revisión de vídeo en postproducción. Si buscas otra cosa suele ser por el precio por asiento, porque tu cliente no es un equipo de post, o porque además de revisar necesitas entregar. Esta guía compara las opciones según tu caso.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'Vimeo', 'Dropbox Replay', 'Frame.io'],
body="""
<p>Frame.io hace muy bien un trabajo concreto: que un equipo de postproducción comente un corte sobre el fotograma exacto y esos comentarios lleguen al montador. Comentarios de fotograma único, de rango y anotaciones dibujadas encima; importación de comentarios como marcadores en Premiere Pro; Camera to Cloud desde el rodaje. Su plan Pro cuesta 15&nbsp;$ por miembro y mes más impuestos, con 2&nbsp;TB y hasta 5 miembros.</p>
<p>Se busca una alternativa, casi siempre, por una de estas razones: el precio por asiento se multiplica cuando cada cliente necesita entrar, la herramienta está pensada para equipos de post y no para presentar un trabajo a un cliente final, o hace falta cubrir también la fotografía y la entrega, no solo la revisión.</p>

<h2>Qué alternativa a Frame.io elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Revisar y entregar foto y vídeo al cliente final</td><td><a href="/">Positiva</a></td><td>Revisión por fotograma y entrega con tu marca, sin pagar por asiento</td></tr>
<tr><td>Alojar vídeo público y hacer marketing con él</td><td>Vimeo</td><td>Reproductor incrustable, showcases y directos</td></tr>
<tr><td>Revisar vídeo y audio donde ya guardas los archivos</td><td>Dropbox Replay</td><td>Complemento sobre el Dropbox que ya pagas, con audio incluido</td></tr>
<tr><td>Postproducción en equipo, con Camera to Cloud</td><td>Quedarte en Frame.io</td><td>Ninguna alternativa replica C2C ni su integración con Premiere</td></tr>
<tr><td>Empezar sin pagar</td><td>Frame.io con Creative Cloud</td><td>Si ya tienes CC, tu plan gratuito sube a 100 GB</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Frame.io</h2>
<ul>
<li><strong>Se paga por miembro.</strong> 15&nbsp;$ por miembro y mes en Pro (hasta 5) y 25&nbsp;$ en Team (hasta 15). Para un flujo interno tiene sentido; para dar acceso a cada cliente, no.</li>
<li><strong>El destinatario es un profesional de post.</strong> La interfaz asume que quien entra sabe qué es un rango A→B. Un cliente de boda o el responsable de marketing de una marca no siempre viene de ahí.</li>
<li><strong>Revisar no es entregar.</strong> Frame.io tiene enlaces de revisión y presentaciones con tu marca, pero no una galería de entrega final con portfolio detrás.</li>
<li><strong>La exportación al editor no cubre a todos.</strong> Premiere Pro sí, con importación de comentarios como marcadores. La integración con DaVinci Resolve está marcada como heredada y sin soporte activo, y para Final Cut Pro no hemos encontrado integración en la documentación oficial. Queda la exportación en CSV.</li>
</ul>
<p>Y el motivo para quedarse: si grabas y necesitas que el material esté en la nube antes de llegar a casa, Camera to Cloud no tiene equivalente en esta lista. Tampoco el trabajo por proyectos con un equipo de montadores dentro.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios y los centros de ayuda de cada herramienta y las hemos comparado según los criterios que decide alguien que busca una alternativa a Frame.io: comentarios por fotograma, exportación al editor, quién puede entrar y a qué precio, fotografía, entrega al cliente, portfolio, idioma y precio. Positiva es nuestro producto, así que señalamos también los casos en los que otra herramienta encaja mejor.</p>

<h2>Positiva: mejor para revisar y entregar al cliente final</h2>
<p><a href="/">Positiva</a> resuelve la parte de Frame.io que mira al cliente, no la que mira al equipo. Tu cliente abre un enlace — sin cuenta, sin instalar nada, en español — y comenta <a href="/revision-video/">sobre el fotograma exacto</a>; tú recibes esos comentarios como marcadores en DaVinci Resolve o Final Cut Pro. Cuando el corte está aprobado, la misma herramienta hace la <a href="/galerias/">entrega final</a>, con fotografías y vídeos en la misma galería y con tu marca.</p>
<p><strong>Mejor para:</strong> fotógrafos, videógrafos y productoras que revisan con el cliente y después entregan.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios por fotograma en vídeo y foto a foto en fotografía, con favoritas.</li>
<li>Exportación de comentarios como marcadores a DaVinci Resolve y Final Cut Pro, y de favoritas a Lightroom.</li>
<li>No se paga por asiento: los revisores entran por enlace, sean uno o quince.</li>
<li>Entrega final y <a href="/portfolio/">portfolio público</a> en la misma herramienta.</li>
<li>Panel, galerías y soporte en español; datos en la Unión Europea; plan gratuito de 15&nbsp;GB.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>No es una herramienta de postproducción colaborativa: no hay Camera to Cloud ni panel dentro de Premiere Pro.</li>
<li>Admite JPEG y MP4 con H.264; no revisa audio suelto, PDF ni proyectos de edición.</li>
<li>Sin gestión de proyectos con miembros, roles y permisos internos por equipo.</li>
<li>El almacenamiento va por plan: 250&nbsp;GB o 1&nbsp;TB, sin crecer por miembro.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB y 2 galerías.</p>
<p><strong>No la elegiríamos si:</strong> tu flujo es de postproducción pura, con varios montadores trabajando dentro de la herramienta.</p>

<h2>Vimeo: mejor para alojar vídeo y hacer marketing con él</h2>
<p>Vimeo es una alternativa a Frame.io cuando la revisión es solo una parte de lo que necesitas y lo demás es publicar: sus enlaces de revisión muestran los comentarios con código de tiempo en la línea de tiempo, y el mismo vídeo sirve luego para incrustarlo en tu web o montar un showcase.</p>
<p><strong>Mejor para:</strong> quien revisa vídeo y además lo publica.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios con código de tiempo, y el revisor puede comentar sin cuenta de Vimeo.</li>
<li>Reproductor incrustable, showcases en todos los planes y portfolios web desde Standard.</li>
<li>Interfaz disponible en español.</li>
<li>2&nbsp;TB de almacenamiento ya en el plan Starter.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Se paga por asiento: 12&nbsp;$ en Starter, 25&nbsp;$ en Standard y 75&nbsp;$ en Advanced por asiento y mes.</li>
<li>Los enlaces de revisión necesitan Standard o superior; en Starter solo hay una versión de demostración.</li>
<li>No hemos encontrado exportación de comentarios como marcadores a Premiere, DaVinci Resolve o Final Cut Pro en su documentación oficial.</li>
<li>Los portfolios son de vídeo: no entregan fotografía.</li>
</ul>
<p><strong>Precio:</strong> Starter, 12&nbsp;$ por asiento/mes (2&nbsp;TB); Standard, 25&nbsp;$ (4&nbsp;TB); Advanced, 75&nbsp;$ (7&nbsp;TB). El desglose entre facturación mensual y anual no aparece en su tabla pública.</p>

<h2>Dropbox Replay: mejor si tu archivo ya está en Dropbox</h2>
<p>Dropbox Replay es la alternativa natural a Frame.io para quien ya paga Dropbox: añade revisión de vídeo y de audio sobre los archivos que ya tienes sincronizados, sin mover nada de sitio.</p>
<p><strong>Mejor para:</strong> equipos que ya viven en Dropbox y revisan también audio.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Revisa vídeo y audio, con audio sin pérdida — Frame.io y Positiva no cubren el audio suelto.</li>
<li>Enlaces protegidos con contraseña, transcripción y subtítulos automáticos, comparación de versiones y fechas de entrega.</li>
<li>Dropbox declara integración con Premiere Pro, Final Cut Pro, DaVinci Resolve y Pro Tools.</li>
<li>Archivos de hasta 150&nbsp;GB y 12 horas de duración.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Exige un plan de pago de Dropbox por debajo: son dos cuotas, no una.</li>
<li>Sin el complemento, el uso gratuito se limita a 4 archivos (10 en Essentials y Business Plus).</li>
<li>No hemos encontrado en su documentación oficial que los comentarios queden vinculados al fotograma exacto, ni que la integración con editores exporte marcadores al timeline.</li>
<li>Es revisión de vídeo y audio: no entrega galerías de fotografía ni tiene portfolio.</li>
</ul>
<p><strong>Precio:</strong> 12&nbsp;$ por usuario/mes con facturación mensual, 10&nbsp;$ con anual (120&nbsp;$/año), <em>más</em> el plan de Dropbox correspondiente — desde 9,99&nbsp;$/mes con facturación anual en Plus.</p>

<h2>Frame.io con Creative Cloud: mejor si ya pagas Adobe</h2>
<p>Antes de cambiar de herramienta conviene mirar la que ya tienes: cualquier suscriptor de Creative Cloud que entre en Frame.io con su Adobe ID obtiene un plan gratuito mejorado con 100&nbsp;GB de almacenamiento y colaboración en hasta cinco proyectos con otra persona. Si el motivo para irte era el precio y trabajas con Adobe, puede que no haga falta irse.</p>
<p><strong>Mejor para:</strong> montadores que ya pagan Creative Cloud y revisan con una persona.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>100&nbsp;GB sin coste adicional sobre la suscripción de Creative Cloud.</li>
<li>Comentarios por fotograma, rango y anotaciones dibujadas; Camera to Cloud.</li>
<li>Importación de comentarios como marcadores en Premiere Pro.</li>
<li>Interfaz en diez idiomas, español incluido, en las experiencias actuales.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>La colaboración gratuita se limita a cinco proyectos y otra persona.</li>
<li>Sigue sin ser una herramienta de entrega final ni de portfolio.</li>
<li>La integración con DaVinci Resolve está marcada como heredada; con Final Cut Pro no hemos encontrado documentación oficial.</li>
</ul>
<p><strong>Precio:</strong> incluido con Creative Cloud. Los planes de pago de Frame.io son Pro, 15&nbsp;$ por miembro/mes más impuestos, y Team, 25&nbsp;$; la facturación anual aplica un 13&nbsp;% de descuento cuya cifra exacta no aparece en su tabla pública.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Comentarios en vídeo</th><th>Exporta al editor</th><th>Fotografía</th><th>Entrega y portfolio</th><th>Modelo de precio</th><th>Precio de referencia</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Por fotograma</span></td><td><span class="pv-si">Marcadores a DaVinci Resolve y Final Cut Pro; favoritas a Lightroom</span></td><td><span class="pv-si">Galerías con favoritas y comentarios</span></td><td><span class="pv-si">Entrega con tu marca + portfolio público</span></td><td>Por cuenta, revisores ilimitados</td><td>89 € + IVA/año (250 GB)</td></tr>
<tr><td>Frame.io</td><td>Por fotograma, por rango y anotaciones dibujadas</td><td>Marcadores en Premiere Pro; CSV; Resolve heredado</td><td>Sí, con visor y enlaces de revisión</td><td>Presentaciones con marca, sin portfolio</td><td>Por miembro</td><td>15 $/miembro/mes (Pro)</td></tr>
<tr><td>Vimeo</td><td>Con código de tiempo</td><td>No documentado</td><td>No</td><td>Showcases y portfolios de vídeo</td><td>Por asiento</td><td>25 $/asiento/mes (Standard)</td></tr>
<tr><td>Dropbox Replay</td><td>Sí; vínculo al fotograma no documentado</td><td>Integración con editores; marcadores no documentados</td><td>No</td><td>No</td><td>Por usuario, sobre un plan de Dropbox</td><td>120 $/usuario/año + Dropbox</td></tr>
</tbody>
</table>
</div>

<h2>Cómo decidir</h2>
<p>Si tu flujo es de postproducción y grabas para la nube, Frame.io sigue siendo difícil de sustituir — y si ya pagas Creative Cloud, su plan gratuito mejorado quizá te baste. Si además de revisar publicas, Vimeo. Si tu archivo vive en Dropbox y revisas audio, Replay. Y si quien tiene que opinar es tu cliente, no tu montador, y después de aprobar hay que entregar el trabajo con tu marca, <a href="/">Positiva</a> está construida para ese recorrido: puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB.</p>
""",
faq=[
('¿Qué alternativa a Frame.io permite comentar sobre el fotograma exacto?',
 'Positiva y Vimeo lo documentan: Positiva con comentarios anclados al fotograma que se exportan como marcadores a DaVinci Resolve y Final Cut Pro, y Vimeo con comentarios de código de tiempo en la línea de tiempo. En Dropbox Replay no hemos encontrado esa precisión declarada en su documentación oficial.'),
('¿Cuál sale más barata si mi cliente tiene que entrar a revisar?',
 'Depende del modelo de precio, no de la tarifa. Frame.io, Vimeo y Dropbox Replay cobran por miembro, asiento o usuario; en Positiva los revisores entran por enlace y no suman coste, así que el precio no cambia porque tu cliente sea una persona o un comité.'),
('¿Alguna alternativa exporta los comentarios a mi editor?',
 'Frame.io importa comentarios como marcadores en Premiere Pro y exporta en CSV, con integración heredada para DaVinci Resolve. Positiva exporta comentarios como marcadores a DaVinci Resolve y Final Cut Pro. En Vimeo no hemos encontrado exportación a editores documentada.'),
('¿Hay alguna que sirva también para fotografía?',
 'Frame.io admite fotografía con visor propio y enlaces de revisión, y Positiva entrega y revisa fotografía y vídeo en la misma galería. Vimeo y Dropbox Replay son de vídeo (y Replay, también de audio).'),
('¿Qué alternativas están en español?',
 'Frame.io ofrece interfaz en diez idiomas incluido el español en sus experiencias actuales, y Vimeo en siete, español incluido. Positiva es española: panel, galerías y soporte en castellano, y datos alojados en la Unión Europea.'),
('¿Puedo usar Frame.io gratis?',
 'Sí, con límites: el plan gratuito son 2 GB y hasta 2 miembros. Si tienes Creative Cloud, iniciar sesión con tu Adobe ID lo sube a 100 GB y cinco proyectos compartidos con otra persona.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada herramienta. Los precios en dólares son los de la edición estadounidense de cada web.</p>',
),

# ══ 5 · ARCADINA ══════════════════════════════════════════════════
dict(
slug='alternativas-a-arcadina',
title='Alternativas a Arcadina para fotógrafos (2026) · Blog de Positiva',
h1='Alternativas a Arcadina para fotógrafos (2026)',
desc='Guía de alternativas a Arcadina: web y galerías para fotógrafos, tienda, gestión del estudio, vídeo y revisión. Precios en euros y datos verificados.',
lede='Arcadina lleva años siendo la opción por defecto del fotógrafo español que quiere web, galerías y tienda en castellano. Si buscas otra cosa, suele ser por el vídeo, por cómo se suman sus planes o porque necesitas revisión de verdad. Esta guía compara las alternativas según tu caso.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'PSPro', 'Pixieset', 'Pic-Time', 'Zenfolio'],
body="""
<p>Arcadina es una empresa española, con sede en Alzira (Valencia), que vende tres servicios independientes: <strong>Negocio</strong> (galerías de cliente y tienda, desde 10&nbsp;€/mes con pago anual, impuestos incluidos), <strong>Web</strong> (el portfolio, 8&nbsp;€/mes anual) y <strong>Manager</strong> (reservas, facturación y contratos, desde 8&nbsp;€/mes anual). También los agrupa en Suites, desde 24&nbsp;€/mes con pago anual. Todo en castellano, con soporte en castellano y sin comisiones por venta.</p>
<p>Los motivos habituales para mirar alternativas: el vídeo, que en sus galerías funciona por enlace de YouTube o Vimeo y no como archivo alojado; la suma de planes cuando quieres web <em>y</em> galerías <em>y</em> gestión; y la ausencia de una revisión con comentarios sobre el fotograma cuando entregas vídeo.</p>

<h2>Qué alternativa a Arcadina elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Entregar y revisar foto y vídeo</td><td><a href="/">Positiva</a></td><td>Vídeo alojado en la galería y comentarios por fotograma</td></tr>
<tr><td>Gestionar todo el estudio en español</td><td>PSPro</td><td>Galerías, web, CRM, contratos, agenda y facturación VeriFactu</td></tr>
<tr><td>Galerías con tienda y un ecosistema grande</td><td>Pixieset</td><td>Galería, web, tienda y gestión, cada módulo aparte</td></tr>
<tr><td>Vender impresiones con automatizaciones</td><td>Pic-Time</td><td>Tienda conectada a más de 30 laboratorios</td></tr>
<tr><td>Web, galerías y venta en una sola suscripción</td><td>Zenfolio</td><td>Suite generalista sin sumar módulos</td></tr>
<tr><td>Web, tienda y reservas en euros y en castellano</td><td>Quedarte en Arcadina</td><td>Pocas alternativas cubren esas tres cosas en español</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Arcadina</h2>
<ul>
<li><strong>El vídeo no se aloja, se enlaza.</strong> Su documentación de ayuda explica que en las galerías se rellena «la URL del vídeo» desde YouTube o Vimeo, o se conecta una cuenta de Vimeo. Si entregas vídeo, dependes de una plataforma más y de sus reglas.</li>
<li><strong>La revisión llega hasta el comentario por imagen.</strong> Arcadina tiene favoritas y permite activar que el cliente añada un comentario en cada imagen o vídeo que selecciona. No hemos encontrado en su documentación oficial comentarios anclados al fotograma de un vídeo.</li>
<li><strong>Los planes se suman.</strong> Web, Negocio y Manager son productos distintos. Quien quiere portfolio, galerías y facturación paga tres cuotas o una Suite.</li>
<li><strong>El almacenamiento del plan de entrada es corto para vídeo:</strong> 30&nbsp;GB en Aperture, 10&nbsp;GB en el plan Web.</li>
</ul>
<p>Y el motivo para quedarse, que no es menor: Arcadina hace en castellano, con soporte en castellano y con precios en euros con impuestos incluidos, un conjunto —web, tienda, reservas, contratos, facturación— que casi ninguna alternativa internacional cubre entero. Si tu problema no es el vídeo, cambiar puede costarte más de lo que resuelve.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios, la documentación y los centros de ayuda de cada plataforma y las hemos comparado según los criterios que decide alguien que busca una alternativa a Arcadina: galerías de cliente, vídeo, revisión, web pública, tienda, gestión del negocio, idioma, alojamiento de los datos y precio. Positiva es nuestro producto, así que señalamos también los casos en los que otra plataforma encaja mejor.</p>

<h2>Positiva: mejor para entregar y revisar foto y vídeo</h2>
<p><a href="/">Positiva</a> es española como Arcadina, pero cubre un trozo distinto del oficio: no vende impresiones ni gestiona reservas, y a cambio el vídeo vive dentro de la <a href="/galerias/">galería</a> — mismo almacenamiento y mismo enlace que las fotografías, sin pasar por YouTube ni por Vimeo — y la revisión llega hasta el comentario <a href="/revision-video/">sobre el fotograma exacto</a>, exportable como marcadores a DaVinci Resolve y Final Cut Pro.</p>
<p><strong>Mejor para:</strong> fotógrafos y videógrafos que entregan vídeo además de fotografía.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>El vídeo se sube y se reproduce en la propia galería: un GB es un GB, sea foto o vídeo.</li>
<li>Favoritas y comentarios <a href="/revision-foto/">foto a foto</a>, y comentarios por fotograma en vídeo.</li>
<li>Un enlace por tipo de acceso, cada uno con su contraseña y su calidad de descarga; los enlaces no caducan.</li>
<li><a href="/portfolio/">Portfolio público</a> alimentado por las entregas que ya tienes.</li>
<li>Empresa española, soporte en castellano, datos alojados en la Unión Europea y plan gratuito de 15&nbsp;GB.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Sin tienda: no se venden copias, álbumes ni descargas desde la galería. Arcadina sí, y sin comisión.</li>
<li>Sin reservas, contratos ni facturación: no hay equivalente al plan Manager.</li>
<li>Sin creador de web completo con páginas, blog y formularios: el portfolio muestra tu trabajo, no sustituye a una web corporativa.</li>
<li>Admite JPEG y MP4 con H.264; los RAW no se suben.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB y 2 galerías. Ojo a la comparación: los precios de Arcadina se publican con impuestos incluidos y los nuestros sin IVA.</p>
<p><strong>No la elegiríamos si:</strong> lo que te da de comer es la venta de impresiones o necesitas la gestión administrativa del estudio.</p>

<h2>PSPro: mejor para gestionar el estudio entero en español</h2>
<p>PSPro es la alternativa española más cercana a lo que hace Arcadina cuando sumas sus tres planes: galerías privadas con venta, web con plantillas, CRM, presupuestos, contratos con firma digital, agenda y facturación VeriFactu, todo en un mismo producto y con soporte en castellano.</p>
<p><strong>Mejor para:</strong> estudios que quieren galerías y administración en una sola herramienta española.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Galerías ilimitadas con venta integrada, favoritas y vista de comparar dos a dos.</li>
<li>Web propia con subdominio y plantillas incluida en todos los planes; dominio propio en Pro y Studio.</li>
<li>CRM, contratos con firma, agenda, fichaje y facturación VeriFactu en el mismo sitio.</li>
<li>Protección anti-captura y marca de agua anti-IA en las galerías.</li>
<li>30 días de prueba sin tarjeta.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Es la opción más cara de la lista: desde 25&nbsp;€/mes con pago anual, y sin IVA incluido.</li>
<li>No hemos encontrado en su documentación pública vídeo en galerías ni comentarios del cliente sobre fotografías o fotogramas.</li>
<li>Tampoco hemos encontrado documentada la ubicación de los datos más allá de «hecho en España» y conformidad con el RGPD.</li>
</ul>
<p><strong>Precio:</strong> Starter, 25&nbsp;€/mes con pago anual (300&nbsp;€/año, 300&nbsp;GB, 2 usuarios); Pro, 42&nbsp;€/mes anual (504&nbsp;€/año, 600&nbsp;GB); Studio, 69&nbsp;€/mes anual (828&nbsp;€/año, 1&nbsp;TB). IVA no incluido. Mensual desde 35&nbsp;€/mes.</p>

<h2>Pixieset: mejor para un ecosistema completo con tienda</h2>
<p>Pixieset es la alternativa internacional más parecida a Arcadina en ambición: galerías, web, tienda y gestión de estudio. La diferencia está en que cada pieza se contrata por separado y en que el panel del fotógrafo está en inglés, aunque la galería que ve tu cliente puede configurarse en español.</p>
<p><strong>Mejor para:</strong> quien quiere el ecosistema más probado y no le importa trabajar en inglés.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Galerías ilimitadas en todos los planes, incluido el gratuito de 3&nbsp;GB.</li>
<li>Tienda integrada sin comisión en los planes de pago.</li>
<li>Galerías configurables en español para el cliente final.</li>
<li>1&nbsp;TB de almacenamiento en el plan Pro.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>El panel de trabajo está en inglés y la facturación es en dólares.</li>
<li>El vídeo se mide en minutos según el plan, no en gigas.</li>
<li>La revisión se queda en favoritas de foto.</li>
<li>Web, tienda y gestión son suscripciones aparte: se suman igual que en Arcadina.</li>
</ul>
<p><strong>Precio:</strong> Client Gallery Plus, 16&nbsp;$/mes con facturación anual — 192&nbsp;$/año — con 100&nbsp;GB; Pro, 24&nbsp;$/mes anual — 288&nbsp;$/año — con 1&nbsp;TB. Plan gratuito de 3&nbsp;GB con un 15&nbsp;% de comisión en la tienda.</p>

<h2>Pic-Time: mejor para vender impresiones</h2>
<p>Si de Arcadina lo que más usas es la tienda, Pic-Time es la comparación honesta: su negocio está construido alrededor de la venta de copias, con conexión a más de 30 laboratorios y automatizaciones de campañas incluidas en todos los planes.</p>
<p><strong>Mejor para:</strong> fotógrafos cuyo ingreso por impresiones justifica la herramienta.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Tienda y automatizaciones de venta en todos los planes.</li>
<li>Galerías cuidadas y Portfolio Page embebible en tu web.</li>
<li>Bolsa propia de almacenamiento de vídeo, ampliable como complemento.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Panel en inglés, con traducción automática opcional, y precios en dólares.</li>
<li>El vídeo va aparte: 30&nbsp;GB en Professional, y ampliar cuesta desde 10&nbsp;$/mes con facturación anual.</li>
<li>Sin revisión de vídeo por fotograma documentada, y sin gestión administrativa.</li>
</ul>
<p><strong>Precio:</strong> Professional, 21&nbsp;$/mes con facturación anual — 252&nbsp;$/año — con 100&nbsp;GB de foto y 30&nbsp;GB de vídeo. Plan gratuito de 3&nbsp;GB de foto y 1&nbsp;GB de vídeo tras los tres primeros meses.</p>

<h2>Zenfolio: mejor para no sumar módulos</h2>
<p>Zenfolio propone en una sola suscripción lo que Arcadina reparte entre Web y Negocio: portfolio, galerías de cliente, proofing de fotografía, venta y reservas. Es la comparación directa si tu queja es que pagas dos planes para tener web y galerías.</p>
<p><strong>Mejor para:</strong> fotógrafos que quieren una suite generalista con una sola cuota.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Web, galerías, proofing y venta en el mismo plan.</li>
<li>Reservas incluidas.</li>
<li>Producto veterano, con dos décadas de recorrido.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>En inglés y en dólares, sin plan gratuito.</li>
<li>Sin foco en vídeo ni revisión por fotograma.</li>
<li>El plan de entrada da 15&nbsp;GB.</li>
</ul>
<p><strong>Precio:</strong> Basic, 7&nbsp;$/mes con facturación anual (15&nbsp;GB); Professional, 11,50&nbsp;$/mes anual — unos 138&nbsp;$/año — con 150&nbsp;GB; Advanced, 20&nbsp;$/mes anual.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Vídeo en la galería</th><th>Revisión</th><th>Web pública</th><th>Tienda</th><th>Gestión del negocio</th><th>Idioma del panel</th><th>Precio de referencia</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Alojado, junto a las fotos</span></td><td><span class="pv-si">Favoritas + comentarios en foto + comentarios de vídeo por fotograma</span></td><td>Portfolio con tus entregas</td><td>No</td><td>No</td><td><span class="pv-si">Español</span></td><td>89 € + IVA/año (250 GB)</td></tr>
<tr><td>Arcadina</td><td>Enlace de YouTube o Vimeo</td><td>Favoritas + comentario por imagen seleccionada</td><td>Sí, plan Web aparte</td><td>Sí, sin comisión</td><td>Sí, plan Manager aparte</td><td>Español</td><td>Negocio desde 120 €/año (IVA incl., 30 GB); Suite Pro 288 €/año</td></tr>
<tr><td>PSPro</td><td>No documentado</td><td>Favoritas y comparar</td><td>Sí, incluida</td><td>Sí, integrada</td><td>CRM, contratos, agenda, VeriFactu</td><td>Español</td><td>300 €/año + IVA (Starter, 300 GB)</td></tr>
<tr><td>Pixieset</td><td>Por minutos según plan</td><td>Favoritas de foto</td><td>Módulo aparte</td><td>Módulo aparte</td><td>Studio Manager, aparte</td><td>Inglés</td><td>192 $/año (Plus, 100 GB)</td></tr>
<tr><td>Pic-Time</td><td>Bolsa aparte (30 GB en Professional)</td><td>Favoritas y selección</td><td>Portfolio Page embebible</td><td>Sí, 30+ laboratorios</td><td>No</td><td>Inglés</td><td>252 $/año (100 GB + 30 GB vídeo)</td></tr>
<tr><td>Zenfolio</td><td>—</td><td>Proofing de foto</td><td>Sí, incluida</td><td>Sí</td><td>Reservas</td><td>Inglés</td><td>138 $/año (Professional, 150 GB)</td></tr>
</tbody>
</table>
</div>
<p>Una advertencia sobre esa última columna: Arcadina publica sus precios con impuestos incluidos, PSPro sin IVA, y las plataformas internacionales en dólares. No son cifras directamente comparables, y conviene mirar también qué entra en cada plan.</p>

<h2>Cómo decidir</h2>
<p>Si vendes impresiones y llevas tu administración dentro de la herramienta, Arcadina sigue siendo una opción razonable en castellano y con soporte en tu idioma; PSPro es la alternativa española si quieres además CRM y facturación modernos. Si lo que buscas es un ecosistema internacional con tienda, Pixieset o Pic-Time. Y si el motivo de tu búsqueda es el vídeo — entregarlo dentro de la galería y que tu cliente lo revise fotograma a fotograma en lugar de comentar un enlace de YouTube —, ahí está el hueco que llena <a href="/">Positiva</a>: puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB. La comparación en detalle está en <a href="/positiva-vs-arcadina/">Positiva vs Arcadina</a>.</p>
""",
faq=[
('¿Cuál es la alternativa española más parecida a Arcadina?',
 'PSPro: galerías privadas con venta, web con plantillas, CRM, contratos con firma, agenda y facturación VeriFactu en un solo producto y con soporte en castellano. Es bastante más cara — desde 300 € al año más IVA — y cubre más terreno administrativo.'),
('¿Qué alternativa a Arcadina maneja mejor el vídeo?',
 'Positiva: el vídeo se sube a la propia galería y comparte almacenamiento y enlace con las fotografías, y el cliente puede comentar sobre el fotograma exacto. En Arcadina el vídeo de las galerías se añade como URL de YouTube o Vimeo.'),
('¿Puedo tener web y galerías sin pagar dos planes?',
 'En Arcadina, no: Web y Negocio son servicios independientes, aunque las Suites los agrupan con descuento desde 24 €/mes con pago anual. Zenfolio y PSPro incluyen web y galerías en la misma suscripción; en Positiva el portfolio público viene con la cuenta, pero no sustituye a una web con páginas y blog.'),
('¿Hay alternativas a Arcadina con plan gratuito?',
 'Arcadina no tiene plan gratuito permanente, solo 30 días de prueba sin tarjeta. Con plan gratuito de verdad: Positiva (15 GB y 2 galerías), Pixieset (3 GB, con 15 % de comisión en tienda) y Pic-Time (3 GB de foto y 1 GB de vídeo tras tres meses).'),
('¿Dónde están alojados los datos de cada una?',
 'Arcadina identifica en su política de privacidad a Hetzner y Amazon Web Services como encargados del tratamiento, bajo el RGPD y con jurisdicción en Valencia; no publica la región concreta de los centros de datos. Positiva aloja los datos en la Unión Europea. Las plataformas estadounidenses no garantizan residencia europea.'),
('¿Merece la pena cambiar si solo entrego fotografía?',
 'Probablemente no, si la tienda o la facturación de Arcadina te están funcionando. El cambio compensa cuando el vídeo pesa en tus entregas o cuando necesitas que el cliente revise y comente, no solo que descargue.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada plataforma. Los precios de Arcadina se publican con impuestos incluidos; los de PSPro y Positiva, sin IVA; los internacionales, en dólares de la edición estadounidense.</p>',
),

# ══ 6 · VIMEO ═════════════════════════════════════════════════════
dict(
slug='alternativas-a-vimeo',
title='Alternativas a Vimeo para entregar y revisar vídeo (2026) · Blog de Positiva',
h1='Alternativas a Vimeo para entregar y revisar vídeo (2026)',
desc='Guía de alternativas a Vimeo: entrega de vídeo a clientes, revisión con comentarios por fotograma, portfolio y precio por asiento. Datos verificados.',
lede='Vimeo hace tres cosas a la vez: aloja vídeo, lo publica y permite revisarlo. Si buscas alternativa suele ser porque solo necesitas una de las tres, o porque el precio por asiento no encaja. Esta guía compara las opciones según lo que realmente uses.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'Frame.io', 'Dropbox Replay', 'Vimeo'],
body="""
<p>Vimeo se paga por asiento: 12&nbsp;$ en Starter, 25&nbsp;$ en Standard y 75&nbsp;$ en Advanced por asiento y mes, con 2, 4 y 7&nbsp;TB de almacenamiento. Sus enlaces de revisión — con comentarios de código de tiempo en la línea de tiempo, y la posibilidad de comentar sin cuenta — requieren el plan Standard o superior; en Starter solo hay una versión de demostración.</p>
<p>Los motivos habituales para buscar otra cosa: pagar un plan de alojamiento y publicación cuando lo único que haces es mandar cortes al cliente; que los comentarios no salgan de Vimeo hacia tu editor; o que la fotografía se quede fuera, porque los portfolios de Vimeo son solo de vídeo.</p>

<h2>Qué alternativa a Vimeo elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Entregar vídeo y fotografía a un cliente y que los revise</td><td><a href="/">Positiva</a></td><td>Galería con tu marca, comentarios por fotograma y sin coste por revisor</td></tr>
<tr><td>Revisión en un equipo de postproducción</td><td>Frame.io</td><td>Comentarios por rango, anotaciones y Camera to Cloud</td></tr>
<tr><td>Revisar vídeo y audio donde ya guardas los archivos</td><td>Dropbox Replay</td><td>Complemento sobre tu Dropbox, con audio sin pérdida</td></tr>
<tr><td>Publicar vídeo, incrustarlo y hacer directos</td><td>Quedarte en Vimeo</td><td>Ninguna alternativa de esta lista aloja vídeo público ni emite en directo</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Vimeo</h2>
<ul>
<li><strong>Pagas por asiento y por publicación aunque solo revises.</strong> El precio se calcula por asiento, y los enlaces de revisión solo funcionan desde Standard, a 25&nbsp;$ por asiento y mes.</li>
<li><strong>Los comentarios se quedan dentro.</strong> No hemos encontrado en su documentación oficial exportación de comentarios como marcadores a Premiere, DaVinci Resolve o Final Cut Pro; hay que copiarlos a mano al timeline.</li>
<li><strong>La fotografía queda fuera.</strong> Los portfolios de Vimeo son de vídeo, así que una entrega mixta de boda o campaña necesita una segunda herramienta.</li>
<li><strong>El dominio propio del portfolio no lleva SSL.</strong> Vimeo documenta que no soporta SSL en portfolios con dominio externo, algo que en 2026 se nota en el navegador de cualquiera.</li>
</ul>
<p>Y el motivo para quedarse: si publicas — vídeo incrustado en tu web, un showcase que enseñas a marcas, eventos en directo — Vimeo hace algo que ninguna de estas alternativas hace. Cambiar por el precio de la revisión y perder el alojamiento público suele salir mal.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios y los centros de ayuda de cada herramienta y las hemos comparado según los criterios que decide alguien que busca una alternativa a Vimeo: entrega al cliente, revisión y comentarios, exportación al editor, fotografía, portfolio y publicación, modelo de precio e idioma. Positiva es nuestro producto, así que señalamos también los casos en los que otra herramienta encaja mejor.</p>

<h2>Positiva: mejor para entregar y revisar con el cliente</h2>
<p><a href="/">Positiva</a> no aloja vídeo para publicarlo: lo entrega. Tu cliente abre una <a href="/galerias/">galería con tu marca</a> donde las fotografías y los vídeos conviven, se reproduce el corte ahí mismo y comenta <a href="/revision-video/">sobre el fotograma exacto</a>; esos comentarios se exportan como marcadores a DaVinci Resolve y Final Cut Pro. Los revisores entran por enlace, así que no hay asientos que contar.</p>
<p><strong>Mejor para:</strong> videógrafos y productoras que entregan a un cliente final y necesitan su aprobación.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios por fotograma que salen hacia tu editor como marcadores.</li>
<li>Sin coste por revisor: entra quien tenga el enlace, sea una persona o un comité.</li>
<li>Fotografía y vídeo en la misma galería y el mismo enlace.</li>
<li>Enlaces que no caducan, con contraseña y calidad de descarga por enlace.</li>
<li>En español, con los datos en la Unión Europea y plan gratuito de 15&nbsp;GB.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>No es un alojamiento de vídeo público: no hay reproductor para incrustar en tu web ni emisiones en directo.</li>
<li>Sin transcripción ni subtítulos automáticos.</li>
<li>Admite MP4 con H.264 y JPEG; no revisa audio suelto.</li>
<li>El almacenamiento va por plan: 250&nbsp;GB o 1&nbsp;TB, frente a los 2-7&nbsp;TB de Vimeo.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB y 2 galerías.</p>
<p><strong>No la elegiríamos si:</strong> lo que necesitas es alojar vídeo público para tu web o para redes.</p>

<h2>Frame.io: mejor para postproducción en equipo</h2>
<p>Frame.io es la alternativa a Vimeo cuando la revisión no es un trámite con el cliente sino el trabajo diario del equipo: comentarios de fotograma único y de rango, anotaciones dibujadas sobre la imagen, versiones y Camera to Cloud desde el rodaje.</p>
<p><strong>Mejor para:</strong> equipos de postproducción con varios montadores.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios por fotograma, por rango A→B y anotaciones dibujadas.</li>
<li>Importación de comentarios como marcadores en Premiere Pro, y exportación en CSV.</li>
<li>Camera to Cloud: el material sube desde el rodaje.</li>
<li>Admite también fotografía, con visor propio y enlaces de revisión.</li>
<li>Interfaz en diez idiomas, español incluido; y con Creative Cloud, plan gratuito de 100&nbsp;GB.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Se paga por miembro: 15&nbsp;$ en Pro (hasta 5) y 25&nbsp;$ en Team (hasta 15) por miembro y mes, más impuestos.</li>
<li>La integración con DaVinci Resolve está marcada como heredada y sin soporte activo; para Final Cut Pro no hemos encontrado documentación oficial.</li>
<li>Sin portfolio público ni alojamiento de vídeo para incrustar.</li>
<li>El plan gratuito son 2&nbsp;GB y 2 miembros.</li>
</ul>
<p><strong>Precio:</strong> Pro, 15&nbsp;$ por miembro/mes más impuestos (2&nbsp;TB); Team, 25&nbsp;$ (3&nbsp;TB). La facturación anual aplica un 13&nbsp;% de descuento cuya cifra exacta no aparece en su tabla pública.</p>

<h2>Dropbox Replay: mejor si tu archivo ya está en Dropbox</h2>
<p>Replay tiene sentido frente a Vimeo si ya pagas Dropbox y lo que quieres es revisar sin subir el material a un tercer sitio — y si además trabajas con audio, que Vimeo no cubre.</p>
<p><strong>Mejor para:</strong> equipos que ya viven en Dropbox y revisan vídeo y audio.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Revisión de vídeo y de audio, con audio sin pérdida.</li>
<li>Transcripción y subtítulos automáticos, comparación de versiones y fechas de entrega.</li>
<li>Enlaces protegidos con contraseña y marca de agua digital.</li>
<li>Archivos de hasta 150&nbsp;GB y 12 horas de duración.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Son dos cuotas: el complemento y el plan de Dropbox que necesita debajo.</li>
<li>Sin el complemento, el uso gratuito se limita a 4 archivos (10 en Essentials y Business Plus).</li>
<li>No hemos encontrado documentado que los comentarios queden anclados al fotograma, ni que su integración con editores exporte marcadores al timeline.</li>
<li>Sin portfolio, sin galerías de fotografía y sin alojamiento público.</li>
</ul>
<p><strong>Precio:</strong> 12&nbsp;$ por usuario/mes con facturación mensual, 10&nbsp;$ con anual (120&nbsp;$/año), más el plan de Dropbox — desde 9,99&nbsp;$/mes con facturación anual en Plus.</p>

<h2>Vimeo: mejor para publicar y emitir</h2>
<p>Merece la pena mirar qué parte de Vimeo estás usando antes de sustituirlo. Si el vídeo que subes acaba incrustado en tu web, en un showcase que enseñas a clientes potenciales o en un directo, ninguna de las alternativas anteriores hace ese trabajo.</p>
<p><strong>Mejor para:</strong> alojar vídeo público, incrustarlo y emitir en directo.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Reproductor incrustable y showcases incluidos en todos los planes.</li>
<li>Portfolios web desde Standard, con protección por contraseña.</li>
<li>Enlaces de revisión con comentarios de código de tiempo, sin cuenta para el revisor.</li>
<li>2&nbsp;TB de almacenamiento ya en Starter; interfaz en español.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Precio por asiento, y la revisión exige Standard o superior.</li>
<li>Sin exportación documentada de comentarios a editores.</li>
<li>Los portfolios son solo de vídeo: la fotografía se queda fuera.</li>
<li>Los portfolios con dominio propio no soportan SSL.</li>
<li>Las cuentas Starter creadas antes del 17 de junio de 2024 conservan un límite de 60 vídeos.</li>
</ul>
<p><strong>Precio:</strong> Starter, 12&nbsp;$ por asiento/mes (2&nbsp;TB); Standard, 25&nbsp;$ (4&nbsp;TB, 5 asientos incluidos); Advanced, 75&nbsp;$ (7&nbsp;TB, 10 asientos). El desglose entre facturación mensual y anual no aparece en su tabla pública.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Comentarios en vídeo</th><th>Exporta al editor</th><th>Fotografía</th><th>Vídeo público / directos</th><th>Modelo de precio</th><th>Precio de referencia</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Por fotograma</span></td><td><span class="pv-si">Marcadores a DaVinci Resolve y Final Cut Pro</span></td><td><span class="pv-si">Galerías con favoritas y comentarios</span></td><td>No</td><td>Por cuenta, revisores ilimitados</td><td>89 € + IVA/año (250 GB)</td></tr>
<tr><td>Vimeo</td><td>Con código de tiempo (desde Standard)</td><td>No documentado</td><td>No</td><td>Sí, con showcases y portfolios</td><td>Por asiento</td><td>25 $/asiento/mes (Standard)</td></tr>
<tr><td>Frame.io</td><td>Por fotograma, por rango y anotaciones</td><td>Marcadores en Premiere Pro; CSV</td><td>Sí, con visor y enlaces de revisión</td><td>No</td><td>Por miembro</td><td>15 $/miembro/mes (Pro)</td></tr>
<tr><td>Dropbox Replay</td><td>Sí; vínculo al fotograma no documentado</td><td>Integración con editores; marcadores no documentados</td><td>No</td><td>No</td><td>Por usuario, sobre un plan de Dropbox</td><td>120 $/usuario/año + Dropbox</td></tr>
</tbody>
</table>
</div>

<h2>Cómo decidir</h2>
<p>Separa alojamiento de revisión y la decisión se vuelve fácil. Si publicas vídeo, quédate en Vimeo aunque revises en otro sitio. Si revisas en equipo y grabas para la nube, Frame.io. Si tu archivo está en Dropbox y hay audio de por medio, Replay. Y si a quien tienes que enseñarle el corte es tu cliente — que después querrá también las fotos, y descargarlas, y un enlace que no caduque —, <a href="/">Positiva</a> cubre ese recorrido entero: puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB.</p>
""",
faq=[
('¿Qué alternativa a Vimeo permite que el cliente comente el vídeo?',
 'Positiva y Frame.io lo hacen sobre el fotograma exacto; Vimeo, con comentarios de código de tiempo desde el plan Standard. En Positiva el revisor entra por enlace y sin cuenta, y en Vimeo también puede comentar sin cuenta de Vimeo.'),
('¿Alguna exporta los comentarios a mi programa de edición?',
 'Positiva exporta los comentarios como marcadores a DaVinci Resolve y Final Cut Pro. Frame.io importa comentarios como marcadores en Premiere Pro y exporta en CSV. En Vimeo no hemos encontrado exportación a editores en su documentación oficial.'),
('¿Cuál sale más barata si solo reviso con clientes?',
 'Las que no cobran por asiento. Vimeo, Frame.io y Dropbox Replay multiplican el precio por miembro, asiento o usuario; en Positiva los revisores entran por enlace y el precio no cambia con el número de personas que opinan.'),
('¿Puedo sustituir Vimeo si lo uso para incrustar vídeo en mi web?',
 'No con las alternativas de esta lista: ninguna aloja vídeo público con reproductor incrustable ni emite en directo. Si publicas y además revisas, lo razonable es separar las dos funciones en dos herramientas.'),
('¿Qué pasa con la fotografía?',
 'Vimeo y Dropbox Replay son de vídeo (y Replay, también de audio). Frame.io admite fotografía con visor propio y enlaces de revisión. Positiva entrega y revisa fotografía y vídeo en la misma galería, con favoritas y comentarios en ambos.'),
('¿Cuánto almacenamiento necesito de verdad?',
 'Depende de si archivas o solo entregas. Vimeo parte de 2 TB porque asume que tu catálogo vive allí; una herramienta de entrega necesita menos, porque el original sigue en tu disco. Los 250 GB del plan Autor de Positiva dan para muchas entregas en curso, pero no para ser tu archivo.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada herramienta. Los precios en dólares son los de la edición estadounidense de cada web.</p>',
),

# ══ 7 · DROPBOX REPLAY ════════════════════════════════════════════
dict(
slug='alternativas-a-dropbox-replay',
title='Alternativas a Dropbox Replay para revisar vídeo (2026) · Blog de Positiva',
h1='Alternativas a Dropbox Replay para revisar vídeo (2026)',
desc='Guía de alternativas a Dropbox Replay: revisión de vídeo con comentarios por fotograma, entrega al cliente, audio y precio real sumando el plan de Dropbox.',
lede='Dropbox Replay añade revisión de vídeo y audio a los archivos que ya tienes en Dropbox. Si buscas alternativa suele ser por el precio real — son dos cuotas — o porque además de revisar necesitas entregar. Esta guía compara las opciones según tu caso.',
date_iso='2026-09-10', date_h='10 de septiembre de 2026',
list_names=['Positiva', 'Frame.io', 'Vimeo', 'Dropbox Replay'],
body="""
<p>Dropbox Replay no es un plan, es un complemento: 12&nbsp;$ por usuario y mes con facturación mensual, 10&nbsp;$ con anual — 120&nbsp;$ al año — <em>sobre</em> un plan de pago de Dropbox, que es requisito. Sin el complemento, Replay funciona con un tope de 4 archivos (10 en Essentials y Business Plus). A cambio trae algo poco común: revisión de audio con calidad sin pérdida, además de vídeo, con archivos de hasta 150&nbsp;GB y 12 horas.</p>
<p>Los motivos habituales para mirar alternativas: que la factura real son dos suscripciones sumadas; que Replay revisa pero no entrega — no hay galería de cliente, ni fotografía, ni portfolio —; y que su documentación no declara si los comentarios quedan anclados al fotograma exacto, algo que en revisión de vídeo no es un detalle menor.</p>

<h2>Qué alternativa a Dropbox Replay elegir</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Si buscas…</th><th>Mejor opción</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Revisar y entregar foto y vídeo al cliente</td><td><a href="/">Positiva</a></td><td>Comentarios por fotograma y entrega con tu marca, en una sola cuota</td></tr>
<tr><td>Revisión en un equipo de postproducción</td><td>Frame.io</td><td>Comentarios por rango, anotaciones y Camera to Cloud</td></tr>
<tr><td>Alojar y publicar el vídeo además de revisarlo</td><td>Vimeo</td><td>Reproductor incrustable, showcases y directos</td></tr>
<tr><td>Revisar audio, o no mover tu archivo de sitio</td><td>Quedarte en Dropbox Replay</td><td>Es la única de la lista que revisa audio, y trabaja sobre tu Dropbox</td></tr>
</tbody>
</table>
</div>

<h2>Por qué cambiar (o no) desde Dropbox Replay</h2>
<ul>
<li><strong>El precio real son dos cuotas.</strong> Los 120&nbsp;$ al año del complemento se suman al plan de Dropbox: con Plus a 9,99&nbsp;$/mes en facturación anual, la cuenta pasa de 240&nbsp;$ anuales por una persona.</li>
<li><strong>Revisar no es entregar.</strong> Cuando el corte está aprobado, la entrega final al cliente — con tu marca, con las fotografías al lado, con permisos por enlace — sigue siendo otro problema y, normalmente, otra herramienta.</li>
<li><strong>La fotografía se queda fuera.</strong> Replay es vídeo y audio; una boda o una campaña mixta necesita algo más.</li>
<li><strong>Faltan garantías documentadas.</strong> No hemos encontrado en su documentación oficial que los comentarios queden vinculados al fotograma, ni que la integración con Premiere, Final Cut Pro o DaVinci Resolve exporte marcadores al timeline; Dropbox declara la integración, pero no ese detalle.</li>
<li><strong>Los equipos que no pagan con tarjeta</strong> deben comprar un mínimo de 10 complementos.</li>
</ul>
<p>Y el motivo para quedarse: si revisas audio — una mezcla, una locución, una banda sonora — Replay es la única de esta comparativa que lo cubre, y con audio sin pérdida. Si además tu archivo ya vive en Dropbox, no mover nada tiene un valor real.</p>

<p><strong>Cómo hemos hecho esta comparativa:</strong> hemos revisado las páginas oficiales de precios y los centros de ayuda de cada herramienta y las hemos comparado según los criterios que decide alguien que busca una alternativa a Dropbox Replay: comentarios y su precisión, audio, exportación al editor, entrega al cliente, fotografía, modelo de precio e idioma. Positiva es nuestro producto, así que señalamos también los casos en los que otra herramienta encaja mejor.</p>

<h2>Positiva: mejor para revisar y entregar al cliente</h2>
<p><a href="/">Positiva</a> cubre el tramo que a Replay le falta: después de revisar hay que entregar. Tu cliente comenta <a href="/revision-video/">sobre el fotograma exacto</a> — y tú te llevas esos comentarios como marcadores a DaVinci Resolve o Final Cut Pro — y cuando el corte está aprobado, la misma <a href="/galerias/">galería</a> hace la entrega final, con las fotografías al lado y con tu marca.</p>
<p><strong>Mejor para:</strong> videógrafos y productoras que revisan con el cliente y después entregan.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios anclados al fotograma, exportables como marcadores a DaVinci Resolve y Final Cut Pro.</li>
<li>Una sola cuota: no necesita ningún otro plan por debajo.</li>
<li>Sin coste por revisor: entra quien tenga el enlace.</li>
<li>Fotografía y vídeo en la misma galería, con favoritas y comentarios <a href="/revision-foto/">foto a foto</a>.</li>
<li>Entrega final con enlaces que no caducan y <a href="/portfolio/">portfolio público</a>; en español y con los datos en la UE.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>No revisa audio suelto: no hay equivalente a la revisión de audio sin pérdida de Replay.</li>
<li>Sin transcripción ni subtítulos automáticos, ni comparación de versiones en paralelo.</li>
<li>No es almacenamiento sincronizado: no sustituye a Dropbox como disco de trabajo.</li>
<li>Admite JPEG y MP4 con H.264; el almacenamiento va por plan.</li>
</ul>
<p><strong>Precio:</strong> <a href="/precios/">Autor, 89&nbsp;€&nbsp;+&nbsp;IVA/año (250&nbsp;GB); Estudio, 219&nbsp;€&nbsp;+&nbsp;IVA/año (1&nbsp;TB)</a>. Plan gratuito de 15&nbsp;GB y 2 galerías.</p>
<p><strong>No la elegiríamos si:</strong> lo que revisas es audio, o necesitas que la herramienta sea también tu disco sincronizado.</p>

<h2>Frame.io: mejor para postproducción en equipo</h2>
<p>Frame.io es la alternativa a Replay cuando la revisión es el trabajo, no un paso: comentarios de fotograma único y de rango, anotaciones dibujadas sobre la imagen y Camera to Cloud desde el rodaje, con integración real en Premiere Pro.</p>
<p><strong>Mejor para:</strong> equipos de postproducción con varios montadores.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios por fotograma, por rango A→B y anotaciones dibujadas.</li>
<li>Importación de comentarios como marcadores en Premiere Pro; exportación en CSV.</li>
<li>Camera to Cloud, y almacenamiento que crece por miembro (2&nbsp;TB en Pro, +2&nbsp;TB por miembro).</li>
<li>Admite también fotografía; interfaz en diez idiomas, español incluido.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Se paga por miembro: 15&nbsp;$ en Pro y 25&nbsp;$ en Team, por miembro y mes, más impuestos.</li>
<li>No revisa audio suelto como producto propio.</li>
<li>La integración con DaVinci Resolve está marcada como heredada; con Final Cut Pro no hemos encontrado documentación oficial.</li>
<li>Sin entrega final con portfolio.</li>
</ul>
<p><strong>Precio:</strong> Pro, 15&nbsp;$ por miembro/mes más impuestos (2&nbsp;TB, hasta 5 miembros); Team, 25&nbsp;$ (3&nbsp;TB, hasta 15). Plan gratuito de 2&nbsp;GB, o 100&nbsp;GB si eres suscriptor de Creative Cloud.</p>

<h2>Vimeo: mejor para alojar y publicar el vídeo</h2>
<p>Vimeo sustituye a Replay si además de revisar necesitas que el vídeo viva en algún sitio público: el mismo archivo que revisas con enlaces de comentarios se incrusta luego en tu web o entra en un showcase.</p>
<p><strong>Mejor para:</strong> quien revisa y además publica.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Comentarios con código de tiempo, y el revisor puede comentar sin cuenta.</li>
<li>Reproductor incrustable y showcases en todos los planes; portfolios desde Standard.</li>
<li>2&nbsp;TB de almacenamiento ya en Starter, 4&nbsp;TB en Standard.</li>
<li>Interfaz en español.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Precio por asiento, y los enlaces de revisión exigen Standard (25&nbsp;$ por asiento/mes) o superior.</li>
<li>Sin exportación documentada de comentarios a editores.</li>
<li>Sin fotografía ni audio.</li>
<li>Los portfolios con dominio propio no soportan SSL.</li>
</ul>
<p><strong>Precio:</strong> Starter, 12&nbsp;$ por asiento/mes; Standard, 25&nbsp;$; Advanced, 75&nbsp;$. El desglose entre facturación mensual y anual no aparece en su tabla pública.</p>

<h2>Dropbox Replay: mejor para revisar audio sin salir de tu archivo</h2>
<p>Conviene mirar qué te está dando Replay antes de sustituirlo. Si revisas audio, o si el material ya está sincronizado en Dropbox y moverlo a otra plataforma implica volver a subirlo todo, el complemento sigue teniendo su lugar.</p>
<p><strong>Mejor para:</strong> revisión de vídeo y audio sobre un archivo que ya vive en Dropbox.</p>
<p><strong>Ventajas:</strong></p>
<ul>
<li>Revisa vídeo y audio, con audio sin pérdida — nadie más en esta lista lo hace.</li>
<li>Transcripción y subtítulos automáticos, comparación de versiones y fechas de entrega.</li>
<li>Enlaces con contraseña y marca de agua digital.</li>
<li>Archivos de hasta 150&nbsp;GB y 12 horas; el material no se mueve de sitio.</li>
</ul>
<p><strong>Limitaciones:</strong></p>
<ul>
<li>Exige un plan de pago de Dropbox por debajo: la factura real son dos cuotas.</li>
<li>Sin el complemento, tope de 4 archivos (10 en Essentials y Business Plus).</li>
<li>Sin galerías de fotografía, sin entrega final y sin portfolio.</li>
<li>Los equipos que no pagan con tarjeta deben comprar un mínimo de 10 complementos.</li>
</ul>
<p><strong>Precio:</strong> 12&nbsp;$ por usuario/mes con facturación mensual, 10&nbsp;$ con anual (120&nbsp;$/año), más el plan de Dropbox: Plus desde 9,99&nbsp;$/mes con facturación anual, Standard 15&nbsp;$/usuario/mes anual.</p>

<h2>Comparativa de datos</h2>
<div class="tabla-scroll">
<table>
<thead><tr><th>Herramienta</th><th>Comentarios en vídeo</th><th>Audio</th><th>Exporta al editor</th><th>Entrega al cliente</th><th>Modelo de precio</th><th>Precio de referencia</th></tr></thead>
<tbody>
<tr><td>Positiva</td><td><span class="pv-si">Por fotograma</span></td><td>No</td><td><span class="pv-si">Marcadores a DaVinci Resolve y Final Cut Pro</span></td><td><span class="pv-si">Galería con tu marca + portfolio</span></td><td>Una cuota, revisores ilimitados</td><td>89 € + IVA/año (250 GB)</td></tr>
<tr><td>Dropbox Replay</td><td>Sí; vínculo al fotograma no documentado</td><td><span class="pv-si">Sí, sin pérdida</span></td><td>Integración con editores; marcadores no documentados</td><td>No</td><td>Por usuario + plan de Dropbox</td><td>120 $/usuario/año + Dropbox</td></tr>
<tr><td>Frame.io</td><td>Por fotograma, por rango y anotaciones</td><td>No como producto propio</td><td>Marcadores en Premiere Pro; CSV</td><td>Presentaciones con marca, sin portfolio</td><td>Por miembro</td><td>15 $/miembro/mes (Pro)</td></tr>
<tr><td>Vimeo</td><td>Con código de tiempo (desde Standard)</td><td>No</td><td>No documentado</td><td>Showcases y portfolios de vídeo</td><td>Por asiento</td><td>25 $/asiento/mes (Standard)</td></tr>
</tbody>
</table>
</div>

<h2>Cómo decidir</h2>
<p>Si revisas audio, quédate: Replay es la única de la lista que lo hace. Si tu equipo es de postproducción y necesitas anotaciones y Camera to Cloud, Frame.io. Si el vídeo acaba publicado, Vimeo. Y si lo que viene después de la revisión es entregar el trabajo a un cliente — con las fotos al lado, con tu marca y con un enlace que no caduque —, ese recorrido entero lo hace <a href="/">Positiva</a> en una sola cuota: puedes <a href="https://app.positiva.studio/registro">probarla gratis</a> con 15&nbsp;GB. La comparación detallada está en <a href="/positiva-vs-dropbox/">Positiva vs Dropbox</a>.</p>
""",
faq=[
('¿Cuánto cuesta realmente Dropbox Replay?',
 'El complemento son 10 $ por usuario y mes con facturación anual —120 $ al año— pero exige un plan de pago de Dropbox por debajo. Con Dropbox Plus a 9,99 $/mes en facturación anual, el coste real de una sola persona supera los 240 $ anuales.'),
('¿Qué alternativa permite comentar sobre el fotograma exacto?',
 'Positiva y Frame.io lo documentan explícitamente, y Frame.io añade comentarios de rango y anotaciones dibujadas. Vimeo trabaja con código de tiempo. En la documentación oficial de Replay no hemos encontrado declarado ese anclaje al fotograma.'),
('¿Hay alguna alternativa que revise audio?',
 'De esta comparativa, no. Replay es la única que revisa audio, y además con calidad sin pérdida. Si el audio es parte de tu flujo, ese es un motivo sólido para quedarse.'),
('¿Puedo usar Replay gratis?',
 'Con límites: sin el complemento de pago se pueden crear 4 archivos en la mayoría de planes de Dropbox y 10 en Essentials y Business Plus. Para uso continuado hace falta el complemento.'),
('¿Cuál sirve también para entregar el trabajo terminado?',
 'Positiva: la misma herramienta con la que revisas hace la entrega final, con fotografías y vídeos en la galería, permisos por enlace y portfolio público. Frame.io tiene presentaciones con marca propia pero no portfolio, y Replay y Vimeo no cubren la entrega de fotografía.'),
('¿Merece la pena cambiar si ya pago Dropbox por el almacenamiento?',
 'Si Dropbox es tu disco de trabajo, no lo sustituyas: ninguna de estas herramientas es almacenamiento sincronizado. La pregunta real es si necesitas el complemento de revisión o si esa parte la resuelve mejor una herramienta que además entregue.'),
],
extra_foot='<p><strong>Datos actualizados:</strong> precios, planes, funcionalidades y límites comprobados el 10 de septiembre de 2026 en las páginas oficiales de precios y los centros de ayuda de cada herramienta. Los precios en dólares son los de la edición estadounidense de cada web.</p>',
),

]
