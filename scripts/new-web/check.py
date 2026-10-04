#!/usr/bin/env python3
"""Comprueba que todo lo que enlazan las páginas de /new/ existe en public/."""
import re, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUB = os.path.join(ROOT, 'public')
falta = set()
for f in glob.glob(os.path.join(PUB, 'new', '**', 'index.html'), recursive=True):
    s = open(f).read()
    for u in re.findall(r'(?:href|src|poster)="(/[^"#?]*)', s):
        if u.startswith('//'): continue
        p = os.path.join(PUB, u.lstrip('/'))
        if u.endswith('/'): p = os.path.join(p, 'index.html')
        if not os.path.exists(p) and not u.startswith('/api/') and u not in ('/soporte/', '/soporte'):
            falta.add((u, os.path.relpath(f, PUB)))
for u, f in sorted(falta): print('FALTA', u, '←', f)
print('enlaces y medios comprobados:', 'todo existe' if not falta else f'{len(falta)} rotos')
