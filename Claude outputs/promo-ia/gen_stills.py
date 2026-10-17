#!/usr/bin/env python3
"""Genera los 6 stills maestros del bloque 1 («Lo que se queda») en Replicate.
Token: se lee de _to_delete/replicate.token (gitignored). No se imprime nunca."""
import json, os, sys, time, urllib.request, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN = (ROOT / "_to_delete" / "replicate.token").read_text().strip()
OUT = pathlib.Path(__file__).resolve().parent / "stills"
MODEL = "black-forest-labs/flux-1.1-pro"

BASE = ("Cinematic film still, shot on 35mm, anamorphic lens, subtle film grain, soft halation, "
        "natural light, muted cold palette (steel blue, slate, desaturated teal), deep shadows, "
        "no text, no logos, no faces visible, photorealistic, documentary feel, full frame image with no black letterbox bars. ")

SHOTS = {
 "01_coche_alba": BASE + "Interior of a car at 5:40 am, camera bags on the passenger seat, rain drops on the windshield, "
   "blurred wet road and grey-blue dawn outside, dashboard dark, shallow depth of field, static frame.",
 "02_boda_contraluz": "Cinematic film still, 200mm telephoto, shot on 35mm, film grain, halation. WARM ACCENT: golden hour backlight. "
   "Full frame, no black bars. A wedding photographer seen from directly behind, crouched, 20 meters away, completely black silhouette "
   "against the low sun, flare, dreamy out-of-focus guests scattered naturally on a lawn, nobody facing camera, no faces, no text.",
 "03_optica_macro": BASE + "Extreme macro of a camera lens front element on black background, a beam of cool light entering the glass, "
   "dust particles floating in the beam, cyan and green coating reflections, very shallow focus.",
 "04_evento_silueta": BASE + "Corporate event, dense haze, ONE single blue spotlight behind, exactly one person: a videographer holding a camera on a gimbal at chest height, "
   "seen from behind, completely black silhouette rimmed with blue light, dark empty auditorium, no other people, no faces.",
 "05_lluvia_tripode": BASE + "Overcast rainy exterior, blue mist, a camera on a tripod covered by a dark umbrella, one figure in rain jacket from behind, "
   "distant bare trees, cold fog, medium shot, no faces.",
 "06_edicion_noche": BASE + "Editing desk at night, monitor out of focus showing an unreadable video timeline, warm small desk lamp on the left, "
   "cup, cables, screen glow on the wall, shallow depth of field, nothing legible.",
}

def run(name, prompt):
    body = json.dumps({"input": {"prompt": prompt, "aspect_ratio": "16:9", "output_format": "jpg",
                                 "output_quality": 90, "safety_tolerance": 2}}).encode()
    req = urllib.request.Request(f"https://api.replicate.com/v1/models/{MODEL}/predictions", data=body,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "Prefer": "wait=60"})
    with urllib.request.urlopen(req, timeout=120) as r:
        pred = json.load(r)
    while pred["status"] not in ("succeeded", "failed", "canceled"):
        time.sleep(3)
        req = urllib.request.Request(pred["urls"]["get"], headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=60) as r:
            pred = json.load(r)
    if pred["status"] != "succeeded":
        print(name, "FAILED", pred.get("error")); return
    url = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
    dst = OUT / f"{name}.jpg"
    urllib.request.urlretrieve(url, dst)
    print(name, "OK", pred.get("metrics", {}).get("predict_time"))

if __name__ == "__main__":
    only = sys.argv[1:]
    for n, p in SHOTS.items():
        if only and n not in only: continue
        run(n, p)
