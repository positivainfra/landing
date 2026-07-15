/**
 * Worker de la landing pública (positiva.studio).
 *
 * Modelo "Worker + static assets": los ficheros de ./public se sirven directos
 * (no invocan al Worker). El Worker solo corre para rutas sin asset — aquí,
 * POST /api/waitlist → Supabase. El resto se delega al binding ASSETS.
 *
 * Secretos por variables del proyecto (NO en el repo):
 *   SUPABASE_URL          https://<ref>.supabase.co
 *   SUPABASE_SERVICE_KEY  service_role key (secreto; solo servidor)
 *
 * ⚠️ Instancia de Supabase EXCLUSIVA de la landing. No es la de la app.
 */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const json = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });

async function handleWaitlist(request, env) {
  if (request.method !== 'POST') return json(405, { error: 'method_not_allowed' });
  if (!env.SUPABASE_URL || !env.SUPABASE_SERVICE_KEY) return json(500, { error: 'not_configured' });

  let data;
  try {
    data = await request.json();
  } catch {
    return json(400, { error: 'bad_json' });
  }

  const email = String(data?.email ?? '').trim().toLowerCase();
  const source = String(data?.source ?? 'landing').slice(0, 40);
  if (!EMAIL_RE.test(email) || email.length > 254) return json(422, { error: 'invalid_email' });

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

  // 23505 unique_violation → ya estaba apuntado; éxito idempotente.
  if (res.status === 409) return json(409, { ok: true, duplicate: true });
  if (!res.ok) return json(502, { error: 'upstream', status: res.status });
  return json(201, { ok: true });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/waitlist') return handleWaitlist(request, env);
    // Cualquier otra ruta: la sirve la capa de assets (incluye su manejo de 404).
    return env.ASSETS.fetch(request);
  },
};
