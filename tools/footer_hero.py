import os, math
OUT = os.environ["OUT"]
A = "#5eead4"
BASE = ('.s{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}'
        '.m{font-family:ui-monospace,SFMono-Regular,Consolas,Menlo,monospace}')
RM = '@media (prefers-reduced-motion:reduce){*{animation:none!important}}'


def svg(W, H, body, css, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{label}"><style>{BASE}{css}{RM}</style>{body}</svg>')


# ================= HERO =================
phrases = ["forecasting industrial emissions", "reverse-engineering game controllers",
           "chasing exoplanets in NASA light curves", "building pipelines that run unattended"]
T = 16.0
css = ('.grid{animation:drift 20s linear infinite}@keyframes drift{to{transform:translateX(32px)}}'
       '.scan{animation:scan 7s linear infinite}@keyframes scan{0%{transform:translateX(-200px);opacity:0}10%{opacity:1}90%{opacity:1}100%{transform:translateX(1160px);opacity:0}}'
       '.cursor{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}'
       '.b1{animation:f1 14s ease-in-out infinite alternate}.b2{animation:f2 18s ease-in-out infinite alternate}'
       '@keyframes f1{to{transform:translate(120px,30px)}}@keyframes f2{to{transform:translate(-140px,-20px)}}'
       '.pulse{stroke-dasharray:900;stroke-dashoffset:900;animation:draw 6s ease-in-out infinite}'
       '@keyframes draw{0%{stroke-dashoffset:900}50%,85%{stroke-dashoffset:0}100%{stroke-dashoffset:-900}}'
       '.nd{animation:nd 3s ease-in-out infinite}@keyframes nd{50%{opacity:.25}}'
       '.ed{stroke-dasharray:4 6;animation:ed 2s linear infinite}@keyframes ed{to{stroke-dashoffset:-20}}'
       '.dot{animation:blink2 2s ease-in-out infinite}@keyframes blink2{50%{opacity:.3}}')


def pc(t):
    return f"{t / T * 100:.2f}%"


body = ('<defs><pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#30363d"/></pattern>'
        '<radialGradient id="g1"><stop offset="0" stop-color="#5eead4" stop-opacity=".22"/><stop offset="1" stop-color="#5eead4" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="g2"><stop offset="0" stop-color="#58a6ff" stop-opacity=".2"/><stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="trail" x1="0" x2="1"><stop offset="0" stop-color="#5eead4" stop-opacity="0"/><stop offset="1" stop-color="#5eead4"/></linearGradient>'
        '<clipPath id="c"><rect width="960" height="240" rx="12"/></clipPath></defs>'
        '<g clip-path="url(#c)"><rect width="960" height="240" fill="#0d1117"/>'
        '<circle cx="300" cy="60" r="200" fill="url(#g1)" class="b1"/><circle cx="780" cy="180" r="220" fill="url(#g2)" class="b2"/>'
        '<rect x="-32" width="1024" height="240" fill="url(#dots)" class="grid" opacity=".8"/>')
# status pill
body += (f'<rect x="48" y="30" width="236" height="26" rx="13" fill="#161b22" stroke="#30363d"/>'
         f'<circle cx="64" cy="43" r="4" fill="{A}" class="dot"/>'
         '<text x="76" y="47" class="m" font-size="11" fill="#8b949e" letter-spacing="1">@AMJADAAYD  ·  OPEN SOURCE</text>')
body += ('<text x="48" y="112" class="s" font-size="58" font-weight="700" fill="#e6edf3" letter-spacing="-1.5">Amjad Aayd</text>'
         '<text x="48" y="146" class="s" font-size="20" fill="#8b949e">Data science, AI and hardware tooling</text>')
# cycling typed line
body += f'<text x="48" y="180" class="m" font-size="14" fill="{A}">&gt; </text>'
seg = T / len(phrases)
for i, ph in enumerate(phrases):
    s = i * seg + 0.2
    e = s + 1.6
    end = (i + 1) * seg - 0.4
    n = len(ph)
    css += (f'.p{i}{{clip-path:inset(0 100% 0 0);animation:y{i} {T}s infinite}}'
            f'@keyframes y{i}{{0%,{pc(s)}{{clip-path:inset(0 100% 0 0);animation-timing-function:steps({n},end)}}'
            f'{pc(e)}{{clip-path:inset(0 0 0 0)}}{pc(end)}{{clip-path:inset(0 0 0 0)}}{pc(end + .3)}{{clip-path:inset(0 100% 0 0)}}100%{{clip-path:inset(0 100% 0 0)}}}}')
    body += f'<text x="68" y="180" class="m p{i}" font-size="14" fill="#c9d1d9">{ph}</text>'
body += f'<rect x="68" y="168" width="8" height="15" fill="{A}" class="cursor" opacity=".0"/>'
# tags
x = 48
for t in ["DATA SCIENCE", "AI", "C# / C++", "REVERSE ENGINEERING"]:
    wd = len(t) * 7.6 + 22
    body += (f'<rect x="{x}" y="200" width="{wd:.0f}" height="24" rx="12" fill="none" stroke="#30363d"/>'
             f'<text x="{x + wd / 2:.0f}" y="216" text-anchor="middle" class="m" font-size="10" fill="#7d8590" letter-spacing="1">{t}</text>')
    x += wd + 8
# network nodes right side
nodes = [(640, 70), (720, 40), (800, 90), (880, 50), (700, 130), (780, 160), (860, 140), (920, 100)]
edges = [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (2, 5), (5, 6), (3, 7), (6, 7), (2, 6)]
for a, b in edges:
    body += f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="#30363d" class="ed" style="animation-delay:{(a + b) * .2}s"/>'
for i, (nx, ny) in enumerate(nodes):
    body += f'<circle cx="{nx}" cy="{ny}" r="4" fill="{A}" class="nd" style="animation-delay:{i * .4}s"/>'
body += ('<path d="M560 205 H640 L656 205 L668 180 L684 226 L698 192 L710 205 H800 L812 205 L822 190 L834 218 L844 205 H912" '
         'fill="none" stroke="#5eead4" stroke-opacity=".55" stroke-width="1.5" stroke-linejoin="round" class="pulse"/>'
         '<text x="912" y="236" text-anchor="end" class="m" font-size="10" fill="#7d8590" letter-spacing="1.5"></text>')
body += ('<line x1="0" y1="239" x2="960" y2="239" stroke="#21262d" stroke-width="2"/>'
         '<g class="scan"><rect x="0" y="238" width="200" height="2" fill="url(#trail)"/></g></g>'
         '<rect x=".5" y=".5" width="959" height="239" rx="12" fill="none" stroke="#30363d"/>')
open(f"{OUT}/assets/hero.svg", "w", encoding="utf-8").write(svg(960, 240, body, css, "Amjad Aayd: data science, AI and hardware tooling"))

# ================= FOOTER =================
import json, urllib.request, datetime


def api(path):
    req = urllib.request.Request("https://api.github.com" + path, headers={"User-Agent": "profile-build", **({"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"]} if os.environ.get("GITHUB_TOKEN") else {})})
    return json.load(urllib.request.urlopen(req, timeout=20))


try:
    u = api("/users/AmjadAAYD")
    repos = [r for r in api("/users/AmjadAAYD/repos?per_page=100") if not r["fork"]]
    stats = {"followers": u["followers"], "stars": sum(r["stargazers_count"] for r in repos), "repos": len(repos) - 1}
except Exception:
    stats = {"followers": 0, "stars": 9, "repos": 7}
stamp = datetime.datetime.utcnow().strftime("%d %b %Y").upper()

SW = 620
pts = []
for x in range(0, SW + 1, 5):
    d = 0
    if 270 <= x <= 350:
        d = 24 * math.sin((x - 270) / 80 * math.pi) ** 0.5
    pts.append((x, 150 + d + math.sin(x / 31) * 2.5))
P = " ".join(f"{x},{y:.1f}" for x, y in pts)
D = "M" + " L".join(f"{x} {y:.1f}" for x, y in pts)
css = ('.cv{stroke-dasharray:100;animation:cd 8s linear infinite}@keyframes cd{0%{stroke-dashoffset:100}90%,100%{stroke-dashoffset:0}}'
       f'.rider{{offset-path:path("{D}");offset-distance:0%;animation:rd 8s linear infinite}}'
       '@keyframes rd{0%{offset-distance:0%}90%,100%{offset-distance:100%}}'
       '.tw{animation:tw 3s ease-in-out infinite}@keyframes tw{50%{opacity:.2}}'
       f'.pln{{animation:pn 8s linear infinite}}@keyframes pn{{0%{{transform:translateX(0)}}90%,100%{{transform:translateX({SW}px)}}}}'
       '.star{animation:sd 8s linear infinite}@keyframes sd{0%,42%{opacity:1}48%,56%{opacity:.55}62%,100%{opacity:1}}'
       '.shoot{animation:sh 9s linear infinite}@keyframes sh{0%,70%{transform:translate(0,0);opacity:0}72%{opacity:1}85%{transform:translate(260px,110px);opacity:0}100%{opacity:0}}'
       '.glow{animation:gl 4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}@keyframes gl{50%{transform:scale(1.15)}}'
       '.row{animation:rw 8s ease-out infinite}@keyframes rw{0%{opacity:0;transform:translateX(14px)}10%,90%{opacity:1;transform:none}100%{opacity:0}}'
       '.live{animation:lv 1.6s ease-in-out infinite}@keyframes lv{50%{opacity:.25}}'
       '.sweep{animation:sw 4s linear infinite}@keyframes sw{from{transform:translateX(0)}to{transform:translateX(300px)}}')
body = ('<defs><radialGradient id="sg"><stop offset="0" stop-color="#fff6d6" stop-opacity=".55"/><stop offset="1" stop-color="#f2c94c" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="swp" x1="0" x2="1"><stop offset="0" stop-color="#5eead4" stop-opacity="0"/><stop offset="1" stop-color="#5eead4" stop-opacity=".9"/></linearGradient>'
        '<clipPath id="fc"><rect width="960" height="240" rx="12"/></clipPath><clipPath id="sky"><rect width="620" height="240"/></clipPath></defs>'
        '<g clip-path="url(#fc)"><rect width="960" height="240" fill="#0d1117"/><g clip-path="url(#sky)">')
for i, (x, y) in enumerate([(50, 26), (140, 60), (230, 20), (420, 34), (520, 24), (580, 70), (90, 110), (480, 100), (350, 14), (20, 70)]):
    body += f'<circle cx="{x}" cy="{y}" r="1.5" fill="#7d8590" class="tw" style="animation-delay:{i * .4}s"/>'
body += '<g class="shoot"><line x1="40" y1="20" x2="12" y2="8" stroke="#e6edf3" stroke-width="1.5" stroke-linecap="round" opacity=".8"/><circle cx="40" cy="20" r="2" fill="#fff"/></g>'
body += ('<g class="star"><circle cx="310" cy="62" r="38" fill="url(#sg)" class="glow"/><circle cx="310" cy="62" r="13" fill="#f2c94c"/></g>'
         '<g class="pln"><circle cx="0" cy="62" r="7" fill="#0d1117" stroke="#30363d"/></g>')
body += (f'<polyline points="{P}" fill="none" stroke="#21262d" stroke-width="2"/>'
         f'<polyline points="{P}" pathLength="100" fill="none" stroke="{A}" stroke-width="2" class="cv"/>'
         f'<circle r="5" fill="#fff" class="rider"/><circle r="10" fill="{A}" opacity=".25" class="rider"/>')
body += ('<text x="310" y="204" text-anchor="middle" class="s" font-size="19" fill="#e6edf3">If it has a baseline, it can be beaten.</text>'
         '<text x="310" y="224" text-anchor="middle" class="m" font-size="10" fill="#7d8590" letter-spacing="2">THANKS FOR STOPPING BY</text></g>')
# telemetry panel
body += ('<line x1="620" y1="20" x2="620" y2="220" stroke="#21262d"/>'
         f'<text x="652" y="42" class="m" font-size="11" fill="{A}" letter-spacing="2">TELEMETRY</text>'
         f'<circle cx="920" cy="38" r="4" fill="{A}" class="live"/><text x="910" y="42" text-anchor="end" class="m" font-size="10" fill="#7d8590">LIVE</text>'
         '<line x1="652" y1="56" x2="928" y2="56" stroke="#21262d"/>')
rows = [("FOLLOWERS", stats["followers"]), ("STARS EARNED", stats["stars"]), ("OWN PROJECTS", stats["repos"])]
for i, (lab, val) in enumerate(rows):
    y = 98 + i * 44
    body += (f'<g class="row" style="animation-delay:{i * .25}s"><text x="652" y="{y}" class="m" font-size="10" fill="#7d8590" letter-spacing="1.5">{lab}</text>'
             f'<text x="928" y="{y + 4}" text-anchor="end" class="s" font-size="30" font-weight="700" fill="#e6edf3">{val}</text>'
             f'<line x1="652" y1="{y + 14}" x2="928" y2="{y + 14}" stroke="#161b22"/></g>')
body += (f'<g clip-path="inset(0)"><rect x="652" y="{98 + 2 * 44 + 14}" width="60" height="2" fill="url(#swp)" class="sweep" style="transform-box:fill-box"/></g>'
         f'<text x="652" y="226" class="m" font-size="10" fill="#7d8590" letter-spacing="1">SYNCED {stamp}</text>'
         '</g><rect x=".5" y=".5" width="959" height="239" rx="12" fill="none" stroke="#30363d"/>')
open(f"{OUT}/assets/footer.svg", "w", encoding="utf-8").write(svg(960, 240, body, css, f"Telemetry: {stats['followers']} followers, {stats['stars']} stars, {stats['repos']} own projects"))
