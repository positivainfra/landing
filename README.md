# Positiva · landing (positiva.studio)

Landing pública, **estática y autocontenida**. Proyecto **independiente** de la app
(`app.positiva.studio`) y de lo desplegado en `test.positiva.studio`. No comparte
repo, build, base de datos ni pipeline con ellos.

## Estructura

Modelo **Worker + static assets** de Cloudflare (`wrangler.jsonc` + `worker.js`).
Los ficheros de `public/` se sirven directos; solo `/api/waitlist` llega al Worker.

```
wrangler.jsonc     →  config: main=worker.js, assets=./public
worker.js          →  Worker: POST /api/waitlist → Supabase; resto → assets
public/            → assets estáticos
  index.html       ·  ~31 KB (antes 180 KB)
  favicon.svg      ·  favicon vectorial "P."
  _headers         ·  caché de estáticos + cabeceras de seguridad (CSP incl.)
  fonts/           ·  5 woff2 auto-alojados (Newsreader, Instrument Sans, Space Mono)
  img/             ·  7 fotos × {avif, webp, jpg}  (el HTML sirve AVIF, con fallbacks)
  assets/          ·  og.png (1200×630), favicons png
schema.sql         →  DDL de la tabla waitlist (para la instancia Supabase NUEVA)
_serve.mjs         →  servidor estático solo para pruebas locales (no se despliega)
```

## Cabecera y pie comunes (nav + footer)

La navegación y el pie viven en **`partials/`** y se propagan a todas las
páginas con marcadores `<!-- pv:nav -->` / `<!-- pv:footer -->`:

```bash
npm run stamp        # re-estampa partials/ en las páginas listadas en scripts/stamp.mjs
```

- Edita `partials/chrome-nav.html` o `partials/chrome-footer.html`, nunca el
  bloque estampado dentro de las páginas (se sobrescribe).
- Página nueva: añade ambos marcadores a su HTML y su ruta a `PAGES` en
  `scripts/stamp.mjs`.
- `/soporte/` queda fuera del stamp (tiene su propio flujo).
- El footer es el mapa del sitio: toda página pública nueva debe enlazarse ahí
  (y añadirse a `sitemap.xml`).

## Legales (generadas, no se editan aquí)

`/aviso-legal/`, `/privacidad/`, `/terminos/` y sus gemelas inglesas
`/en/legal-notice/`, `/en/privacy/`, `/en/terms/` **no se mantienen a mano**:
las genera el repo de la app (SHOWCASEBRAIN) desde el mismo texto que pinta
`/legal/*` (`frontend/src/legal/content/` y `content/en/`). Un cambio de texto
va allí, en castellano e inglés a la vez, y se vuelve a generar. Cada página
declara el hreflang de su pareja, y de ese `<link>` sale el enlace de idioma de
su nav y su pie. `scripts/.huellas-legales.json` guarda la huella de cada una:
si se edita a mano, el generador se niega a pisarla.

(Hasta el 25/10/2026 las castellanas eran a mano y se quedaron en el texto
anterior a la corrección del 06/10 de la app.)

El orden importa:

```bash
# 1. en SHOWCASEBRAIN/frontend (POSITIVA_LANDING_DIR si la landing no es la carpeta hermana)
npm run legales:landing
# 2. aquí: nav y pie (las inglesas reciben los parciales .en)
npm run stamp
# 3. aquí: lastmod (las URLs ya están en sitemap.xml)
npm run sitemap
```

`scripts/new-web/gen.py` no toca ninguno de esos ficheros (puede ir antes o
después), pero sí usa `partials/chrome-footer.en.html`: si cambias ese pie,
ejecuta gen.py **y** stamp. Volver a ejecutar el paso 1 después del 2 no
cambia nada (`npm run legales:landing -- --check` sale con 0).
`gen-sitemap.mjs` saca el lastmod del último commit del fichero: tras
commitear un cambio de legales, vuelve a pasarlo para que lo recoja.

`/legal/extension/` (privacidad de la extensión de Chrome) sigue a mano: no
existe en la app. El contrato de encargado de tratamiento (cuarto documento de
la app) no se publica aquí en ningún idioma.

## Rendimiento

- **Cero peticiones a dominios externos.** Fuentes e imágenes auto-alojadas.
- Fuentes con `font-display:swap`, subconjunto latino y ejes de variación
  instanciados (Newsreader pasó de 278 KB a ~70 KB de carga real).
- Imágenes en AVIF con fallback WebP/JPG vía `<picture>`. Primer fotograma con
  `fetchpriority=high`; el resto `loading=lazy`.

## Desarrollo local

```bash
node _serve.mjs public 4321      # http://localhost:4321
```

Para regenerar imágenes/fuentes hace falta `sharp` (Node) y `fonttools`+`brotli`
(Python). No es necesario para desplegar.

## Despliegue (Cloudflare Worker + assets)

Worker **nuevo y separado**, conectado al repo de GitHub. El build de Git
ejecuta `wrangler deploy`, que lee `wrangler.jsonc`. Sin comando de build extra.

Validar en local antes de subir:

```bash
npx wrangler deploy --dry-run --outdir=/tmp/out   # valida config + bundle
```

### Variables del Worker (⚠️ instancia de Supabase exclusiva de la landing)

| Variable | Valor | Tipo |
|---|---|---|
| `SUPABASE_URL` | `https://<ref>.supabase.co` | Text |
| `SUPABASE_SERVICE_KEY` | service_role key | **Secret** (encrypt) |

### Base de datos (Supabase nuevo)

Ejecutar [`schema.sql`](schema.sql) en el SQL editor del proyecto Supabase nuevo.

## Dominio

`positiva.studio` (raíz) → este Worker (Settings → Domains & Routes → Custom
domain). **No** apuntar el DNS hasta revisar la preview `*.workers.dev`.
`app.` y `test.` no se tocan.
