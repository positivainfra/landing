---
titulo: Hay archivos que no se suben
descripcion: Cuando un archivo se queda fuera de la galería la causa suele ser su formato y no la conexión: identifica el síntoma en pantalla y aplica su solución.
categoria: problemas
audiencia: fotografo
orden: 40
actualizado: 31 de agosto de 2026
relacionados: [formatos-admitidos, subida-interrumpida, subir-fotos-y-videos]
---

Sueltas una tanda de archivos y parte de ellos no llega a la galería: unos no aparecen ni en la lista de subida, otros muestran un mensaje de error y otros terminan la subida sin llegar a mostrarse.

Casi siempre la causa es el formato del archivo, no la conexión. Las comprobaciones siguientes están ordenadas por frecuencia, y cada una parte de lo que se ve en pantalla.

Antes de empezar, conviene saber cómo se reconoce un archivo fallido: **las filas con error no se pintan en rojo**. Lo que las distingue es el texto del error dentro de la fila y el enlace de **«reintentar»** que aparece a su derecha.

## Comprobaciones, en orden

### 1. Cada archivo soltado tiene su fila en la cola

**Qué mirar.** La lista de subida, justo después de soltar los archivos.

**Qué debería verse.** Una fila por cada archivo soltado, aunque alguna termine fallando.

**Qué hacer si no es así.** Si no aparece ni fila, ni mensaje de error, ni barra de progreso, esos archivos son casi con seguridad **RAW** —CR2, NEF, ARW, DNG— o algún formato que el sistema no reconoce como imagen ni como vídeo. Se descartan en silencio, sin llegar a figurar siquiera como fila fallida. Revela el material y expórtalo a JPEG. Consulta [Formatos de archivo admitidos](/soporte/es/formatos-admitidos/).

### 2. Las filas no muestran mensajes de decodificación

**Qué mirar.** El texto de cada fila, incluidos los mensajes en inglés o con terminología técnica.

**Qué debería verse.** Filas que avanzan hasta completarse y desaparecen de la lista.

**Qué hacer si no es así.** Un mensaje de ese tipo significa que el navegador no sabe decodificar ese formato. Los formatos que lo provocan son **HEIC** —el del iPhone— y **TIFF**. No pulses el enlace de reintentar: cada intento vuelve a subir el original entero, falla en el mismo punto y consume más espacio. Exporta a JPEG y sube esa versión.

### 3. Los archivos que suben enteros y no aparecen en la galería

**Qué mirar.** La rejilla del paso **Fotos y vídeos**, comparando lo que hay dentro con lo que habías soltado.

**Qué debería verse.** Cada archivo que completa su subida aparece en la rejilla.

**Qué hacer si no es así.** El original ha subido completo y ha fallado al generar las miniaturas y las versiones derivadas. La fotografía se queda a medias y no llega a mostrarse: Positiva no muestra un archivo incompleto, porque se vería roto delante de tu cliente.

Es la misma causa que la comprobación anterior, con el almacenamiento ya consumido. Exporta a JPEG y sube esa versión. Consulta [Formatos de archivo admitidos](/soporte/es/formatos-admitidos/).

### 4. Los vídeos no muestran «No se pudo leer el vídeo.»

**Qué mirar.** El mensaje de las filas correspondientes a vídeos.

**Qué debería verse.** El vídeo genera su fotograma de portada y empieza a subir.

**Qué hacer si no es así.** El mensaje **«No se pudo leer el vídeo.»** indica que tu navegador no puede reproducir ese archivo, de modo que ni siquiera intenta subirlo. El rechazo es temprano y no consume espacio. Exporta a MP4 con H.264.

### 5. Queda espacio en tu almacenamiento

**Qué mirar.** Si han fallado varios archivos a la vez con el mismo mensaje, y la barra de almacenamiento de tu cuenta.

**Qué debería verse.** Espacio libre suficiente para la tanda completa.

**Qué hacer si no es así.** El mensaje **«Te has quedado sin espacio. Reintentar no servirá hasta que liberes sitio o amplíes tu almacenamiento.»** indica que el saldo está agotado, y reintentar no sirve de nada mientras no haya sitio. Junto al aviso hay un enlace **«Ampliar almacenamiento»**. También puedes liberar el que ya tienes purgando [las versiones antiguas](/soporte/es/versiones-antiguas/).

En la fila de cada archivo afectado, el motivo se lee como **«No hay saldo suficiente para este archivo.»**

:::aviso Recarga la página después de ampliar el almacenamiento
El aviso de falta de espacio permanece en pantalla el resto de la sesión, aunque ya hayas ampliado y las subidas nuevas funcionen con normalidad. Recarga la página para dejar de verlo.
:::

### 6. La subida arranca en un tiempo razonable

**Qué mirar.** Cuánto tarda la cola en empezar a moverse, y en qué navegador estás trabajando.

**Qué debería verse.** La cola arranca en cuanto sueltas los archivos.

**Qué hacer si no es así.** Si estás en **Safari** y has entrado en una galería que ya contiene cientos de fotografías, la subida puede tardar unos segundos de más en arrancar: el navegador está descargando las miniaturas de lo que ya había y comparte la conexión con la subida. Arranca por sí sola. Consulta [La galería tarda demasiado en cargar](/soporte/es/galeria-lenta/).

### 7. El progreso de un vídeo largo detenido al final

**Qué mirar.** La barra de progreso del vídeo y su estado en la lista.

**Qué debería verse.** El vídeo pasa a «listo» al terminar.

**Qué hacer si no es así.** Un vídeo detenido en el último tramo de la barra no está bloqueado: falta la tira de miniaturas, que se genera **en paralelo a la subida**, no después, y que todavía no ha terminado. Positiva la espera al final, hasta unos dos minutos, y el vídeo no pasa a «listo» hasta entonces. Espera y no recargues la página. Consulta [Cómo subir fotografías y vídeos a una galería](/soporte/es/subir-fotos-y-videos/).

### 8. El error menciona la política CORS

**Qué mirar.** El texto completo del error de la fila.

**Qué debería verse.** Cualquier mensaje relativo al archivo o al espacio disponible, no a la infraestructura de almacenamiento.

**Qué hacer si no es así.** Este mensaje no depende de tu archivo ni de tu conexión:

> El bucket no expuso la cabecera ETag (revisa la política CORS).

Corresponde a un fallo de configuración de nuestra infraestructura, no a algo que puedas resolver desde el panel. Escribe a `hola@positiva.studio` con el nombre de la galería. Respondemos en un plazo de 24 a 48 horas.

## Si el problema continúa

Reúne estos datos antes de escribir a soporte:

- El nombre de la galería y cuántos archivos componían la tanda.
- La extensión y el tamaño de un archivo que haya fallado.
- El texto exacto del error de esa fila.
- El navegador y la versión que estabas utilizando.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
