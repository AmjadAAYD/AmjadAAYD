import os, re
OUT = os.environ["OUT"]
NAVY = "#0b1d45"
os.makedirs(f"{OUT}/assets/bg", exist_ok=True)


def read(p):
    return open(f"{OUT}/assets/{p}.svg", encoding="utf-8").read()


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
    r = 18
    # backdrop path with optional rounded top / bottom corners
    tl = r if round_top else 0
    bl = r if round_bottom else 0
    d = (f"M{tl} 0 H{out_w - tl} " + (f"A{tl} {tl} 0 0 1 {out_w} {tl} " if tl else "") +
         f"V{H - bl} " + (f"A{bl} {bl} 0 0 1 {out_w - bl} {H} " if bl else "") +
         f"H{bl} " + (f"A{bl} {bl} 0 0 1 0 {H - bl} " if bl else "") + f"V{tl} " + (f"A{tl} {tl} 0 0 1 {tl} 0 " if tl else "") + "Z")
    yoff = CUR['y']
    blobs = ""
    for (bx, by, br, bc, bo) in BLOBS:
        blobs += f'<circle cx="{bx - xoff}" cy="{by - yoff}" r="{br}" fill="url(#g{bc})" opacity="{bo}"/>'
    bgd = ('<defs>'
           '<radialGradient id="gT"><stop offset="0" stop-color="#2dd4bf"/><stop offset="1" stop-color="#2dd4bf" stop-opacity="0"/></radialGradient>'
           '<radialGradient id="gV"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>'
           '<radialGradient id="gB"><stop offset="0" stop-color="#3b82f6"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>'
           f'<pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse" patternTransform="translate({-(xoff % 40)} {-(yoff % 40)})">'
           '<path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>'
           f'<clipPath id="pg"><path d="{d}"/></clipPath></defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {out_w} {H:.2f}" width="{out_w}" height="{H:.2f}">'
           f'{bgd}<path d="{d}" fill="#060a1a"/><g clip-path="url(#pg)">{blobs}<rect width="{out_w}" height="{H:.2f}" fill="url(#gr)"/></g>{s}</svg>')
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
img = lambda n, alt, w="100%": f'<img src="assets/bg/{n}.svg" alt="{alt}" width="{w}" align="top">'
card = lambda n: f'<a href="https://github.com/AmjadAAYD/{n}"><img src="assets/bg/p-{n}.svg" alt="{n}" width="50%" align="top"></a>'
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
md = '<p align="center">' + "".join(parts) + '</p>\n\n<p align="center">\n  <img src="https://hits.sh/github.com/AmjadAAYD/profile.svg?style=flat-square&label=profile%20views&color=5eead4&labelColor=0b1d45" alt="Profile views">\n</p>\n'
open(f"{OUT}/README.md", "w", encoding="utf-8").write(md)
