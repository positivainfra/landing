---
titulo: «Este enlace no es válido o ha caducado»
descripcion: El aviso «Este enlace no es válido o ha caducado» corresponde a tres situaciones distintas y la pantalla no indica cuál de ellas es la que se ha producido.
categoria: problemas
audiencia: ambos
orden: 10
actualizado: 31 de agosto de 2026
relacionados: [enlace-de-cliente, revocar-un-enlace, contrasena-del-enlace]
---

Quien intenta abrir la galería encuentra una pantalla con este texto y nada más:

> Este enlace no es válido o ha caducado. Pídele uno nuevo a tu fotógrafo.

Detrás de esa frase hay **tres situaciones distintas**, y la pantalla no distingue entre ellas:

- El enlace **no existe**: una errata en la dirección, o un carácter que se perdió al copiarla.
- El fotógrafo **lo ha revocado**.
- El propio enlace tenía **fecha de caducidad** y ya ha pasado.

La ambigüedad es deliberada. Quien tiene un enlace equivocado no debería poder averiguar si esa galería existe o no.

:::nota Hay un segundo mensaje, parecido pero distinto
**«Esta galería no está disponible.»**, precedido del rótulo **«Vaya»**, aparece al abrir una galería desde la **web pública del estudio** cuando esa galería está desactivada o ha caducado. No lo produce nunca un enlace de cliente. Consulta [Cómo poner fecha de caducidad a una galería](/soporte/es/caducidad-de-galeria/).
:::

:::nota La pantalla que pide contraseña es otra
Si el enlace se abre y lo que aparece es una petición de contraseña, no estás en este caso: estás en la pantalla **«Galería privada»**, y lo que falta es la contraseña. Consulta [La contraseña del enlace de cliente](/soporte/es/contrasena-del-enlace/).
:::

## Comprobaciones, en orden

### 1. El enlace ha llegado completo

Esta comprobación la hace quien recibió el enlace.

**Qué mirar.** La dirección completa en la barra del navegador, comparada con la del mensaje original.

**Qué debería verse.** La dirección entera, tal y como la envió el fotógrafo, sin caracteres de menos al final.

**Qué hacer si no es así.** Vuelve al mensaje original y abre el enlace desde ahí, en lugar de copiarlo y pegarlo. Los enlaces se truncan con facilidad al pasarlos de una aplicación a otra: al reenviar un mensaje, al copiarlo de un correo o al pegarlo en una nota. Si aun así no funciona, pídele el enlace de nuevo a tu fotógrafo: es la vía más rápida y resuelve la mayoría de los casos.

:::aviso Una página en blanco o cargando de forma indefinida no es este mensaje
Si la pantalla no llega a mostrar el aviso de enlace no válido, sino que se queda en blanco o cargando, lo más probable es que el enlace haya llegado truncado. Ábrelo desde el mensaje original.
:::

### 2. El estado del enlace en el panel

Esta comprobación y la siguiente las hace el fotógrafo.

**Qué mirar.** La lista de enlaces del paso **Compartir** de esa galería.

**Qué debería verse.** El enlace que repartiste, con su estado en activo.

**Qué hacer si no es así.** La lista indica el estado real de cada enlace: activo, **Revocado** o **Caducado**. Un enlace revocado no se puede recuperar: hay que [crear uno nuevo](/soporte/es/enlace-de-cliente/) y volver a repartirlo. Consulta [Cómo revocar un enlace de cliente](/soporte/es/revocar-un-enlace/).

### 3. La dirección corresponde a un enlace y no a la web pública

**Qué mirar.** La forma de la dirección que está abriendo tu cliente.

**Qué debería verse.** Un enlace de cliente, con la forma `https://tuestudio.positiva.studio/g/…`.

**Qué hacer si no es así.** Si la dirección apunta a la galería publicada en tu web pública y no a un enlace de cliente, el mensaje que verá tu cliente no es este sino **«Esta galería no está disponible.»**, y la causa es que la galería está desactivada o ha caducado. Vuelve a activarla desde la cabecera y comprueba su fecha de caducidad. Consulta [Diferencia entre galería activa y galería pública](/soporte/es/activa-o-publica/).

## Los otros mensajes de esa pantalla

| Mensaje | Qué significa |
|---|---|
| «Demasiados intentos. Espera unos minutos y vuelve a probar.» | Se han introducido demasiadas contraseñas incorrectas seguidas. No hay que hacer nada: el bloqueo se levanta solo pasados unos minutos. |
| «No se pudo conectar. Inténtalo de nuevo.» | Un problema de red en el dispositivo que abre la galería, no un problema del enlace. |
| «Contraseña incorrecta.» | La contraseña introducida no es la del enlace. Una contraseña no se puede recuperar: el fotógrafo tiene que establecer una nueva y comunicarla. Consulta [La contraseña del enlace de cliente](/soporte/es/contrasena-del-enlace/). |

## Un caso que parece un fallo y no lo es

Si eres fotógrafo de Positiva y abres el enlace de **otro** estudio con tu sesión iniciada en el panel, la galería te pedirá la contraseña igual que a cualquier otro visitante.

Es el comportamiento correcto. Tu sesión no te concede ningún privilegio sobre galerías que no son tuyas: tener cuenta en Positiva no te convierte en invitado de las entregas de otros estudios.

## Si el problema continúa

Si eres el cliente, el camino más corto es pedirle al fotógrafo un enlace nuevo. Si eres el fotógrafo y las tres comprobaciones son correctas, reúne estos datos antes de escribir a soporte:

- El nombre de la galería y la dirección completa del enlace afectado.
- El estado que muestra ese enlace en el paso **Compartir**: **«Activo»**, **«Revocado»** o **«Caducado»**.
- Si la galería figura como **Activa** y si tiene fecha de caducidad.
- El texto exacto que ve tu cliente y desde qué dispositivo y navegador lo abre.

Escribe a `hola@positiva.studio`. Respondemos en un plazo de 24 a 48 horas.
