---
titulo: Cómo exportar los marcadores a DaVinci Resolve o Final Cut
descripcion: Los comentarios anclados al código de tiempo (timecode) se descargan como marcadores de línea de tiempo para DaVinci Resolve o para Final Cut Pro.
categoria: revision
audiencia: fotografo
orden: 60
actualizado: 24 de agosto de 2026
relacionados: [comentarios-en-el-panel, como-funciona-la-revision, formatos-admitidos]
---

Al terminar este proceso tendrás los comentarios de tu cliente dentro de tu programa de montaje, convertidos en marcadores de línea de tiempo situados en su fotograma exacto, en lugar de en una pestaña del navegador que hay que consultar en paralelo.

## Antes de empezar

- La galería tiene que ser de **revisión** y contener al menos un comentario anclado al código de tiempo de un vídeo. Los comentarios sobre fotografías y sobre la galería entera no generan marcadores. Consulta [Cómo comentar un vídeo en un instante concreto](/soporte/es/revisor-comentar-video/).
- Necesitas saber a cuántos fotogramas por segundo está tu material. Positiva no detecta ese dato y no puede deducirlo del archivo.
- Solo se admiten velocidades enteras: **24, 25 y 30**. El material a 23,976 o a 29,97 fotogramas por segundo, es decir NTSC, no está soportado, porque requeriría código de tiempo con salto de fotograma y hoy no se genera.

:::plan La exportación de marcadores requiere el plan Autor o el plan Estudio
Depende de la revisión de vídeo, que no está incluida en el plan Gratis. Consulta [Qué incluye cada plan](/soporte/es/planes-y-precios/).
:::

## Dónde se hace

Panel → **Galerías** → la galería → paso **Comentarios** → bloque **«Exportar marcadores»**.

La galería tiene un único bloque **«Exportar marcadores»**, con un solo selector de fotogramas por segundo y, debajo, una fila por cada vídeo. Cada fila incluye sus dos botones, **«⬇ EDL»** y **«⬇ FCPXML»**. El resto del paso es la lista de comentarios, que se lee y se responde por separado. Consulta [Cómo leer y responder los comentarios de tu cliente](/soporte/es/comentarios-en-el-panel/).

## Pasos

1. **Accede al paso Comentarios de la galería y localiza el bloque «Exportar marcadores».**
2. **Ajusta el selector de fotogramas por segundo al valor de tu material**, entre **24**, **25** y **30**. El selector viene fijado en **25** por defecto.
3. **Busca la fila del vídeo que quieras exportar.** Cada vídeo con comentarios anclados al código de tiempo tiene la suya.
4. **Pulsa «⬇ EDL» si vas a montar en DaVinci Resolve, o «⬇ FCPXML» si vas a montar en Final Cut Pro.** El archivo se descarga en tu equipo.
5. **Importa el archivo descargado en tu programa de montaje**, por la ruta que corresponda de las dos que se describen a continuación.

:::aviso El selector de fotogramas por segundo es único para toda la galería
El valor que fijes se aplica a todas las exportaciones de esa galería, no solo a la del vídeo cuya fila estás usando. Si en la misma entrega conviven piezas a velocidades distintas, cambia el selector antes de descargar cada una.

Positiva no detecta los fotogramas por segundo reales del vídeo. Si tu material va a otra velocidad y no lo corriges, los marcadores se desincronizan de forma acumulativa a lo largo del vídeo: al principio caen cerca del fotograma correcto y al final quedan lejos. Comprueba el selector en cada exportación.
:::

## Cómo se importa el archivo

### DaVinci Resolve, con el EDL

El EDL es un **CMX3600** que contiene un marcador amarillo por comentario, cada uno con su código de tiempo y con su texto en el formato `autor: comentario`.

Para importarlo, haz clic derecho sobre la línea de tiempo y elige **Timelines → Import → Timeline Markers from EDL**.

### Final Cut Pro, con el FCPXML

Para importarlo, abre **File → Import → XML**.

Si lo abres como proyecto nuevo, Final Cut crea una línea de tiempo con los marcadores en su posición exacta.

:::nota El FCPXML declara siempre 1920×1080
Si tu material es vertical o de 4K y dejas que Final Cut cree un proyecto nuevo a partir del archivo, el formato declarado en el proyecto no coincidirá con el del metraje.
:::

## Resultado

Cada comentario anclado al código de tiempo aparece como un marcador situado en el fotograma que le corresponde, de modo que el montaje avanza de marcador en marcador sin volver al navegador. El archivo descargado es una copia del estado de la galería en ese momento: si tu cliente añade comentarios después, hay que exportarlo de nuevo.

## Problemas frecuentes

- **Los marcadores no caen donde deberían y el desajuste crece a lo largo del vídeo.** El selector de fotogramas por segundo no coincide con la velocidad real del material. Ajústalo y vuelve a descargar el archivo.
- **Tu material va a 23,976 o a 29,97 fotogramas por segundo.** Esas velocidades no están soportadas: el selector solo admite 24, 25 y 30, y cualquiera de esos tres valores desfasa los marcadores con material NTSC.
- **Final Cut crea un proyecto con un formato que no corresponde al metraje.** El FCPXML declara siempre 1920×1080. Importa el archivo sobre un proyecto ya creado con el formato correcto, en lugar de dejar que Final Cut lo cree.
