# Positiva · landing (positiva.studio)

Landing pública, **estática y autocontenida**. Proyecto **independiente** de la app
(`app.positiva.studio`) y de lo desplegado en `test.positiva.studio`. No comparte
repo, build, base de datos ni pipeline con ellos.

## Estructura

```
public/            → raíz estática que publica Cloudflare Pages
  index.html       ·  ~31 KB (antes 180 KB)
  favicon.svg      ·  favicon vectorial "P."
  _headers         ·  caché de estáticos + cabeceras de seguridad (CSP incl.)
  fonts/           ·  5 woff2 auto-alojados (Newsreader, Instrument Sans, Space Mono)
  img/             ·  7 fotos × {avif, webp, jpg}  (el HTML sirve AVIF, con fallbacks)
  assets/          ·  og.png (1200×630), favicons png
functions/
  api/waitlist.js  →  Pages Function: POST /api/waitlist → Supabase
schema.sql         →  DDL de la tabla waitlist (para la instancia Supabase NUEVA)
_serve.mjs         →  servidor estático solo para pruebas locales (no se despliega)
```

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

## Despliegue (Cloudflare Pages)

Proyecto de Pages **nuevo y separado**. Sin comando de build.

- **Build command:** *(vacío)*
- **Build output directory:** `public`
- **Root directory:** `/` (para que Pages detecte `functions/`)

### Variables de entorno del proyecto de Pages (Producción y Preview)

La Function necesita estos secretos (⚠️ instancia de Supabase **exclusiva** de la
landing, nunca la de la app):

| Variable | Valor |
|---|---|
| `SUPABASE_URL` | `https://<ref>.supabase.co` |
| `SUPABASE_SERVICE_KEY` | service_role key (secreto; solo servidor) |

### Base de datos (Supabase nuevo)

Ejecutar [`schema.sql`](schema.sql) en el SQL editor del proyecto Supabase nuevo.

## Dominio

`positiva.studio` (raíz) → este proyecto de Pages. **No** apuntar el DNS hasta
revisar la preview `*.pages.dev`. `app.` y `test.` no se tocan.
