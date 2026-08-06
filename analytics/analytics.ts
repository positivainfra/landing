/**
 * @labbo/analytics · wrapper de Umami
 *
 * Regla de oro: NUNCA llames a `window.umami` directamente desde un componente.
 * Usa siempre `track()` con un evento del catálogo (`Events`).
 *
 * Funciona en cualquier app del ecosistema (Positiva, CRM, portfolio, landing).
 * No rompe en SSR (comprueba `window`) y jamás lanza (la analítica no debe
 * tumbar la app).
 */
import type { EventName } from "./events";
import type { CommonProps } from "./properties";

type Props = CommonProps & Record<string, string | number | boolean | null | undefined>;

declare global {
  interface Window {
    umami?: {
      track: (event: string, data?: Record<string, unknown>) => void;
      identify?: (data: Record<string, unknown>) => void;
    };
  }
}

/** Envía un evento a Umami. Silencioso si el tracker aún no ha cargado. */
export function track(event: EventName, data?: Props): void {
  try {
    if (typeof window === "undefined" || !window.umami) return;
    if (data && Object.keys(data).length) window.umami.track(event, data);
    else window.umami.track(event);
  } catch {
    /* la analítica nunca debe romper la app */
  }
}

/** Adjunta propiedades persistentes al visitante (opcional, Umami v2). */
export function identify(data: Props): void {
  try {
    window?.umami?.identify?.(data);
  } catch {
    /* noop */
  }
}
