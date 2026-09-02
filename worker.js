/**
 * Worker de la landing pública (positiva.studio).
 *
 * Modelo "Worker + static assets": los ficheros de ./public se sirven directos.
 * El Worker solo corre para rutas sin asset — aquí, POST /api/waitlist.
 *
 * La waitlist NO usa base de datos. Cada alta envía un correo a NOTIFY_TO
 * mediante Cloudflare Email Routing (binding send_email). Sin Supabase,
 * sin terceros, sin píxeles.
 *
 * Requiere en Cloudflare (una sola vez):
 *   1. Email Routing activo en positiva.studio.
 *   2. NOTIFY_TO añadido y VERIFICADO como Destination Address en Email Routing.
 *   3. Binding send_email "SEB" y vars NOTIFY_TO / NOTIFY_FROM (ver wrangler.jsonc).
 *
 * NOTIFY_FROM debe ser una dirección de un dominio tuyo con Email Routing
 * (no necesita recibir correo; es solo el remitente).
 */

import { EmailMessage } from 'cloudflare:email';

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const json = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
  });

// Codifica UTF-8 a base64 (para el cuerpo del correo).
function b64utf8(str) {
  const bytes = new TextEncoder().encode(str);
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin);
}

// Construye un MIME text/plain válido (con Date y Message-ID, que CF exige).
function buildMime({ from, to, replyTo, subject, text }) {
  const id = `${crypto.randomUUID()}@positiva.studio`;
  return [
    `From: Positiva <${from}>`,
    `To: <${to}>`,
    `Reply-To: <${replyTo}>`,
    `Message-ID: <${id}>`,
    `Date: ${new Date().toUTCString()}`,
    `Subject: ${subject}`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset="utf-8"',
    'Content-Transfer-Encoding: base64',
    '',
    b64utf8(text),
  ].join('\r\n');
}

async function handleWaitlist(request, env) {
  if (request.method !== 'POST') return json(405, { error: 'method_not_allowed' });
  if (!env.SEB || !env.NOTIFY_TO || !env.NOTIFY_FROM) return json(500, { error: 'not_configured' });

  let data;
  try {
    data = await request.json();
  } catch {
    return json(400, { error: 'bad_json' });
  }

  const email = String(data?.email ?? '').trim().toLowerCase();
  const source = String(data?.source ?? 'landing').slice(0, 40);
  if (!EMAIL_RE.test(email) || email.length > 254) return json(422, { error: 'invalid_email' });

  const text =
    `Nuevo registro en la lista de espera de Positiva.\n\n` +
    `Email:   ${email}\n` +
    `Origen:  ${source}\n` +
    `Fecha:   ${new Date().toISOString()}\n\n` +
    `Responde a este correo para escribirle directamente.`;

  const mime = buildMime({
    from: env.NOTIFY_FROM,
    to: env.NOTIFY_TO,
    replyTo: email, // responder = escribir al interesado
    subject: 'Nuevo registro en la lista de espera',
    text,
  });

  try {
    await env.SEB.send(new EmailMessage(env.NOTIFY_FROM, env.NOTIFY_TO, mime));
  } catch (err) {
    // Visible en `wrangler tail landing`. Causa habitual: NOTIFY_TO no es una
    // destination address verificada en Email Routing (ver wrangler.jsonc).
    console.error('waitlist email_failed:', err && err.message, '| to:', env.NOTIFY_TO, '| from:', env.NOTIFY_FROM);
    return json(502, { error: 'email_failed', detail: String(err && err.message || err).slice(0, 160) });
  }
  return json(201, { ok: true });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/waitlist') return handleWaitlist(request, env);
    // Página fusionada en /galerias/ (el asset ya no existe; el Worker corre y redirige).
    if (url.pathname === '/agencias' || url.pathname.startsWith('/agencias/')) {
      return Response.redirect(url.origin + '/productoras/', 301);
    }
    if (url.pathname === '/diseno-de-galerias' || url.pathname.startsWith('/diseno-de-galerias/')) {
      return Response.redirect(url.origin + '/galerias/#diseno', 301);
    }
    // Cualquier otra ruta: la sirve la capa de assets (incluye su 404).
    return env.ASSETS.fetch(request);
  },
};
