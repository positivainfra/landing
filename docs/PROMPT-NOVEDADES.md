# Procedimiento · Novedades e impacto en soporte

Procedimiento para poblar `/novedades/` y detectar impacto en `/soporte/` a partir
de lo desplegado en la aplicación. Lo ejecuta cualquier chat de Claude: el estado
vive en archivos de este repo, no en la memoria de ningún chat.

**Cuándo se ejecuta:** después de un despliegue a producción de la app, cuando
Rodrigo lo pida («desplegado hasta `<hash>`» o simplemente «pasa novedades»).
Nunca de forma autónoma sobre commits sin desplegar.

## Entradas

- Repo de la aplicación: `~/Docs mac/CODE/SHOWCASEBRAIN` (conectar la carpeta si no lo está).
- Repo de la landing (este): `~/Docs mac/CODE/positiva-landing`.
- Marcador: `docs/novedades-estado.txt` — hash del último commit ya procesado.

## Pasos

1. **Rango.** Leer el marcador y ejecutar en SHOWCASEBRAIN:
   `git log --oneline <marcador>..<hash-desplegado>`.
   Si Rodrigo no da hash, preguntar hasta dónde está desplegado. **Regla dura:
   no se publica nada que no esté en producción.**

2. **Clasificar.** Separar visible-para-el-usuario de interno.
   - Visible: cambios de UI, funciones nuevas, textos del panel o de la galería,
     rendimiento que el usuario nota, arreglos de bugs que alguien sufría.
   - Interno (no va a novedades): refactors, tests, tooling, logs, dependencias,
     cambios de infraestructura sin efecto perceptible.
   Ante la duda, leer el diff del commit, no adivinar por el mensaje.

3. **Redactar la entrada** (una por despliegue; si el lote es muy heterogéneo,
   una por tema). Usar la plantilla comentada al inicio de la lista en
   `public/novedades/index.html`. Reglas de tono:
   - Titular corto en una línea, en el registro de la web (directo, sin humo).
   - 2-3 frases sobre **qué cambia para el usuario**, nunca cómo está hecho.
     Sin jerga: nada de workers, RLS, derivadas, caches.
   - Etiquetas permitidas: Web, Vídeo, Revisión, Rendimiento, Seguridad,
     Arreglo, Portfolio, Panel, Producto.
   - Fecha = fecha del despliegue, no del commit.
   La entrada se inserta la primera dentro de su mes (crear `<h2 class="mes">`
   si el mes no existe) y se actualiza el `lastmod` de `/novedades/` en
   `public/sitemap.xml`.

4. **Informe de impacto** — el paso que evita la deriva. Para cada cambio
   visible, listar qué contenido existente puede haber quedado desactualizado:

   | Área del cambio | Artículos de soporte a revisar | Páginas de landing |
   |---|---|---|
   | Enlaces, contraseñas, descargas | enlace-de-cliente, permisos-de-descarga, revocar-un-enlace, contrasena-del-enlace, zip-descarga-completa, no-puedo-descargar | /galerias/ |
   | Subidas y formatos | subir-fotos-y-videos, formatos-admitidos, subida-interrumpida, archivos-que-no-suben, reemplazar-un-archivo, versiones-antiguas | /galerias/ |
   | Diseño de galería, temas, marca | disenos-de-galeria, disenos-de-video, tema-y-tipografia, logo-y-marca, dominio-propio | /diseno-de-galerias/ |
   | Revisión y comentarios | como-funciona-la-revision, rondas-de-revision, revisor-*, comentarios-en-el-panel, quien-ve-los-comentarios, convertir-entrega-revision | /revision-video/, /agencias/ |
   | Vídeo | disenos-de-video, exportar-marcadores-video, revisor-comentar-video | /revision-video/ |
   | Panel y pasos | el-panel-por-dentro, los-pasos-de-una-galeria, crear-una-galeria, crear-tu-primera-galeria, activa-o-publica, enviar-la-galeria | — |
   | Momentos y organización | momentos | /bodas/, /galerias/ |
   | Favoritas y analítica | favoritas-del-cliente, analitica | /galerias/, /agencias/ |
   | Web pública y portfolio | perfil-publico, portfolio | /portfolio/ |
   | Planes, precios, almacenamiento | planes-y-precios, cambiar-de-plan, almacenamiento, ampliar-almacenamiento | /precios/, /freelance/ |

   El informe indica **qué afirmación o literal** hay que verificar, no el texto
   nuevo. Se guarda en `docs/INFORME-NOVEDADES-PENDIENTE.md` (sobrescribiendo el
   anterior una vez atendido).

   **Regla dura:** este flujo NO edita `/soporte/` jamás. Los artículos citan
   literales exactos de la UI y solo se corrigen verificándolos contra el
   producto real — eso lo hace el chat de soporte con su propia metodología,
   a partir de este informe. Las páginas de landing sí pueden corregirse desde
   aquí si el cambio está desplegado y verificado.

5. **Cerrar.** Actualizar `docs/novedades-estado.txt` con el hash procesado y
   commitear (o entregar los archivos a Rodrigo si el chat no tiene git).

## Qué no hacer

- No publicar entradas de cosas sin desplegar «para adelantar».
- No inventar impacto de usuario a partir del mensaje de un commit sin leer el diff.
- No convertir cada commit en una entrada: novedades cuenta despliegues, no historia de git.
- No citar literales de UI que no se hayan visto en pantalla.
