// Servidor estático mínimo para verificación local (no es parte del deploy).
// Emula el html_handling de Cloudflare assets: /bodas → 301 /bodas/ →
// bodas/index.html, y /precios también resuelve a precios/index.html.
// Soporta peticiones Range (obligatorio para que Safari reproduzca vídeo).
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(process.argv[2] || '.');
const PORT = Number(process.argv[3] || 4321);
const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2', '.avif': 'image/avif', '.webp': 'image/webp',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
  '.json': 'application/json', '.ico': 'image/x-icon', '.mp4': 'video/mp4',
  '.xml': 'application/xml; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
};

const exists = (f) => { try { return fs.statSync(f); } catch { return null; } };

http.createServer((req, res) => {
  const p = decodeURIComponent(req.url.split('?')[0]);
  let file = path.join(ROOT, p);
  if (!file.startsWith(ROOT)) { res.writeHead(403).end(); return; }

  let st = exists(file);
  if (st?.isDirectory()) {
    // /bodas → /bodas/ (igual que Cloudflare), /bodas/ → bodas/index.html
    if (!p.endsWith('/')) { res.writeHead(301, { Location: p + '/' }).end(); return; }
    file = path.join(file, 'index.html');
    st = exists(file);
  } else if (!st && !path.extname(file) && exists(file + '.html')) {
    file = file + '.html'; // /pagina → pagina.html si existiera
    st = exists(file);
  }

  if (!st || !st.isFile()) { res.writeHead(404, { 'Content-Type': 'text/plain' }).end('404'); return; }

  const type = MIME[path.extname(file)] || 'application/octet-stream';
  const size = st.size;
  const range = req.headers.range;

  if (range) {
    // "bytes=inicio-fin" · Safari no reproduce vídeo sin respuestas 206
    const m = /^bytes=(\d*)-(\d*)$/.exec(range);
    let start = m && m[1] !== '' ? Number(m[1]) : 0;
    let end = m && m[2] !== '' ? Number(m[2]) : size - 1;
    if (!m || start > end || start >= size) {
      res.writeHead(416, { 'Content-Range': `bytes */${size}` }).end(); return;
    }
    end = Math.min(end, size - 1);
    res.writeHead(206, {
      'Content-Type': type,
      'Content-Range': `bytes ${start}-${end}/${size}`,
      'Content-Length': end - start + 1,
      'Accept-Ranges': 'bytes',
    });
    fs.createReadStream(file, { start, end }).pipe(res);
    return;
  }

  res.writeHead(200, { 'Content-Type': type, 'Content-Length': size, 'Accept-Ranges': 'bytes' });
  fs.createReadStream(file).pipe(res);
}).listen(PORT, () => console.log(`static server on http://localhost:${PORT} root=${ROOT}`));
