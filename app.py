import os

from flask import Flask

app = Flask(__name__)
TITEL = 'zu Hause'
VERSION = os.environ.get("APP_VERSION", "dev")
APP_ENV = os.environ.get("APP_ENV", "dev")


@app.get("/")
def index():
    banner = f'<div class="banner">Testserver – wird {VERSION}</div>' if APP_ENV == "test" else ""
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITEL}</title>
<style>
body{{margin:0;font-family:system-ui,sans-serif;background:#f7f7f5;color:#1f2328}}
.banner{{background:#fff4c2;border-bottom:1px solid #e6d58a;padding:8px 16px;font-size:14px}}
main{{max-width:640px;margin:15vh auto;padding:0 16px}}
h1{{font-weight:600}} small{{color:#6b6f76}}
</style></head><body>
{banner}<main><h1>{TITEL}</h1><p>Läuft. Hier entsteht die neue App.</p><small>Version {VERSION}</small></main>
</body></html>"""


@app.get("/health")
def health():
    return {"status": "ok", "version": VERSION, "umgebung": APP_ENV}
