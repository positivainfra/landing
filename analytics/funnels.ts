/**
 * @labbo/analytics · embudos (documentación viva)
 *
 * Umami Community no tiene embudos visuales (como Mixpanel o PostHog), pero con
 * 50 clientes no los necesitas: te basta con contar cada paso y mirar las caídas.
 *
 * Este fichero NO ejecuta nada: define los embudos como datos para que (a) todos
 * hablemos del mismo embudo y (b) puedas construir un panel o un script que
 * cuente cada `step` a partir de la API de Umami.
 *
 * Cómo leerlo: cuenta visitantes únicos que dispararon cada evento en orden y
 * mira dónde se cae la gente.
 */
import { Events, type EventName } from "./events";

export interface Funnel {
  id: string;
  label: string;
  steps: EventName[];
}

export const Funnels: Record<string, Funnel> = {
  // Antes del lanzamiento: cuánta gente convierte la landing en lista de espera.
  waitlist: {
    id: "waitlist",
    label: "Landing → lista de espera",
    steps: [Events.COMPARISON_OPENED, Events.CTA_REGISTER_CLICK, Events.WAITLIST_SUBMITTED],
  },

  // El embudo de activación del producto (cuando abras).
  activation: {
    id: "activation",
    label: "Alta → primera galería compartida",
    steps: [
      Events.SIGNUP_COMPLETED,
      Events.GALLERY_CREATED,
      Events.UPLOAD_COMPLETED,
      Events.GALLERY_SHARED,
    ],
  },

  // El que paga las facturas.
  monetization: {
    id: "monetization",
    label: "Alta → cliente de pago",
    steps: [
      Events.SIGNUP_COMPLETED,
      Events.GALLERY_SHARED,
      Events.CHECKOUT_STARTED,
      Events.CHECKOUT_COMPLETED,
    ],
  },
};

/**
 * Ejemplo de lectura (lo que buscas ver):
 *
 *   signup_completed   256
 *   gallery_created    220
 *   upload_completed   198
 *   gallery_shared     165
 *   checkout_completed  48
 *
 * Eso ya te dice dónde se rompe la activación sin necesidad de embudos visuales.
 */
