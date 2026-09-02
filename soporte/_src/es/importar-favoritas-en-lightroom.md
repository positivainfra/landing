---
titulo: Cómo llevar las favoritas de tu cliente a Lightroom Classic
descripcion: Instalación y uso del plugin de Positiva para Lightroom Classic, que convierte la selección de tu cliente en una colección de tu catálogo.
categoria: revision
audiencia: fotografo
orden: 52
actualizado: 31 de agosto de 2026
relacionados: [favoritas-del-cliente, etiquetar-favoritas-en-finder, como-funciona-la-revision]
---

El plugin de Positiva para Lightroom Classic lee la lista de favoritas que exportas desde el panel y crea con ella **una colección** en tu catálogo. A partir de ahí trabajas con la selección de tu cliente como con cualquier otra colección, sin comparar nombres de archivo a mano.

Es la vía recomendada si editas en Lightroom Classic. La instalación se hace una sola vez, no pasa por ninguna pantalla de seguridad del sistema operativo y no modifica ningún archivo de tu disco.

## Antes de empezar

- **Lightroom Classic.** El Lightroom «de nube» no admite plugins y no puede usar esto.
- **Los originales ya importados en tu catálogo.** El plugin no importa fotografías desde el disco: busca entre las que ya tienes en el catálogo.
- **Los nombres de archivo intactos, extensión incluida.** Es la condición que más problemas da; está explicada en el apartado siguiente.

:::aviso El nombre tiene que coincidir con la extensión
El plugin compara el nombre completo del archivo, extensión incluida. Si subiste a Positiva `DSC_0042.jpg` y en tu catálogo de Lightroom tienes el archivo original `DSC_0042.NEF`, **el plugin no lo encuentra**: ese nombre aparecerá en la lista de no encontrados y la colección saldrá vacía o incompleta.

Para que funcione, en el catálogo tienen que estar las mismas piezas que subiste, con el mismo nombre y la misma extensión. Si tu flujo consiste en revelar en RAW y subir JPEG exportados, importa también esos JPEG al catálogo, o utiliza en su lugar [el script de etiquetas del Finder](/soporte/es/etiquetar-favoritas-en-finder/), que trabaja sobre la carpeta de archivos que tú le indiques.
:::

## Dónde se hace

Panel → **Galerías** → la galería → paso **Favoritas** → sección **Exportar selección**.

## Instalación, una sola vez

### 1. Descarga el plugin

Pulsa **«Plugin de Lightroom (.zip)»**. Se descarga el archivo `positiva-plugin-lightroom.zip`.

:::nota Son dos archivos .zip distintos
El paso **Favoritas** ofrece dos descargas con extensión `.zip` y no son lo mismo. `positiva-plugin-lightroom.zip` es **el plugin**, siempre el mismo y sin datos de ninguna galería. `‹nombre-de-la-galería›-seleccion.zip` es **el script de Finder**, con la lista de esa galería concreta dentro.
:::

### 2. Descomprímelo y guarda la carpeta en un sitio estable

Del `.zip` sale una carpeta llamada **`positiva.lrplugin`**. Guárdala donde vaya a quedarse: **Lightroom no la copia, la usa desde donde esté**. Si la dejas en Descargas y algún día vacías esa carpeta, el plugin deja de funcionar.

Un sitio razonable en macOS es `~/Library/Application Support/Adobe/Lightroom/`. Cualquier carpeta permanente vale.

### 3. Añádela en Lightroom

En Lightroom Classic: **Archivo → Gestor de plugins → Añadir**, y selecciona la carpeta `positiva.lrplugin`. El plugin aparece en la lista con el nombre **Positiva**.

## Cada vez que quieras importar una selección

### 1. Exporta la lista desde el panel

En el paso **Favoritas**, pulsa **«Nombres (.txt)»** o **«Hoja de cálculo (.csv)»**. El plugin acepta los dos y el resultado es idéntico: de la hoja de cálculo solo lee la primera columna, la del nombre de archivo.

### 2. Ábrela desde Lightroom

**Biblioteca → Complementos → «Importar selección de Positiva…»**. Se abre un cuadro de diálogo titulado **«Selección de Positiva»** que solo muestra archivos `.txt` y `.csv`. Elige el que acabas de descargar y pulsa **«Importar»**.

### 3. Espera al recuento

El plugin recorre **todo tu catálogo** comparando nombres. Mientras lo hace muestra la barra **«Positiva: buscando N fotos en el catálogo…»**, que puedes cancelar. El tiempo depende del tamaño del catálogo, no de lo larga que sea la selección.

### 4. Decide si además pones la bandera

Al terminar aparece el resumen:

> Colección «Positiva > ‹nombre›» lista: 42 fotos añadidas (42 de 42 nombres de la lista).
>
> ¿Quieres marcarlas también con la bandera de seleccionada?

Con **«Sí, poner bandera»** el plugin marca además cada fotografía con la bandera de seleccionada de Lightroom. Con **«No, solo la colección»** deja el catálogo como estaba salvo por la colección.

## Resultado

En el panel de colecciones aparece un conjunto llamado **Positiva** y, dentro, una colección con **el nombre del archivo que has abierto**, sin su extensión. Como el panel exporta con el nombre de la galería, queda algo como `Positiva > boda-ana-y-luis-seleccion`.

Es una colección normal, no una colección inteligente: no se actualiza sola.

:::truco El nombre de la colección lo decide el nombre del archivo
No hay ningún campo para escribirlo. Si quieres que la colección se llame de otra manera, renombra el `.txt` antes de abrirlo con el plugin.
:::

## Notas de uso

### Qué escribe y qué no

El plugin crea la colección y, si lo aceptas, pone la bandera de seleccionada. **No pone estrellas ni etiquetas de color**, y **no toca ningún archivo de tu disco**: todo lo que hace vive dentro del catálogo.

De la hoja de cálculo ignora la columna con el número de favoritos. Para el plugin, el `.txt` y el `.csv` son equivalentes.

### Los nombres que no encuentra

El resumen los lista debajo, ordenados alfabéticamente y con el recuento. Si son más de quince, muestra los quince primeros y una línea con cuántos quedan.

Si no encuentra ninguno, no llega a crear nada y avisa:

> Ninguna de las N fotos de la lista está en este catálogo.
>
> La búsqueda es por nombre de archivo: comprueba que has importado los originales (con su nombre original) en este catálogo.

### Un mismo nombre en varias carpetas

El plugin busca en el catálogo entero y no se puede acotar a una carpeta ni a una selección. Si el mismo nombre existe en varios sitios, **añade todas las coincidencias** y lo dice en el resumen: «Algún nombre existe en más de una carpeta del catálogo: se han añadido todas las coincidencias.»

### Si lo ejecutas dos veces

Con el mismo archivo, reutiliza la colección existente y vuelve a añadir las fotografías. **La colección acumula: no se sincroniza.** Una fotografía que tu cliente haya desmarcado después sigue dentro, y la bandera tampoco se retira sola.

Ten en cuenta además que si descargas la lista por segunda vez, el sistema suele guardarla como `‹nombre› (1).txt`. Ese nombre distinto crea **una colección nueva** dentro del mismo conjunto Positiva, en lugar de reutilizar la anterior.

### Los vídeos de la selección

Si tu cliente ha marcado vídeos, sus nombres viajan también en la exportación y aparecerán entre los no encontrados si no están en tu catálogo de Lightroom. No es un fallo.

### Las favoritas sin nombre de archivo guardado

El paso **Favoritas** avisa cuando hay marcas de las que no se conserva el nombre del archivo original. Esas no entran en ninguna exportación, así que el recuento del plugin puede no coincidir con el número de favoritas del panel. Consulta [Las favoritas de tu cliente y cómo exportarlas](/soporte/es/favoritas-del-cliente/).

<!-- DUDA: ¿el plugin funciona en Windows? El código Lua no usa nada específico de macOS, pero la única ruta de instalación documentada es la de macOS. Confirmar y, si funciona, añadir la ruta equivalente de Windows al paso 2. -->

## Problemas frecuentes

- **«Ninguna de las N fotos de la lista está en este catálogo.»** Casi siempre es la extensión. Comprueba que las piezas del catálogo se llaman exactamente igual que las que subiste a Positiva, extensión incluida.

- **«El archivo está vacío o no se pudo leer.»** El archivo elegido no tiene contenido legible. Vuelve a exportarlo desde el paso **Favoritas**.

- **«No se encontró ningún nombre de archivo en la lista.»** El archivo se ha leído pero no contiene nombres. Comprueba que has elegido el `.txt` o el `.csv` de la selección y no otro archivo.

- **«Error inesperado del plugin: …»** La operación no ha llegado a completarse. Vuelve a intentarlo; si se repite, anota el texto completo del mensaje antes de escribir a soporte.

- **La entrada del menú no aparece.** Comprueba en **Archivo → Gestor de plugins** que Positiva figura en la lista y está habilitado. Si la carpeta `positiva.lrplugin` se ha movido o se ha borrado, Lightroom la marca como no encontrada.

- **La colección aparece con menos fotografías de las que marcó el cliente.** Compara el recuento del resumen con el del paso **Favoritas** y revisa la lista de no encontrados: ahí está la diferencia.

:::truco Salir del paso sin instalar nada
Si necesitas la selección una sola vez, abre el `.txt` y pon todos los nombres en una línea separados por espacios. En Lightroom Classic, con la barra de filtros abierta (tecla `\`), ve a **Texto → Nombre de archivo → Contiene** y pega la línea: aparecen todas las de la lista. Selecciónalas y arrástralas a una colección.

Tiene un límite práctico: con selecciones largas el campo se atasca, así que hay que pegar por tandas de cincuenta o cien nombres. El plugin no tiene ese límite.
:::

## Si el problema continúa

Reúne estos datos antes de escribir a soporte:

- El nombre de la galería y el número de favoritas que muestra el paso **Favoritas**.
- Tu versión de Lightroom Classic y tu sistema operativo.
- El texto completo del resumen o del error que muestra el plugin.
- Un ejemplo de nombre de archivo tal y como aparece en el `.txt` y tal y como aparece en tu catálogo.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
