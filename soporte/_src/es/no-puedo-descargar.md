---
titulo: El cliente no puede descargar los archivos
descripcion: Tu cliente ve la galería pero no encuentra ningún botón de descarga: la causa está casi siempre en la calidad con la que se creó el enlace que abrió.
categoria: problemas
audiencia: fotografo
orden: 20
actualizado: 31 de agosto de 2026
relacionados: [permisos-de-descarga, zip-descarga-completa, enlace-de-cliente]
---

Tu cliente entra en la galería, ve las fotografías y no encuentra la forma de descargarlas, o solo consigue descargar una parte de lo que esperaba.

En la mayoría de los casos no hay ningún fallo: la galería se comporta según los permisos del enlace que tu cliente está utilizando. La descarga la gobierna un único ajuste, **«Calidad de descarga»**, que se fija al crear cada enlace.

Si tu cliente no llega siquiera a ver la galería, el problema es otro. Consulta [«Este enlace no es válido o ha caducado»](/soporte/es/enlace-no-valido/).

## Comprobaciones, en orden

### 1. La calidad de descarga del enlace

**Qué mirar.** El paso **Compartir** de la galería, en la tarjeta del enlace que le enviaste a tu cliente. La calidad está en la zona de permisos, bajo el rótulo **«Descarga:»**.

**Qué debería verse.** **«Web»** o **«Alta (web + original)»**, según lo que quieras entregar.

**Qué hacer si no es así.** Si el desplegable indica **«Ninguna (solo ver)»**, ahí está la explicación: tu cliente ve la galería completa y no puede descargar nada. Es el valor con el que nace todo enlace nuevo, porque es el que trae el formulario de creación por defecto.

Cámbialo ahí mismo: el desplegable guarda al elegir y el enlace sigue siendo el mismo. Consulta [Qué puede descargar tu cliente](/soporte/es/permisos-de-descarga/).

:::aviso Tu cliente no verá el cambio hasta que recargue
El panel lo advierte bajo la lista de enlaces: quien tenga la galería abierta seguirá viendo los botones de antes. Pídele que recargue la página antes de dar por hecho que el cambio no ha funcionado.
:::

:::nota Tu cliente no ve botones de descarga desactivados
Un botón que no puede funcionar no se dibuja. Con **«Ninguna (solo ver)»** no aparece un botón en gris que invite a pulsarlo: no hay botón. Que tu cliente diga que no ve absolutamente nada encaja con esta causa, no la descarta.
:::

### 2. El enlace que tu cliente ha abierto

**Qué mirar.** Cuántos enlaces tiene esa galería en el paso **Compartir**, y cuál de ellos abrió tu cliente. Pídele que te reenvíe la dirección que está utilizando.

**Qué debería verse.** Que el enlace comprobado en el punto anterior es exactamente el mismo que él tiene.

**Qué hacer si no es así.** La calidad de descarga va **por enlace**, no por galería: dos enlaces de la misma galería pueden entregar permisos distintos. Comprueba la tarjeta del enlace que tu cliente abrió de verdad y aplícale la comprobación 1. Consulta [Cómo crear el enlace para tu cliente](/soporte/es/enlace-de-cliente/).

:::nota Si lo que falta es solo el botón de descargar las favoritas
Ese botón depende además del permiso **«Favoritas:»** del enlace. Con las favoritas apagadas desaparece, aunque la calidad de descarga sea **«Web»** o **«Alta (web + original)»**. Consulta [Las favoritas de tu cliente y cómo exportarlas](/soporte/es/favoritas-del-cliente/).
:::

### 3. El archivo ZIP de descarga completa

**Qué mirar.** La sección «Descarga completa» del paso **Compartir**.

**Qué debería verse.** Un archivo ZIP subido, si lo que falta a tu cliente es únicamente el botón **«Descargar todo»**.

**Qué hacer si no es así.** Cuando tu cliente descarga fotografías sueltas pero no encuentra la descarga en bloque, el permiso del enlace es correcto y lo que falta es el ZIP. Ese archivo lo subes tú a mano, en **Compartir** → «Descarga completa» → **«Subir zip»**. Mientras no exista, el botón **«Descargar todo»** no aparece en la galería. Consulta [El botón «Descargar todo» y el archivo ZIP](/soporte/es/zip-descarga-completa/).

### 4. La diferencia entre «Web» y «Alta (web + original)»

**Qué mirar.** De nuevo la calidad de la fila de ese enlace, cuando tu cliente sí descarga archivos pero afirma que no son los originales.

**Qué debería verse.** **«Alta (web + original)»**, si tu cliente tiene que llevarse los archivos tal y como los subiste.

**Qué hacer si no es así.** El enlace está en **«Web»**, el permiso intermedio: entrega la versión comprimida, la misma que se ve dentro de la galería. Para entregar los originales hay que crear un enlace nuevo en **«Alta (web + original)»** y enviar ese, porque el permiso del enlace que ya tiene no se puede modificar.

### 5. Lo que no se descarga es un vídeo

**Qué mirar.** Otra vez la calidad de la fila de ese enlace, cuando tu cliente descarga las fotografías sin problema pero no encuentra cómo descargar los vídeos.

**Qué debería verse.** **«Alta (web + original)»**, que es la única calidad que permite descargar vídeo.

**Qué hacer si no es así.** Con **«Web»**, los vídeos se reproducen dentro de la galería pero no se pueden descargar: esa calidad habilita la descarga solo de las fotografías. No es un fallo del archivo ni del navegador. Para que tu cliente pueda llevarse el vídeo, crea un enlace nuevo en **«Alta (web + original)»** y envía ese.

### 6. La descarga de las fotografías marcadas

**Qué mirar.** Si lo que tu cliente no encuentra es cómo descargar solo su selección. Ese botón no está en el paso **Compartir**, sino dentro del visor: se llama **«Descargar marcadas»** en una galería de revisión y **«Descargar favoritas»** en una de entrega, y solo aparece cuando hay fotografías marcadas.

**Qué debería verse.** El botón, y al pulsarlo una ventana con la resolución, **«Elegir carpeta y guardar ahí»** y **«O descargar como archivos sueltos»**.

**Qué hacer si no es así.** Cada síntoma tiene una causa distinta:

- **No aparece el botón.** El enlace es de calidad **«Ninguna (solo ver)»**, que omite el bloque entero aunque haya fotografías marcadas.
- **Aparece, pero sin la opción Alta.** El enlace es de calidad **«Web»**: el selector de resolución solo ofrece **Alta** en los enlaces de calidad alta.
- **La descarga se detiene a media selección.** Es el navegador pidiendo permiso para bajar varios archivos seguidos, algo que la ventana avisa a partir de más de diez fotografías. Basta con aceptarlo una vez, y con la descarga a carpeta no llega a pedirse.

Consulta [Qué puede descargar tu cliente](/soporte/es/permisos-de-descarga/).

## Qué dice tu cliente y dónde mirar

| Lo que te dice tu cliente | Dónde mirar |
|---|---|
| «No hay ningún botón de descarga» | La calidad de descarga de **ese** enlace |
| «Yo abrí el enlace que me mandaste» | Cuál de los enlaces de la galería está usando |
| «No puedo bajarlo todo junto» | Si el archivo ZIP está subido |
| «Lo que me bajo no es el original» | El enlace está en **«Web»**; crea otro en **«Alta (web + original)»** |
| «Las fotos sí, pero el vídeo no me deja» | El enlace está en **«Web»**; solo **«Alta (web + original)»** permite descargar vídeo |
| «No encuentro dónde bajarme mi selección» | El botón está en el visor, y desaparece con **«Ninguna (solo ver)»** |

## Si el problema continúa

Reúne estos datos antes de escribir a soporte:

- El nombre de la galería y la dirección del enlace que está usando tu cliente.
- El texto **«· descarga: …»** que muestra la fila de ese enlace.
- Si el archivo ZIP está subido, en caso de que lo que falte sea **«Descargar todo»**.
- Qué ve tu cliente exactamente, y desde qué dispositivo y navegador abre la galería.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
