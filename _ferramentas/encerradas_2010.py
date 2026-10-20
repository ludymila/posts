from render import *
OUT = "/home/claude/posts/2026-10-20"
# POST 4 — 9h (Brasília) · imagem única · estilo A: inscrições encerradas da Mentoria Individual
p4 = [page_a("""
<h1>Inscrições <span class="c">encerradas</span></h1>
<div class="sub" style="margin-top:18px">Mentoria Individual · método <b style="color:#6C4CF1">GPS</b></div>
<div class="card"><div class="d" style="font-size:32px;color:rgba(246,245,251,.92)">Obrigada a cada pessoa que confiou no método e garantiu sua vaga. Agora é com a gente: plano traçado, rota definida e foco na aprovação.</div></div>
<div class="sub">Me siga para ficar por dentro dos concursos de TI.</div>
""", top_photo="fotos/ludy-trabalho-selfie.jpg", top_h=780)]
render(p4, OUT + "/post-4")
print("ok")
