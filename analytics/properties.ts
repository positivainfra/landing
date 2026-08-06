/**
 * @labbo/analytics · propiedades comunes
 *
 * Propiedades que quieres poder filtrar SIEMPRE en Umami. No repitas strings
 * sueltos: usa estos tipos para que `plan`, `source`, etc. sean coherentes en
 * todo el ecosistema.
 *
 * Umami añade solo país, navegador, dispositivo y referrer; aquí van las
 * propiedades de negocio.
 */

/** Planes de Positiva (el mismo string en app, landing y CRM). */
export type Plan = "free" | "author" | "studio";

/** De dónde viene un evento de adquisición. */
export type Source =
  | "landing"
  | "precios"
  | "comparativa"
  | "bodas"
  | "freelance"
  | "agencias"
  | "profile"
  | "email"
  | "instagram";

/** Producto del ecosistema que emite el evento. */
export type Product = "positiva" | "crm" | "portfolio" | "landing";

/** Propiedades opcionales que casi cualquier evento puede llevar. */
export interface CommonProps {
  product?: Product;
  source?: Source;
  plan?: Plan;
  amount?: number; // en euros, sin IVA
  place?: string; // ubicación del elemento (nav, hero, footer…)
}

/** Helper: marca el producto una sola vez y reutilízalo al llamar a track(). */
export const withProduct = (product: Product) =>
  <T extends CommonProps>(props?: T): T =>
    ({ product, ...(props ?? {}) }) as T;
