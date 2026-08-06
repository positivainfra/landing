# @labbo/analytics

Capa de analítica compartida para todo el ecosistema Labbo (Positiva, CRM,
portfolio, landing). Envía eventos a una instancia **autoalojada de Umami**
(`analytics.labbo.studio`), que es *cookieless* y first-party.

Una sola regla: **nunca llames a `window.umami` directamente.** Usa `track()`
con un evento del catálogo `Events`.

## Archivos

| Fichero | Qué es |
|---|---|
| `analytics.ts` | Wrapper de Umami: `track()` e `identify()`. No rompe en SSR ni lanza. |
| `events.ts` | Catálogo de nombres de evento (única fuente de verdad). |
| `properties.ts` | Tipos de propiedades comunes (`plan`, `source`, `product`…). |
| `funnels.ts` | Embudos como datos, para paneles/lectura. No ejecuta nada. |

## Instalación (por app)

1. Copia esta carpeta a la app (o publícala como paquete interno del monorepo).
2. Carga el script de Umami una vez, en el `<head>` del documento raíz:

   ```html
   <script defer
     src="https://analytics.labbo.studio/script.js"
     data-website-id="TU_WEBSITE_ID"></script>
   ```

   Cada app/propiedad tiene su propio `website-id` en Umami. Con IDs distintos
   separas datos por producto; si quieres verlo todo junto, comparte ID.

## Uso

```ts
import { track } from "@labbo/analytics/analytics";
import { Events } from "@labbo/analytics/events";

// evento simple
track(Events.GALLERY_CREATED);

// con propiedades
track(Events.CHECKOUT_COMPLETED, { plan: "studio", amount: 219, product: "positiva" });
```

El IDE autocompleta los eventos y TypeScript te avisa si te inventas uno. Así en
Umami nunca aparece un `gallery_cretaed` duplicado.

## Nombrar eventos

- snake_case, en **pasado** (`gallery_created`, no `create_gallery`).
- Agrupa por dominio en `events.ts`.
- **No borres** un evento ya lanzado: rompes el histórico. Márcalo `@deprecated`.

## Embudos

Umami Community no tiene embudos visuales, pero no los necesitas todavía. Cuenta
cada paso de `funnels.ts` (visitantes únicos por evento, en orden) y mira las
caídas:

```
signup_completed   256
gallery_created    220
upload_completed   198
gallery_shared     165
checkout_completed  48
```

## La landing

La landing (`positiva.studio`) es HTML estático sin build, así que **no** usa
este paquete TS: usa su gemelo en JS plano `public/js/analytics.js`, con el mismo
`track()` y un subconjunto de `Events`. Mantén ambos catálogos alineados.
