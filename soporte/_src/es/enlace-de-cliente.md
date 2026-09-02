---
titulo: Cómo crear el enlace para tu cliente
descripcion: El enlace de cliente se crea en el paso Compartir de la galería y lleva sus propios permisos de descarga, de favoritas y su contraseña.
categoria: compartir
audiencia: fotografo
orden: 10
actualizado: 31 de agosto de 2026
relacionados: [contrasena-del-enlace, permisos-de-descarga, revocar-un-enlace]
---

Al terminar este proceso tendrás una dirección privada, servida desde tu propio dominio, que tu cliente puede abrir en cualquier navegador sin crear una cuenta ni instalar nada. Una misma galería admite tantos enlaces como necesites, cada uno con su contraseña y sus propios permisos.

## Antes de empezar

- La galería debe estar creada. El contenido no tiene que estar completo: puedes crear el enlace mientras la subida continúa.
- Decide qué debe poder descargar quien reciba este enlace y si debe poder marcar favoritas. Los dos permisos se pueden corregir después sin rehacer el enlace.
- Si quieres que el enlace se sirva desde tu dominio propio, configúralo antes de crearlo. Consulta [Cómo usar tu propio dominio](/soporte/es/dominio-propio/).

## Dónde se hace

Panel → **Galerías** → la galería → paso **Compartir** → sección «Enlace de cliente».

## Pasos

El bloque **«Crear un enlace»** está siempre visible al principio de esa sección, con los valores por defecto ya establecidos. Se rellena de arriba abajo y **«Crear enlace»** es el botón que lo cierra.

1. Revisa el texto final de la dirección en el campo **«Cadena de texto»**. Positiva lo deriva del nombre de la galería, en minúsculas y sin acentos, y puedes editarlo mientras el enlace no esté creado. Debajo, **«El enlace será»** muestra la dirección resultante.
2. Selecciona la **«Calidad de descarga»**. El valor por defecto es **«Ninguna (solo ver)»**; las otras dos opciones son **«Web»** y **«Alta (web + original)»**. Consulta [Qué puede descargar tu cliente](/soporte/es/permisos-de-descarga/).
3. Decide si dejas marcada la casilla **«Permitir marcar favoritas»**, que aparece marcada por defecto. Apagarla retira de ese enlace los corazones, el contador y el filtro de favoritas. Consulta [Las favoritas de tu cliente y cómo exportarlas](/soporte/es/favoritas-del-cliente/).
4. Mantén marcada la casilla **«Proteger con contraseña»**, que aparece marcada por defecto, y escribe la contraseña. La dirección deriva del nombre de la galería y es previsible, de modo que la contraseña es la credencial que protege el acceso. Consulta [La contraseña del enlace de cliente](/soporte/es/contrasena-del-enlace/).
5. Pulsa **«Crear enlace»**. El enlace se crea en ese momento y aparece en la lista de la sección.
6. Hazlo llegar a tu cliente con **«Copiar»**, o con **«Compartir»** → **«Email»** o **«WhatsApp»**. Ni el correo ni el mensaje de WhatsApp incorporan la contraseña por su cuenta: consulta [Cómo enviar la galería por correo o WhatsApp](/soporte/es/enviar-la-galeria/) antes del envío.

## Resultado

El enlace tiene esta forma:

`https://tuestudio.positiva.studio/g/loquesea`

La primera parte es siempre tuya: tu subdominio, o tu dominio propio si ya está activo. El dominio del panel no aparece nunca en el enlace de un cliente.

## La tarjeta de un enlace

Cada enlace ocupa una tarjeta dividida en tres zonas, de arriba abajo:

| Zona | Qué contiene |
|---|---|
| **Uso diario** | La dirección completa, el botón **«Copiar»** —que pasa a **«Copiado»** durante unos segundos— y el botón **«Compartir»**, que despliega **«Email»** y **«WhatsApp»**. |
| **Permisos** | Tres parejas de rótulo y control: **«Descarga:»**, **«Favoritas:»** y **«Contraseña:»**. Los dos primeros son desplegables que guardan al elegir. El tercero muestra **«••••»** si el enlace tiene contraseña, o **«sin»** si no, con las acciones **«cambiar»**, **«quitar»** o **«añadir»** al lado. |
| **Estado** | La pastilla **«Activo»**, **«Revocado»** o **«Caducado»**, la fecha de creación y, si la tiene, su caducidad. En el extremo opuesto, separado del resto a propósito, el único botón destructivo: **«Revocar»**. |

:::nota En un enlace revocado, los permisos son solo texto
La zona central deja de tener desplegables y se lee como texto plano: **«Descarga: …»**, **«Favoritas: sí»** o **«Favoritas: no»**, y **«Con contraseña»** o **«Sin contraseña»**.

Un enlace **caducado** se comporta de otra manera: conserva sus desplegables y se puede seguir tocando, aunque ya no abra nada. Lo único que pierde, igual que el revocado, es el botón **«Compartir»**.
:::

Bajo la lista de enlaces, el panel recuerda una regla que se aplica a los tres permisos: «Los cambios se aplican al momento. Un cliente que tenga la galería abierta seguirá viendo los botones de antes hasta que recargue, y una descarga que ya hubiera empezado termina.»

## Varios enlaces para la misma galería

Una galería admite tantos enlaces como necesites: no hay límite. Cada uno lleva su propia contraseña y sus propios permisos, de modo que puedes repartir accesos distintos sin duplicar el contenido:

- Un enlace para la pareja, con descarga en **«Alta (web + original)»**.
- Otro para la familia, con descarga en **«Web»**.
- Otro de vista previa, en **«Ninguna (solo ver)»** y con las favoritas apagadas.

Para crear el segundo enlace, cambia el texto final de la dirección.

:::aviso El texto final de la dirección es único en todo Positiva
La restricción no se limita a los enlaces de una misma galería: ese texto no puede coincidir con el de **ningún** otro enlace de Positiva, sea de la galería y del estudio que sea. Como el texto se deriva por defecto del nombre de la galería, dos galerías con el mismo nombre chocan entre sí. Cuando ocurra, edita el texto —añadiendo la fecha o el apellido del cliente, por ejemplo— y vuelve a crear el enlace.
:::

## Cómo se cierra el acceso

El formulario de creación no incluye ningún campo de caducidad: una vez creado, el enlace permanece activo hasta que intervengas. Hay tres formas de cerrarlo:

- **Revocar el enlace**, que es definitivo y afecta solo a ese enlace. Consulta [Cómo revocar un enlace de cliente](/soporte/es/revocar-un-enlace/).
- **Bajar sus permisos** a **«Ninguna (solo ver)»** y **«Favoritas: No»**, que deja la galería visible pero sin nada que llevarse.
- **Desactivar la galería** con la pastilla de su cabecera, o dejar que caduque sola. Consulta [Cómo poner fecha de caducidad a una galería](/soporte/es/caducidad-de-galeria/).

:::aviso Desactivar la galería no revoca sus enlaces
Una galería desactivada desaparece de tu web pública, pero eso es una cosa distinta de cerrar un enlace privado ya repartido. Cuando lo que quieres es que una persona concreta deje de entrar, revoca **su** enlace.
:::

:::aviso «Copiar» sigue funcionando sobre un enlace revocado
Al revocar un enlace desaparece de su tarjeta el botón **«Compartir»**, pero **«Copiar»** permanece y se deja pulsar. Las señales de que ese enlace ya no sirve son su texto tachado y la pastilla **«Revocado»** de la zona de estado. Comprueba la tarjeta antes de copiar: un enlace revocado no abre nada.
:::

## «Previsualizar» no es el enlace de cliente

La cabecera de una galería de revisión incluye además un botón **«Previsualizar»**. Abre la galería desde el dominio del panel, entrando como fotógrafo, para que puedas ver lo que ve tu cliente y responder a sus comentarios. Consulta [Qué es una galería de revisión y cómo funciona](/soporte/es/como-funciona-la-revision/).

:::aviso La dirección que aparece al previsualizar no sirve para tu cliente
Después de pulsar **«Previsualizar»**, la dirección de la barra del navegador es la del panel, no la del enlace de cliente. No la copies desde ahí. Vuelve al paso **Compartir** y usa **«Copiar»** en la tarjeta del enlace.
:::

## Problemas frecuentes

- **«No se pudo crear el enlace.»** La creación no se ha completado y el enlace no existe. Repite la operación; si el mensaje vuelve a aparecer, escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
- **«Ya existe un enlace con ese texto de URL. Cámbialo o revoca el anterior.»** Ese texto final ya está ocupado por otro enlace de Positiva, que no tiene por qué ser de esta galería: la restricción es global. Modifícalo, o revoca el enlace que lo ocupa si es tuyo y ya no lo necesitas.
- **«Escribe la contraseña, o desmarca la casilla para crear un enlace abierto.»** Has dejado marcada la casilla de contraseña sin rellenar el campo. Escribe una, o desmarca la casilla si el enlace debe ser abierto.
- **«Enlace anterior (aleatorio): no se puede recuperar.»** Aparece en galerías con enlaces creados antes del sistema actual, de los que solo se conservó una huella y no la dirección. Positiva no puede mostrarlos, así que no se pueden copiar ni reenviar; sí puedes cambiarles la contraseña o revocarlos. Para volver a enviar esa galería, crea un enlace nuevo.
