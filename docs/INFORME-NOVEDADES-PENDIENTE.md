# Informe de impacto · lote 2a59b6c → 783e41b (desplegado a 17/10/2026)

627 commits en main. Publicadas **27 entradas** en `/novedades/` (6 de septiembre y 21 de octubre),
con la fecha del merge a main como fecha de despliegue.

Esta vez, por petición expresa de Rodrigo, el soporte **sí se ha editado desde este flujo**:
12 artículos nuevos, unos 40 revisados, y la categoría nueva «Archivos y solicitudes» (05).
El índice, los raíles, las migas, el buscador y las tarjetas «Seguir leyendo» salen ahora de
`scripts/soporte-indice.py` (fuente única del orden de categorías y artículos).

Artículos nuevos: archivos-y-carpetas, que-ve-quien-recibe-tu-enlace, seleccionar-varios-archivos,
borrar-y-archivar-archivos, pedir-archivos, subir-a-una-solicitud, archivos-recibidos,
crear-galeria-desde-archivos, versiones-de-un-video, comparar-versiones,
revisor-idioma-de-la-galeria, idioma-del-panel. `compartir-un-archivo-suelto` se reescribe como
«Cómo compartir un archivo o una carpeta» (misma URL) y pasa a Archivos y solicitudes.

Corregido en la landing: /archivos/ decía que las solicitudes llevan «contraseña opcional».
No la llevan (el código no la tiene); sí la llevan los enlaces de lo que compartes.

## Posible bug de la app (para Claude Code en SHOWCASEBRAIN)

- Crear galería desde Archivos con el plan Gratis al límite: el diálogo probablemente muestra
  el código crudo «limite_de_galerias» (`DialogoCrearGaleria.tsx` imprime `err.message` en vez
  del texto traducido de `createGallery` en `data.ts`). El artículo no cita el mensaje.

## A verificar en pantalla

Archivos
1. Enlaces `/f/` antiguos: una nota dice que volver a compartir da un enlace nuevo; el código
   reactiva el mismo. El artículo sigue al código y dice que esos enlaces no admiten contraseña.
2. En la vista «Archivados», el botón de lote sigue diciendo «Archivar» aunque restaura.
3. Lo archivado dentro de una carpeta compartida puede seguir visible por su enlace.
4. Renombrar una carpeta compartida quizá no cambia el nombre que ve quien la recibe.
5. Si el plan Gratis tiene Archivos (los artículos dicen «en los demás planes» sin concretar).
6. La tarjeta genérica de vista previa para estudios con marca blanca.

Solicitudes
7. El contador de la pestaña «Solicitudes» es por navegador (lo dice el artículo).
8. Qué ve quien está subiendo cuando cierras la solicitud.
9. Días tras los que una subida a medias empieza de cero (el artículo dice «varios días»).
10. «Esta solicitud no acepta archivos ahora mismo»: según el código sale cuando el plan ya no
    incluye solicitudes; el artículo para quien sube lo explica como que la cuenta no puede recibir.

Panel y galerías
11. activa-o-publica habla de galerías archivadas «por inactividad»; el código bloquea el
    interruptor para el estado que el panel llama «Desactivada». ¿Es lo mismo?
12. Una galería nueva sigue Branding «mientras no le cambies el tema»: confirmar que tocar un
    campo del tema fija el resto.

Subida y versiones
13. Desde el 05/10 la cola solo muestra errores conocidos o «Error de subida»: confirmar con un
    HEIC y con la cuota llena.
14. Que «Previsualizar» abre la galería en modo fotógrafo (donde salen «Comparar» y liberar versión).
15. subir-fotos-y-videos pone los partidos de fútbol como ejemplo de bloqueo de operadoras:
    quitarlo si no se quiere decir en público.

Revisión
16. El filtro «Abiertos / Todos / Resueltos» también en la revisión de fotos, y el punto atenuado
    del comentario resuelto.
17. El selector ES / EN oculto en la cabecera de la revisión de vídeo en móvil.

Diseño y marca
18. Selector S/M/L debajo de portada y cuadrícula; aviso de «Limpiar títulos» al abrir la galería;
    galerías anteriores al 15/10 con Playfair Display e Inter.

Cuenta
19. La barra de almacenamiento en «Cuenta y facturación» en todos los planes, y la casilla del
    correo diario de descargas en Gratis (en el código no hay filtro de plan en la casilla).
20. «un enlace corto» en la intro de «Descargas sueltas»: no está claro a qué se refiere.

Pendiente fuera de este lote: la tanda 2 de octubre (cliente, avisos y aprobaciones) no está en main.
