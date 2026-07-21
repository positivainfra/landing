# Prompt para Claude Code — Aplicar la marca Positiva

Copia desde aquí hacia abajo y pégalo en Claude Code dentro del repo de la app.

---

Aplica la identidad de marca de Positiva (monograma B·5-10) a este proyecto. La marca ya está decidida y cerrada: no propongas alternativas ni "mejoras" al dibujo — ejecútala tal cual.

## La marca

El logo es una P construida con una montura de diapositiva de 35 mm: la panza es la montura, la ventana es el fotograma 3:2 y lleva un punto ámbar (el grano de luz del proyector). SVG canónico del icono (viewBox normalizado, NO alteres las coordenadas):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 56 59">
  <path fill-rule="evenodd" fill="currentColor" d="M12 0 H40 A12 12 0 0 1 52 12 V29 A12 12 0 0 1 40 41 H12 A12 12 0 0 1 0 29 V12 A12 12 0 0 1 12 0 Z M10 10 H42 V31 H10 Z"/>
  <path fill="currentColor" d="M0 20 H10 V50 A5 5 0 0 1 5 55 A5 5 0 0 1 0 50 Z"/>
  <circle cx="26" cy="20.5" r="3.8" fill="#C98A2B"/>
</svg>
```

`currentColor` en los trazos permite variante positiva (tinta `#171614` sobre claro) y negativa (`#EDECE8` sobre oscuro) heredando el color del contenedor. El punto es SIEMPRE `#C98A2B`, nunca negro ni blanco. Única excepción: versión a una tinta (impresión monocolor), donde el punto toma el color del trazo.

El wordmark es texto, no imagen: `POSITIVA.` en Space Mono Bold, mayúsculas, `letter-spacing: .22em`, con el punto final en ámbar (`<b>` o `<span>` coloreado). No uses Playfair ni ninguna otra fuente para el wordmark.

Lockup principal (nav, cabeceras): icono + wordmark en fila, gap ~11px, icono ~27px de alto, wordmark ~14px. El icono también funciona solo (favicon, avatar, marca de agua).

## Tokens

Si el repo ya tiene `tokens.css` (o equivalente), usa esas variables; no dupliques valores. Referencia:

```
--pv-papel:#F1F0EC  --pv-luz:#FFFFFF  --pv-bandeja:#E6E5E0
--pv-sala:#0E0E0D   --pv-sala-2:#1A1A18
--pv-tinta:#171614  --pv-tinta-60:#6E6D67  --pv-tinta-30:#A9A8A2
--pv-linea:#D6D5CF  --pv-linea-sala:#2A2A27
--pv-ambar:#C98A2B  --pv-ambar-luz:#F5E9D2  --pv-graso:#E0402A
```

Tipografías (autoalojadas, cero CDN): Space Mono 700 = solo marca · Playfair Display 300/400 = titulares · Instrument Sans = interfaz y cuerpo · IBM Plex Mono = metadatos y etiquetas.

## Reglas duras

1. El punto es ámbar o no es.
2. Por debajo de ~16 px de alto, el icono va SIN punto (a ese tamaño ensucia).
3. Zona de respeto: media panza (26/52 del ancho del icono) en todo el perímetro.
4. El monograma nunca aparece dos veces en la misma vista: si el lockup completo está en pantalla, el icono no firma solo en otra esquina.
5. No deformar, no rotar, no recolorear, no engordar el punto, no ponerlo sobre foto sin contraste (usa la variante según luminancia del fondo).
6. Fondos más oscuros que un gris 50% → variante negativa.

## Tareas

1. Sustituye el logo actual en todos los puntos de la interfaz: nav/header, pantallas de login/registro, emails transaccionales, y cualquier sitio donde hoy haya un logotipo tipográfico antiguo.
2. Favicon: genera `favicon.svg` con media query interna `@media (prefers-color-scheme: dark)` para invertir el trazo (tinta ↔ `#EDECE8`), punto r4.6 (más generoso para 16–32 px). Añade `favicon-32.png` (tinta sobre transparente) y `apple-touch-icon.png` 180×180 (fondo `#0E0E0D`, icono negativo centrado).
3. Estado de carga: el spinner de la app es el monograma con el punto "respirando" — anima SOLO el `circle` del punto (opacity 1→.35, scale 1→.72, ~2.2s ease-in-out infinito, `transform-box: fill-box; transform-origin: center`). Respeta `prefers-reduced-motion` (sin animación).
4. Contraetiqueta en galerías de cliente: pie con icono pequeño + texto en IBM Plex Mono uppercase `ENTREGADO CON POSITIVA · POSITIVA.STUDIO`, color tenue según fondo.
5. Marca de agua opcional sobre fotos: icono blanco al ~90% de opacidad, esquina, tamaño discreto, sin punto si queda por debajo de 16 px.

## Verificación (hazla antes de dar nada por terminado)

- Captura el favicon renderizado a 16 y 32 px: la P debe leerse; a 16 px no debe haber punto.
- Comprueba el lockup sobre fondo claro y oscuro: el trazo invierte, el punto sigue ámbar.
- Busca en el repo restos del logo anterior (`grep` de la palabra Positiva en Playfair, logos SVG/PNG antiguos) y elimínalos o reemplázalos.
- El monograma no aparece duplicado en ninguna vista.
- El spinner se detiene con `prefers-reduced-motion: reduce`.

Los artes finales de referencia (SVG/PDF/PNG en positivo, negativo y una tinta) están en `branding/arte-final/` del repo de la landing (positiva-landing). Si este repo necesita copias, cópialas desde ahí en vez de redibujarlas.
