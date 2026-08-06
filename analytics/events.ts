/**
 * @labbo/analytics · catálogo de eventos
 *
 * Única fuente de verdad de los nombres de evento de TODO el ecosistema.
 * El IDE autocompleta, no hay typos, y en Umami no aparecen eventos
 * duplicados por un `gallery_cretaed` perdido.
 *
 * Convención: nombre en snake_case, en pasado (algo que YA ocurrió).
 * Agrupa por dominio con un comentario. No borres nombres ya lanzados
 * (romperías el histórico); márcalos como @deprecated si dejan de usarse.
 */
export const Events = {
  // ── Adquisición / landing ──────────────────────────────
  WAITLIST_SUBMITTED: "waitlist_submitted",
  WAITLIST_INVALID_EMAIL: "waitlist_invalid_email",
  CTA_REGISTER_CLICK: "cta_register_click",
  COMPARISON_OPENED: "comparison_opened",
  GALLERY_DEMO_OPENED: "gallery_demo_opened",

  // ── Onboarding ─────────────────────────────────────────
  SIGNUP_STARTED: "signup_started",
  SIGNUP_COMPLETED: "signup_completed",

  // ── Producto: galerías ─────────────────────────────────
  GALLERY_CREATED: "gallery_created",
  GALLERY_SHARED: "gallery_shared",
  UPLOAD_STARTED: "upload_started",
  UPLOAD_COMPLETED: "upload_completed",
  CLIENT_FAVORITED: "client_favorited",
  CLIENT_COMMENTED: "client_commented",

  // ── Perfil público ─────────────────────────────────────
  PROFILE_PUBLISHED: "profile_published",
  PROFILE_VIEWED: "profile_viewed",

  // ── Monetización ───────────────────────────────────────
  CHECKOUT_STARTED: "checkout_started",
  CHECKOUT_COMPLETED: "checkout_completed",
  PLAN_UPGRADED: "plan_upgraded",
  PLAN_CANCELLED: "plan_cancelled",
} as const;

/** Unión de todos los nombres de evento válidos. */
export type EventName = (typeof Events)[keyof typeof Events];
