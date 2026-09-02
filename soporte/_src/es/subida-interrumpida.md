---
titulo: La subida se ha interrumpido
descripcion: Cuando una tanda de subida se corta, lo que ya había terminado está a salvo y el resto desaparece de la cola: qué comprobar y cómo recuperar lo que falta.
categoria: subida
audiencia: fotografo
orden: 50
actualizado: 31 de agosto de 2026
relacionados: [subir-fotos-y-videos, archivos-que-no-suben, ampliar-almacenamiento]
---

La cola de subida se detiene antes de llegar a cero, o la lista aparece vacía y en la galería falta parte del material que habías soltado.

Un corte de red no suele romper nada: cada llamada se reintenta por su cuenta varias veces antes de dar el archivo por fallido, y el resto de la cola continúa subiendo mientras tanto. La causa habitual de una tanda perdida no es la conexión, sino el cierre de la pestaña del navegador.

Cuando un archivo sí acaba fallando, su fila conserva el texto del error y un enlace de **«reintentar»** a la derecha. Las filas fallidas **no se pintan en rojo**: se reconocen por ese texto y por ese enlace, no por el color.

## Comprobaciones, en orden

### 1. La pestaña del navegador ha permanecido abierta

**Qué mirar.** La pestaña de Positiva y la lista de la cola, en el paso **Fotos y vídeos** de la galería.

**Qué debería verse.** La cola en marcha, con cinco archivos subiendo de forma simultánea y el resto esperando turno hasta que el recuento llega a cero.

**Qué hacer si no es así.** Si cerraste la pestaña o recargaste la página, la cola se ha perdido. Lo que ya había terminado está a salvo, porque está en el almacenamiento y en la galería; lo que estaba subiendo o esperando turno desaparece de la lista y hay que volver a soltarlo.

Los archivos **grandes** suben por partes y pueden retomar la subida donde se quedaron, pero solo si vuelves a soltar exactamente el mismo archivo. Los archivos de tamaño normal empiezan de cero.

:::aviso Positiva no ofrece «continuar donde lo dejaste»
No hay ningún aviso de que tenías una subida sin terminar, ni una pantalla que te lo recuerde al volver a la galería. Si cierras la pestaña a mitad de tanda, eres tú quien tiene que llevar la cuenta de lo que faltaba.
:::

La regla práctica es dejar la pestaña abierta y el ordenador despierto hasta que la cola llegue a cero. Puedes moverte por otros pasos de la misma galería mientras tanto, porque eso no interrumpe la subida.

### 2. Las filas con mensaje de error dentro de la cola

**Qué mirar.** Cada fila de la lista de subida, leyendo el texto que acompaña al archivo.

**Qué debería verse.** Filas que avanzan y desaparecen al terminar, sin texto de error y sin enlace de **«reintentar»**.

**Qué hacer si no es así.** Pulsa **«reintentar»** en esa fila: un fallo de red aislado se resuelve casi siempre al segundo intento. La excepción es el formato: si el archivo es HEIC o TIFF, reintentar vuelve a subir el original entero y falla en el mismo punto, consumiendo más espacio en cada intento. Consulta [Formatos de archivo admitidos](/soporte/es/formatos-admitidos/).

### 3. El aviso de espacio agotado

**Qué mirar.** Si han fallado varios archivos a la vez y todos con el mismo mensaje.

**Qué debería verse.** Fallos aislados, con mensajes distintos entre sí, si es que hay alguno.

**Qué hacer si no es así.** Cuando la cuota se agota a mitad de tanda, el mensaje es este:

> Te has quedado sin espacio. Reintentar no servirá hasta que liberes sitio o amplíes tu almacenamiento.

El aviso es exacto: reintentar no sirve de nada mientras no haya espacio disponible. Tienes dos caminos para conseguirlo: [ampliar el almacenamiento](/soporte/es/ampliar-almacenamiento/), o liberar el que ya tienes empezando por [las versiones antiguas](/soporte/es/versiones-antiguas/), que son el espacio que más rápido se recupera.

:::aviso El aviso de espacio agotado permanece el resto de la sesión
Aunque amplíes el almacenamiento y las subidas siguientes funcionen con normalidad, el mensaje sigue en pantalla hasta que recargues la página. Recárgala después de ampliar para dejar de leer un error que ya no es cierto.
:::

### 4. Los archivos que suben enteros y no aparecen en la galería

**Qué mirar.** La rejilla del paso **Fotos y vídeos**, comparando lo que hay dentro con lo que habías soltado.

**Qué debería verse.** Cada archivo que termina su subida aparece en la rejilla.

**Qué hacer si no es así.** Una fotografía puede subir su original completo y fallar después, al generar sus versiones derivadas. En ese caso no aparece en la galería: se queda a medias. Es el comportamiento previsto, porque un archivo incompleto se mostraría roto delante de tu cliente.

La causa casi nunca es la red, sino el formato: un HEIC o un TIFF que el navegador no sabe decodificar. Reintentar repite la subida completa del original y vuelve a fallar en el mismo punto. Exporta a JPEG y sube esa versión. Consulta [Formatos de archivo admitidos](/soporte/es/formatos-admitidos/).

## Si el problema continúa

Reúne estos datos antes de escribir a soporte:

- El nombre de la galería y cuántos archivos componían la tanda.
- El navegador y la versión que estabas utilizando.
- El texto exacto del error de una de las filas fallidas.
- Si el aviso de espacio agotado llegó a aparecer, y si el problema persiste después de recargar la página.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
