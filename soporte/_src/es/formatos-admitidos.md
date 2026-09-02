---
titulo: Formatos de archivo admitidos
descripcion: Positiva admite lo que tu navegador sepa leer como imagen o como vídeo, con consecuencias muy distintas para el RAW, el HEIC, el TIFF y el PNG.
categoria: subida
audiencia: fotografo
orden: 20
actualizado: 24 de agosto de 2026
relacionados: [subir-fotos-y-videos, archivos-que-no-suben, subida-interrumpida]
---

Positiva admite **lo que tu navegador sepa leer como imagen o como vídeo**. No existe una lista blanca de extensiones, porque la decisión no la toma Positiva: la toma el navegador que tengas abierto en ese momento.

Estas tablas recogen el comportamiento de los formatos que llegan con más frecuencia desde una cámara o un teléfono. Te sirven antes de exportar una entrega, y también después, para identificar por qué un archivo concreto se ha quedado fuera de la galería.

## Formatos de fotografía

| Formato | Qué ocurre al subirlo |
|---|---|
| **JPEG** | Se sube y se muestra siempre. Es el formato que conviene entregar. |
| **PNG** | Se sube y funciona, pero todas las versiones que ve tu cliente se generan en **JPEG** y pierden la transparencia. |
| Cualquier otra imagen que tu navegador decodifique (**WebP**, por ejemplo) | Se sube y funciona. Como con el PNG, las versiones que ve tu cliente se generan en **JPEG**. |
| **RAW** (CR2, NEF, ARW, DNG…) | Normalmente ni siquiera entra en la cola. Se descarta en silencio. |
| **HEIC** (el formato del iPhone) | Puede entrar en la cola, subir el original entero y fallar después. Consume almacenamiento y la fotografía no llega a aparecer. |
| **TIFF** | Igual que HEIC: ningún navegador principal lo decodifica. |

## Formatos de vídeo

| Formato | Qué ocurre al subirlo |
|---|---|
| **MP4 con H.264** | Se sube y se reproduce en cualquier navegador. Es el formato que conviene entregar. |
| Cualquier vídeo que tu navegador no reproduzca | Falla antes de subir nada, con el mensaje **«No se pudo leer el vídeo.»** No consume almacenamiento. |

## Notas de uso

### El RAW se descarta sin dejar rastro

Si sueltas una carpeta de archivos RAW y no ocurre nada —ni fila en la cola, ni mensaje de error, ni barra de progreso—, este es el motivo. El sistema operativo no le atribuye al archivo un tipo de imagen reconocible, de modo que se descarta en silencio: no llega a aparecer siquiera como fila fallida.

Es el comportamiento previsto, aunque no lo parezca. Revela el material y expórtalo a JPEG.

### El HEIC y el TIFF consumen almacenamiento antes de fallar

Estos dos formatos son los únicos que tienen coste. Un HEIC **sí puede entrar en la cola**. Cuando eso ocurre, el original **se sube entero** —y ocupa tu almacenamiento— y **después** falla al generar las versiones derivadas, porque el navegador no sabe decodificarlo. La fotografía queda a medias y no aparece en la galería.

:::aviso Reintentar un HEIC repite la subida completa y vuelve a fallar
El enlace de reintentar vuelve a subir el original entero y falla exactamente en el mismo punto. Cada intento consume más espacio y ninguno va a completarse. Exporta la fotografía a JPEG y sube esa versión.
:::

Con TIFF ocurre lo mismo y por el mismo motivo.

### El PNG se entrega en JPEG

Un PNG se sube y se muestra sin incidencias, pero las versiones que Positiva genera a partir de él son JPEG. La transparencia del original se pierde en esas versiones, que son las que ve tu cliente. Si el archivo depende de su fondo transparente, esa transparencia no llega a la galería.

### El rechazo del vídeo es temprano

Con vídeo el comportamiento es más limpio que con fotografía. Si tu navegador no puede reproducir el archivo, la subida falla **antes** de transferir nada, con este mensaje:

> No se pudo leer el vídeo.

No consume espacio ni deja el archivo a medias. Es un rechazo temprano, no un error del sistema.

### Qué exportar

- **Fotografía: JPEG.**
- **Vídeo: H.264 en MP4.**

Estos dos formatos son los que garantizan que el archivo funcione en cualquier navegador: el tuyo al subirlo y el de tu cliente al abrirlo. Un formato que se abre sin problemas en tu ordenador no es necesariamente un formato que se abra en el navegador de quien revisa la galería desde el móvil.

:::nota Los mensajes de error de decodificación los redacta el navegador
Cuando un archivo falla al decodificarse, el texto que aparece en la fila procede del navegador, no de Positiva. Por eso a veces se muestra en inglés y con terminología técnica. No es un problema de traducción.
:::

Si tienes archivos que se quedan fuera y no sabes en cuál de estos casos encajan, [Hay archivos que no se suben](/soporte/es/archivos-que-no-suben/) está ordenado por síntoma.
