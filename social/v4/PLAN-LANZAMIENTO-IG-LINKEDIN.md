# Positiva · Plan de lanzamiento en Instagram y LinkedIn

Arranque: **lunes 21 de septiembre de 2026**. Cuatro semanas (21 sep – 16 oct). CTA único: **crea tu cuenta gratis** (15 GB, sin tarjeta) → app.positiva.studio. Gancho de cierre: **Tarifa Fundador** para los 50 primeros de pago.

Diseños en `social/v4/` (1080×1350, sirven para IG feed y LinkedIn sin recortar). Fuentes en `social/v4/src/` — `node build-v4.mjs` regenera los seis. La v3 (carteles bold) queda descartada; `social/v3` se puede borrar.

---

## 1. Objetivo

- **Primario:** 150 cuentas gratuitas creadas en 4 semanas, atribuibles a redes (UTM `?utm_source=instagram|linkedin&utm_medium=social&utm_campaign=lanzamiento`).
- **Secundario:** 15 altas de pago (Fundador) · 40 DMs/comentarios de fotógrafos o productoras · 500 seguidores nuevos combinados.
- [Suposición] Cifras sin histórico: son un listón para saber si funciona, no una promesa. Revísalas a la semana 2.

## 2. Audiencia

| Canal | Segmento | Dolor que compran | Etapa |
|---|---|---|---|
| Instagram | Fotógrafos/videógrafos de boda y evento, autónomos, España | Enlaces que caducan, reenviar, herramientas en inglés, pagar dos servicios (foto + vídeo) | Conciencia → consideración |
| LinkedIn (perfil) | Productoras de vídeo, agencias, videógrafos corporativos | Revisión de vídeo con comentarios en el fotograma; exportar a Resolve/FCP; RGPD/UE | Consideración → decisión |
| LinkedIn (página) | Los mismos, cuando llegan desde el perfil | Coherencia de marca, señales de producto serio | Decisión |

**Lo que NO haces:** perseguir fotógrafos aficionados ni cuentas de «tips de Lightroom». Compran por precio, no por marca.

## 3. Mensajes

**Núcleo:** *Entrégalo una vez, con tu marca, y no lo reenvíes nunca.*

| Mensaje | Prueba | Dónde |
|---|---|---|
| El enlace no caduca | Cambias archivos semanas después, el enlace es el mismo | IG post 2, LI semana 1 |
| Foto y vídeo en la misma galería | Un GB es un GB, sin bolsas separadas | IG post 4, LI semana 2 |
| Precio honesto, sin «ilimitado» | Autor 250 GB · 89 €/año · UE · sin comisiones | IG post 6, LI semana 3 |
| Revisión de vídeo profesional | Comentarios en el fotograma → EDL/FCPXML | Solo LinkedIn (semana 2) |
| Tu web sin hacer web | Portfolio montado con lo ya entregado | IG post 5 |

Tono: el de la web. Frase corta, sin bullets de features, sin emojis en LinkedIn. El humor va contra el problema, nunca contra Pixieset/Pic-Time por nombre en redes (la comparativa vive en la web).

## 4. Sistema visual v4 (la tirada de agosto, refinada)

Tres registros que rotan en la rejilla, con las referencias que marcaste:

| Registro | Referencia | Qué es | Posts |
|---|---|---|---|
| **Oficio** | @mymind | Cita real de un fotógrafo en Playfair sobre ámbar, autor en itálica, una foto tuya impresa debajo. Cultura por encima de producto. | 2 |
| **Práctico** | @pixieset (mensaje, no diseño) | Un problema concreto y su solución en una frase. Sin features. | 4, 6 |
| **Comunidad** | @pictime_us | Galería real entregada con Positiva, con el nombre del estudio. | 5 |
| **Marca** | tirada de agosto | Foto real protagonista o definición tipográfica. | 1, 3 |

Reglas:
- Playfair 300 para titulares (110–176 px), itálica 400 en ámbar para la palabra que importa. Instrument Sans 400 a 40–44 px para la segunda línea. **Nada por debajo de 30 px**; lo que antes iba en mono a 11 px se ha eliminado o subido a 40 px.
- Fondos: sala / ámbar / papel / foto, sin repetir dos seguidos. Ámbar es acento salvo en el post de cita, donde es fondo (como el naranja de mymind).
- Lockup icono + wordmark, una vez por pieza. En ámbar el punto va a una tinta.
- Fotos: solo tuyas o galerías reales de clientes con permiso. Nada de recortes de retratos ajenos.

**[Seguro] Bloquea el despliegue:** el post 5 muestra la galería de Aitana y David (ya pública en tu landing, pero confirma que pueden salir en redes). El post 1 usa el fotograma del showcase de boda: mismo permiso.

**Banco de citas para el registro Oficio** (cortas, atribuidas, una por semana): Cartier-Bresson sobre las diez mil primeras fotos · Robert Capa sobre acercarse más · Diane Arbus sobre el secreto de una foto · Vivian Maier sobre mirar · Berger sobre la elección del momento. Tradúcelas tú; son tu voz.

## 5. Calendario · 4 semanas

Ritmo: **IG 3 posts/semana + Stories** · **LinkedIn perfil 2/semana** · **página 1/semana** (republica el post de perfil con mejor tracción, sin texto nuevo).

| Sem | Día | Instagram | LinkedIn (perfil) | LinkedIn (página) |
|---|---|---|---|---|
| 1 · 21–25 sep | L | **Post 1 · Ya está aquí** (foto boda, sala) | Texto de fundador: «12 años entregando bodas por WeTransfer. Hoy abro Positiva.» + post 1 | — |
| | X | **Post 4 · El enlace ha caducado** (Manolo, sala) · candidato a Reel | — | Post 1 + una línea |
| | V | **Post 3 · Positiva (adj.)** (papel) | Post 4 con caso real: «Un cliente abrió la galería 6 semanas después. Mismo enlace.» | — |
| | Stories | Encuesta «¿Con qué entregas hoy?» · captura del registro sin tarjeta | | |
| 2 · 28 sep–2 oct | L | **Post 4 · ¿Todavía usas enlaces que caducan?** (sala) · candidato a Reel | Revisión de vídeo: captura de un comentario anclado al fotograma + export EDL a Resolve | — |
| | X | **Reel 15 s**: recorrido de una galería real (móvil, sin voz, texto grande) | — | Post de revisión de vídeo |
| | V | **Post 5 · Entregado con Positiva** (galería real, papel) | Post 4 + «Un GB es un GB» | — |
| | Stories | Detrás de: una decisión de producto, a cámara | | |
| 3 · 5–9 oct | L | **Post 6 · Sin ilimitado** (sala) | Post 6 con la cuenta: qué cuesta 1 TB de verdad y por qué no vendemos «ilimitado» | — |
| | X | Carrusel «cómo se ve»: 4 capturas de una galería (con permiso del cliente) | — | Post 6 |
| | V | Cita de oficio nueva (misma plantilla, sin foto): «Reenviar el enlace no es tu trabajo.» | RGPD/UE: «Tus entregas en la UE, sin entrenar IA con tu material.» | — |
| | Stories | Pregunta abierta «¿Qué te cobra de más tu herramienta?» | | |
| 4 · 12–16 oct | L | Carrusel «galería de la semana» (boda real) | Aprendizajes de 3 semanas: números reales de altas | — |
| | X | Reel a cámara: por qué lo construyo | — | Carrusel galería |
| | V | **CTA Fundador**: «Quedan N plazas» (plantilla post 6, número gigante) | CTA Fundador para productoras (plan Estudio 1 TB) | — |
| | Stories | Recuento de plazas · testimonios de los primeros | | |

**Dependencias:** UTM en el enlace de bio y en cada post de LinkedIn antes del lunes 21 · página de LinkedIn con banner y logo (ya en `branding/redes/`) el viernes 18 · permiso de retratos antes del post 1 · permiso de cliente antes de los carruseles de semana 3–4.

## 6. Copys · Instagram (pies)

**Post 1 · Ya está aquí**
Positiva ya está abierta.
Galerías privadas de fotos y vídeo con tu marca. Un enlace que no caduca. El cliente elige, comenta y descarga; tú no reenvías nada.
Plan gratis de 15 GB, sin tarjeta. Link en bio.
#fotografodebodas #videografo #entregadefotos #positiva

**Post 4 · El enlace ha caducado**
Entregas un viernes. El cliente lo abre el miércoles. Enlace muerto.
En Positiva el enlace es siempre el mismo: cambias archivos, subes la versión final semanas después, sigue vivo.
Cuenta gratis en el link de la bio.
#wetransfer #workflow #fotografodebodas #positiva

**Post 3 · Positiva (adj.)**
Dicho de una entrega: hacerla una vez, con tu marca, y no reenviarla nunca.
Así entendemos el trabajo terminado.
#fotografia #fotografoprofesional #positiva

**Post 2 · Cita de oficio**
«Tus primeras diez mil fotografías serán las peores.» — Henri Cartier-Bresson.
Las siguientes las entregas con tu marca.
#fotografia #oficio #positiva

**Post 5 · Entregado con Positiva**
Aitana y David, Valencia. Galería de fotos y vídeo de @quieroweddingstudio, entregada en un solo enlace con su marca.
¿Entregas con Positiva? Etiquétanos y la enseñamos.
#entregadefotos #fotografodebodas #positiva

**Post 6 · Sin ilimitado**
El almacenamiento cuesta dinero real. Quien te vende «ilimitado» te lo cobra en otro sitio.
Autor: 250 GB, foto y vídeo, con tu marca, 89 €/año. Los 50 primeros, tarifa Fundador para siempre.
#preciohonesto #fotografodebodas #positiva

## 7. Copys · LinkedIn (perfil, semana 1)

**Lunes**
Doce años entregando bodas y documentales por WeTransfer y Drive. Enlaces caducados, reenvíos a las once de la noche, mi logo debajo del de otro.
Hoy abro Positiva: galerías de fotos y vídeo con tu marca, un enlace que no caduca y revisión de vídeo con comentarios en el fotograma que se exportan a DaVinci Resolve y Final Cut.
Hecha en Valencia, datos en la UE, precios en euros, sin comisiones.
Plan gratis de 15 GB sin tarjeta → positiva.studio

**Viernes**
Un cliente abrió su galería seis semanas después de la entrega. Mismo enlace, versión final ya subida, cero correos.
Eso es lo único que tiene que hacer una herramienta de entrega. Lo demás es ruido.

## 8. Métricas

| Métrica | Objetivo 4 sem. | Dónde se mide |
|---|---|---|
| Cuentas gratis con UTM social | 150 | Umami (landing) + registros app |
| Altas Fundador | 15 | App |
| Guardados + compartidos por post (IG) | > 5 % del alcance | Insights IG |
| Clics al enlace de bio / posts LI | 600 | Insights + Umami |
| DMs y comentarios cualificados | 40 | Manual, hoja semanal |

Revisión **cada viernes**, 20 minutos. Si un formato dobla al resto en guardados, repítelo la semana siguiente en lugar de seguir el calendario.

## 9. Riesgos

| Riesgo | Mitigación |
|---|---|
| Fotos de clientes sin permiso para redes | Confirmar con Aitana y David antes del 21; si no, post 5 pasa a la galería de Álvaro y Elena (`galeria-alvaro.jpg`) |
| Alcance cero en página de LinkedIn | La página no lidera nada: republica. El perfil lleva la voz |
| Registro gratis que no activa | Email día 1 con «crea tu primera galería en 2 minutos» (fuera de este plan, pero sin él el objetivo primario no vale) |
| Quemar el chiste WeTransfer | Una vez al mes como máximo |

## 10. Antes del lunes 21

1. Permiso de Aitana y David para el post 1 y el post 5.
2. Bio de IG: «Galerías de fotos y vídeo con tu marca. Entrégalo una vez, no lo reenvíes nunca.» + enlace con UTM.
3. Página de LinkedIn con banner y logo de `branding/redes/`.
4. Revisar los pies: son tu voz, no la mía.
5. Programar semana 1 entera (Meta Business Suite / Buffer) para no depender del día a día.
