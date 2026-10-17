#!/usr/bin/env python3
"""Anima los stills con Kling 2.5 Turbo Pro (image-to-video) en Replicate. Salida: clips/<name>.mp4"""
import json, sys, time, io, pathlib, urllib.request, mimetypes, uuid
from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN = (ROOT / "_to_delete" / "replicate.token").read_text().strip()
H = {"Authorization": f"Bearer {TOKEN}", "User-Agent": "positiva-promo/1.0"}
HERE = pathlib.Path(__file__).resolve().parent
STILLS, CLEAN, CLIPS = HERE/"stills", HERE/"stills_clean", HERE/"clips"
CLEAN.mkdir(exist_ok=True); CLIPS.mkdir(exist_ok=True)
MODEL = "kwaivgi/kling-v2.5-turbo-pro"
NEG = "text, letters, logo, watermark, extra people, faces, deformed hands, fast motion, camera shake, morphing"

MOTION = {
 "01_coche_alba": "Static camera inside the car. Rain drops slowly run down the windshield, wipers do not move, distant headlights flicker softly, very subtle breathing of the frame. Slow, quiet, realistic.",
 "02_boda_contraluz": "Very slow push-in on the crouched photographer seen from behind. He stays still, slight shift of weight. Guests out of focus sway gently, sun flare pulses softly, grass moves in a light breeze. Cinematic, slow.",
 "03_optica_macro": "Macro, static camera. Dust particles drift slowly through the light beam inside the lens, reflections shift subtly as the light moves a few degrees. Very slow, elegant.",
 "04_evento_silueta": "Silhouette seen from behind stays almost still, adjusting the gimbal slightly. Haze drifts slowly across the blue spotlight, light rays shimmer. Slow handheld micro-movement.",
 "05_lluvia_tripode": "Static camera. Rain falls steadily, drops bounce off the umbrella, mist drifts over the field, the figure stays still looking at the camera on the tripod. Slow, quiet, overcast.",
 "06_edicion_noche": "Static camera. Screen glow flickers subtly on the wall, the blurred timeline on the monitor scrolls very slowly, lamp light steady. Nothing readable on screen. Calm, late night.",
}

def getj(url, tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=60) as r: return json.load(r)
        except Exception as e:
            if i == tries-1: raise
            time.sleep(5)

def finish(name, pred, t0):
    while pred["status"] not in ("succeeded","failed","canceled"):
        time.sleep(8); pred = getj(pred["urls"]["get"])
    if pred["status"] != "succeeded": print(name, "FAILED", pred.get("error")); return
    out = pred["output"] if isinstance(pred["output"], str) else pred["output"][0]
    urllib.request.urlretrieve(out, CLIPS/f"{name}.mp4")
    print(name, "OK", f"{time.time()-t0:.0f}s", pred.get("metrics",{}).get("predict_time"))

STATE = HERE/"_qc"/"pending.json"
def launch(names):
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    for name in names:
        clean = CLEAN/f"{name}.jpg"; strip_bars(STILLS/f"{name}.jpg", clean); url = upload(clean)
        body = json.dumps({"input": {"start_image": url, "prompt": MOTION[name], "duration": 5,
                                     "aspect_ratio": "16:9", "negative_prompt": NEG}}).encode()
        req = urllib.request.Request(f"https://api.replicate.com/v1/models/{MODEL}/predictions", data=body,
            headers={**H, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r: pred = json.load(r)
        st[name] = pred["urls"]["get"]; print("launched", name)
    STATE.parent.mkdir(exist_ok=True); STATE.write_text(json.dumps(st))

def collect():
    st = json.loads(STATE.read_text()); done = []
    for name, url in st.items():
        pred = getj(url)
        if pred["status"] in ("succeeded","failed","canceled"):
            finish(name, pred, time.time()); done.append(name)
        else: print(name, pred["status"])
    for n in done: st.pop(n)
    STATE.write_text(json.dumps(st))

def resume(name):
    d = getj("https://api.replicate.com/v1/predictions")
    for pr in d["results"]:
        if pr.get("model") == MODEL:
            print("resuming", pr["id"], pr["status"]); finish(name, getj(pr["urls"]["get"]), time.time()); return
    print("no prediction found")

def strip_bars(src, dst):
    im = Image.open(src).convert("RGB")
    bg = Image.new("RGB", im.size, (0,0,0))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda p: 255 if p > 18 else 0)
    bbox = diff.getbbox()
    if bbox: im = im.crop((0, bbox[1], im.width, bbox[3]))
    im.save(dst, "JPEG", quality=92); return im.size

def upload(path):
    boundary = uuid.uuid4().hex
    data = path.read_bytes()
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"content\"; filename=\"{path.name}\"\r\n"
            f"Content-Type: image/jpeg\r\n\r\n").encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request("https://api.replicate.com/v1/files", data=body,
        headers={**H, "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=120) as r: return json.load(r)["urls"]["get"]

def run(name):
    src = STILLS/f"{name}.jpg"; clean = CLEAN/f"{name}.jpg"
    size = strip_bars(src, clean)
    url = upload(clean)
    body = json.dumps({"input": {"start_image": url, "prompt": MOTION[name], "duration": 5,
                                 "aspect_ratio": "16:9", "negative_prompt": NEG}}).encode()
    req = urllib.request.Request(f"https://api.replicate.com/v1/models/{MODEL}/predictions", data=body,
        headers={**H, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r: pred = json.load(r)
    finish(name, pred, time.time())

if __name__ == "__main__":
    if sys.argv[1:2] == ["--resume"]: resume(sys.argv[2])
    elif sys.argv[1:2] == ["--launch"]: launch(sys.argv[2:])
    elif sys.argv[1:2] == ["--collect"]: collect()
    else:
        for n in (sys.argv[1:] or list(MOTION)): run(n)
