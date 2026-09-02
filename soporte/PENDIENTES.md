# Soporte · lo que falta

Generado por `node soporte/build.mjs`. No lo edites a mano: sale del frontmatter
de cada artículo (`estado:` y `motivo:`).

- **pendiente** → el artículo NO se publica. Solo existe el archivo con su ficha.
- **borrador** → el artículo SÍ se publica, con una banda de "En obra" encima.

## Por escribir (4)

Requieren criterio tuyo, un vídeo, o una decisión que el código no responde.

- [ ] **Facturas y datos fiscales** `es/facturacion.md` — Requiere el detalle real de Cuéntica, la numeración de facturas y el trato del IVA intracomunitario, que no está en el código.
- [ ] **Los datos de tus clientes y el RGPD** `es/datos-de-tus-clientes.md` — Requiere criterio legal, no técnico. Está pendiente la revisión de abogado de la Política de Privacidad, el DPA y las T&C, y este artículo tiene que ser coherente con esos textos, no adelantarlos. Añadido el 31/08 un punto nuevo al guion: la aplicación envía errores del navegador a Sentry, un tercero, y eso entra en el texto legal.
- [ ] **Qué ocurre si tu plan deja de estar activo** `es/dejar-de-pagar.md` — Decisión comercial pendiente. El código no dice qué pasa al vencer un plan con más datos de los que caben en la cuota nueva.
- [ ] **Copias de seguridad de tu material** `es/copias-de-seguridad.md` — La función de backup está en diseño, sin construir. Hasta que exista, el artículo tiene que decir qué se puede prometer hoy sobre durabilidad y retención.

## Publicados con aviso de "en obra" (2)

Documentan algo que está cambiando. Revisar cuando el frente se cierre.

- [ ] **Tu web pública en Positiva** `es/perfil-publico.md` — Todo estudio dispone de una web pública en su subdominio, con cuatro páginas y cuatro diseños, y un interruptor que no afecta a las galerías.
- [ ] **El portfolio de tu web pública** `es/portfolio.md` — El portfolio es la selección de fotografías y vídeos que alimenta tu web pública y se monta con material de tus propias galerías.

## Dudas anotadas en los artículos (6)

Preguntas que quedaron abiertas al escribir. Vienen de los comentarios HTML del
Markdown, que **no** se publican. Resuélvela, borra el comentario del archivo y
vuelve a generar.

### `es/crear-una-galeria.md`

- cuando falla la creación con «No se pudo crear la galería.», ¿queda algo creado a medias en el listado, o no se crea nada? Lo he escrito de forma que el fotógrafo lo compruebe él, pero si nunca queda nada, esa comprobación sobra y se puede decir «vuelve a pulsar y ya».

### `es/los-pasos-de-una-galeria.md`

- en el paso Datos sabemos qué falta para marcarlo como hecho (la fecha). ¿Qué condición marca como hecho cada uno de los demás pasos? Sería útil ponerlo en una tabla.

### `es/activa-o-publica.md`

- cuando se cierre el acceso del enlace privado a una galería desactivada (Rodrigo lo apuntó el 31/08), hay que reescribir el bloque «Desactivar no cierra los enlaces» y la fila «Al apagarla» de la tabla, y revisar también caducidad-de-galeria.

### `es/caducidad-de-galeria.md`

- cuando se cierre el acceso del enlace privado a una galería desactivada (Rodrigo lo apuntó el 31/08), este bloque pasa de :::aviso a :::nota y se reescribe el primer párrafo. También habrá que revisar el texto de los dos correos y el diálogo de confirmación del panel, que hoy ya afirman que el cliente deja de poder entrar.

### `es/importar-favoritas-en-lightroom.md`

- ¿el plugin funciona en Windows? El código Lua no usa nada específico de macOS, pero la única ruta de instalación documentada es la de macOS. Confirmar y, si funciona, añadir la ruta equivalente de Windows al paso 2.

### `es/borrar-una-galeria.md`

- si el borrado se corta a la mitad, ¿basta con volver a pulsar «Borrar galería» para terminar el trabajo, o queda algo colgando que haya que limpiar desde soporte? El brief solo dice que no hay reanudación automática.
