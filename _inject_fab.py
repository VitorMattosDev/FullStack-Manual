#!/usr/bin/env python3
# Injeta o botão flutuante "Praticar" (link p/ jogo.html#<id>) em cada manual.
# Idempotente: pula arquivos que já contêm o marcador FSQUEST-FAB.
import os, sys

PAGES = "pages"
MAP = {
    "typescript.html": "typescript",
    "javascript.html": "javascript",
    "manual-html.html": "html",
    "manual-css.html": "css",
    "manual-react.html": "react",
    "manual-tailwind.html": "tailwind",
    "manual-nextjs.html": "nextjs",
    "manual-nodejs.html": "nodejs",
    "manual-hono.html": "hono",
    "manual-sql-postgresql.html": "sql",
    "manual-drizzle.html": "drizzle",
    "manual-zod.html": "zod",
    "manual-autenticacao.html": "auth",
    "manual-git.html": "git",
    "manual-docker.html": "docker",
    "manual-bash.html": "bash",
    "manual-regex.html": "regex",
    "manual-testes.html": "testes",
    "manual-devops.html": "devops",
    "manual-capstone.html": "capstone",
}

MARKER = "FSQUEST-FAB"

def fab(mod_id):
    return (
        '<!-- ' + MARKER + ' -->\n'
        '<a href="../jogo.html#' + mod_id + '" title="Praticar este volume no FullStack Quest" '
        'style="position:fixed;right:1.25rem;bottom:1.25rem;z-index:9999;display:inline-flex;align-items:center;gap:0.55rem;'
        'padding:0.7rem 1.05rem;border-radius:999px;text-decoration:none;'
        'font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;font-weight:700;'
        'color:#0f0d0b;background:linear-gradient(135deg,#f0a830,#e08c2a);'
        'box-shadow:0 8px 26px -6px rgba(240,168,48,0.55);transition:transform .15s;" '
        'onmouseover="this.style.transform=\'translateY(-2px)\'" '
        'onmouseout="this.style.transform=\'none\'">'
        '<span style="font-size:1.05rem;">\U0001F3AE</span><span>Praticar &rarr;</span></a>\n'
    )

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    pages_dir = os.path.join(base, PAGES)
    done, skipped, missing = [], [], []
    for fname, mod_id in MAP.items():
        path = os.path.join(pages_dir, fname)
        if not os.path.exists(path):
            missing.append(fname); continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if MARKER in html:
            skipped.append(fname); continue
        if "</body>" not in html:
            missing.append(fname + " (sem </body>)"); continue
        html = html.replace("</body>", fab(mod_id) + "</body>", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        done.append(fname)
    print("Injetado em %d: %s" % (len(done), ", ".join(done)))
    if skipped: print("Pulados (já tinham): %d: %s" % (len(skipped), ", ".join(skipped)))
    if missing: print("Problemas: %s" % ", ".join(missing))

if __name__ == "__main__":
    main()
