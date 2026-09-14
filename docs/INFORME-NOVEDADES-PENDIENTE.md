# Informe de impacto · lote b6e3647 → 2a59b6c (desplegado el 14/09/2026)

33 commits, cinco temas visibles. Publicadas **seis entradas** en `/novedades/`
(14, 13, 13, 12, 11 y 10 de septiembre).

Interno y fuera de novedades: los prompts y runbooks, la inversión de
`run_worker_first`, el marcador HSTS, los tests del Worker y el relleno hacia
atrás del códec en las filas existentes.

---

## 1 · ZIP por momento (14/09)

`GET /media/zip?scope=moment`. Botón junto al título de cada sección del visor.
Condiciones reales, leídas del código: tier ≠ `none`, momento no vacío, **más de
un grupo**, cuadrícula con momentos; nunca en «Otros» ni con el filtro de
favoritas. Convive con el zip manual global.

**Editado aquí:** `zip-descarga-completa` (sección «Descargar un momento
suelto») y `momentos` (sección «Qué ve tu cliente»).

**A verificar en pantalla:**
1. Cómo se llama y dónde está exactamente el control: lo describo como «su
   propio botón de descarga junto al título». El commit dice que se unificó a
   **un solo icono de descarga en todo el visor** — si tiene una etiqueta de
   texto visible o un tooltip, conviene citarla tal cual.
2. Que con el filtro de favoritas el botón efectivamente desaparece (lo digo).
3. El nombre del archivo: según `0934f9f` queda `Galería - Momento.zip`, sin el
   sufijo « - fotos». No lo cito en el artículo; si quieres citarlo, confírmalo.

## 2 · Indexación (12-13/09)

`GALLERY_ROBOTS_MODE` se queda en **noindex permanente** para `/g/` y `/f/`
(Disallow impediría rastrear pero no listar, y este producto consiste en
repartir esos enlaces). El panel entero fuera del índice por inversión:
`X-Robots-Tag` noindex salvo lista cerrada. Portfolios inyectados en el edge con
HTMLRewriter: título, descripción, canonical, H1, bio, `<img>` con alt, OG y
JSON-LD Person/ProfilePage. Umbral: sin bio y sin galería publicada, noindex.
Etiquetas `/galerias/<tag>`: noindex en v1. Sitemap por subdominio.
Despublicado → 404 con página de marca.

**Editado aquí:** `perfil-publico` (sección «Tu web y los buscadores»).

**A verificar:**
1. Que el umbral es exactamente «sin bio **y** sin ninguna galería publicada»
   (lo escribo así).
2. Si el panel avisa de alguna forma de que un perfil está fuera del índice. Si
   no avisa, el artículo es el único sitio donde el fotógrafo puede enterarse.

**Otros artículos que puede tocar (no editados):** `portfolio` (si promete
visibilidad en buscadores sin matizar el umbral) y `enlace-de-cliente` (ahora se
puede afirmar que un enlace repartido no acaba en Google).

## 3 · Portero de códec, HEVC y póster provisional (11-12/09)

Tres estados en `videoGate.ts`: **entra** (códec web), **entra avisando**
(`hardware-only` = HEVC), **no entra** (`not-web` con etiqueta, o desconocido
del que el navegador no saca fotogramas). Un fourCC desconocido que sí da
fotogramas entra y avisa a Sentry.

**Editado aquí:** `formatos-admitidos` — tabla de vídeo rehecha, secciones «Qué
dice el aviso cuando un vídeo no entra», «El HEVC entra, pero avisando» y «Un
vídeo sin portada se sube igual». La entradilla ya distingue foto (decide el
navegador) de vídeo (comprobación propia).

**Literales usados, sacados del código y NO vistos en pantalla:**

| Literal | Origen |
|---|---|
| `«archivo» está en ProRes 422 — Es un códec de edición: los navegadores no lo reproducen…` | `describeRejection()`, rama EDITING. El nombre del archivo y el códec del ejemplo son míos |
| `«archivo» no tiene imagen — Solo tiene sonido: en la galería tus clientes verían un rectángulo negro.` | `describeRejection()`, rama `codec === "none"` |
| `«archivo» no se puede reproducir en el navegador` | `describeRejection()`, rama desconocido |
| `2 vídeos en HEVC (el formato que graba el iPhone por defecto)…` | `hardwareOnlyNotice()`, texto completo y literal |

**A verificar:**
1. Dónde se pinta cada aviso (fila de la cola, banda al terminar la tanda,
   toast) — el artículo dice «al terminar la tanda» para el de HEVC, que es lo
   que sugiere el código (`UNA vez por tanda con el número`).
2. Que el aviso incluye el peso («Pesa 2,4 GB») como dice `pesoLegible`.
3. Que la portada provisional se puede cambiar desde el panel: lo afirmo, y es
   la única frase de esa sección que no está respaldada por el diff que leí.
4. **Contradicción pendiente en otro artículo:** `archivos-que-no-suben` y
   `subir-fotos-y-videos` pueden seguir diciendo que el vídeo falla con «No se
   pudo leer el vídeo.» Ese mensaje ya no es el único camino. No los he editado
   para no tocar más alcance del necesario — decide si van en este lote o en el
   siguiente.

## 4 · Dominios propios automáticos (10-11/09)

Alta automática en Cloudflare tras verificar la propiedad; correo al fotógrafo
cuando el dominio sirve; el panel muestra el estado real de cada registro en vez
de pedirle que mire. `CNAME_DESTINO = saas.positiva.studio`, TXT
`_positiva-verify.<hostname>`.

**Editado aquí:** `dominio-propio` — **reescrito**. El artículo anterior decía
que el DNS y el certificado se configuran «a mano, en 24-48 horas», que ya es
falso. También cambia su `<meta name="description">`.

**Literales usados (de `registrosDe()` en `Branding.tsx`, no vistos en
pantalla):** los seis estados del CNAME de la tabla «Qué dice el panel en cada
momento», copiados uno a uno.

**A verificar:**
1. Que el bloque sigue estando en **Branding** y se llama «Dominio propio».
2. Que el panel muestra el TXT y el CNAME con nombre y valor copiables, como
   describo en el paso 3.
3. Que el aviso de Cloudflare «DNS only» aparece tal cual (yo lo resumo).

## 5 · Rescate de avisos (10/09)

Un aviso que fallaba podía dejar sin cerrar la fila y llevarse por delante el
resumen de descargas del día; los 5xx transitorios de Supabase ya se reintentan.

**Editado aquí:** solo la entrada de novedades (etiqueta Arreglo).

**A verificar:** nada en soporte. `analitica` ya describe el resumen diario y no
prometía fiabilidad, así que no queda desactualizado.

---

## Cierre

- `docs/novedades-estado.txt` → `2a59b6c`.
- **Sitemap:** no lo he tocado. Ahora se genera con `npm run sitemap`, que saca
  los `lastmod` de la fecha real del último commit de cada página — hay que
  ejecutarlo **después** de commitear este lote, no antes.
