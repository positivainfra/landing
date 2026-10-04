#!/usr/bin/env python3
"""Genera public/new/index.html y public/new/archivos/index.html a partir de
scripts/new-web/home.src.html (prototipo D «Aire»): rutas reales, fuentes auto-alojadas, pie común,
formulario de demo, noindex. Uso: python3 scripts/new-web/gen.py  (desde la raíz del repo)"""
import re, os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(os.path.dirname(HERE))
src=open(f'{HERE}/home.src.html').read()

# ── 1. estilos ──────────────────────────────────────────────────────────────
style=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
style=style.replace("/* conmutador de prototipo */","/* (conmutador de prototipo retirado) */")
style=re.sub(r'\.proto\{.*?\n\.proto a\[aria-current\][^\n]*\n','',style,flags=re.S)
style=re.sub(r'\n\.view\{display:none\}.*?\nbody:has\(#archivos:target\) #home\{display:none\}','',style,flags=re.S)
style=style.replace("font-weight:500","font-weight:400")  # Playfair solo trae 300–400
FONTS="""@font-face{font-family:'Playfair Display';font-style:normal;font-weight:300 400;font-display:swap;src:url(/fonts/playfair.woff2) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:300 400;font-display:swap;src:url(/fonts/playfair-italic.woff2) format('woff2')}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:400 700;font-display:swap;src:url(/fonts/instrument.woff2) format('woff2')}
@font-face{font-family:'IBM Plex Mono';font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/ibmplexmono-400.woff2) format('woff2')}
@font-face{font-family:'IBM Plex Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/ibmplexmono-700.woff2) format('woff2')}
@font-face{font-family:'Space Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/spacemono-700.woff2) format('woff2')}
"""
# tokens que usa el pie común (partials/chrome-footer.html)
PVTOK="""
:root{--pv-papel:#F3F2EE;--pv-luz:#FFFFFF;--pv-bandeja:#E8E7E1;--pv-sala:#0E0E0D;--pv-tinta:#171614;--pv-tinta-60:#6E6D67;--pv-tinta-30:#A9A8A2;--pv-linea:#DEDDD6;--pv-linea-sala:#2A2A27;--pv-ambar:#C98A2B;--pv-ambar-luz:#F6EAD2;--pv-ambar-hover:#B37A24;--pv-ambar-ink:#8F5F15;--pv-graso:#E0402A;--pv-display:'Playfair Display',Georgia,serif;--pv-sans:'Instrument Sans',-apple-system,system-ui,sans-serif;--pv-mono:'IBM Plex Mono',ui-monospace,monospace;--pv-r-pill:999px;--pv-s1:4px;--pv-s2:8px;--pv-s3:12px;--pv-s4:16px;--pv-s5:24px;--pv-s6:32px;--pv-s7:48px;--pv-s8:64px;--pv-s9:96px;--pv-s10:128px;--pv-ease:cubic-bezier(.4,0,.2,1)}
footer.site{margin-top:0}
.saltar{position:absolute;left:-9999px;top:auto}.saltar:focus{left:16px;top:16px;z-index:100;background:var(--tinta);color:var(--luz);padding:10px 14px;border-radius:999px}
/* formulario de demo */
.demo{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;width:100%;max-width:560px}
.demo input{flex:1;min-width:220px;font:inherit;font-size:16px;padding:14px 18px;border:1px solid var(--linea);border-radius:999px;background:var(--luz);color:var(--tinta)}
.demo input:focus{outline:2px solid var(--ambar);outline-offset:2px}
.demo button{appearance:none;cursor:pointer;font:inherit}
.demo-msg{font-family:var(--mono);font-size:12px;color:var(--tinta-2)}
"""
style=FONTS+style+PVTOK

# ── 2. cuerpo ───────────────────────────────────────────────────────────────
body=src.split('</style>',1)[1]
body=re.sub(r'<div class="proto".*?</div></div>\n','',body,flags=re.S)
body=re.sub(r'<script>.*</script>\s*$','',body,flags=re.S)
# imágenes y vídeos → rutas reales
body=re.sub(r'@@img:public(/[^@|]+)(?:\|\d+)?@@',r'\1',body)
VID={'showcase-hero':'/video/showcase-hero.mp4','revision-video':'/video/revision-video.mp4','entrega':'/video/pasos/entrega.mp4',
     'revision':'/video/pasos/revision.mp4','galeria-hero-720':'/video/galeria-hero-720.mp4','subes':'/video/pasos/subes.mp4',
     'disenas':'/video/pasos/disenas.mp4','revision-comentar':'/video/revision-comentar.mp4','cliente':'/video/pasos/cliente.mp4'}
body=re.sub(r'@@vid:([^@]+)@@',lambda m:VID[m.group(1)],body)
body=body.replace('src="/video/galeria-hero-720.mp4"','data-start="1.6" src="/video/galeria-hero-720.mp4"')
# enlaces del prototipo → enlaces reales
nav_links={'>Entrega</a>':'/galerias/','>Revisión</a>':'/revision-video/','>Portfolio</a>':'/portfolio/','>Precios</a>':'/precios/','>Blog</a>':'/notas/'}
for k,v in nav_links.items(): body=body.replace('<a href="#home"'+k,f'<a href="{v}"'+k)
body=body.replace('<a href="#archivos">Archivos</a>','<a href="/new/archivos/">Archivos</a>')
body=body.replace('<a class="btn ghost" href="#home">Entrar</a>','<a class="btn ghost" href="https://app.positiva.studio">Entrar</a>')
body=body.replace('<a href="#home" class="logo"','<a href="/new/" class="logo"')
body=re.sub(r'<a class="btn" href="#home">Empieza gratis</a>','<a class="btn" href="https://app.positiva.studio/registro" data-ev="register_click">Empieza gratis</a>',body)
body=re.sub(r'<a class="btn ghost" href="#home">Empieza gratis</a>','<a class="btn ghost" href="https://app.positiva.studio/registro" data-ev="register_click">Empieza gratis</a>',body)
body=body.replace('href="#home">Reserva una demo</a>','href="#demo">Reserva una demo</a>')
body=body.replace('href="#home">Probar con el plan Estudio</a>','href="/precios/">Probar con el plan Estudio</a>')
body=body.replace('href="#home">Probar el plan Estudio</a>','href="/precios/">Probar el plan Estudio</a>')
body=body.replace('href="#home">Elegir Autor</a>','href="https://app.positiva.studio/registro" data-ev="register_click">Elegir Autor</a>')
body=body.replace('href="#home">Elegir Estudio</a>','href="https://app.positiva.studio/registro" data-ev="register_click">Elegir Estudio</a>')
body=body.replace('href="#home">Comparativa completa →</a>','href="/positiva-vs-pictime-vs-pixieset/">Comparativa completa →</a>')
# pasos y tarjetas
rep=[('<a class="more" href="#archivos">Archivos y solicitudes</a>','<a class="more" href="/new/archivos/">Archivos y solicitudes</a>'),
     ('<a class="more" href="#home">Revisión de vídeo y foto</a>','<a class="more" href="/revision-video/">Revisión de vídeo y foto</a>'),
     ('<a class="more" href="#home">Galerías de entrega</a>','<a class="more" href="/galerias/">Galerías de entrega</a>'),
     ('<a class="more" href="#home">Portfolio público</a>','<a class="more" href="/portfolio/">Portfolio público</a>'),
     ('<a class="q r d2" href="#archivos">','<a class="q r d2" href="/new/archivos/">')]
for a,b in rep: body=body.replace(a,b)
cards={'Ver las galerías':'/galerias/','Ver los diseños':'/galerias/#diseno','Ver los enlaces':'/galerias/','Ver la revisión de vídeo':'/revision-video/',
       'Ver la revisión de foto':'/revision-foto/','Ver el portfolio':'/portfolio/','Ver la analítica':'/soporte/es/analitica/'}
def card_fix(m):
    block=m.group(0)
    for k,v in cards.items():
        if f'<span class="go">{k}</span>' in block: return block.replace('href="#home"',f'href="{v}"',1)
    return block
body=re.sub(r'<a class="q r[^"]*" href="#home">.*?</a>\n',card_fix,body,flags=re.S)
# cualquier #home restante → /new/
body=body.replace('href="#home"','href="/new/"')

# ── 4. separar vistas ───────────────────────────────────────────────────────
nav_html=re.search(r'<nav class="top".*?</nav>',body,re.S).group(0)
home=re.search(r'<main id="home" class="view">(.*?)</main>',body,re.S).group(1)
arc=re.search(r'<main id="archivos" class="view">(.*?)</main>',body,re.S).group(1)

# página Archivos: hero y lede reescritos
arc=arc.replace('<span class="eyebrow">Archivos y solicitudes · plan Estudio</span>','<span class="eyebrow">Archivos y solicitudes · herramienta de trabajo · plan Estudio</span>')
arc=re.sub(r'<h1 class="h-xl">.*?</h1>','<h1 class="h-xl"><span class="w"><span>Tus&nbsp;archivos</span></span> <span class="w"><span>de&nbsp;trabajo,</span></span> <span class="w"><span><em class="a">donde&nbsp;ya</em></span></span> <span class="w"><span><em class="a">entregas.</em></span></span></h1>',arc,count=1,flags=re.S)
arc=re.sub(r'<p class="lede"><strong[^>]*>.*?</p>','<p class="lede"><strong style="color:var(--tinta);font-weight:600">Almacenamiento, envíos y solicitudes de archivos para fotógrafos, videógrafos y productoras.</strong> Organiza tus carpetas, comparte material con clientes y compañeros, y pide brutos, logos o selecciones con un enlace. No es una función para tu cliente: es tu mesa de trabajo, en el mismo sitio donde entregas.</p>',arc,count=1,flags=re.S)
USOS='''
<section class="sec">
  <div class="head r"><span class="eyebrow">Para qué sirve</span><h2 class="h-l">Tres cosas. Una carpeta.</h2><p class="lede">Lo que hoy haces entre un disco duro, un Drive y un WeTransfer, aquí vive junto a tus galerías.</p></div>
  <div class="flow">
    <div class="r"><div class="num">01</div><h3>Organiza</h3><p>Carpetas de trabajo con la cuota de tu plan: brutos, selecciones, logos de cliente, versiones. El mismo subidor que tus galerías.</p></div>
    <div class="r d1"><div class="num">02</div><h3>Comparte</h3><p>Envía una carpeta o unos archivos a un cliente, un compañero o un laboratorio con un enlace. Sin reenviar, sin que caduque a los siete días.</p></div>
    <div class="r d2"><div class="num">03</div><h3>Solicita</h3><p>Pide material con un enlace: brutos a un segundo operador, logos a un cliente, archivos a un proveedor. Suben sin cuenta y cae donde tú dijiste.</p></div>
  </div>
</section>
'''
arc=arc.replace('<section class="sec">\n  <div class="head r"><span class="eyebrow">Cómo funciona</span><h2 class="h-l">Tres pasos.',USOS+'<section class="sec">\n  <div class="head r"><span class="eyebrow">Cómo funciona una solicitud</span><h2 class="h-l">Tres pasos.',1)
arc=arc.replace('<details><summary>¿Cuánto puede subirme un cliente?</summary>','<details><summary>¿Mis clientes tienen que aprender a usarlo?</summary><p>No. Ellos solo abren un enlace: para ver lo que compartes o para subir lo que pides. Archivos es tu herramienta, no la suya.</p></details>\n    <details><summary>¿Cuánto puede subirme alguien?</summary>')

# formulario de demo (sustituye los botones del cierre de la home)
DEMO='''<form class="demo r d3" id="wl" novalidate>
    <input type="email" name="email" id="wl-email" placeholder="nombre@tuestudio.com" required aria-label="Tu email" autocomplete="email">
    <button type="submit" class="btn">Reserva una demo</button>
  </form>
  <small class="demo-msg r d3" id="msg">Sin compromiso y sin newsletter: te escribo solo para agendarla.</small>'''
home=home.replace('<div class="r d3" style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center"><a class="btn" href="#demo">Reserva una demo</a><a class="btn ghost" href="https://app.positiva.studio/registro" data-ev="register_click">Empieza gratis</a></div>',DEMO)
home=home.replace('<section class="final"><div class="wrap inner">','<section class="final" id="demo"><div class="wrap inner">')

# pie común: copia literal del bloque pv:footer de la home actual
idx=open(f'{ROOT}/public/index.html').read()
i=idx.index('<!-- pv:footer -->'); j=idx.index('<!-- /pv:footer -->')+len('<!-- /pv:footer -->')
footer=idx[i:j]

SCRIPT=open(f'{HERE}/new.js').read()

def page(title,desc,url,main,extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<!-- Versión en pruebas de la nueva web: NO indexar. Al pasar a la raíz, quitar
     esta etiqueta y la regla /new/* de public/_headers. -->
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="Positiva">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://positiva.studio{url}">
<meta property="og:image" content="https://positiva.studio/assets/og.png?v=2">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#F3F2EE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/fonts/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/playfair-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/instrument.woff2" as="font" type="font/woff2" crossorigin>
{extra_head}<style>
{style}
</style>
<script defer src="https://analytics.labbo.studio/stats" data-website-id="ddf13c3b-1f69-4fac-bd38-4629c55611bd"></script>
<script defer src="/js/analytics.js"></script>
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
{nav_html}
<main id="contenido">
{main}
</main>
{footer}
<script>
{SCRIPT}
</script>
</body>
</html>
'''

os.makedirs(f'{ROOT}/public/new/archivos',exist_ok=True)
open(f'{ROOT}/public/new/index.html','w').write(page(
 'Positiva · Galerías, revisión, archivos y portfolio para fotógrafos y videógrafos',
 'Recibe los archivos, revisa con tu cliente sobre la foto o el fotograma, entrega en galerías con tu marca y publica tu portfolio. Alojado en la UE.',
 '/new/',home,'<link rel="preload" href="/video/showcase-hero-poster.jpg" as="image" fetchpriority="high">\n'))
open(f'{ROOT}/public/new/archivos/index.html','w').write(page(
 'Archivos y solicitudes · Positiva',
 'Almacenamiento, envíos y solicitudes de archivos para fotógrafos, videógrafos y productoras. Organiza, comparte y pide brutos con un enlace, sin cuenta para quien sube.',
 '/new/archivos/',arc))
print('ok', len(home), len(arc))
