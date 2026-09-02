/**
 * POSITIVA · Generador de la base de conocimiento (/soporte)
 *
 * Por qué existe: la landing se despliega SIN build (wrangler sube ./public tal
 * cual). Escribir 50 artículos en HTML a mano significa duplicar cabecera,
 * estilos, navegación y pie en cada archivo — y que cambiar el menú sean 50
 * ediciones. Este script mantiene una sola plantilla y una sola hoja de estilos.
 *
 * El HTML generado SE COMMITEA. El despliegue no cambia: Cloudflare sigue
 * subiendo ./public sin ejecutar nada.
 *
 * Uso:
 *   node soporte/build.mjs            # genera
 *   node soporte/build.mjs --check    # no escribe; falla si algo está mal
 *
 * Entrada:  soporte/_src/<idioma>/*.md   (+ soporte/plantilla.html, soporte/soporte.css)
 * Salida:   public/soporte/<idioma>/            → índice
 *           public/soporte/<idioma>/<slug>/     → artículo
 *           public/soporte/soporte.css          → hoja compartida
 *           soporte/PENDIENTES.md               → lo que falta por escribir
 *
 * Sin dependencias a propósito: `npm install` no hace falta para desplegar la
 * landing y no queremos que empiece a hacer falta por esto.
 */

import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync, copyFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const AQUI = dirname(fileURLToPath(import.meta.url));
const RAIZ = resolve(AQUI, '..');
const SRC = join(AQUI, '_src');
const SALIDA = join(RAIZ, 'public', 'soporte');
const SOLO_COMPROBAR = process.argv.includes('--check');

const SITIO = 'https://positiva.studio';
const APP = 'https://app.positiva.studio';
const CONTACTO = 'hola@positiva.studio';

/* ── Categorías ───────────────────────────────────────────────────────────
 * El orden de esta lista es el orden del índice. Una categoría que no esté
 * aquí hace fallar el build a propósito: evita que un artículo aterrice en
 * una sección inventada y desaparezca de la navegación.
 */
const CATEGORIAS = [
  { id: 'primeros-pasos', titulo: 'Primeros pasos',        resumen: 'Qué es Positiva y cómo preparar y entregar tu primer trabajo.' },
  { id: 'galerias',       titulo: 'Galerías',              resumen: 'Crear, organizar y gestionar tus galerías.' },
  { id: 'subida',         titulo: 'Subir fotos y vídeos',  resumen: 'Formatos admitidos, sustitución de archivos, versiones y resolución de incidencias.' },
  { id: 'compartir',      titulo: 'Compartir y descargas', resumen: 'Enlaces, contraseñas y qué puede descargar tu cliente.' },
  { id: 'revision',       titulo: 'Revisión y comentarios',resumen: 'Cómo recibir, responder y gestionar los comentarios de tu cliente.' },
  { id: 'revisor',        titulo: 'Si vas a revisar',      resumen: 'Para quien recibe una galería de revisión. No se necesita cuenta en Positiva.' },
  { id: 'diseno',         titulo: 'Diseño y marca',        resumen: 'Diseños de galería, colores, tipografía, logotipo y dominio propio.' },
  { id: 'cuenta',         titulo: 'Cuenta y planes',       resumen: 'Planes, almacenamiento, facturación y analítica.' },
  { id: 'problemas',      titulo: 'Resolución de problemas',     resumen: 'Incidencias frecuentes, su causa y cómo resolverlas.' },
];

const IDIOMAS = { es: { nombre: 'Español', locale: 'es_ES', dir: 'es' } };

/* ── Utilidades ──────────────────────────────────────────────────────────── */

const escapar = (s) => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

const errores = [];
const avisos = [];

/* ── Frontmatter ─────────────────────────────────────────────────────────── */

function leerFrontmatter(texto, archivo) {
  if (!texto.startsWith('---\n')) {
    errores.push(`${archivo}: falta el bloque de frontmatter (--- al principio).`);
    return [{}, texto];
  }
  const fin = texto.indexOf('\n---', 4);
  if (fin === -1) {
    errores.push(`${archivo}: el frontmatter no se cierra con ---.`);
    return [{}, texto];
  }
  const meta = {};
  for (const linea of texto.slice(4, fin).split('\n')) {
    if (!linea.trim() || linea.trimStart().startsWith('#')) continue;
    const i = linea.indexOf(':');
    if (i === -1) continue;
    const clave = linea.slice(0, i).trim();
    let valor = linea.slice(i + 1).trim();
    if (/^\[.*\]$/.test(valor)) {
      valor = valor.slice(1, -1).split(',').map((v) => v.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
    } else {
      valor = valor.replace(/^["']|["']$/g, '');
    }
    meta[clave] = valor;
  }
  return [meta, texto.slice(fin + 4).replace(/^\n+/, '')];
}

/* ── Markdown → HTML ──────────────────────────────────────────────────────
 * Subconjunto deliberadamente pequeño: encabezados, párrafos, listas, tablas,
 * citas, bloques de código, reglas, y los avisos :::. Si un artículo necesita
 * algo que esto no cubre, casi siempre es señal de que el artículo es
 * demasiado complicado, no de que falte sintaxis.
 */

function enLinea(s) {
  // El código en línea se aparta antes de tocar nada más, para que un
  // `**` dentro de `código` no se convierta en negrita.
  const trozos = [];
  let t = s.replace(/`([^`]+)`/g, (_, c) => {
    trozos.push(`<code>${escapar(c)}</code>`);
    return `%%c${trozos.length - 1}%%`;
  });
  t = escapar(t);
  t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, txt, url) => {
    const externo = /^https?:\/\//.test(url) && !url.startsWith(SITIO);
    const attrs = externo ? ' target="_blank" rel="noopener noreferrer"' : '';
    return `<a href="${url}"${attrs}>${txt}</a>`;
  });
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/(^|[\s(¡¿"])\*([^*\n]+)\*/g, '$1<em>$2</em>');
  t = t.replace(/(^|[\s(])_([^_\n]+)_/g, '$1<em>$2</em>');
  t = t.replace(/ -- /g, ' — ');
  return t.replace(/%%c(\d+)%%/g, (_, i) => trozos[Number(i)]);
}

const AVISOS = {
  aviso: { clase: 'nota nota-aviso', rotulo: 'Importante' },
  ojo: { clase: 'nota nota-aviso', rotulo: 'Importante' },
  truco: { clase: 'nota nota-truco', rotulo: 'Atajo' },
  nota: { clase: 'nota nota-info', rotulo: 'Nota' },
  plan: { clase: 'nota nota-plan', rotulo: 'Disponibilidad' },
  obra: { clase: 'nota nota-obra', rotulo: 'En desarrollo' },
};

/* Dimensiones de un WebP, leídas de su cabecera RIFF.
 *
 * Sirven para dos cosas: dar `width`/`height` al `<img>` —sin ellos la página
 * salta cuando cargan las capturas— y decidir el ancho. Una captura de un
 * diálogo del sistema es más alta que ancha; a ancho completo de la columna
 * quedaría enorme y desplazaría el texto que la explica.
 */
function medirWebp(ruta) {
  const b = readFileSync(ruta);
  if (b.length < 30 || b.toString('ascii', 0, 4) !== 'RIFF' || b.toString('ascii', 8, 12) !== 'WEBP') return null;
  const formato = b.toString('ascii', 12, 16);
  if (formato === 'VP8X') return { ancho: (b.readUIntLE(24, 3) & 0xffffff) + 1, alto: (b.readUIntLE(27, 3) & 0xffffff) + 1 };
  if (formato === 'VP8 ') return { ancho: b.readUInt16LE(26) & 0x3fff, alto: b.readUInt16LE(28) & 0x3fff };
  if (formato === 'VP8L') {
    const n = b.readUInt32LE(21);
    return { ancho: (n & 0x3fff) + 1, alto: ((n >> 14) & 0x3fff) + 1 };
  }
  return null;
}

function renderizar(md, ctx) {
  const lineas = md.split('\n');
  const salida = [];
  const indice = [];
  let i = 0;

  const parrafo = (buf) => {
    if (buf.length) salida.push(`<p>${enLinea(buf.join(' '))}</p>`);
    buf.length = 0;
  };
  const buf = [];

  while (i < lineas.length) {
    const l = lineas[i];

    // Bloque de aviso :::tipo … :::
    const abre = l.match(/^:::(\w+)\s*(.*)$/);
    if (abre && AVISOS[abre[1]]) {
      parrafo(buf);
      const tipo = AVISOS[abre[1]];
      const cuerpo = [];
      i++;
      while (i < lineas.length && lineas[i].trim() !== ':::') cuerpo.push(lineas[i++]);
      i++;
      const rotulo = abre[2].trim() || tipo.rotulo;
      salida.push(`<aside class="${tipo.clase}"><b>${escapar(rotulo)}</b>${renderizar(cuerpo.join('\n'), ctx).html}</aside>`);
      continue;
    }

    // Captura de pantalla en su propia línea: ![alt](archivo.webp "pie")
    // El pie es obligatorio. Una captura sin pie obliga al lector a deducir
    // qué está mirando, y en un artículo de pasos eso es justo lo que no
    // puede pasar.
    const img = l.match(/^!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)\s*$/);
    if (img) {
      parrafo(buf);
      const [, alt, archivo, pie] = img;
      const local = !/^https?:|^\//.test(archivo);
      const ruta = join(AQUI, '_img', archivo);
      if (local && !existsSync(ruta)) {
        errores.push(`${ctx.idioma}/${ctx.slug}.md: la captura "${archivo}" no existe en soporte/_img/.`);
      }
      if (!alt) avisos.push(`${ctx.idioma}/${ctx.slug}.md: la captura "${archivo}" no lleva texto alternativo.`);

      const medida = local && existsSync(ruta) && archivo.endsWith('.webp') ? medirWebp(ruta) : null;
      // Más alta que ancha, o poco más ancha que alta: es un diálogo, no una
      // ventana. Se pinta a un ancho contenido.
      const estrecha = medida && medida.ancho / medida.alto < 1.35;
      const dim = medida ? ` width="${medida.ancho}" height="${medida.alto}"` : '';
      const src = local ? `/soporte/img/${archivo}` : archivo;

      salida.push(
        `<figure class="captura${estrecha ? ' captura-estrecha' : ''}">` +
        `<img src="${src}" alt="${escapar(alt)}"${dim} loading="lazy" decoding="async">` +
        (pie ? `<figcaption>${enLinea(pie)}</figcaption>` : '') +
        `</figure>`
      );
      i++;
      continue;
    }

    // Bloque de código
    if (l.startsWith('```')) {
      parrafo(buf);
      const cuerpo = [];
      i++;
      while (i < lineas.length && !lineas[i].startsWith('```')) cuerpo.push(lineas[i++]);
      i++;
      salida.push(`<pre><code>${escapar(cuerpo.join('\n'))}</code></pre>`);
      continue;
    }

    // Encabezados
    const h = l.match(/^(#{2,4})\s+(.*)$/);
    if (h) {
      parrafo(buf);
      const nivel = h[1].length;
      const texto = h[2].trim();
      const id = texto.toLowerCase()
        .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
      if (nivel === 2) indice.push({ id, texto });
      salida.push(`<h${nivel} id="${id}">${enLinea(texto)}</h${nivel}>`);
      i++;
      continue;
    }

    // Regla
    if (/^---+\s*$/.test(l)) { parrafo(buf); salida.push('<hr>'); i++; continue; }

    // Tabla
    if (l.includes('|') && i + 1 < lineas.length && /^\s*\|?[\s:|-]+\|[\s:|-]*$/.test(lineas[i + 1])) {
      parrafo(buf);
      const celdas = (fila) => fila.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
      const cab = celdas(l);
      i += 2;
      const filas = [];
      while (i < lineas.length && lineas[i].includes('|') && lineas[i].trim()) filas.push(celdas(lineas[i++]));
      salida.push(
        '<div class="tabla-scroll"><table><thead><tr>' +
        cab.map((c) => `<th>${enLinea(c)}</th>`).join('') +
        '</tr></thead><tbody>' +
        filas.map((f) => `<tr>${f.map((c) => `<td>${enLinea(c)}</td>`).join('')}</tr>`).join('') +
        '</tbody></table></div>'
      );
      continue;
    }

    // Cita
    if (l.startsWith('> ')) {
      parrafo(buf);
      const cuerpo = [];
      while (i < lineas.length && lineas[i].startsWith('>')) cuerpo.push(lineas[i++].replace(/^>\s?/, ''));
      salida.push(`<blockquote>${renderizar(cuerpo.join('\n'), ctx).html}</blockquote>`);
      continue;
    }

    // Listas (un nivel de anidamiento)
    const punto = l.match(/^(\s*)([-*]|\d+\.)\s+(.*)$/);
    if (punto) {
      parrafo(buf);
      const ordenada = /\d/.test(punto[2]);
      const etiqueta = ordenada ? 'ol' : 'ul';
      const items = [];
      let actual = null;
      while (i < lineas.length) {
        const m = lineas[i].match(/^(\s*)([-*]|\d+\.)\s+(.*)$/);
        if (m) {
          if (m[1].length >= 2 && actual) {
            actual.hijos.push(m[3]);
          } else {
            actual = { texto: m[3], hijos: [], continua: [] };
            items.push(actual);
          }
          i++;
        } else if (lineas[i].trim() && /^\s{2,}/.test(lineas[i]) && actual) {
          actual.continua.push(lineas[i].trim());
          i++;
        } else break;
      }
      salida.push(`<${etiqueta}>` + items.map((it) => {
        let html = enLinea(it.texto);
        if (it.continua.length) html += ` ${enLinea(it.continua.join(' '))}`;
        if (it.hijos.length) html += `<ul>${it.hijos.map((h2) => `<li>${enLinea(h2)}</li>`).join('')}</ul>`;
        return `<li>${html}</li>`;
      }).join('') + `</${etiqueta}>`);
      continue;
    }

    if (!l.trim()) { parrafo(buf); i++; continue; }
    buf.push(l.trim());
    i++;
  }
  parrafo(buf);
  return { html: salida.join('\n'), indice };
}

/* ── Carga de artículos ──────────────────────────────────────────────────── */

function cargar(idioma) {
  const dir = join(SRC, idioma);
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter((f) => f.endsWith('.md'))
    .map((archivo) => {
      const slug = archivo.replace(/\.md$/, '');
      const bruto = readFileSync(join(dir, archivo), 'utf8');
      const [meta, cuerpoBruto] = leerFrontmatter(bruto, `${idioma}/${archivo}`);
      const estado = meta.estado || 'publicado';

      // Los comentarios HTML son notas de quien escribe, no contenido. Se
      // sacan del artículo y se recogen en PENDIENTES.md, para que una duda
      // anotada no acabe impresa en la página del cliente.
      const dudas = [...cuerpoBruto.matchAll(/<!--([\s\S]*?)-->/g)].map((m) => m[1].trim());
      const cuerpo = cuerpoBruto.replace(/<!--[\s\S]*?-->/g, '').replace(/\n{3,}/g, '\n\n').trim();

      if (!meta.titulo) errores.push(`${idioma}/${archivo}: falta "titulo".`);
      if (!meta.descripcion && estado !== 'pendiente') errores.push(`${idioma}/${archivo}: falta "descripcion".`);
      if (!CATEGORIAS.some((c) => c.id === meta.categoria)) {
        errores.push(`${idioma}/${archivo}: categoría "${meta.categoria}" desconocida. Válidas: ${CATEGORIAS.map((c) => c.id).join(', ')}`);
      }
      if (!['publicado', 'borrador', 'pendiente'].includes(estado)) {
        errores.push(`${idioma}/${archivo}: estado "${estado}" no válido (publicado | borrador | pendiente).`);
      }
      if (meta.descripcion && meta.descripcion.length > 165) {
        avisos.push(`${idioma}/${archivo}: la descripción pasa de 165 caracteres; Google la va a cortar.`);
      }

      return {
        slug, idioma, estado, cuerpo, dudas,
        titulo: meta.titulo || slug,
        descripcion: meta.descripcion || '',
        categoria: meta.categoria,
        audiencia: meta.audiencia || 'fotografo',
        orden: Number(meta.orden || 100),
        actualizado: meta.actualizado || '',
        relacionados: Array.isArray(meta.relacionados) ? meta.relacionados : (meta.relacionados ? [meta.relacionados] : []),
        motivo: meta.motivo || '',
      };
    })
    .sort((a, b) => a.orden - b.orden || a.titulo.localeCompare(b.titulo, 'es'));
}

/* ── Plantilla y cromo común ─────────────────────────────────────────────
 * La cabecera y el pie NO se copian aquí: se leen de los mismos parciales
 * que `npm run stamp` propaga al resto del sitio. Un solo sitio donde editar
 * el menú, dos consumidores (stamp para las páginas de la landing, este
 * generador para las del soporte).
 *
 * Los parciales son autocontenidos: traen su CSS, su marcado y su JS.
 */

const plantilla = readFileSync(join(AQUI, 'plantilla.html'), 'utf8');

function leerParcial(nombre) {
  const ruta = join(RAIZ, 'partials', `chrome-${nombre}.html`);
  if (!existsSync(ruta)) {
    console.error(`\n✗ Falta partials/chrome-${nombre}.html.`);
    console.error('  El soporte lee la cabecera y el pie de los mismos parciales que `npm run stamp`.');
    console.error('  Si los has movido, actualiza la ruta en soporte/build.mjs.\n');
    process.exit(1);
  }
  return readFileSync(ruta, 'utf8').trim();
}

const NAV = leerParcial('nav');
const PIE = leerParcial('footer');

function pintar(datos) {
  const todo = { ...datos, NAV, PIE };
  return plantilla.replace(/\{\{(\w+)\}\}/g, (_, clave) => (clave in todo ? todo[clave] : ''));
}

const AUDIENCIAS = {
  fotografo: { etiqueta: 'Para el fotógrafo', clase: 'aud-foto' },
  revisor: { etiqueta: 'Para quien revisa', clase: 'aud-revisor' },
  ambos: { etiqueta: 'Para los dos', clase: 'aud-ambos' },
};

/** Número de la categoría (01, 02…), como los de las secciones de la portada. */
const numeroCat = (id) => String(CATEGORIAS.findIndex((c) => c.id === id) + 1).padStart(2, '0');

/** El buscador vive en el marco común de la plantilla; aquí solo el marcado. */
function buscador(placeholder, compacto = false) {
  return `<form class="busca${compacto ? ' busca-mini' : ''}" role="search" data-busca>
  <label class="sr" for="q">Buscar en el soporte</label>
  <div class="busca-campo">
    <svg class="busca-lupa" viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12.8 12.8 17 17" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    <input id="q" type="search" role="combobox" aria-expanded="false" aria-controls="busca-panel" aria-autocomplete="list"
           placeholder="${escapar(placeholder)}" autocomplete="off" spellcheck="false">
    <kbd class="busca-tecla" aria-hidden="true">/</kbd>
  </div>
  <div class="busca-panel" id="busca-panel" hidden></div>
</form>`;
}

/** Markdown a texto plano, para el índice del buscador. */
function aTextoPlano(md) {
  return md
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/^:::\w*.*$/gm, ' ')
    .replace(/^:::$/gm, ' ')
    .replace(/^\s*\|[-:\s|]+\|\s*$/gm, ' ')
    .replace(/^#{1,6}\s+/gm, '')
    .replace(/\[([^\]]+)\]\([^)\s]+\)/g, '$1')
    .replace(/[*_`>]/g, '')
    .replace(/^\s*[-*]\s+/gm, '')
    .replace(/\|/g, ' · ')
    .replace(/\s+/g, ' ')
    // Las tablas dejan puntos medios pegados donde había celdas vacías o
    // bordes de fila. Un fragmento del buscador que empieza por «· ·» parece
    // un error de la página.
    .replace(/(?:·\s*){2,}/g, '· ')
    .replace(/^[·\s]+/, '')
    .trim();
}

function paginaArticulo(art, todos) {
  const cat = CATEGORIAS.find((c) => c.id === art.categoria);
  const { html, indice } = renderizar(art.cuerpo, art);
  const aud = AUDIENCIAS[art.audiencia] || AUDIENCIAS.fotografo;
  const base = `/soporte/${art.idioma}`;

  const hermanos = todos
    .filter((a) => a.categoria === art.categoria && a.slug !== art.slug && a.estado !== 'pendiente')
    .slice(0, 5);

  const explicitos = art.relacionados
    .map((s) => todos.find((a) => a.slug === s && a.estado !== 'pendiente'))
    .filter(Boolean);

  const relacionados = [...explicitos, ...hermanos]
    .filter((a, i, arr) => arr.findIndex((x) => x.slug === a.slug) === i)
    .slice(0, 4);

  const sumario = indice.length >= 3
    ? `<nav class="sumario" aria-label="En esta página"><b>En esta página</b><ol>${
        indice.map((h) => `<li><a href="#${h.id}">${escapar(h.texto)}</a></li>`).join('')
      }</ol></nav>`
    : '';

  const banda = art.estado === 'borrador'
    ? `<aside class="nota nota-obra"><b>Sección en desarrollo</b><p>Esta parte de Positiva está en desarrollo activo. La información de esta página es correcta a fecha de hoy, pero puede quedar incompleta en las próximas semanas. Si encuentras alguna discrepancia, escribe a <a href="mailto:${CONTACTO}">${CONTACTO}</a>.</p></aside>`
    : '';

  // El raíl no repite lo que ya hay abajo: en móvil se queda solo con el
  // buscador y la vuelta al índice, porque «Seguir leyendo» ya cubre a los
  // hermanos al final del artículo.
  const enSeccion = todos.filter((a) => a.categoria === art.categoria && a.estado !== 'pendiente');

  const cuerpo = `
<div class="wrap doc">
  <aside class="rail">
    <a class="rail-volver" href="${base}/"><span aria-hidden="true">←</span> Todo el soporte</a>
    ${buscador('Buscar…', true)}
    <div class="rail-seccion">
      <p class="eyebrow"><span class="idx">${numeroCat(cat.id)}</span> ${escapar(cat.titulo)}</p>
      <ul class="rail-lista">${enSeccion.map((a) => `<li>${a.slug === art.slug
        ? `<span aria-current="page">${escapar(a.titulo)}</span>`
        : `<a href="${base}/${a.slug}/">${escapar(a.titulo)}</a>`}</li>`).join('')}</ul>
    </div>
  </aside>

  <article class="art">
    <nav class="miga" aria-label="Migas de pan">
      <a href="${base}/">Soporte</a> <span aria-hidden="true">·</span>
      <a href="${base}/#${cat.id}">${escapar(cat.titulo)}</a>
    </nav>
    ${/* La etiqueta solo se pinta cuando dice algo. Cuatro de cada cinco
          artículos son para el fotógrafo: rotularlos todos es ruido, y hace
          que la etiqueta deje de leerse justo donde importa. */ ''
    }${art.audiencia !== 'fotografo' ? `<span class="aud ${aud.clase}">${aud.etiqueta}</span>` : ''}
    <h1>${escapar(art.titulo)}</h1>
    <p class="lede">${escapar(art.descripcion)}</p>
    ${banda}
    ${sumario}
    <div class="prosa">
${html}
    </div>
    ${art.actualizado ? `<p class="sello">Revisado contra la versión en producción el ${escapar(art.actualizado)}.</p>` : ''}
    <section class="ayuda">
      <h2 id="sigue-sin-resolverse">¿Sigue sin resolverse?</h2>
      <p>Si este artículo no responde a tu caso, escríbenos. Respondemos todas las consultas en un plazo de 24 a 48 horas.</p>
      <p><a class="btn btn-primario" href="mailto:${CONTACTO}?subject=${encodeURIComponent('Soporte · ' + art.titulo)}">Escribir a ${CONTACTO}</a></p>
    </section>
    ${relacionados.length ? `<section class="relacionados">
      <h2 id="seguir-leyendo">Seguir leyendo</h2>
      <ul>${relacionados.map((a) => `<li><a href="${base}/${a.slug}/"><b>${escapar(a.titulo)}</b><span>${escapar(a.descripcion)}</span></a></li>`).join('')}</ul>
    </section>` : ''}
  </article>
</div>`;

  return pintar({
    LANG: art.idioma,
    TITULO: `${escapar(art.titulo)} · Soporte de Positiva`,
    DESCRIPCION: escapar(art.descripcion),
    CANONICA: `${SITIO}${base}/${art.slug}/`,
    LOCALE: IDIOMAS[art.idioma].locale,
    CLASE: 'pagina-articulo',
    CONTENIDO: cuerpo,
    JSONLD: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'TechArticle',
      headline: art.titulo,
      description: art.descripcion,
      inLanguage: art.idioma,
      dateModified: art.actualizado || undefined,
      publisher: { '@type': 'Organization', name: 'Positiva', url: SITIO },
      mainEntityOfPage: `${SITIO}${base}/${art.slug}/`,
    }),
  });
}

/* Las dos vías de entrada. No son categorías: son las dos personas que llegan
 * aquí. El fotógrafo trabaja sobre papel (el panel) y quien revisa trabaja en
 * el cuarto oscuro (la galería) — misma regla de color que el producto. */
const VIAS = [
  {
    clase: 'via-papel', rotulo: 'Soy fotógrafo', idx: 'A',
    lede: 'Tienes una cuenta en Positiva. Subes tu trabajo, lo entregas con tu marca y gestionas tus galerías desde el panel.',
    enlaces: ['crear-tu-primera-galeria', 'enlace-de-cliente', 'planes-y-precios'],
  },
  {
    clase: 'via-sala', rotulo: 'Me han mandado una galería', idx: 'B',
    lede: 'Has recibido el enlace de una galería. No necesitas cuenta ni instalar nada para verla, marcar tu selección y comentar.',
    enlaces: ['revisor-entrar-en-la-galeria', 'revisor-comentar-video', 'revisor-atajos-de-teclado'],
  },
];

function paginaIndice(idioma, todos) {
  const base = `/soporte/${idioma}`;
  const publicos = todos.filter((a) => a.estado !== 'pendiente');
  const conArticulos = CATEGORIAS.filter((c) => publicos.some((a) => a.categoria === c.id));

  const vias = VIAS.map((via) => {
    const arts = via.enlaces.map((s) => publicos.find((a) => a.slug === s)).filter(Boolean);
    for (const s of via.enlaces) {
      if (!publicos.some((a) => a.slug === s)) errores.push(`Vía "${via.rotulo}": el artículo "${s}" no existe o no se publica.`);
    }
    return `<div class="via ${via.clase}">
      <p class="eyebrow"><span class="idx">${via.idx}</span> ${escapar(via.rotulo)}</p>
      <p class="via-lede">${escapar(via.lede)}</p>
      <ul class="via-lista">${arts.map((a) => `<li><a href="${base}/${a.slug}/">${escapar(a.titulo)}<span aria-hidden="true">→</span></a></li>`).join('')}</ul>
    </div>`;
  }).join('\n');

  const secciones = conArticulos.map((cat) => {
    const arts = publicos.filter((a) => a.categoria === cat.id);
    return `<section class="cat" id="${cat.id}">
  <p class="eyebrow"><span class="idx">${numeroCat(cat.id)}</span> ${escapar(cat.titulo)}</p>
  <p class="cat-resumen">${escapar(cat.resumen)}</p>
  <ul class="filas">${arts.map((a) => `<li>
      <a href="${base}/${a.slug}/">
        <span class="fila-t">${escapar(a.titulo)}${a.audiencia === 'revisor' ? '<i class="marca-revisor">Revisor</i>' : ''}</span>
        <span class="fila-d">${escapar(a.descripcion)}</span>
        <span class="fila-v" aria-hidden="true">→</span>
      </a></li>`).join('')}</ul>
</section>`;
  }).join('\n');

  const cuerpo = `
<header class="portada">
  <div class="wrap portada-caja">
    <p class="eyebrow">Soporte</p>
    <h1>Documentación<br>de <em>Positiva.</em></h1>
    <p class="lede">Documentación completa de Positiva: ${publicos.length} artículos sobre galerías, entrega, revisión de fotografía y vídeo, planes y almacenamiento. El buscador recorre el texto completo de cada artículo, no solo los títulos.</p>
    ${buscador('contraseña, RAW, rondas, descargar…')}
  </div>
</header>

<section class="vias-banda">
  <div class="wrap vias">
${vias}
  </div>
</section>

<div class="wrap indice">
  <aside class="rail">
    <p class="rail-rotulo">El índice</p>
    <ul class="rail-cats">${conArticulos.map((c) => `<li><a href="#${c.id}"><span class="idx">${numeroCat(c.id)}</span> ${escapar(c.titulo)}</a></li>`).join('')}</ul>
  </aside>
  <div class="indice-cuerpo">
${secciones}
  </div>
</div>

<section class="dark cierre">
  <div class="wrap cierre-caja">
    <p class="eyebrow"><span class="idx">··</span> Contacto</p>
    <h2>¿No encuentras lo que <em>buscabas?</em></h2>
    <p class="lede">Escríbenos y te ayudamos con tu caso concreto. Respondemos todas las consultas en un plazo de 24 a 48 horas. Si tu duda no está recogida en esta documentación, la incorporamos.</p>
    <p><a class="btn btn-primario" href="mailto:${CONTACTO}?subject=${encodeURIComponent('Soporte de Positiva')}">Escribir a ${CONTACTO}</a></p>
  </div>
</section>`;

  return pintar({
    LANG: idioma,
    TITULO: 'Soporte · Positiva',
    DESCRIPCION: 'Guías y respuestas sobre Positiva: galerías, entrega, revisión de foto y vídeo, planes y almacenamiento.',
    CANONICA: `${SITIO}${base}/`,
    LOCALE: IDIOMAS[idioma].locale,
    CLASE: 'pagina-indice',
    CONTENIDO: cuerpo,
    JSONLD: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'CollectionPage',
      name: 'Soporte de Positiva',
      inLanguage: idioma,
      url: `${SITIO}${base}/`,
    }),
  });
}

/* ── Escritura ───────────────────────────────────────────────────────────── */

let escritos = 0;
function escribir(ruta, contenido) {
  if (SOLO_COMPROBAR) return;
  mkdirSync(dirname(ruta), { recursive: true });
  writeFileSync(ruta, contenido);
  escritos++;
}

const todosIdiomas = {};
for (const idioma of Object.keys(IDIOMAS)) todosIdiomas[idioma] = cargar(idioma);

// Enlaces internos: un "relacionados" o un enlace /soporte/ que apunta a un
// artículo inexistente es un 404 que nadie va a notar hasta que un cliente lo
// pise. Se comprueban antes de escribir nada.
for (const [idioma, arts] of Object.entries(todosIdiomas)) {
  const existentes = new Set(arts.map((a) => a.slug));
  for (const art of arts) {
    for (const s of art.relacionados) {
      if (!existentes.has(s)) errores.push(`${idioma}/${art.slug}.md: relacionado "${s}" no existe.`);
    }
    for (const [, slug] of art.cuerpo.matchAll(new RegExp(`\\(/soporte/${idioma}/([a-z0-9-]+)/\\)`, 'g'))) {
      if (!existentes.has(slug)) errores.push(`${idioma}/${art.slug}.md: enlace a "/soporte/${idioma}/${slug}/", que no existe.`);
      else if (arts.find((a) => a.slug === slug).estado === 'pendiente') {
        errores.push(`${idioma}/${art.slug}.md: enlaza a "${slug}", que está en estado pendiente y no se publica.`);
      }
    }
  }
}

if (errores.length) {
  console.error('\n✗ El build no ha generado nada. Corrige esto primero:\n');
  for (const e of errores) console.error(`  · ${e}`);
  console.error('');
  process.exit(1);
}

for (const [idioma, arts] of Object.entries(todosIdiomas)) {
  if (!arts.length) continue;
  escribir(join(SALIDA, idioma, 'index.html'), paginaIndice(idioma, arts));
  for (const art of arts) {
    if (art.estado === 'pendiente') continue;
    escribir(join(SALIDA, idioma, art.slug, 'index.html'), paginaArticulo(art, arts));
  }

  // Índice del buscador. Se descarga solo cuando alguien toca el campo, así
  // que puede permitirse llevar el texto de los artículos: es lo que hace que
  // buscar «HEIC» o «Cuarto oscuro» devuelva algo.
  const indiceBusca = arts
    .filter((a) => a.estado !== 'pendiente')
    .map((a) => ({
      slug: a.slug,
      titulo: a.titulo,
      descripcion: a.descripcion,
      categoria: CATEGORIAS.find((c) => c.id === a.categoria).titulo,
      audiencia: a.audiencia,
      // Sin recorte. Con el tope de 3000 caracteres que había antes, las
      // últimas secciones de un artículo largo —justo donde vive «Problemas
      // frecuentes»— quedaban fuera del buscador.
      texto: aTextoPlano(a.cuerpo),
    }));
  escribir(join(SALIDA, idioma, 'buscador.json'), JSON.stringify(indiceBusca));
}

escribir(join(SALIDA, 'soporte.css'), readFileSync(join(AQUI, 'soporte.css'), 'utf8'));

// Capturas: se copian tal cual de soporte/_img/ a public/soporte/img/. Se
// preparan a mano (WebP, 1400 px de ancho como mucho) antes de meterlas ahí;
// el generador no redimensiona nada.
const DIR_IMG = join(AQUI, '_img');
let capturas = 0;
if (existsSync(DIR_IMG)) {
  for (const archivo of readdirSync(DIR_IMG)) {
    if (archivo.startsWith('.')) continue;
    if (!SOLO_COMPROBAR) {
      mkdirSync(join(SALIDA, 'img'), { recursive: true });
      copyFileSync(join(DIR_IMG, archivo), join(SALIDA, 'img', archivo));
    }
    capturas++;
  }
}

// Redirección de /soporte/ al idioma por defecto, sin tocar el Worker.
escribir(join(SALIDA, 'index.html'),
  `<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">` +
  `<title>Soporte · Positiva</title><link rel="canonical" href="${SITIO}/soporte/es/">` +
  `<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=/soporte/es/">` +
  `</head><body><p><a href="/soporte/es/">Ir al soporte</a></p></body></html>`);

/* ── PENDIENTES.md: lo que falta por escribir a mano ──────────────────────── */

const pendientes = Object.values(todosIdiomas).flat().filter((a) => a.estado === 'pendiente');
const borradores = Object.values(todosIdiomas).flat().filter((a) => a.estado === 'borrador');

const listado = (arr) => arr.length
  ? arr.map((a) => `- [ ] **${a.titulo}** \`${a.idioma}/${a.slug}.md\` — ${a.motivo || a.descripcion || 'sin motivo anotado'}`).join('\n')
  : '_Nada pendiente._';

escribir(join(AQUI, 'PENDIENTES.md'), `# Soporte · lo que falta

Generado por \`node soporte/build.mjs\`. No lo edites a mano: sale del frontmatter
de cada artículo (\`estado:\` y \`motivo:\`).

- **pendiente** → el artículo NO se publica. Solo existe el archivo con su ficha.
- **borrador** → el artículo SÍ se publica, con una banda de "En obra" encima.

## Por escribir (${pendientes.length})

Requieren criterio tuyo, un vídeo, o una decisión que el código no responde.

${listado(pendientes)}

## Publicados con aviso de "en obra" (${borradores.length})

Documentan algo que está cambiando. Revisar cuando el frente se cierre.

${listado(borradores)}

## Dudas anotadas en los artículos (${Object.values(todosIdiomas).flat().reduce((n, a) => n + a.dudas.length, 0)})

Preguntas que quedaron abiertas al escribir. Vienen de los comentarios HTML del
Markdown, que **no** se publican. Resuélvela, borra el comentario del archivo y
vuelve a generar.

${Object.values(todosIdiomas).flat().filter((a) => a.dudas.length).map((a) =>
  `### \`${a.idioma}/${a.slug}.md\`\n\n${a.dudas.map((d) => `- ${d.replace(/^DUDA:\s*/i, '')}`).join('\n')}`
).join('\n\n') || '_Ninguna._'}
`);

/* ── Resumen ─────────────────────────────────────────────────────────────── */

const total = Object.values(todosIdiomas).flat();
const publicados = total.filter((a) => a.estado === 'publicado').length;

if (avisos.length) {
  console.warn('\nAvisos:');
  for (const a of avisos) console.warn(`  · ${a}`);
}

console.log(`\n${SOLO_COMPROBAR ? '✓ Comprobado' : '✓ Generado'}: ${publicados} publicados, ${borradores.length} en obra, ${pendientes.length} por escribir, ${capturas} captura(s).`);
if (!SOLO_COMPROBAR) console.log(`  ${escritos} archivos en public/soporte/ · pendientes en soporte/PENDIENTES.md\n`);
