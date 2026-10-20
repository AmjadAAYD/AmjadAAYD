import os, re
OUT = os.environ["OUT"]
NAVY = "#0b1d45"
os.makedirs(f"{OUT}/assets/bg", exist_ok=True)


def read(p):
    return open(f"{OUT}/assets/{p}.svg", encoding="utf-8").read()



import random, math
NB_CSS = ('.da{animation:da 38s ease-in-out infinite alternate}.db{animation:db 46s ease-in-out infinite alternate}.dc{animation:dc 52s ease-in-out infinite alternate}'
          '@keyframes da{to{transform:translate(60px,26px)}}@keyframes db{to{transform:translate(-70px,34px)}}@keyframes dc{to{transform:translate(44px,-46px)}}'
          '.gr{animation:gr 140s linear infinite}@keyframes gr{to{transform:rotate(360deg)}}'
          '.t0{animation:tw 3s ease-in-out infinite}.t1{animation:tw 4.5s ease-in-out infinite;animation-delay:-1.2s}.t2{animation:tw 6s ease-in-out infinite;animation-delay:-3s}'
          '@keyframes tw{50%{opacity:.15}}'
          '.sh{animation:sh 11s linear infinite}@keyframes sh{0%,80%{transform:translate(0,0);opacity:0}82%{opacity:1}94%{transform:translate(300px,140px);opacity:0}100%{opacity:0}}'
          '@media (prefers-reduced-motion:reduce){*{animation:none!important}}')
CLOUDS = [(200, 300, 560, 320, "#7c3aed", .55, "da"), (860, 700, 520, 300, "#db2777", .42, "db"), (150, 1100, 560, 320, "#2563eb", .55, "dc"),
          (880, 1500, 500, 300, "#0d9488", .38, "da"), (250, 1950, 580, 320, "#6d28d9", .55, "db"), (850, 2400, 540, 300, "#be185d", .4, "dc"),
          (200, 2850, 560, 320, "#1d4ed8", .55, "da"), (850, 3250, 520, 300, "#7c3aed", .45, "db"), (300, 3700, 560, 320, "#db2777", .4, "dc")]
LANES = [(480, 900, 420, 130, -12), (560, 1800, 460, 120, 10), (420, 2650, 440, 130, -8), (600, 3500, 440, 120, 12)]
GALAXIES = [(780, 400, 150, -25, "#c4b5fd"), (170, 1380, 130, 30, "#7dd3fc"), (830, 2150, 160, -15, "#f0abfc"), (190, 3050, 140, 20, "#fde68a")]
_r = random.Random(11)
STARS = [(_r.uniform(0, 1000), _r.uniform(0, 4300), _r.choice([.6, .8, 1.0, 1.3, 1.8]), _r.choice(["#ffffff", "#cfe3ff", "#ffe9c4", "#e9d5ff"]), _r.random()) for _ in range(1500)]
_g = random.Random(5)
GAL_DOTS = {}
for gi, (gx, gy, gr, gt, gc) in enumerate(GALAXIES):
    dots = []
    for arm in range(2):
        for i in range(90):
            t = i / 90
            th = arm * math.pi + t * 3.4 * math.pi + _g.uniform(-.18, .18)
            rr = t * gr * (1 + _g.uniform(-.08, .08))
            dots.append((rr * math.cos(th), rr * math.sin(th), _g.uniform(.7, 1.9) * (1.1 - t * .5), (1 - t) * .85 + .1))
    GAL_DOTS[gi] = dots


def nebula(xoff, yoff, w, h, d):
    x0, y0, x1, y1 = xoff, yoff, xoff + w, yoff + h
    o = ('<defs>'
         '<radialGradient id="kK"><stop offset="0" stop-color="#000" stop-opacity=".8"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
         '<radialGradient id="kC"><stop offset="0" stop-color="#fff7e0" stop-opacity=".95"/><stop offset=".35" stop-color="#ffd9a0" stop-opacity=".35"/><stop offset="1" stop-color="#ffd9a0" stop-opacity="0"/></radialGradient>')
    cols = sorted({c[4] for c in CLOUDS})
    for c in cols:
        o += f'<radialGradient id="n{c[1:]}"><stop offset="0" stop-color="{c}" stop-opacity="1"/><stop offset=".55" stop-color="{c}" stop-opacity=".35"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
    o += f'<clipPath id="pg"><path d="{d}"/></clipPath></defs><style>{NB_CSS}</style>'
    o += f'<path d="{d}" fill="#04050f"/><g clip-path="url(#pg)">'
    for (cx, cy, rx, ry, col, op, cl) in CLOUDS:
        if cx + rx < x0 or cx - rx > x1 or cy + ry < y0 or cy - ry > y1:
            continue
        o += f'<g class="{cl}"><ellipse cx="{cx - x0:.0f}" cy="{cy - y0:.0f}" rx="{rx}" ry="{ry}" fill="url(#n{col[1:]})" opacity="{op}"/></g>'
    for (cx, cy, rx, ry, rot) in LANES:
        if cx + rx < x0 or cx - rx > x1 or cy + ry < y0 or cy - ry > y1:
            continue
        o += f'<ellipse cx="{cx - x0:.0f}" cy="{cy - y0:.0f}" rx="{rx}" ry="{ry}" fill="url(#kK)" transform="rotate({rot} {cx - x0:.0f} {cy - y0:.0f})"/>'
    for (x, y, r, c, rnd) in STARS:
        if x < x0 - 2 or x > x1 + 2 or y < y0 - 2 or y > y1 + 2:
            continue
        cls = "" if rnd < .55 else f' class="t{int(rnd * 100) % 3}"'
        o += f'<circle cx="{x - x0:.0f}" cy="{y - y0:.0f}" r="{r}" fill="{c}" opacity="{.5 + rnd * .5:.2f}"{cls}/>'
    for gi, (gx, gy, gr, gt, gc) in enumerate(GALAXIES):
        if gx + gr * 1.1 < x0 or gx - gr * 1.1 > x1 or gy + gr * 1.1 < y0 or gy - gr * 1.1 > y1:
            continue
        o += f'<g transform="translate({gx - x0:.0f} {gy - y0:.0f}) rotate({gt}) scale(1 .42)">'
        o += f'<circle r="{gr * .55:.0f}" fill="url(#kC)" opacity=".7"/><g class="gr">'
        for (dx, dy, dr, dop) in GAL_DOTS[gi]:
            o += f'<circle cx="{dx:.0f}" cy="{dy:.0f}" r="{dr:.1f}" fill="{gc}" opacity="{dop:.2f}"/>'
        o += '</g></g>'
    # shooting stars
    for k, (sx, sy) in enumerate([(120, 640), (700, 1700), (300, 2500), (760, 3300)]):
        if y0 <= sy <= y1 and x0 <= sx <= x1:
            o += f'<g class="sh" style="animation-delay:{k * 2.7}s"><line x1="{sx - x0}" y1="{sy - y0}" x2="{sx - x0 - 40}" y2="{sy - y0 - 18}" stroke="#fff" stroke-width="1.5" stroke-linecap="round" opacity=".85"/></g>'
    o += '</g>'
    return o

CUR = {'y': 0}
BLOBS = [(160, 120, 520, 'T', .30), (900, 520, 560, 'V', .38), (120, 980, 560, 'B', .34), (880, 1500, 560, 'T', .26), (200, 2000, 580, 'V', .34), (860, 2450, 560, 'B', .34), (150, 2900, 560, 'T', .26), (880, 3300, 560, 'V', .3), (200, 3700, 560, 'B', .3)]


def wrap(name, src, inner_w, pad_x, top, bottom, out_w, round_top=False, round_bottom=False, inner_h=None, xoff=0, advance=True):
    s = read(src)
    m = re.match(r'<svg [^>]*viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    vw, vh = float(m.group(1)), float(m.group(2))
    ih = inner_h or inner_w * vh / vw
    H = top + ih + bottom
    # re-open the svg tag as a nested one
    s = re.sub(r'<svg [^>]*?(viewBox="[^"]+")[^>]*?(role="img"[^>]*)>',
               lambda mm: f'<svg x="{pad_x}" y="{top}" width="{inner_w}" height="{ih:.2f}" {mm.group(1)} {mm.group(2)}>', s, count=1)
    s = s.replace('xmlns="http://www.w3.org/2000/svg"', "")
    s = s.replace('fill="#0d1117"', 'fill="#070a18" fill-opacity=".74"')
    r = 18
    # backdrop path with optional rounded top / bottom corners
    tl = r if round_top else 0
    bl = r if round_bottom else 0
    d = (f"M{tl} 0 H{out_w - tl} " + (f"A{tl} {tl} 0 0 1 {out_w} {tl} " if tl else "") +
         f"V{H - bl} " + (f"A{bl} {bl} 0 0 1 {out_w - bl} {H} " if bl else "") +
         f"H{bl} " + (f"A{bl} {bl} 0 0 1 0 {H - bl} " if bl else "") + f"V{tl} " + (f"A{tl} {tl} 0 0 1 {tl} 0 " if tl else "") + "Z")
    yoff = CUR['y']
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {out_w} {H:.2f}" width="{out_w}" height="{H:.2f}">'
           f'{nebula(xoff, yoff, out_w, H, d)}{s}</svg>')
    if advance:
        CUR['y'] += H
    open(f"{OUT}/assets/bg/{name}.svg", "w", encoding="utf-8").write(svg)
    return H


FULL = dict(inner_w=960, pad_x=20, out_w=1000)
wrap("hero", "hero", top=20, bottom=8, round_top=True, **FULL)
wrap("x20ctl", "x20ctl-card", top=8, bottom=8, **FULL)
wrap("numbers-h", "h-numbers", top=22, bottom=2, **FULL)
wrap("numbers", "numbers", top=2, bottom=8, **FULL)
wrap("about-h", "h-about", top=22, bottom=2, **FULL)
wrap("about", "about", top=2, bottom=8, **FULL)
wrap("does-h", "h-does", top=22, bottom=2, **FULL)
wrap("does", "does", top=2, bottom=8, **FULL)
wrap("work-h", "h-work", top=22, bottom=2, **FULL)
CP = ["exoplanet-transit-detection", "weather-data-pipeline", "sma-veille-technologique",
      "arima-vs-lstm-forecasting", "pneumonia-detection-pytorch", "spam-detection-nlp"]
for k in range(0, 6, 2):
    h = wrap("p-" + CP[k], "projects/" + CP[k], inner_w=480, pad_x=10, top=6, bottom=6, out_w=500, xoff=0, advance=False)
    wrap("p-" + CP[k + 1], "projects/" + CP[k + 1], inner_w=480, pad_x=10, top=6, bottom=6, out_w=500, xoff=500, advance=False)
    CUR['y'] += h
wrap("stack-h", "h-stack", top=22, bottom=2, **FULL)
wrap("stack", "stack", top=2, bottom=8, **FULL)
wrap("footer", "footer", top=16, bottom=22, round_bottom=True, **FULL)

# README
img = lambda n, alt, w="100%": f'<img src="assets/bg/{n}.svg?v=5" alt="{alt}" width="{w}" align="top">'
card = lambda n: f'<a href="https://github.com/AmjadAAYD/{n}"><img src="assets/bg/p-{n}.svg?v=5" alt="{n}" width="50%" align="top"></a>'
projs = ["exoplanet-transit-detection", "weather-data-pipeline", "sma-veille-technologique",
         "arima-vs-lstm-forecasting", "pneumonia-detection-pytorch", "spam-detection-nlp"]
parts = [img("hero", "Amjad Aayd: data science, AI and hardware tooling"),
         '<a href="https://github.com/AmjadAAYD/x20ctl">' + img("x20ctl", "X20CTL: open configuration library for EasySMX X20 controllers") + '</a>',
         img("numbers-h", "By the numbers"), img("numbers", "9 stars on X20CTL, 7 public projects, 43,848 hourly readings forecast, 87.5% pneumonia test accuracy"),
         img("about-h", "Who I am"), img("about", "amjad aayd, data science and AI student in Morocco"),
         img("does-h", "What I do"), img("does", "Forecast, reverse engineer, build pipelines, chase signals"),
         img("work-h", "Selected work")] + [card(n) for n in projs] + \
        [img("stack-h", "Toolbox"), img("stack", "Python, PyTorch, scikit-learn, LangGraph, Airflow, Docker, C#, C++"),
         img("footer", "If it has a baseline, it can be beaten.")]
md = '<p align="center">' + "".join(parts) + '</p>\n'
open(f"{OUT}/README.md", "w", encoding="utf-8").write(md)
