# Base de conocimiento · /soporte

La documentación pública de Positiva. Vive en este repo, se despliega con la
landing y **no cambia nada del pipeline**: Cloudflare sigue subiendo `./public`
sin ejecutar ningún build.

## Cómo funciona

```
partials/                     ← CROMO COMÚN (compartido con el resto del sitio)
  chrome-nav.html             ·  cabecera: CSS + marcado + JS
  chrome-footer.html          ·  pie: CSS + marcado

soporte/                      ← FUENTE (no se despliega)
  _src/es/*.md                ·  un archivo = un artículo = una URL
  plantilla.html              ·  el marco propio del soporte
  soporte.css                 ·  la hoja de estilos del soporte
  build.mjs                   ·  el generador
  PENDIENTES.md               ·  generado: lo que falta por escribir

public/soporte/               ← SALIDA (esto sí se despliega, y se commitea)
  es/index.html               ·  /soporte/es/
  es/<slug>/index.html        ·  /soporte/es/<slug>/
  es/buscador.json            ·  índice de texto completo del buscador
  soporte.css
  index.html                  ·  redirección de /soporte/ a /soporte/es/
```

## La cabecera y el pie no viven aquí

`build.mjs` **lee** `partials/chrome-nav.html` y `partials/chrome-footer.html`,
los mismos que `npm run stamp` propaga al resto de páginas. No hay copia: si
cambias el menú en el parcial, cambia en las 51 páginas del soporte igual que en
las 10 de la landing.

Por eso, después de editar un parcial hay que ejecutar **los dos** comandos:

```bash
npm run stamp            # las 10 páginas de la landing
node soporte/build.mjs   # las 51 del soporte
```

Conviene añadirlo a `package.json` para no olvidarse de uno:

```json
"chrome": "npm run stamp && node soporte/build.mjs"
```

`soporte.css` ya no define nada del cromo. Lo único que conserva al respecto es
una línea de convivencia: el parcial estiliza la cabecera con el selector de
elemento `nav`, y el soporte tiene migas de pan y sumarios que también son
`<nav>`. Si desaparece `main nav{position:static}`, la miga de pan de cada
artículo se va a la esquina superior izquierda.

Escribes en `_src/`, generas, y commiteas las dos cosas. El HTML generado va al
repositorio a propósito: es lo que hace que no haga falta un paso de build en
el despliegue.

## Comandos

```bash
node soporte/build.mjs           # genera public/soporte/ y PENDIENTES.md
node soporte/build.mjs --check   # valida sin escribir; útil antes de commitear
```

El generador **falla y no escribe nada** si encuentra un error: falta un campo
del frontmatter, la categoría no existe, o un enlace interno apunta a un
artículo que no existe o que no se publica. Es deliberado: un 404 dentro de la
documentación lo descubre un cliente, no tú.

## Escribir un artículo

Crea `soporte/_src/es/<slug>.md`. **El nombre del archivo es la URL.**

```markdown
---
titulo: Cómo crear tu primera galería y compartirla
descripcion: Una frase completa, con verbo. Sale en la ficha del índice y en Google. Entre 90 y 160 caracteres.
categoria: primeros-pasos
audiencia: fotografo
orden: 20
actualizado: 24 de agosto de 2026
relacionados: [entrega-o-revision, enlace-de-cliente]
---

Texto del artículo. Sin `#` de nivel 1: el título sale del frontmatter.
```

| Campo | Qué hace |
|---|---|
| `categoria` | Una de las nueve de `build.mjs`. Otra cosa hace fallar el build. |
| `audiencia` | `fotografo`, `revisor` o `ambos`. Pinta la etiqueta de arriba. |
| `orden` | Ordena dentro de su categoría. Deja huecos (10, 20, 30…). |
| `relacionados` | Slugs. Se completan solos con los de la misma categoría. |
| `estado` | `publicado` (por defecto), `borrador` o `pendiente`. |
| `motivo` | Solo con `pendiente`: por qué no está escrito. Sale en PENDIENTES.md. |

### Los tres estados

- **publicado** — se publica y punto.
- **borrador** — se publica **con una banda de «En obra»** encima. Para lo que
  documenta una parte del producto que está cambiando ahora mismo.
- **pendiente** — **no se publica**. El archivo existe con su ficha y su motivo,
  y aparece en `PENDIENTES.md`. Para lo que hace falta escribir a mano.

### Sintaxis

Encabezados `##` y `###`, párrafos, listas, tablas, `código`, `**negrita**`,
`*cursiva*`, `> citas`, `---`, enlaces `[texto](/soporte/es/slug/)`, y bloques
de aviso:

```
:::aviso Título opcional
Lo que puede salir mal. El bloque más útil de todos.
:::

:::truco     Atajos y consejos
:::plan      En qué planes está disponible algo
:::nota      Matices
```

Los comentarios HTML (`<!-- DUDA: ... -->`) **no se publican**: se recogen en la
sección «Dudas anotadas» de `PENDIENTES.md`. Sirven para dejar una pregunta
abierta dentro del artículo sin que la lea un cliente.

### Capturas de pantalla

Van en `soporte/_img/` y el generador las copia a `public/soporte/img/`. En el
Markdown, cada una en su propia línea:

```
![Texto alternativo, describiendo lo que se ve](nombre-del-archivo.webp "Pie de foto, con **negrita** si hace falta.")
```

El generador **falla si el archivo no existe** en `_img/`, y avisa si falta el
texto alternativo. El pie no es obligatorio pero conviene: una captura sin pie
obliga al lector a deducir qué está mirando.

No se redimensiona nada automáticamente. Prepara los archivos antes: **WebP,
1400 px de ancho como máximo, calidad 82**. La columna de lectura son 760 px,
así que con eso sobra para pantallas de densidad doble.

## Añadir el inglés

`build.mjs` ya está montado para varios idiomas. Añade `en` a la constante
`IDIOMAS`, crea `_src/en/` y genera: sale en `/soporte/en/`. Las categorías y
sus títulos habría que traducirlos en `CATEGORIAS`.

## Reglas que no conviene romper

1. **Los literales de la interfaz se copian, no se recuerdan.** Si un artículo
   entrecomilla el texto de un botón, tiene que coincidir palabra por palabra
   con el código. Un botón mal citado hace que el lector busque algo que no
   existe.
2. **Lo que está `[PARCIAL]` en `config/plans.ts` no se promete entero.** El
   dominio propio es el caso vivo: guardarlo no lo activa.
3. **Lo que está en obra va como `borrador`, no como artículo normal.** Un
   artículo que miente cuesta más soporte que uno que no existe.
4. **Antes de commitear, `node soporte/build.mjs --check`.**
