# Informe de novedades · pendiente para el chat de soporte

Generado el 2026-09-02 · rango `f384d1d..6d1de1e` · **desplegado en producción,
confirmado por Rodrigo el 02/09**. Sustituye al informe del 25/08 (atendido).

Nota: las entradas de /novedades/ del 31 de agosto ya estaban publicadas, pero
aquel ciclo no generó informe de impacto ni actualizó el marcador — este informe
cubre por tanto TODO el lote (31 ago + 1-2 sep). Marcador actualizado a 6d1de1e.

## Qué se ha publicado hoy en /novedades/ (2 sep)

1. Dominio propio completo: vídeos y ZIP ya se sirven desde el dominio propio (plan Estudio).
2. Seguridad: una galería desactivada (a mano o por caducidad) corta el acceso al momento;
   reactivar lo devuelve sin reabrir enlace; el fotógrafo sí puede entrar en la suya.

## Artículos de soporte a revisar (afirmación a verificar, no texto nuevo)

| Artículo | Qué verificar |
|---|---|
| dominio-propio | Ahora TODO se sirve desde el dominio propio, incluidos vídeos y descargas ZIP. Si el artículo listaba limitaciones («los vídeos salen de positiva.studio»), quedaron obsoletas. |
| enlace-de-cliente · revocar-un-enlace | Comportamiento nuevo al desactivar: el acceso se corta también para sesiones ya abiertas; reactivar restaura sin reabrir el enlace. |
| disenos-de-galeria | Cuadrículas: ahora SEIS (Filas, Magazine, Mosaico, Denso, Columna, Tres columnas — labels verificados en el código). Portadas siguen siendo siete (Editorial, Split, Overlay, Magazine, Minimal, Foto Top, Cartel). Nuevo modo «el Pase» (proyección a pantalla completa) y portada de cine (clip como portada). El paso Diseño ya no tiene presets: dos selectores directos. |
| disenos-de-video | Videoteca se suma a Estreno, Cartel, Vitrina y Montaje. El selector avisa cuando un diseño no encaja con el número de piezas. |
| favoritas-del-cliente | Las favoritas se activan POR ENLACE (antes por galería). Nuevo plugin de Lightroom Classic: importa la selección (.txt/.csv) como colección; se descarga desde el panel de favoritas. |
| enlace-de-cliente · contrasena-del-enlace | Caducidad OPCIONAL de galería: fecha, desactivación automática y avisos por email. El claim «los enlaces no caducan» sigue siendo cierto por defecto — la caducidad es una decisión del fotógrafo. |
| el-panel-por-dentro · los-pasos-de-una-galeria | Buscador de fotos en el editor; orden por toma o nombre elegido por galería; tarjeta de enlace reorganizada en tres zonas. |
| revisor-atajos-de-teclado | Velo de atajos al entrar por primera vez en la revisión de vídeo (botón «?» para recuperarlo). |
| enviar-la-galeria | Al compartir un enlace, la tarjeta de previsualización muestra la portada (estable). Al compartir una foto no viaja texto. |
| perfil-publico · portfolio | Los datos de contacto del perfil cierran también las galerías de entrega. Orden aleatorio opcional de la rejilla del portfolio. |

## Landing (ya corregida desde este flujo, 2 sep)

/galerias/ y home: «cinco cuadrículas» → «seis»; Videoteca añadida a las listas de
diseños de vídeo en /galerias/ y /revision-video/. Recuentos verificados contra los
registros del código (grids/registry.ts, heroes/registry.ts, videoLayouts/registry.ts).

---

## Nota para el chat de soporte: el chrome ahora se estampa (2026-09-02)

Por orden de Rodrigo, el menú y el pie de /soporte/ se han igualado al del sitio
DESDE la landing: `npm run stamp` ahora recoge también `public/soporte/es/**/index.html`
(glob en `scripts/stamp.mjs`) y sobrescribe sus bloques `pv:nav` y `pv:footer` con
los parciales de `partials/`. Qué significa para el flujo de soporte:

- Los artículos deben CONSERVAR los marcadores `<!-- pv:nav -->…<!-- /pv:nav -->`
  y `<!-- pv:footer -->…<!-- /pv:footer -->`; su contenido lo pisa el stamp.
- Si el generador de soporte lleva una copia propia del chrome, ya no hace falta
  mantenerla al día: basta con emitir los marcadores (con cualquier contenido) y
  ejecutar `npm run stamp` tras generar.
- El CSS antiguo del chrome que viva FUERA de los marcadores en las plantillas de
  soporte puede retirarse cuando toque; hoy no interfiere (el bloque estampado es
  autocontenido y posterior en el documento).


## Añadido 2026-09-03 · Favoritas con nombre (desplegado hasta 4c0aac4)

Actualizado DESDE la landing por orden de Rodrigo: entrada en /novedades/ (3 sep),
/galerias/ («Las favoritas vuelven a tu editor») y el artículo de soporte
favoritas-del-cliente (nueva sección «Quién ha marcado cada favorita», paso de
exportación con «Solo clientes / Todos», sello al 03/09). Los literales salen de
los commits (A-D de new/favorites), no de pantalla: conviene el repaso visual del
flujo de soporte cuando toque. Marcador de novedades en 4c0aac4.
