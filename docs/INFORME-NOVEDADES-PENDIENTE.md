# Informe de impacto · lote 4c0aac4 → b6e3647 (desplegado el 10/09/2026)

82 commits. Tres temas visibles para el usuario: la **descarga ZIP automática**,
la **analítica de descargas** y la **reanudación** de descargas grandes. Todo lo
demás del lote (CRC-32 en la subida, barridos del archiver, presupuesto de
subpeticiones, tests, runbooks) es interno y no va a novedades.

Publicado ya en `/novedades/`: tres entradas con fecha 10/09/2026 (Producto,
Rendimiento, Panel).

---

## 1 · Descarga completa automática

`VITE_GALLERY_ZIP="1"` en `frontend/.env.production`. El botón «Descargar todo»
deja de depender de que el fotógrafo suba un zip: se genera al vuelo en
`GET /media/zip` respetando el tier del enlace. El zip manual sobrevive como
opción, pero **solo** con `zip_mode='manual'` **y** tier `high`.

**Hecho desde este flujo** (cambio desplegado y verificado en el código):

- `public/soporte/es/zip-descarga-completa/index.html` — **reescrito entero**.
  Rodrigo pidió expresamente reescribirlo aquí en vez de dejarlo en informe.
- `public/galerias/index.html` — la sección «Permisos y descarga» decía que el
  ZIP «lo preparas tú».
- `public/bodas/index.html` — la tarjeta «El ZIP de "Descargar todo"» decía lo mismo.

**Literales usados en el artículo** (sacados del código, NO vistos en pantalla —
conviene confirmarlos en el producto real):

| Literal | Origen en el código |
|---|---|
| `Descargar todo` | `DownloadAllButton.tsx` (auto y manual) |
| `24 fotos · 1,2 GB · 2 vídeos no incluidos` | `formatZipLabel()` — ejemplo compuesto por mí a partir del formato, no una captura |
| `Este enlace no permite descargar vídeos.` | `formatZipEmptyReason()` |
| `Todavía no hay nada listo para descargar. Vuelve a intentarlo en unos minutos.` | `formatZipEmptyReason()` |
| `Usar mi zip en lugar del automático` | `GalleryZipPanel.tsx` |
| `Solo en enlaces con descarga en alta…` | `GalleryZipPanel.tsx` (parafraseado en el artículo) |
| `Subir zip` / `Reemplazar zip` / `Preparando…` | `GalleryZipPanel.tsx`, `DownloadAllButton.tsx` |
| `Zip subido el 12/08/2026 · 14 archivos añadidos después. Tu zip no los incluye; el automático sí.` | `GalleryZipPanel.tsx` — fecha y cifra inventadas como ejemplo |
| `¿Quitar tu zip? Tu cliente seguirá viendo "Descargar todo", servido con el zip automático.` | `GalleryZipPanel.tsx` (`confirm`) |
| `No hay saldo suficiente: usas X de Y. Amplía el almacenamiento para subir este zip.` | `GalleryZipPanel.tsx` — ya estaba en el artículo anterior |

**A verificar en pantalla antes de dar el artículo por bueno:**

1. Que el botón por sección (fotos ↔ vídeos) se comporta como digo: el de la
   vista de fotos se lleva fotos y el del visor de vídeo, vídeos.
2. Que el tooltip de cifras es exactamente ese formato y con esos separadores.
3. Que la sección del panel se sigue llamando «Descarga completa» y está en el
   paso **Compartir** (el artículo lo mantiene del texto anterior).
4. Que la casilla del interruptor solo aparece **si hay zip subido**
   (`GalleryZipPanel` no la pinta sin `filename`); el artículo lo da por hecho
   implícitamente al describir el orden subir → marcar.

**Otros artículos de soporte que pueden haber quedado tocados** (este flujo NO
los ha editado):

- `almacenamiento` — si enumera el ZIP entre lo que ocupa espacio, ahora hay que
  matizar: el automático no ocupa, el subido por ti sí.
- `permisos-de-descarga` — la relación entre calidad del enlace y descarga
  completa cambia: en «Web» ya no se sirve el zip manual aunque exista.
- `no-puedo-descargar` — el motivo «el fotógrafo no ha subido el ZIP» deja de
  ser una causa válida; aparecen dos nuevas (enlace sin vídeos, archivos aún
  procesándose).
- `enlace-de-cliente`, `revocar-un-enlace` — revisar si mencionan que el botón
  depende de haber subido un archivo.

## 2 · Analítica de descargas

`gallery_analytics()` devuelve tres cifras con su unidad en vez de un total, y
la tabla «Quién ha entrado» ya no depende de `isEvent`.

**Hecho desde este flujo:** `public/soporte/es/analitica/index.html` — tabla
«Qué mide» (tres filas nuevas), nota sobre no sumar unidades, sección nueva
«El aviso por email», sección «La tabla de quién ha entrado» corregida (ya
aparece en entregas cuando alguien deja su nombre al marcar favoritas) y tabla
por tipo de galería.

**Literales usados:** `Fotos sueltas`, `Lotes de favoritas`, `Galería completa`,
`Reproducciones`, `Avisarme por email de las descargas`, `Un resumen al día con
lo que ha descargado tu cliente, sólo los días que haya descargas.`, `El email es
autodeclarado por el visitante, no verificado, salvo que lo confirmara desde su
correo.` — todos de `AnalyticsPanel.tsx` y `GalleryInfoEditor.tsx`.

**A verificar en pantalla:**

1. Que la casilla del aviso está en el paso **Datos** (el código la sitúa en
   `GalleryInfoEditor`, que es ese paso — confirmar el nombre del paso en el raíl).
2. El hint exacto de «Galería completa» (`describeZip`) con datos reales: el
   artículo lo describe en prosa, sin citar el literal.
3. Que la línea D5 («Las descargas anteriores al … no se guardaban») ya no
   aparece — se retiró en `80f351d`, y el artículo no la menciona.

**Otros artículos posiblemente tocados:** `favoritas-del-cliente` (la
identificación al marcar favoritas ahora alimenta la tabla de la analítica),
`planes-y-precios` (si enumera qué incluye la analítica de Autor/Estudio).

## 3 · Reanudación

El navegador retoma una descarga cortada (ETag + If-Range) y el panel la sigue
contando como una sola descarga (id de descarga con TTL de 30 min).

**Hecho:** una entrada de novedades (Rendimiento) y una sección nueva en el
artículo del ZIP («Si la descarga se corta»).

**A verificar:** que el navegador ofrece efectivamente «Reanudar» en la lista de
descargas tras cortar la conexión a mitad — es la única afirmación del artículo
que depende del comportamiento del navegador y no solo del servidor.
