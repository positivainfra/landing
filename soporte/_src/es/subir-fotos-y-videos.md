---
titulo: Cómo subir fotografías y vídeos a una galería
descripcion: Positiva sube los archivos desde tu navegador en tandas de cinco simultáneos, genera las versiones derivadas por el camino y espera al vídeo hasta el final.
categoria: subida
audiencia: fotografo
orden: 10
actualizado: 31 de agosto de 2026
relacionados: [formatos-admitidos, subida-interrumpida, archivos-que-no-suben]
---

Al terminar este proceso tendrás las fotografías y los vídeos del encargo dentro de la galería, con sus versiones derivadas generadas y visibles para tu cliente.

La subida se ejecuta en el navegador y avanza en segundo plano: mientras la cola trabaja puedes seguir editando otros pasos de la misma galería.

## Antes de empezar

- La galería creada. Consulta [Cómo crear una galería](/soporte/es/crear-una-galeria/).
- Los archivos exportados en un formato que el navegador sepa leer: JPEG para fotografía y MP4 con H.264 para vídeo. Los archivos RAW no se admiten. Consulta [Formatos de archivo admitidos](/soporte/es/formatos-admitidos/).
- Espacio libre suficiente en tu cuenta. Si el espacio se agota a mitad de tanda, los archivos que queden por subir fallan. Consulta [Cómo se calcula tu almacenamiento](/soporte/es/almacenamiento/).
- Tiempo para dejar la pestaña abierta hasta el final. La cola reside en la ventana del navegador y no sobrevive a un cierre ni a una recarga. Consulta [La subida se ha interrumpido](/soporte/es/subida-interrumpida/).

## Dónde se hace

Panel → **Galerías** → la galería → paso **Fotos y vídeos**.

## Pasos

### 1. Suelta los archivos en la galería

Dispones de tres zonas donde soltarlos, y las tres inician la subida:

- La **zona de subida**. También puedes pulsar sobre ella para seleccionar los archivos desde tu equipo.
- La **rejilla** de lo que ya has subido.
- El **chip de un momento**. Los archivos que sueltes ahí entran ya clasificados en ese momento.

:::aviso Los vídeos no entran en ningún momento
Un vídeo queda siempre fuera de los momentos, con independencia de dónde lo sueltes, incluso sobre el chip de un momento. Los momentos agrupan fotografías; los vídeos se ordenan en una lista aparte.
:::

### 2. Deja que la cola llegue a cero

Positiva sube **cinco archivos de forma simultánea** y mantiene el resto en cola. No hay límite de archivos por tanda: el proceso se ha verificado con 673 fotografías y 2,3 GB correspondientes a una boda completa en una sola sesión.

Los bytes viajan del navegador **directamente al almacenamiento**, sin pasar por ningún servidor intermedio. Por tanto, la velocidad la determina la subida de tu conexión a internet, no la carga que tenga Positiva en ese momento.

Mientras el original sube, tu propio navegador genera la miniatura y las versiones derivadas de **400 px, 800 px y 2000 px**. Ese trabajo cuesta unos 80 milisegundos por fotografía y se ejecuta en tu equipo, no en el nuestro: es una razón más para mantener la pestaña abierta hasta el final.

Puedes moverte por otros pasos de la misma galería mientras la subida avanza. Eso no la interrumpe.

### 3. Espera las dos fases propias del vídeo

Un vídeo no se comporta como una fotografía y añade dos esperas:

- **Antes de empezar a subir** se genera el fotograma de portada. Son hasta 8 segundos durante los cuales la pantalla no muestra ningún avance.
- **En paralelo a la subida**, desde el primer momento, se genera la tira de miniaturas que se ve al pasar el cursor por la barra de tiempo. Positiva solo la espera al final, y solo si todavía no ha terminado: puede tardar hasta unos dos minutos, y el vídeo no pasa a «listo» hasta entonces.

:::aviso El progreso detenido en el último tramo de la barra no es un bloqueo
Si un vídeo largo se queda al final de la barra sin avanzar, los bytes ya han subido y lo que falta es la tira de miniaturas. Espera a que termine: no canceles la subida ni recargues la página.
:::

Si la tira de miniaturas falla o no llega a tiempo, se omite sin mostrar ningún mensaje y el vídeo queda igualmente listo con su fotograma de portada. No es un fallo y no hay que repetir la subida.

### 4. Selecciona los archivos en la rejilla

La rejilla admite cuatro formas de selección: clic sobre un archivo, **Mayús+clic** para seleccionar un rango, **Cmd/Ctrl+clic** para ir añadiendo archivos sueltos, y arrastrar un rectángulo sobre el fondo.

El selector de tamaño de miniatura **S/M/L** cambia cuántos archivos ves a la vez. Positiva recuerda tu elección.

### 5. Marca la portada

Selecciona **una sola fotografía** y pulsa **«Marcar como portada»**, que pasa a **«Quitar portada»** si ya lo era. Este botón exige una única selección y solo admite fotografías.

Si lo que quieres es que la portada sea un **clip de vídeo**, se elige en el paso **Diseño**, sección **Portada de la galería**. Consulta [Los diseños de galería](/soporte/es/disenos-de-galeria/).

### 6. Ordena las fotografías dentro de cada momento

Arrastra las fotografías hasta la posición que quieras darles. El orden que fijes aquí manda sobre cualquier otro criterio. Si prefieres no colocarlas a mano, el paso **Diseño** ofrece ordenarlas por hora de toma o por nombre de archivo: consulta [En qué orden ve tu cliente las fotografías](/soporte/es/orden-de-las-fotos/).

## Resultado

Los archivos quedan en la galería con su orden, su momento y su portada, y tu cliente los ve al abrir el enlace.

En cuanto la galería contiene al menos un vídeo, la rejilla se divide en dos pestañas, **«Fotos»** y **«Vídeos»**. Si la galería solo tiene fotografías, esas pestañas no aparecen. Las fotografías se agrupan por momentos; los vídeos se presentan en una lista.

## Buscar una fotografía dentro de la galería

Sobre la rejilla, debajo de los chips de momento, hay un campo de búsqueda: **«Buscar por nombre de archivo o título»**, o solo **«Buscar por título»** si ninguna pieza de esa galería conserva su nombre de archivo.

Filtra según escribes, sin botón de buscar. No distingue mayúsculas ni acentos, y exige que **todos** los términos aparezcan, repartidos como sea entre el nombre y el título: «boda maria» encuentra una fotografía titulada «Boda María». Mientras hay texto escrito, al lado se lee cuántas piezas quedan a la vista —**«12 de 240 fotos»**— y la acción **«Limpiar»**.

Con la búsqueda puesta vuelven a verse las cabeceras de momento aunque tengas un chip seleccionado, para que el resultado te diga también en qué momento está cada pieza.

Si no encuentra nada, la rejilla muestra **«Sin resultados»**, la frase **«Ninguna foto se llama así.»** y la acción **«Limpiar la búsqueda»**.

:::aviso Filtrar no deselecciona
Lo que seleccionaste sigue seleccionado aunque la búsqueda deje de mostrarlo. Puedes buscar, marcar, buscar otra cosa y seguir marcando, y todas las acciones operan sobre la selección real, no sobre lo visible.

Por eso el diálogo de borrado añade una línea cuando procede: **«N de ellas no se ven con la búsqueda actual.»** Conviene leerla.
:::

## Eliminar archivos de la galería

Selecciona los archivos y pulsa **«Eliminar»**. La confirmación es esta:

> ¿Eliminar N archivo(s)? Se borran de forma permanente. No se puede deshacer.

:::aviso El borrado se ejecuta en lotes de seis archivos
Si el proceso se interrumpe a la mitad, una parte de los archivos ya está borrada y el mensaje de error no indica cuántos. Mantén la pestaña abierta hasta que el borrado termine.
:::

## Problemas frecuentes

- **La subida tarda unos segundos de más en arrancar en Safari.** Ocurre al entrar a una galería que ya contiene cientos de fotografías y soltar archivos ahí mismo: el navegador está descargando las miniaturas de lo que ya había y comparte la conexión con la subida. La cola arranca por sí sola. Consulta [La galería tarda demasiado en cargar](/soporte/es/galeria-lenta/).
- **Algunos archivos no aparecen después de soltarlos.** Es lo habitual con RAW, HEIC y TIFF, y cada uno falla en un punto distinto. Consulta [Hay archivos que no se suben](/soporte/es/archivos-que-no-suben/).
- **Has cerrado la pestaña con la cola a medias.** Lo que ya había terminado está a salvo; el resto hay que volver a soltarlo. Consulta [La subida se ha interrumpido](/soporte/es/subida-interrumpida/).
