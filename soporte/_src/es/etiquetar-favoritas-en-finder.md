---
titulo: Cómo etiquetar en Finder las favoritas de tu cliente
descripcion: Recorrido completo del script de Finder, con las pantallas de seguridad que macOS muestra la primera vez y cómo superarlas paso a paso.
categoria: revision
audiencia: fotografo
orden: 55
actualizado: 31 de agosto de 2026
relacionados: [favoritas-del-cliente, importar-favoritas-en-lightroom, como-funciona-la-revision]
---

Al terminar este proceso, cada fotografía original que tu cliente ha marcado como favorita tendrá una **etiqueta roja de Finder** en tu propio ordenador. A partir de ahí puedes filtrar por esa etiqueta en el Finder o en tu programa de edición, sin comparar nombres de archivo a mano.

Es el proceso más largo de Positiva y la razón está fuera de nuestra herramienta: el sistema de seguridad de macOS, llamado Gatekeeper, bloquea por defecto cualquier script que no venga firmado por un desarrollador registrado en Apple, y la primera ejecución exige pasar por tres pantallas de seguridad. **Solo hay que hacerlo una vez por script descargado.** Las pantallas están todas documentadas abajo, con captura.

:::truco Si editas en Lightroom Classic, hay un camino más corto
El **plugin de Lightroom** hace lo mismo sin pasar por ninguna pantalla de seguridad de macOS: deja la selección de tu cliente como una colección dentro de tu catálogo. Se instala una sola vez. Consulta [Cómo llevar las favoritas de tu cliente a Lightroom Classic](/soporte/es/importar-favoritas-en-lightroom/).

Este script sigue siendo la vía indicada si trabajas sobre carpetas del Finder, si tu programa de edición no es Lightroom, o si en el catálogo no tienes las mismas piezas que subiste a Positiva: el script busca en la carpeta que tú le indiques, no en un catálogo.
:::

:::nota Solo funciona en macOS
El script utiliza las etiquetas de color del Finder, que no existen en Windows ni en Linux. En esos sistemas, las exportaciones que sí sirven son **«Nombres (.txt)»** y **«Hoja de cálculo (.csv)»**.
:::

## Antes de empezar

- Un Mac, y la carpeta con las fotografías originales localizada en él.
- Los nombres de archivo de los originales deben ser los mismos con los que subiste las fotografías a Positiva. Si los renombraste después de subirlas, el script no las encontrará.
- Permisos de administrador en ese Mac. La primera ejecución los pide, y sin ellos no se puede completar.

## Dónde se hace

Panel → **Galerías** → la galería → paso **Favoritas** → **«Etiquetar en Finder (.zip)»**.

## Pasos

### 1. Descarga el script desde el paso Favoritas

![Paso Favoritas del panel de Positiva, con los tres botones de exportación y las fotografías marcadas por el cliente](finder-01-panel-favoritas.webp "El paso **Favoritas** reúne la selección del cliente. El tercer botón, **«Etiquetar en Finder (.zip)»**, es el que genera el script.")

El archivo se descarga con el nombre de la galería: `<nombre-de-la-galeria>-seleccion.zip`. Pesa unos pocos kilobytes, porque dentro no hay ninguna fotografía: solo una lista de nombres de archivo y las instrucciones para buscarlos.

### 2. Mueve el .zip a la carpeta de los originales

Este paso decide **dónde va a buscar el script**. Al ejecutarse, recorre la carpeta en la que se encuentra y todas sus subcarpetas. Si lo dejas en Descargas, no encontrará nada.

![Ventana del Finder con las fotografías originales y el archivo test-favoritos-seleccion.zip dentro de la misma carpeta](finder-02-zip-en-la-carpeta.webp "El `.zip`, ya movido junto a los originales. Puede haber subcarpetas: la búsqueda es recursiva.")

### 3. Descomprime el .zip con doble clic

Del `.zip` sale un archivo `.command` con el mismo nombre.

![La misma carpeta tras descomprimir, con el archivo .command seleccionado junto al .zip original](finder-03-command-descomprimido.webp "El archivo `.command` ya sale con permiso de ejecución. Descomprimirlo es la razón por la que Positiva entrega un `.zip` y no el script suelto.")

:::nota Por qué se entrega dentro de un .zip
Un navegador nunca marca como ejecutable lo que descarga. Un `.command` descargado directamente fallaría al abrirse y habría que corregirlo desde el Terminal. El formato `.zip` sí conserva los permisos del archivo, y la Utilidad de Archivos de macOS los restaura al descomprimirlo. Por eso este paso no se puede saltar copiando el `.command` de otro sitio.
:::

### 4. Haz doble clic en el .command

La primera vez macOS lo bloquea y muestra este aviso:

> Apple no ha podido verificar que `<nombre-del-script>.command` no contenga software malicioso que pueda dañar tu Mac o comprometer tu privacidad.


![Aviso de macOS que dice que no se ha abierto el archivo porque Apple no ha podido verificar que no contenga software malicioso, con los botones Trasladar a la Papelera y Aceptar](finder-04-bloqueo-gatekeeper.webp "El aviso no ofrece ninguna opción para abrir el archivo. Pulsa **«Aceptar»**: nunca **«Trasladar a la Papelera»**.")

:::aviso Este aviso no se resuelve con clic derecho → Abrir
En versiones anteriores de macOS, el mensaje decía que el archivo procedía de un **desarrollador no identificado** y bastaba con hacer clic derecho sobre él y elegir **Abrir** para saltárselo. Apple retiró ese atajo. En macOS reciente el diálogo solo ofrece **«Trasladar a la Papelera»** y **«Aceptar»**, y la autorización se concede desde los Ajustes del Sistema, como se describe en el paso siguiente.

Si tu Mac te ofrece la opción de abrir con el clic derecho, úsala: estás en una versión anterior y te ahorras los pasos 5 y 6.
:::

### 5. Autoriza el script en Ajustes del Sistema

Abre **Ajustes del Sistema → Privacidad y seguridad** y baja hasta el apartado **Seguridad**. Ahí aparece el script bloqueado, con un botón para autorizarlo.

![Ajustes del Sistema, sección Privacidad y seguridad, con el mensaje de que se ha bloqueado el archivo y el botón Abrir igualmente](finder-05-ajustes-privacidad.webp "Pulsa **«Abrir igualmente»**. El aviso solo aparece aquí durante un rato después del intento de apertura: si no lo ves, vuelve al paso 4 y haz doble clic otra vez.")

macOS pide confirmación una segunda vez. Aquí sí existe la opción de abrir:

![Diálogo de confirmación con tres botones: Trasladar a la Papelera, Abrir igualmente y Aceptar](finder-06-abrir-igualmente.webp "Pulsa **«Abrir igualmente»** de nuevo. Es la última confirmación de esta pantalla.")

Por último, macOS pide la contraseña de administrador o Touch ID:

![Solicitud de contraseña de administración o Touch ID para permitir la apertura](finder-07-permiso-administrador.webp "Autoriza con Touch ID o con tu contraseña de administrador. Es el requisito que hace falta tener permisos de administrador en ese Mac.")

### 6. Concede el permiso de automatización

Al arrancar, el script abre una ventana del Terminal y macOS puede pedir permiso para que **Terminal controle Finder**. Acéptalo: es exactamente la operación que aplica las etiquetas de color.

Este permiso queda registrado en **Ajustes del Sistema → Privacidad y seguridad → Automatización** y no vuelve a solicitarse.

### 7. Lee el resultado en el Terminal

El script recorre la carpeta y va etiquetando. Al terminar imprime un resumen:

```
Listo: 3 archivo(s) etiquetados, 0 no encontrados.
Pulsa Enter para cerrar...
```

Si algún nombre no aparece en la carpeta, lo indica antes del resumen con una línea por archivo: `No encontrado: <nombre>`. Pulsa Enter para cerrar la ventana.

## Resultado

Las fotografías favoritas quedan con un punto rojo junto a su nombre en el Finder.

![Ventana del Finder con las fotografías originales, tres de ellas con un punto rojo de etiqueta](finder-08-etiquetas-aplicadas.webp "Las tres fotografías marcadas por el cliente, ya etiquetadas en rojo. El resto de la carpeta queda intacto.")

Para trabajar con la selección puedes ordenar por etiqueta en el Finder, buscar por etiqueta con **Buscar** o arrastrar la etiqueta desde la barra lateral.

:::nota Ninguna fotografía se modifica
La etiqueta de color es un metadato del Finder. El script no abre, no convierte, no mueve y no borra ningún archivo. Para retirar una etiqueta: clic derecho sobre la fotografía → **Etiquetas** → el círculo gris con la equis.
:::

Una vez aplicadas las etiquetas, el `.zip` y el `.command` ya no hacen falta y puedes borrarlos de la carpeta. Si tu cliente marca más fotografías después, descarga un script nuevo: el que tienes contiene la lista del momento en que lo generaste.

## Cambiar el color de la etiqueta

El script aplica el color rojo. Si prefieres otro, abre el `.command` con cualquier editor de texto y cambia el número de esta línea:

```
LABEL_INDEX=2
```

Los valores válidos van del 1 al 7 y corresponden a los siete colores del menú de etiquetas del Finder. Guarda el archivo y ejecútalo de nuevo.

## Problemas frecuentes

- **El resumen dice «0 archivo(s) etiquetados» y todos aparecen como no encontrados.** El script no está en la carpeta correcta. Muévelo dentro de la carpeta que contiene los originales y ejecútalo otra vez. Comprueba también que no renombraste los archivos después de subirlos a Positiva.

- **En Ajustes del Sistema no aparece el botón «Abrir igualmente».** Ese aviso solo se muestra durante un tiempo limitado después de intentar abrir el archivo. Vuelve a hacer doble clic en el `.command` y regresa de inmediato a **Privacidad y seguridad**.

- **Faltan fotografías que tu cliente sí había marcado.** Comprueba en el paso **Favoritas** el número de favoritas sin nombre de archivo guardado. Esas no entran en ninguna exportación. Consulta [Las favoritas de tu cliente y cómo exportarlas](/soporte/es/favoritas-del-cliente/).

- **Se han etiquetado más archivos de los previstos.** El script etiqueta **todas** las coincidencias de cada nombre, en todas las subcarpetas. Si dentro de la misma carpeta conviven los originales y una copia de trabajo con los mismos nombres, quedan marcadas las dos versiones.

- **El aviso de seguridad vuelve a aparecer con un script nuevo.** Es lo previsto: la autorización se concede a ese archivo concreto, no al conjunto. Cada script descargado pasa por los pasos 4 y 5 una vez. El permiso de automatización del paso 6, en cambio, se concede una sola vez y ya no se repite.

## Si el problema continúa

Reúne estos datos antes de escribir a soporte:

- El nombre de la galería y el número de favoritas que muestra el paso **Favoritas**.
- La versión de macOS de tu equipo (menú Apple → **Acerca de este Mac**).
- El texto exacto que muestra la ventana del Terminal, incluido el resumen final.
- Si el script llegó a ejecutarse o se quedó bloqueado en alguna de las pantallas de seguridad.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
