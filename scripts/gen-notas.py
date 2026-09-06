#!/usr/bin/env python3
# Genera /notas/ (índice + artículos) a partir de ARTICLES.
import os, json, html

ROOT = os.path.join(os.path.dirname(__file__), '..', 'public')

CSS = """
.notas-doc{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:clamp(36px,5vw,72px);padding-top:clamp(110px,14vh,150px);padding-bottom:var(--pv-s8)}
.notas-doc .art{max-width:720px;min-width:0}
.notas-fecha{font-family:var(--pv-mono);font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--pv-tinta-30);margin-bottom:var(--pv-s6)}
.notas-rail{position:sticky;top:110px;align-self:start;display:grid;gap:var(--pv-s4)}
.banner-pv{background:var(--pv-sala);color:#EDECE8;border-radius:var(--pv-r-panel);padding:var(--pv-s5)}
.banner-pv .bp-logo{font-family:'Space Mono',ui-monospace,monospace;font-weight:700;font-size:15px;letter-spacing:.2em;text-transform:uppercase}
.banner-pv .bp-logo b{color:var(--pv-ambar)}
.banner-pv p{font-size:14px;line-height:1.6;color:#B8B7B1;margin:10px 0 16px}
.banner-pv .bp-btn{display:inline-block;background:var(--pv-ambar);color:#171614;font-family:var(--pv-mono);font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;padding:12px 18px;border-radius:var(--pv-r-pill)}
.banner-pv .bp-nota{display:block;font-family:var(--pv-mono);font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#7A7973;margin-top:12px}
.banner-mini{border:1px solid var(--pv-linea);border-radius:var(--pv-r-panel);padding:var(--pv-s4) var(--pv-s5);background:var(--pv-luz)}
.banner-mini h3{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--pv-tinta-60);margin-bottom:var(--pv-s3)}
.banner-mini a{display:block;font-size:13.5px;color:var(--pv-tinta-60);text-decoration:none;padding:4px 0}
.banner-mini a:hover{color:var(--pv-tinta)}
.prosa .tabla-scroll{overflow-x:auto;margin:var(--pv-s5) 0}
.prosa table th{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--pv-tinta-60);text-align:left;padding:10px 12px;border-bottom:2px solid var(--pv-tinta)}
.prosa table td{padding:10px 12px;border-bottom:1px solid var(--pv-linea);vertical-align:top}
.prosa table td:first-child{font-weight:700;white-space:nowrap}
.pv-si{color:var(--pv-ambar-ink);font-weight:700}
.notas-lista{display:grid;gap:var(--pv-s5);margin-top:var(--pv-s7)}
.nota-card{display:block;border:1px solid var(--pv-linea);border-radius:var(--pv-r-panel);background:var(--pv-luz);padding:var(--pv-s5) var(--pv-s6);text-decoration:none;color:var(--pv-tinta);transition:box-shadow .2s,transform .2s}
.nota-card:hover{box-shadow:0 24px 60px -30px rgba(23,22,20,.35);transform:translateY(-2px)}
.nota-card .nc-fecha{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--pv-tinta-30)}
.nota-card h2{font-size:clamp(21px,2.2vw,27px);margin:8px 0 8px}
.nota-card p{font-size:15.5px;line-height:1.6;color:var(--pv-tinta-60)}
@media(max-width:960px){.notas-doc{grid-template-columns:1fr}.notas-rail{position:static}}
"""

RAIL = """
  <aside class="notas-rail">
    <div class="banner-pv">
      <span class="bp-logo">Positiva<b>.</b></span>
      <p>Galerías de entrega y revisión de fotos y vídeo, con tu marca. En español y con los datos en la Unión Europea.</p>
      <a class="bp-btn" href="https://app.positiva.studio">Prueba Positiva gratis</a>
      <span class="bp-nota">15 GB y 2 galerías · sin tarjeta</span>
    </div>
    <div class="banner-mini">
      <h3>Comparativas</h3>
      <a href="/positiva-vs-wetransfer/">Positiva vs WeTransfer</a>
      <a href="/positiva-vs-pictime-vs-pixieset/">Positiva vs Pic-Time · Pixieset</a>
      <a href="/positiva-vs-dropbox/">Positiva vs Dropbox</a>
      <a href="/positiva-vs-google-drive/">Positiva vs Google Drive</a>
    </div>
    <div class="banner-mini">
      <h3>Conoce Positiva</h3>
      <a href="/galerias/">Galerías de entrega</a>
      <a href="/revision-video/">Revisión de vídeo</a>
      <a href="/revision-foto/">Revisión de fotografías</a>
      <a href="/precios/">Precios</a>
    </div>
  </aside>
"""

HEAD = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="https://positiva.studio{path}">
<meta property="og:image" content="https://positiva.studio/assets/og.png">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#F1F0EC">
<link rel="canonical" href="https://positiva.studio{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/fonts/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/instrument.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/soporte/soporte.css">
<style>{css}</style>
{schema}
</head>
<body class="pagina-articulo">

<a class="saltar" href="#contenido">Saltar al contenido</a>

<!-- pv:nav -->
<!-- /pv:nav -->
"""

FOOT = """
<!-- pv:footer -->
<!-- /pv:footer -->

</body>
</html>
"""


def article_page(a):
    schema_blocks = []
    items = [{"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(a['list_names'])]
    schema_blocks.append({
        "@context": "https://schema.org", "@type": "Article",
        "headline": a['h1'],
        "description": a['desc'],
        "datePublished": a['date_iso'], "dateModified": a['date_iso'],
        "inLanguage": "es",
        "author": {"@type": "Organization", "name": "Positiva", "url": "https://positiva.studio/"},
        "publisher": {"@id": "https://positiva.studio/#org"},
        "mainEntityOfPage": f"https://positiva.studio/notas/{a['slug']}/",
    })
    schema_blocks.append({
        "@context": "https://schema.org", "@type": "ItemList",
        "name": a['h1'], "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "itemListElement": items,
    })
    if a.get('faq'):
        schema_blocks.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a['faq']],
        })
    schema = '\n'.join(
        '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + '</script>'
        for b in schema_blocks)

    faq_html = ''
    if a.get('faq'):
        faq_html = '\n<h2>Preguntas frecuentes</h2>\n' + '\n'.join(
            f'<h3>{q}</h3>\n<p>{r}</p>' for q, r in a['faq'])

    body = HEAD.format(title=a['title'], desc=a['desc'], ogtype='article',
                       path=f"/notas/{a['slug']}/", css=CSS, schema=schema)
    body += f"""
<main id="contenido">
<div class="wrap notas-doc">
  <article class="art">
    <nav class="miga" aria-label="Migas de pan"><a href="/notas/">Notas</a> <span aria-hidden="true">·</span> <span>Alternativas</span></nav>
    <h1>{a['h1']}</h1>
    <p class="lede">{a['lede']}</p>
    <p class="notas-fecha">{a['date_h']} · Notas de Positiva</p>
    <div class="prosa">
{a['body']}
{faq_html}
    </div>
  </article>
{RAIL}
</div>
</main>
"""
    body += FOOT
    d = os.path.join(ROOT, 'notas', a['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(body)
    print('✓ notas/' + a['slug'])


def index_page(articles):
    schema = '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Blog",
        "name": "Notas de Positiva",
        "url": "https://positiva.studio/notas/",
        "inLanguage": "es",
        "publisher": {"@id": "https://positiva.studio/#org"},
    }, ensure_ascii=False) + '</script>'
    cards = '\n'.join(f"""      <a class="nota-card" href="/notas/{a['slug']}/">
        <span class="nc-fecha">{a['date_h']}</span>
        <h2>{a['h1']}</h2>
        <p>{a['lede']}</p>
      </a>""" for a in articles)
    body = HEAD.format(
        title='Notas · Positiva',
        desc='Guías y comparativas para fotógrafos, videógrafos y productoras: alternativas a las herramientas de siempre, entrega de galerías y revisión de fotos y vídeo.',
        ogtype='website', path='/notas/', css=CSS, schema=schema)
    body += f"""
<main id="contenido">
<div class="wrap notas-doc">
  <div class="art">
    <p class="eyebrow">Notas</p>
    <h1 style="font-size:clamp(32px,3.8vw,50px);margin:var(--pv-s3) 0 var(--pv-s4)">Guías y comparativas para foto y vídeo</h1>
    <p class="lede">Lo que aprendemos construyendo Positiva, contado sin humo: qué herramienta encaja en cada flujo, cuánto cuesta de verdad y qué letra pequeña conviene leer.</p>
    <div class="notas-lista">
{cards}
    </div>
  </div>
{RAIL}
</div>
</main>
"""
    body += FOOT
    os.makedirs(os.path.join(ROOT, 'notas'), exist_ok=True)
    open(os.path.join(ROOT, 'notas', 'index.html'), 'w').write(body)
    print('✓ notas/ (índice)')


if __name__ == '__main__':
    from notas_content import ARTICLES
    for a in ARTICLES:
        article_page(a)
    index_page(ARTICLES)
