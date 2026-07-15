/**
 * POST /api/waitlist  → inserta {email, source, created_at} en Supabase (tabla waitlist).
 *
 * Cloudflare Pages Function (runtime Workers). Sin dependencias, sin build.
 * Secretos por variables de entorno del proyecto de Pages (NO en el repo):
 *   SUPABASE_URL          p.ej. https://xxxx.supabase.co
 *   SUPABASE_SERVICE_KEY  service_role key (solo servidor, nunca en el cliente)
 *
 * Esta instancia de Supabase es EXCLUSIVA de la landing pública.
 * No comparte base de datos con la app (test./producción).
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const json = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });

export async function onRequest({ request, env }) {
  if (request.method !== 'POST') return json(405, { error: 'method_not_allowed' });

  if (!env.SUPABASE_URL || !env.SUPABASE_SERVICE_KEY) {
    return json(500, { error: 'not_configured' });
  }

  let data;
  try {
    data = await request.json();
  } catch {
    return json(400, { error: 'bad_json' });
  }

  const email = String(data?.email ?? '').trim().toLowerCase();
  const source = String(data?.source ?? 'landing').slice(0, 40);

  if (!EMAIL_RE.test(email) || email.length > 254) {
    return json(422, { error: 'invalid_email' });
  }

  const res = await fetch(`${env.SUPABASE_URL}/rest/v1/waitlist`, {
    method: 'POST',
    headers: {
      apikey: env.SUPABASE_SERVICE_KEY,
      Authorization: `Bearer ${env.SUPABASE_SERVICE_KEY}`,
      'Content-Type': 'application/json',
      Prefer: 'return=minimal',
    },
    body: JSON.stringify({ email, source }),
  });

  // 23505 = unique_violation → ya estaba apuntado. Lo tratamos como éxito idempotente.
  if (res.status === 409) return json(409, { ok: true, duplicate: true });

  if (!res.ok) {
    return json(502, { error: 'upstream', status: res.status });
  }

  return json(201, { ok: true });
}
