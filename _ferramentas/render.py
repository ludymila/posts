import base64, sys, os
from playwright.sync_api import sync_playwright

SP = os.path.dirname(os.path.abspath(__file__))
AV = base64.b64encode(open(os.path.join(SP, "avatar.png"), "rb").read()).decode()

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:'Inter','Inter Display',sans-serif;-webkit-font-smoothing:antialiased}
.v{color:#6C4CF1}.c{color:#22D3B6}
"""

# ---------- Estilo A: fundo escuro tech + título forte ----------
A_CSS = BASE_CSS + """
body{background:#14112B;color:#F6F5FB;position:relative}
.bg{position:absolute;inset:0;
 background:
  radial-gradient(circle at 85% 12%, rgba(108,76,241,.55), transparent 42%),
  radial-gradient(circle at 10% 70%, rgba(34,211,182,.22), transparent 40%),
  linear-gradient(rgba(246,245,251,.05) 1px, transparent 1px) 0 0/60px 60px,
  linear-gradient(90deg, rgba(246,245,251,.05) 1px, transparent 1px) 0 0/60px 60px,
  #14112B}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,17,43,0) 30%,rgba(20,17,43,.95) 75%)}
.code{position:absolute;top:150px;left:80px;right:80px;font-family:'DejaVu Sans Mono',monospace;font-size:26px;line-height:1.7;color:rgba(246,245,251,.16);white-space:pre}
.top{position:absolute;top:56px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:3px;font-weight:600;color:rgba(246,245,251,.7)}
.pill{background:rgba(20,17,43,.55);border-radius:40px;padding:8px 22px;letter-spacing:1px}
.top span:first-child{background:rgba(20,17,43,.55);border-radius:40px;padding:8px 22px}
.content{position:absolute;left:80px;right:80px;bottom:110px}
.badge{display:inline-flex;align-items:center;gap:14px;background:rgba(246,245,251,.1);border:1px solid rgba(246,245,251,.2);border-radius:40px;padding:10px 24px 10px 10px;font-size:26px;font-weight:600;margin-bottom:36px}
.badge img{width:48px;height:48px;border-radius:50%}
h1{font-family:'Inter Display','Inter',sans-serif;font-weight:900;text-transform:uppercase;font-size:92px;line-height:.98;letter-spacing:-2px}
h2{font-family:'Inter Display','Inter',sans-serif;font-weight:800;font-size:68px;line-height:1.05;letter-spacing:-1px;margin-bottom:34px}
p{font-size:38px;line-height:1.4;color:rgba(246,245,251,.88)}
p b{color:#F6F5FB}
.sub{margin-top:30px;font-size:34px;color:rgba(246,245,251,.75)}
.num{font-family:'Inter Display';font-weight:900;font-size:150px;line-height:1;color:#22D3B6;margin-bottom:10px}
.card{background:rgba(246,245,251,.07);border:1px solid rgba(246,245,251,.16);border-radius:28px;padding:34px 38px;margin-top:22px}
.card .k{font-size:26px;letter-spacing:2px;text-transform:uppercase;color:#22D3B6;font-weight:700;margin-bottom:8px}
.card .t{font-size:40px;font-weight:700;line-height:1.2}
.card .d{font-size:30px;color:rgba(246,245,251,.8);margin-top:8px;line-height:1.35}
.src{position:absolute;left:80px;right:80px;bottom:48px;font-size:22px;color:rgba(246,245,251,.5)}
"""

CODE_BG = """def estudar(edital):
    for materia in edital.por_peso():
        questoes = banca.filtrar(materia)
        revisar(erros(questoes))
    return aprovacao  # GPS"""


def _photo_layer(photo):
    """photo: caminho local de um JPG/PNG (Canva ou Unsplash/Pexels). Fica escurecido com degradê para #14112B."""
    ext = "png" if photo.lower().endswith(".png") else "jpeg"
    b64 = base64.b64encode(open(photo, "rb").read()).decode()
    return (f'<div style="position:absolute;inset:0;background:url(data:image/{ext};base64,{b64}) center/cover"></div>'
            '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,17,43,.25) 0%,'
            'rgba(20,17,43,.55) 40%,rgba(20,17,43,.97) 72%)"></div>')


MINIMAL_BG = ('<div style="position:absolute;inset:0;background:#14112B"></div>'
  '<svg style="position:absolute;top:0;right:0" width="560" height="560" viewBox="0 0 560 560" fill="none">'
  '<circle cx="470" cy="90" r="300" stroke="#6C4CF1" stroke-opacity=".55" stroke-width="2"/>'
  '<circle cx="470" cy="90" r="200" stroke="#6C4CF1" stroke-opacity=".3" stroke-width="2"/>'
  '<circle cx="257" cy="302" r="9" fill="#22D3B6"/></svg>')


def page_a(inner, idx=None, total=None, src="", photo=None, top_photo=None, top_h=470, minimal=False):
    """Estilo A. photo=caminho: foto como fundo inteiro (capas). top_photo=caminho: foto no topo do slide
    (ex.: prédio do órgão), com o conteúdo embaixo. Sem nenhum dos dois: fundo tech."""
    pill = f'<span class="pill">{idx}/{total}</span>' if total else '<span></span>'
    if minimal:
        bg = MINIMAL_BG
    elif photo:
        bg = _photo_layer(photo)
    elif top_photo:
        ext = "png" if top_photo.lower().endswith(".png") else "jpeg"
        b64 = base64.b64encode(open(top_photo, "rb").read()).decode()
        bg = ('<div class="bg"></div>'
              f'<div style="position:absolute;left:0;right:0;top:0;height:{top_h}px;background:url(data:image/{ext};base64,{b64}) center/cover"></div>'
              f'<div style="position:absolute;left:0;right:0;top:0;height:{top_h}px;background:linear-gradient(180deg,rgba(20,17,43,.6) 0%,rgba(20,17,43,0) 22%,rgba(20,17,43,0) 70%,#14112B 100%)"></div>')
    else:
        bg = f'<div class="bg"></div><div class="code">{CODE_BG}</div><div class="fade"></div>'
    return f"""<html><head><style>{A_CSS}</style></head><body>
{bg}
<div class="top"><span>@LUDY.DEV</span>{pill}</div>
<div class="content">{inner}</div>
{f'<div class="src">{src}</div>' if src else ''}
</body></html>"""


def badge():
    return f'<div class="badge"><img src="data:image/png;base64,{AV}">@ludy.dev</div>'


# ---------- Estilo B: tweet (claro, como os carrosséis atuais) ----------
B_CSS = BASE_CSS + """
body{background:#F6F5FB;color:#14112B;padding:56px 66px}
.head{display:flex;align-items:center;gap:22px}
.head img{width:96px;height:96px;border-radius:50%}
.name{font-size:34px;font-weight:800;display:flex;align-items:center;gap:10px}
.chk{width:30px;height:30px;border-radius:50%;background:#6C4CF1;color:#fff;font-size:18px;display:inline-flex;align-items:center;justify-content:center}
.user{font-size:28px;color:#5d5a78}
.pill{margin-left:auto;background:#E7E4F7;color:#3d3a5c;border-radius:40px;padding:10px 24px;font-size:28px;font-weight:600}
.body{margin-top:90px}
h1{font-family:'Inter Display','Inter';font-weight:900;font-size:96px;line-height:1.05;letter-spacing:-2.5px}
h2{font-family:'Inter Display','Inter';font-weight:900;font-size:72px;line-height:1.08;letter-spacing:-1.5px;margin-bottom:40px}
p{font-size:40px;line-height:1.42;color:#2a2745;margin-bottom:26px}
.lead{font-size:40px;color:#5d5a78;margin-top:34px;line-height:1.35}
.tag{display:inline-block;background:#6C4CF1;color:#F6F5FB;font-weight:800;font-size:30px;border-radius:14px;padding:8px 20px;margin-bottom:34px;letter-spacing:1px}
.box{background:#14112B;color:#F6F5FB;border-radius:28px;padding:38px 42px;font-size:38px;line-height:1.4;margin-top:20px}
.box b{color:#22D3B6}
.hl{background:linear-gradient(transparent 60%, rgba(34,211,182,.45) 60%)}
"""


def page_b(inner, idx, total):
    return f"""<html><head><style>{B_CSS}</style></head><body>
<div class="head"><img src="data:image/png;base64,{AV}"><div>
<div class="name">Ludymila Lobo <span class="chk">✓</span></div><div class="user">@ludy.dev</div></div>
<span class="pill">{idx}/{total}</span></div>
<div class="body">{inner}</div></body></html>"""


def render(pages, outdir):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, html in enumerate(pages, 1):
            pg.set_content(html)
            pg.wait_for_timeout(150)
            pg.screenshot(path=os.path.join(outdir, f"slide_{i:02d}.png"))
        b.close()
