---
titulo: Las favoritas de tu cliente y cómo exportarlas
descripcion: El paso Favoritas reúne la selección de tu cliente y la exporta a tu ordenador: lista de nombres, hoja de cálculo, etiquetas de Finder o colección de Lightroom.
categoria: revision
audiencia: fotografo
orden: 50
actualizado: 31 de agosto de 2026
relacionados: [como-funciona-la-revision, importar-favoritas-en-lightroom, permisos-de-descarga]
---

Al terminar este proceso tendrás en tu ordenador la selección de tu cliente en un formato que puedes usar para editar: una lista de nombres de archivo, una hoja de cálculo, los archivos originales etiquetados por color en el Finder o una colección dentro de tu catálogo de Lightroom Classic.

## Antes de empezar

- **Que tu cliente pueda marcar favoritas depende del enlace por el que entra**, no del tipo de galería. Es un permiso que se decide enlace a enlace y que viene activado de fábrica; está explicado más abajo.
- Para **«Etiquetar en Finder (.zip)»** necesitas macOS, la carpeta con los archivos originales y permisos de administrador en ese equipo.
- Para **«Plugin de Lightroom (.zip)»** necesitas Lightroom Classic y tus originales ya importados en el catálogo.
- Las cuatro exportaciones se generan en tu propio navegador. No se envía nada a ningún servidor.

:::nota El paso Favoritas no muestra nunca la marca de paso completado
No es una tarea tuya: registra el uso que hace tu cliente de la galería, y termina cuando él deja de marcar fotografías.
:::

## Dónde se hace

Panel → **Galerías** → la galería → paso **Favoritas** → sección **Exportar selección**.

## Pasos

1. **Accede al paso Favoritas de la galería.** El panel muestra las fotografías que ha marcado tu cliente y el número de favoritas que no tienen un nombre de archivo guardado.
2. **Comprueba que ese número de favoritas sin nombre de archivo es cero.** Si no lo es, esas fotografías tendrás que localizarlas a mano en la galería, porque no aparecerán en ninguna exportación.
3. **Elige el formato que necesites y pulsa su botón.** Las cuatro opciones son estas:
   - **«Nombres (.txt)»** genera un nombre de archivo por línea, para pegarlo en un buscador o en una lista.
   - **«Hoja de cálculo (.csv)»** genera dos columnas, el nombre de archivo y cuántos revisores distintos lo marcaron. Es la opción útil cuando la galería la revisan varias personas y quieres ver en qué coinciden.
   - **«Etiquetar en Finder (.zip)»** genera un script que etiqueta los originales en tu propio ordenador. Solo funciona en macOS.
   - **«Plugin de Lightroom (.zip)»** descarga el plugin que convierte la selección en una colección de tu catálogo de Lightroom Classic.

## Cuál te conviene

| Si trabajas… | Usa | Por qué |
|---|---|---|
| **En Lightroom Classic** | **«Plugin de Lightroom (.zip)»** | Deja la selección como colección dentro del catálogo. Se instala una vez y no pasa por ninguna pantalla de seguridad del sistema. |
| **Sobre carpetas del Finder, en un Mac** | **«Etiquetar en Finder (.zip)»** | Marca los archivos originales con una etiqueta roja, visible desde cualquier programa. |
| **En Windows, o en cualquier otro programa** | **«Nombres (.txt)»** | Una lista de nombres se pega en el buscador de casi cualquier catalogador. |
| **Con varios revisores y quieres ver coincidencias** | **«Hoja de cálculo (.csv)»** | Añade cuántas personas marcaron cada fotografía. |

Con **«Nombres (.txt)»** y **«Hoja de cálculo (.csv)»** el proceso termina al descargar. Los otros dos tienen su propio artículo:

- [Cómo llevar las favoritas de tu cliente a Lightroom Classic](/soporte/es/importar-favoritas-en-lightroom/)
- [Cómo etiquetar en Finder las favoritas de tu cliente](/soporte/es/etiquetar-favoritas-en-finder/)

## Quién puede marcar favoritas

El permiso vive en el **enlace de cliente**, no en la galería, de modo que dos enlaces de la misma galería pueden comportarse de forma distinta.

- **Al crear el enlace**, en la casilla **«Permitir marcar favoritas»**, que nace marcada. El panel lo explica así: «Apágalo para el enlace que reparte la galería a quien solo va a mirarla: sin corazones, sin contador y sin filtro de favoritas.»
- **Después**, en la tarjeta de ese enlace, bajo el rótulo **«Favoritas:»**, con un desplegable de **«Sí»** y **«No»** que guarda al elegir.

Todos los enlaces creados antes de que existiera este permiso tienen las favoritas **activadas**: nada cambió de comportamiento.

:::nota Qué desaparece exactamente con el permiso apagado
En una galería de **entrega**: el corazón de cada miniatura y el del visor grande, el filtro **«Favoritas»** con su contador y el botón **«Descargar favoritas»**.

En una galería de **revisión**: el punto rojo de marcar en la hoja de contactos y en el visor, el contador **«N / M marcadas»** y el botón **«Descargar marcadas»**.
:::

:::aviso Apagar el permiso no borra las marcas que ya existen
Las favoritas ya marcadas se conservan, se siguen contando en este paso y siguen saliendo en las cuatro exportaciones. Lo que se impide es **marcar más**. Quien ya hubiera marcado puede además seguir **desmarcando**.

Y como todos los permisos del enlace, el cambio no llega a quien tenga la galería abierta hasta que recargue.
:::

## Resultado

Las cuatro exportaciones trabajan con **nombres de archivo, no con imágenes**: ninguna contiene fotografías. Lo que tu cliente puede descargar de la galería es una cuestión distinta, y se decide en el enlace. Consulta [Qué puede descargar tu cliente](/soporte/es/permisos-de-descarga/).

## Las favoritas sin nombre de archivo

:::aviso Las favoritas sin nombre de archivo guardado quedan fuera de las cuatro exportaciones
No existe ningún dato por el que buscarlas, de modo que no se pueden listar, ni etiquetar, ni encontrar en un catálogo. El panel indica cuántas son; si el número no es cero, esas fotografías tendrás que localizarlas a mano en la galería.
:::

## Problemas frecuentes

- **«No se pudo exportar.»** El archivo no ha llegado a generarse. Como todo el trabajo lo realiza tu navegador, la primera medida es volver a pulsar el botón.
- **Faltan fotografías en la exportación.** Comprueba el número de favoritas sin nombre de archivo en el paso **Favoritas**. Esas no salen en ninguno de los cuatro formatos.
- **Tu cliente dice que no ve los corazones.** Comprueba el permiso **«Favoritas:»** del enlace concreto que esa persona está utilizando. Si lo acabas de cambiar, pídele que recargue la página.
- **Los vídeos marcados aparecen en la lista.** Tu cliente puede marcar vídeos, y sus nombres viajan en las exportaciones igual que los de las fotografías. En el Finder y en Lightroom aparecerán como no encontrados si esas piezas no están en la carpeta o en el catálogo.
- **Cualquier problema con el script de Finder o con el plugin.** Sus incidencias propias están recogidas en sus artículos respectivos.
