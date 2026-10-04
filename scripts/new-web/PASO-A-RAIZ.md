# Pasar la web nueva de /new/ a la raíz

Mientras la web nueva vive en `/new/`, todo sale con `noindex` y la web pública
no cambia. Este es el paso a la raíz, en un solo commit.

## Qué hay en /new/

- **16 páginas nuevas** (home, archivos, producto, casos, comparativas, sobre
  nosotros): fuente en `scripts/new-web/pages/*.html`.
- **70 páginas derivadas** (blog, soporte, novedades, legales): NO tienen fuente
  propia. `gen.py` coge cada página real de `public/` y le cambia el envoltorio
  (nav nuevo, `docs.css`, noindex). Su contenido sigue en su sitio de siempre.
- Hojas comunes: `positiva.css` (páginas nuevas), `chrome.css` (nav, todas),
  `docs.css` (capa para las de contenido), `positiva.js`.

Regenerar: `python3 scripts/new-web/gen.py` · comprobar: `python3 scripts/new-web/check.py`

## El cambio, paso a paso

1. **Corregir antes** las comparativas de Arcadina (precios antiguos) y
   WeTransfer (precio Ultimate no verificable).
2. En `scripts/new-web/gen.py`: `INDEXABLE = True`, `BASE = '/'`, y que las
   páginas nuevas se escriban en `public/` en vez de `public/new/`.
3. En `partials/new-nav.html`: cambiar `/new/` por `/` y copiarlo sobre
   `partials/chrome-nav.html`. A partir de ahí `npm run stamp` pone el nav nuevo
   en blog, soporte, novedades y legales (que es exactamente lo que hoy simula
   la derivación).
4. Añadir a esas páginas `<link rel="stylesheet" href="/docs.css">` (una línea
   en `gen-notas.py`, en la plantilla del soporte y en novedades/legales).
5. En `scripts/stamp.mjs`, quitar de `PAGES` las 14 páginas que pasan a generarse
   con `gen.py` (ya no llevan marcadores `pv:nav`).
6. Quitar la regla `/new/*` de `public/_headers`, borrar `public/new/` y
   ejecutar `npm run sitemap` después del commit.
7. Revisar que el buscador de soporte (`buscador.json`) sigue enlazando bien.
