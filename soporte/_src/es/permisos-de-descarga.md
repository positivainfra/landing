---
titulo: Qué puede descargar tu cliente
descripcion: La calidad de descarga se decide en cada enlace y determina si tu cliente solo puede ver el material, descargarlo o llevarse los originales.
categoria: compartir
audiencia: fotografo
orden: 30
actualizado: 31 de agosto de 2026
relacionados: [enlace-de-cliente, zip-descarga-completa, no-puedo-descargar]
---

Lo que tu cliente puede llevarse de una galería lo determina un único ajuste: el selector **«Calidad de descarga»**. Ofrece tres valores —**«Ninguna (solo ver)»**, **«Web»** y **«Alta (web + original)»**— y se aplica **por enlace**, no por galería, de modo que dos enlaces de la misma galería pueden entregar permisos distintos.

## Cómo se elige

Hay dos sitios, los dos en el paso **Compartir** de la galería:

- **Al crear el enlace**, en el selector **«Calidad de descarga»** del formulario **«Crear un enlace»**.
- **Después**, en la tarjeta de ese enlace, en la zona de permisos, bajo el rótulo **«Descarga:»**. Es un desplegable con los mismos tres valores y **guarda al elegir**, sin botón de confirmación.

:::aviso Todo enlace nuevo nace en «Ninguna (solo ver)»
Es el valor con el que aparece el formulario y la causa más frecuente de que un cliente comunique que no puede descargar nada. Si la entrega debe poder descargarse, cambia el selector **antes** de pulsar **«Crear enlace»**, o corrígelo después desde la tarjeta.
:::

:::nota Cambiar la calidad no obliga a repartir un enlace nuevo
El enlace es el mismo y su dirección no cambia. Lo que sí conviene saber es cuándo se nota: **un cliente que tenga la galería abierta seguirá viendo los botones de antes hasta que recargue**, y una descarga que ya hubiera empezado termina. El propio panel lo advierte debajo de la lista de enlaces.

Si el cambio se ha hecho para *retirar* un permiso y el asunto es delicado, no basta con bajar la calidad: [revoca el enlace](/soporte/es/revocar-un-enlace/) y reparte uno nuevo.
:::

:::nota En un enlace revocado no se puede cambiar nada
La zona de permisos de un enlace revocado se convierte en texto de solo lectura: la calidad, las favoritas y la contraseña se leen, pero ya no hay desplegables. Un enlace **caducado** sí los conserva, aunque cambiarlos no sirva de nada mientras no abra.
:::

Si el cambio falla, el desplegable vuelve solo al valor anterior y aparece el aviso **«No se pudo cambiar la calidad de descarga.»** En ese caso el permiso sigue siendo el de antes.

## Qué implica cada opción

| Opción | Fotografías | Vídeos |
|---|---|---|
| **«Ninguna (solo ver)»** | Nada. No aparece ningún botón de descarga. | Nada. |
| **«Web»** | La versión comprimida, la misma que se muestra en la galería. | **No se pueden descargar.** |
| **«Alta (web + original)»** | Las dos versiones, incluido el archivo original tal y como lo subiste. | El archivo tal y como lo subiste. |

:::aviso Con «Web» los vídeos no se pueden descargar
La calidad **«Web»** habilita la descarga únicamente de las fotografías. **«Alta (web + original)»** es la única opción que permite descargar vídeo, y lo entrega tal y como lo subiste, sin versión comprimida intermedia.

Si la entrega incluye vídeo que tu cliente debe conservar, **«Alta (web + original)»** es el valor que necesitas. Con **«Web»**, el vídeo se ve dentro de la galería pero no aparece ningún botón para descargarlo.
:::

## Es el único ajuste que controla la descarga

El resto de la configuración de una galería regula el **acceso**: quién entra y con qué contraseña. La descarga depende solo de este selector.

Dicho al revés: si un enlace está en **«Alta (web + original)»**, cualquiera que disponga de ese enlace y de su contraseña puede descargar los archivos originales. Cuando eso no deba estar al alcance de todos los destinatarios, crea un enlace por grupo, con el permiso que corresponda, y reparte cada uno a quien proceda.

El ajuste gobierna también la descarga completa: el botón **«Descargar todo»** obedece al mismo selector y desaparece con **«Ninguna (solo ver)»**, igual que las descargas sueltas, aunque el archivo ZIP esté subido. Consulta [El botón «Descargar todo» y el archivo ZIP](/soporte/es/zip-descarga-completa/).

## Qué ve tu cliente

Un botón que no puede funcionar no se muestra. Con **«Ninguna (solo ver)»**, tu cliente no ve un botón de descarga desactivado: no ve ningún botón.

Por eso, cuando alguien comunique que en la galería no encuentra dónde descargar, la comprobación no está en la galería sino en la calidad de descarga del enlace concreto que esa persona está utilizando. La lista completa de comprobaciones está en [El cliente no puede descargar los archivos](/soporte/es/no-puedo-descargar/).

## La descarga de las fotografías marcadas

Cuando tu cliente ha marcado fotografías, el visor le ofrece además un botón para descargar solo esa selección: **«Descargar marcadas»** en una galería de revisión y **«Descargar favoritas»** en una de entrega. Al pulsarlo se abre una ventana con las opciones de descarga.

:::nota En una entrega, ese botón solo aparece con el filtro de favoritas puesto
No basta con haber marcado fotografías: tu cliente tiene que estar viendo **solo las favoritas**, con el filtro activado. Con el filtro apagado el botón no se pinta, aunque haya marcas. En una galería de revisión no ocurre: ahí basta con que haya alguna marcada.

Es la explicación de un aviso frecuente: «he marcado mis fotos y no me deja descargarlas solo esas».
:::

- **Resolución.** Un selector con dos valores, **Web** y **Alta**. **Alta** solo aparece si el enlace es de calidad **«Alta (web + original)»**; con un enlace en **«Web»**, el selector entero se omite y la descarga sale en calidad web.
- **Dónde se guarda.** La opción principal es **«Elegir carpeta y guardar ahí»**, que pide una carpeta del ordenador y deja los archivos dentro. Debajo, **«O descargar como archivos sueltos»** los baja uno a uno a la carpeta de descargas habitual. En los navegadores que no admiten elegir carpeta, la única opción es **«Descargar»**, que corresponde a esta segunda vía.
- **Selecciones grandes.** A partir de más de diez fotografías, la ventana avisa de que el navegador puede pedir permiso para descargar varios archivos seguidos. Ese permiso se acepta una sola vez, y con la descarga a carpeta no llega a pedirse.

Este bloque obedece al mismo selector que el resto: con **«Ninguna (solo ver)»** no aparece, aunque tu cliente haya marcado fotografías. Consulta [Las favoritas de tu cliente y cómo exportarlas](/soporte/es/favoritas-del-cliente/).

:::aviso Apagar las favoritas de un enlace también retira esta descarga
El enlace tiene un segundo permiso, **«Favoritas:»**, que decide si tu cliente puede marcar. Si lo pones en **«No»**, desaparecen el corazón, el contador, el filtro **«Favoritas»** y **también este botón de descarga por lote**, aunque la calidad siga en **«Web»** o en **«Alta (web + original)»**.

Las descargas sueltas y el botón **«Descargar todo»** no se ven afectados.
:::

## Un reparto con dos enlaces

Una boda entregada con dos enlaces de la misma galería:

- **La pareja**, con un enlace en **«Alta (web + original)»**: reciben los archivos tal y como salieron de tu exportación.
- **La familia**, con un enlace en **«Web»**: ven la galería completa y descargan lo que quieran en la versión comprimida, suficiente para el móvil o para redes sociales.

Cada enlace lleva su propia contraseña, y desde ninguno de los dos se aprecia qué permisos tiene el otro.
