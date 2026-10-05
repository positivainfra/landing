#!/usr/bin/env python3
"""
Web nueva de Positiva (en pruebas bajo /new/).

  python3 scripts/new-web/gen.py        (desde la raíz del repo)

Cada página es scripts/new-web/pages/<ruta>.html con una cabecera de metadatos
en un comentario y solo el contenido de <main>. Este script:
  · copia positiva.css y positiva.js a public/new/
  · envuelve cada página con <head>, nav (partials/new-nav.html), pie común
    (partials/chrome-footer.html) y scripts, con los marcadores pv:newnav y
    pv:footer para que `npm run stamp` pueda refrescarlos después
  · escribe public/new/<ruta>/index.html

Cabecera de cada página:
  <!--
  title: Título de la pestaña
  description: Meta descripción
  path: /new/galerias/
  preload: /video/galeria-hero-poster.jpg      (opcional)
  -->

Atajos dentro del contenido:
  <!-- @demo -->          formulario de «Reserva una demo» (usa /api/waitlist)
  <!-- @tabla clave -->   tabla comparativa con la celda ganadora de cada fila
                          (fuente única: scripts/comparativas.py, compartida con el blog)

Mientras la web nueva esté en /new/ todas las páginas salen con noindex.
Al pasar a la raíz: cambia INDEXABLE a True y BASE a '/', regenera, y quita la
regla /new/* de public/_headers.
"""
import re, os, sys, shutil, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import comparativas
OUT = os.path.join(ROOT, 'public', 'new')
INDEXABLE = False
BASE = '/new/'

nav = open(os.path.join(ROOT, 'partials', 'new-nav.html')).read().strip()
footer = open(os.path.join(ROOT, 'partials', 'chrome-footer.html')).read().strip()

DEMO = '''<form class="demo" id="wl" data-demo novalidate>
    <input type="email" name="email" id="wl-email" placeholder="nombre@tuestudio.com" required aria-label="Tu email" autocomplete="email">
    <button type="submit" class="btn">Reserva una demo</button>
  </form>
  <small class="demo-msg" id="msg">Sin compromiso y sin newsletter: te escribo solo para agendarla.</small>'''

def meta(src):
    m = re.match(r'\s*<!--(.*?)-->', src, re.S)
    if not m: raise SystemExit('falta la cabecera de metadatos')
    d = {}
    for line in m.group(1).strip().splitlines():
        k, _, v = line.partition(':')
        d[k.strip()] = v.strip()
    return d, src[m.end():].strip()

MIGRADAS = ['galerias', 'revision-video', 'revision-foto', 'portfolio', 'precios',
            'bodas', 'freelance', 'productoras', 'sobre-nosotros',
            'positiva-vs-pictime-vs-pixieset', 'positiva-vs-arcadina', 'positiva-vs-dropbox',
            'positiva-vs-google-drive', 'positiva-vs-wetransfer']

DERIVADAS = ['notas', 'soporte/es', 'novedades', 'aviso-legal', 'privacidad', 'terminos', 'legal/extension']

def enlaces(html):
    if BASE == '/': return html
    for slug in MIGRADAS:
        html = re.sub(rf'href="/{slug}/', f'href="{BASE}{slug}/', html)
    # páginas de contenido: solo URLs de página (acaban en / o llevan #), nunca ficheros
    for slug in DERIVADAS:
        html = re.sub(rf'href="/{slug}/((?:[a-z0-9-]+/)*)(#[^"]*)?"', lambda m: f'href="{BASE}{slug}/{m.group(1)}{m.group(2) or ""}"', html)
    html = re.sub(r'href="/soporte/?"', f'href="{BASE}soporte/es/"', html)
    return html.replace('href="/#', f'href="{BASE}#')

def page(d, body):
    robots = '' if INDEXABLE else ('<!-- Web nueva en pruebas: NO indexar. Ver scripts/new-web/gen.py -->\n'
                                   '<meta name="robots" content="noindex, nofollow">\n')
    canon = d['path'].replace('/new/', '/', 1) if INDEXABLE else d['path']
    pre = ''.join(f'<link rel="preload" href="{p.strip()}" as="image" fetchpriority="high">\n'
                  for p in d.get('preload', '').split(',') if p.strip())
    body = enlaces(comparativas.pintar(body.replace('<!-- @demo -->', DEMO)))
    foot = enlaces(footer)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{d['title']}</title>
<meta name="description" content="{d['description']}">
{robots}<link rel="canonical" href="https://positiva.studio{canon}">
<meta property="og:title" content="{d.get('og', d['title'])}">
<meta property="og:description" content="{d['description']}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://positiva.studio{canon}">
<meta property="og:image" content="https://positiva.studio/assets/og.png?v=2">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3F2EE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/fonts/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/playfair-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/instrument.woff2" as="font" type="font/woff2" crossorigin>
{pre}<link rel="stylesheet" href="{BASE}chrome.css">
<link rel="stylesheet" href="{BASE}positiva.css">
<script defer src="https://analytics.labbo.studio/stats" data-website-id="ddf13c3b-1f69-4fac-bd38-4629c55611bd"></script>
<script defer src="/js/analytics.js"></script>
</head>
<body>
{nav}
<main id="contenido">
{body}
</main>
{foot}
<script src="{BASE}positiva.js" defer></script>
</body>
</html>
'''

os.makedirs(OUT, exist_ok=True)
# positiva.css + las tablas comparativas (mismo CSS que el blog)
open(os.path.join(OUT, 'positiva.css'), 'w').write(open(os.path.join(HERE, 'positiva.css')).read()
    + '\n/* ── Tablas comparativas: scripts/comparativas.py ── */' + comparativas.CSS)
shutil.copy(os.path.join(HERE, 'positiva.js'), os.path.join(OUT, 'positiva.js'))
for f in ('chrome.css', 'docs.css'):
    shutil.copy(os.path.join(HERE, f), os.path.join(OUT, f))
n = 0
for f in sorted(glob.glob(os.path.join(HERE, 'pages', '*.html'))):
    d, body = meta(open(f).read())
    rel = d['path'].replace('/new/', '', 1).strip('/')
    dst = os.path.join(OUT, rel, 'index.html') if rel else os.path.join(OUT, 'index.html')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'w').write(page(d, body))
    n += 1
    print('✓', d['path'])
print(f'{n} página(s) en public/new/')

# ── Páginas derivadas ─────────────────────────────────────────────────────
def derivar(html):
    html = re.sub(r'<!-- pv:nav -->.*?<!-- /pv:nav -->', '<!-- pv:nav -->\n' + nav + '\n<!-- /pv:nav -->', html, count=1, flags=re.S)
    html = re.sub(r'\s*<a class="saltar" href="#contenido">[^<]*</a>', '', html)
    html = re.sub(r'<meta name="robots"[^>]*>\s*', '', html)
    if not INDEXABLE:
        html = html.replace('</title>', '</title>\n<!-- Web nueva en pruebas: NO indexar -->\n<meta name="robots" content="noindex, nofollow">', 1)
    html = html.replace('</head>', f'<link rel="stylesheet" href="{BASE}docs.css">\n</head>', 1)
    html = html.replace('</body>', f'<script src="{BASE}positiva.js" defer></script>\n</body>', 1)
    return enlaces(html)

m = 0
PUB = os.path.join(ROOT, 'public')
for slug in DERIVADAS:
    for src in sorted(glob.glob(os.path.join(PUB, slug, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(src, PUB)
        html = open(src).read()
        if '<!-- pv:nav -->' not in html:
            print('  (sin marcador pv:nav, se omite)', rel); continue
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'w').write(derivar(html))
        m += 1
print(f'{m} página(s) de contenido derivadas en public/new/')
