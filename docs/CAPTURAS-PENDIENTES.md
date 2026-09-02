# Capturas y clips pendientes · positiva.studio

Todo el material gráfico que falta por producir, página a página. Salvo que se
indique lo contrario, los ejemplos se montan con las fotos de
`public/img/placeholders/` (proyecto **Campaña NYC** para color, sesión
**La segunda línea** para B/N) — nunca con material de clientes reales, excepto
las páginas de boda, que usan las galerías de boda ya publicadas.

## Especificaciones técnicas

**Estáticas** · JPG (o PNG si hay UI fina), ancho ≥1600px. Solo la interfaz,
sin barra del navegador. Yo genero los derivados optimizados.

**Vídeo normal (loop / showcase)** · MP4 H.264, sin audio, <4MB, con un JPG
del primer fotograma como póster. Se reproduce en bucle al entrar en pantalla.

**Vídeo de paso (historia de la home)** · Descartado el scrubbing por scroll
(los seeks no rinden bien en navegador real): los pasos se reproducen en
autoplay al entrar su acto y se congelan en el último fotograma. Graba 4-10 s
terminando en el estado final del paso; MP4 H.264 normal, sin audio, <2MB.

---

## 1 · Home — la historia del hero (prioridad máxima)

La tarjeta CSS de cada paso se sustituye por tu clip (scrub) o estática.
El paso «zip arcaico» se queda en CSS. Galería: **Campaña NYC**.

| Archivo destino | Qué grabar | Tipo |
|---|---|---|
| ~~`video/pasos/subes.mp4` + `-poster.jpg`~~ | **HECHO** — integrado desde `carga-fotos-videos.mp4` (recortado a 10,2 s: lo grabado a partir de ahí — galería pública y visor — pisa los actos siguientes) | ✔ |
| ~~`video/pasos/disenas.mp4` + `-poster.jpg`~~ | **HECHO** — integrado desde `diseños.mp4` (14,7 s, autoplay en el acto 02) | ✔ |
| ~~`video/pasos/compartes.mp4`~~ | **YA NO HACE FALTA** — el acto 03 es una animación CSS de enlaces (campana-nyc / -prensa / -invitados con Descarga·Favoritas·Contraseña·Desactivar), movida por el scroll | ✔ |
| ~~`video/pasos/cliente.mp4` + `-poster.jpg`~~ | **HECHO** — integrado desde `comentarios.mp4` (11 s, autoplay en el acto 04) | ✔ |
| (opcional) `img/pasos/hero-galeria.jpg` | La galería Campaña NYC terminada, portada arriba | Estática — hoy es un mock CSS que ya funciona |

## 2 · Home — resto

| Archivo | Qué | Tipo |
|---|---|---|
| `video/showcase-hero.mp4` (existe) | Regrabar el showcase de 40 s con Campaña NYC para que toda la home cuente la misma galería | Vídeo loop · opcional |
| Tarjetas «Qué hace Positiva» | Con vídeo al hover: Entrega, Revisión foto, Revisión vídeo y Diseño ya reales. Falta solo refrescar Portfolio si la UI cambió | Estática · opcional |

## 3 · /revision-video/ — COMPLETA

| Archivo | Qué | Tipo |
|---|---|---|
| ~~`video/revision-comentar.mp4`~~ | **HECHO** — integrado desde `revision-video-comentar.mp4` (16 s, loop) | ✔ |
| ~~`video/revision-export.mp4`~~ | **HECHO** — integrado desde `revision-video-exportar.mp4` (12 s, loop) | ✔ |
| ~~`img/revision/rondas-panel`~~ | **HECHO** — vídeo en su lugar, desde `revision-video-rondas.mp4` (15 s, loop) | ✔ |

## 4 · /revision-foto/

| Archivo | Qué | Tipo |
|---|---|---|
| `img/revision-foto/rejilla-favoritas.jpg` | La rejilla de revisión con favoritas marcadas, usando la sesión B/N La segunda línea (sustituye la captura de boda actual en la sección oscura) | Estática |
| (opcional) `img/revision-foto/panel-comentarios.jpg` | Tu panel recibiendo favoritas y comentarios | Estática |

## 5 · /galerias/

| Archivo | Qué | Tipo |
|---|---|---|
| `video/showcase-generico.mp4` (existe) | Regrabar con Campaña NYC si quieres coherencia total | Vídeo loop · opcional |
| `img/galerias/momentos-cabecera.jpg` | Cabecera de una galería con sus momentos y recuentos, con placeholders (hoy usa una captura de boda) | Estática |
| (opcional) `img/galerias/analitica.jpg` | El bloque de analítica real de una galería (hoy son cifras esquemáticas en CSS que funcionan bien) | Estática · opcional |

## 6 · /agencias/ y /productoras/

| Archivo | Qué | Tipo |
|---|---|---|
| 2 estáticas de galerías de marca | La tira usa las galerías reales de Clifton Pro (slide-2 y slide-4). Si prefieres no usar trabajo de cliente real, sustituir por dos galerías montadas con placeholders | Estáticas · solo si Clifton no puede usarse |

## 7 · Sin capturas pendientes

/portfolio/ (perfil-rmq y perfil-qws ya reales — refrescar solo si la UI cambió),
/bodas/ y /freelance/ (material de boda ya publicado), /precios/, comparativas,
/novedades/, /soporte/.

## Recordatorio de pendientes que no son capturas

Hex reales de los 4 temas de galería · textos legales aprobados (aviso legal,
privacidad, términos) · llms.txt.

---

Cuando tengas archivos, déjalos en las rutas de arriba (o pásamelos) y los
integro: los pasos de la historia con scrubbing por scroll, los clips en bucle
con su póster, y las estáticas con sus derivados optimizados.
