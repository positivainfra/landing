#!/usr/bin/env python3
"""
Índice del soporte: fuente única del orden de categorías y artículos.

  python3 scripts/soporte-indice.py          (desde la raíz del repo)

A partir de CATS (abajo) y de cada artículo (su <h1> y su <p class="lede">):
  · rehace las secciones del índice public/soporte/es/index.html y su raíl
  · rehace en cada artículo el raíl de su categoría, la miga y las tarjetas
    de «Seguir leyendo» (título y descripción al día)
  · actualiza public/soporte/es/buscador.json (añade los nuevos y refresca
    título, descripción, categoría y texto de los que cambian)

Para añadir un artículo: crea su carpeta, añádelo a CATS y ejecuta esto.
Después: `npm run stamp` (nav y pie) y `python3 scripts/new-web/check.py`.
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES = os.path.join(ROOT, 'public', 'soporte', 'es')

# (id, nombre, resumen para el índice, [slugs en orden])
CATS = [
 ('primeros-pasos', 'Primeros pasos', None, ['que-es-positiva', 'crear-tu-primera-galeria', 'entrega-o-revision', 'el-panel-por-dentro']),
 ('galerias', 'Galerías', None, ['crear-una-galeria', 'crear-galeria-desde-archivos', 'los-pasos-de-una-galeria', 'activa-o-publica', 'caducidad-de-galeria', 'momentos', 'orden-de-las-fotos', 'convertir-entrega-revision', 'borrar-una-galeria']),
 ('subida', 'Subir fotos y vídeos', None, ['subir-fotos-y-videos', 'formatos-admitidos', 'reemplazar-un-archivo', 'versiones-antiguas', 'subida-interrumpida']),
 ('compartir', 'Compartir y descargas', None, ['enlace-de-cliente', 'contrasena-del-enlace', 'permisos-de-descarga', 'enviar-la-galeria', 'zip-descarga-completa', 'revocar-un-enlace']),
 ('archivos', 'Archivos y solicitudes', 'Tus carpetas de trabajo, enlaces para compartirlas y solicitudes para que te suban material.',
  ['archivos-y-carpetas', 'compartir-un-archivo-suelto', 'que-ve-quien-recibe-tu-enlace', 'seleccionar-varios-archivos', 'borrar-y-archivar-archivos', 'pedir-archivos', 'subir-a-una-solicitud', 'archivos-recibidos']),
 ('revision', 'Revisión y comentarios', None, ['como-funciona-la-revision', 'comentarios-en-el-panel', 'quien-ve-los-comentarios', 'rondas-de-revision', 'versiones-de-un-video', 'comparar-versiones', 'marcar-favoritas', 'favoritas-del-cliente', 'importar-favoritas-en-lightroom', 'etiquetar-favoritas-en-finder', 'exportar-marcadores-video']),
 ('revisor', 'Si vas a revisar', None, ['revisor-entrar-en-la-galeria', 'revisor-idioma-de-la-galeria', 'revisor-marcar-y-comentar-fotos', 'revisor-comentar-video', 'revisor-atajos-de-teclado', 'revisor-terminar-ronda', 'revisor-no-me-llega-el-email']),
 ('diseno', 'Diseño y marca', None, ['disenos-de-galeria', 'disenos-de-video', 'el-pase', 'tema-y-tipografia', 'logo-y-marca', 'dominio-propio', 'perfil-publico', 'portfolio']),
 ('cuenta', 'Cuenta y planes', None, ['planes-y-precios', 'almacenamiento', 'ampliar-almacenamiento', 'cambiar-de-plan', 'idioma-del-panel', 'analitica']),
 ('problemas', 'Resolución de problemas', None, ['enlace-no-valido', 'no-puedo-descargar', 'galeria-lenta', 'archivos-que-no-suben']),
]
# Audiencia de los artículos que aún no están en buscador.json
AUDIENCIA_NUEVOS = {
 'archivos-y-carpetas': 'fotografo', 'borrar-y-archivar-archivos': 'fotografo', 'seleccionar-varios-archivos': 'fotografo',
 'que-ve-quien-recibe-tu-enlace': 'ambos', 'pedir-archivos': 'fotografo', 'subir-a-una-solicitud': 'ambos',
 'archivos-recibidos': 'fotografo', 'crear-galeria-desde-archivos': 'fotografo', 'versiones-de-un-video': 'ambos',
 'comparar-versiones': 'ambos', 'revisor-idioma-de-la-galeria': 'revisor', 'idioma-del-panel': 'fotografo',
}

rd = lambda p: open(p, encoding='utf-8').read()
def wr(p, t):
    if rd(p) != t: open(p, 'w', encoding='utf-8').write(t); return 1
    return 0
plano = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()

info, cat_de = {}, {}
for i, (cid, nombre, _, slugs) in enumerate(CATS, 1):
    for s in slugs:
        p = os.path.join(ES, s, 'index.html')
        assert os.path.exists(p), f'falta el artículo {s}'
        t = rd(p)
        info[s] = dict(h1=re.search(r'<h1>(.*?)</h1>', t, re.S).group(1).strip(),
                       lede=re.search(r'<p class="lede">(.*?)</p>', t, re.S).group(1).strip())
        cat_de[s] = (i, cid, nombre)
huerfanos = sorted(d for d in os.listdir(ES) if os.path.isdir(os.path.join(ES, d)) and d not in info)
assert not huerfanos, f'artículos fuera de CATS: {huerfanos}'

# ── artículos: raíl, miga y «Seguir leyendo»
cambiados = 0
for s, (i, cid, nombre) in cat_de.items():
    p = os.path.join(ES, s, 'index.html'); t = rd(p)
    lis = ''.join(f'<li><span aria-current="page">{info[x]["h1"]}</span></li>' if x == s else
                  f'<li><a href="/soporte/es/{x}/">{info[x]["h1"]}</a></li>' for x in CATS[i-1][3])
    rail = (f'<div class="rail-seccion">\n      <p class="eyebrow"><span class="idx">{i:02d}</span> {nombre}</p>\n'
            f'      <ul class="rail-lista">{lis}</ul>\n    </div>')
    t, n = re.subn(r'<div class="rail-seccion">.*?</ul>\s*</div>', lambda m: rail, t, count=1, flags=re.S)
    assert n == 1, f'{s}: sin raíl'
    t, n = re.subn(r'(<nav class="miga"[^>]*>.*?<span aria-hidden="true">·</span>\s*)<a href="/soporte/es/#[^"]*">[^<]*</a>',
                   lambda m: m.group(1) + f'<a href="/soporte/es/#{cid}">{nombre}</a>', t, count=1, flags=re.S)
    assert n == 1, f'{s}: sin miga'
    def tarjeta(m):
        x = m.group(1)
        if x not in info: return m.group(0)
        return f'<a href="/soporte/es/{x}/"><b>{info[x]["h1"]}</b><span>{info[x]["lede"]}</span></a>'
    t = re.sub(r'<a href="/soporte/es/([a-z0-9-]+)/"><b>[^<]*</b><span>.*?</span></a>', tarjeta, t, flags=re.S)
    cambiados += wr(p, t)

# ── índice
p = os.path.join(ES, 'index.html'); t = rd(p)
resumen_previo = dict(re.findall(r'<section class="cat" id="([a-z-]+)">.*?<p class="cat-resumen">(.*?)</p>', t, re.S))
secs = []
for i, (cid, nombre, resumen, slugs) in enumerate(CATS, 1):
    resumen = resumen or resumen_previo[cid]
    filas = '<li>'.join(f'''
      <a href="/soporte/es/{x}/">
        <span class="fila-t">{info[x]["h1"]}</span>
        <span class="fila-d">{info[x]["lede"]}</span>
        <span class="fila-v" aria-hidden="true">→</span>
      </a></li>''' for x in slugs)
    secs.append(f'<section class="cat" id="{cid}">\n  <p class="eyebrow"><span class="idx">{i:02d}</span> {nombre}</p>\n'
                f'  <p class="cat-resumen">{resumen}</p>\n  <ul class="filas"><li>{filas}</ul>\n</section>')
a = t.find('<section class="cat" id="')
b = t.find('</section>', t.rfind('<section class="cat" id="')) + len('</section>')
assert a > 0 and b > a
assert not re.sub(r'<section class="cat" id="[^"]+">.*?</section>', '', t[a:b], flags=re.S).strip(), 'las secciones del índice no son contiguas'
t = t[:a] + '\n'.join(secs) + t[b:]
cats_rail = ''.join(f'<li><a href="#{cid}"><span class="idx">{i:02d}</span> {nombre}</a></li>' for i, (cid, nombre, _, _) in enumerate(CATS, 1))
t, n = re.subn(r'<ul class="rail-cats">.*?</ul>', lambda m: f'<ul class="rail-cats">{cats_rail}</ul>', t, count=1, flags=re.S)
assert n == 1
cambiados += wr(p, t)

# ── buscador
bp = os.path.join(ES, 'buscador.json')
_crudo = rd(bp)
SEP = (',', ':') if '":"' in _crudo[:300] else (', ', ': ')
prev = {x['slug']: x for x in json.load(open(bp, encoding='utf-8'))}
out = []
for cid, nombre, _, slugs in CATS:
    for s in slugs:
        art = rd(os.path.join(ES, s, 'index.html'))
        e = dict(prev.get(s, {}))
        nuevo_o_revisado = s not in prev or '17 de octubre de 2026' in art
        e.update(slug=s, titulo=plano(info[s]['h1']), descripcion=plano(info[s]['lede']), categoria=nombre)
        e.setdefault('audiencia', AUDIENCIA_NUEVOS.get(s, 'fotografo'))
        if nuevo_o_revisado or 'texto' not in e:
            prosa = re.search(r'<div class="prosa">(.*?)</div>\s*<p class="sello">', art, re.S)
            e['texto'] = plano(prosa.group(1)) if prosa else e.get('texto', '')
        out.append({k: e[k] for k in ('slug', 'titulo', 'descripcion', 'categoria', 'audiencia', 'texto')})
nuevo = json.dumps(out, ensure_ascii=False, separators=SEP)
if rd(bp) != nuevo: open(bp, 'w', encoding='utf-8').write(nuevo); cambiados += 1
print(f'{len(info)} artículos en {len(CATS)} categorías · {cambiados} fichero(s) actualizados')
