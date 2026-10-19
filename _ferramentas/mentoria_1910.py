from render import *

OUT = "/home/claude/posts/2026-10-19"

# POST 1 — 10h · imagem única · estilo A (foto ampulheta): último dia
p1 = [page_a(badge() + """
<h1>Último dia: <span class="v">Mentoria Individual</span> e bônus <span class="c">encerram hoje</span></h1>
<div class="card"><div class="k">Só até hoje, 19/10</div>
<div class="d">📲 Acompanhamento direto comigo pelo WhatsApp<br>
📚 PDFs e videoaulas dos principais assuntos de TI<br>
💳 Condições especiais no pagamento, com bônus exclusivos</div></div>
<div class="sub">Live hoje às 20h (Brasília) no grupo VIP · Comenta <b style="color:#22D3B6">GPS</b> que eu te mando o link</div>
""", photo="fotos/ampulheta-1.jpg")]

# POST 2 — 12h · carrossel · estilo B (tweet): 3 coisas que mais atrasam a aprovação (conteúdo de valor + live)
T2 = 5
p2 = [
 page_b('<span class="tag">LIVE HOJE · 20H (BRASÍLIA)</span><h1>As 3 coisas que mais <span class="v">atrasam a aprovação</span> em concursos de TI.</h1><div class="lead">Se você se identificar com alguma, salva esse post →</div>', 1, T2),
 page_b('<span class="tag">01</span><h2>Perder tempo decidindo o que estudar</h2><p>Edital gigante, mil materiais e nenhum plano claro. Você senta pra estudar e gasta a energia <span class="hl">escolhendo por onde começar</span>.</p>', 2, T2),
 page_b('<span class="tag">02</span><h2>Estudar muito o que quase não cai</h2><p>Horas e horas investidas em assunto que a banca mal cobra, enquanto o que mais pontua fica pra depois.</p>', 3, T2),
 page_b('<span class="tag">03</span><h2>Não saber onde está errando</h2><p>Sem dados, você repete os mesmos erros prova após prova.</p><p>É aqui que meu trabalho com <span class="hl">análise de dados</span> entra: os indicadores de desempenho mostram exatamente onde ajustar a rota.</p>', 4, T2),
 page_b('<h2>Hoje, às 20h (Brasília), na live:</h2><p>✅ Dicas de estudo para fugir dessas 3 armadilhas</p><p>✅ Os erros que eu cometi quando comecei a estudar</p><p>✅ Como eu uso indicadores para guiar cada aluno</p><div class="box">A live é exclusiva para o grupo VIP.<br>Comenta <b>GPS</b> que eu te mando o link.</div>', 5, T2),
]

# POST 3 — 17h · imagem única · estilo A (foto câmera): a live é hoje
p3 = [page_a(badge() + """
<h1>A live é <span class="c">hoje</span>, às <span class="v">20h</span> de Brasília</h1>
<div class="sub" style="margin-top:20px">Exclusiva para o grupo VIP</div>
<div class="card"><div class="t">Tudo sobre a Mentoria Individual GPS: o método, o acompanhamento e a plataforma</div>
<div class="d">E hoje é o último dia das inscrições e do bônus.</div></div>
<div class="sub">Comenta <b style="color:#22D3B6">GPS</b> e entra no grupo agora para receber o link.</div>
""", photo="fotos/ludy-sentada-azul.jpg")]

# POST 4 — 9h (Brasília) · imagem única · estilo A (foto da Ludy): aviso de data e horário da live
p4 = [page_a(badge() + """
<h1>Hoje tem <span class="c">live</span></h1>
<div style="font-family:'Inter Display';font-weight:800;font-size:46px;line-height:1.15;color:#22D3B6;margin:26px 0 6px">As 3 coisas que mais atrasam sua aprovação em concurso</div>
<div class="card"><div class="k">Segunda-feira, 19/10 · 20h, horário de Brasília</div>
<div class="d">Apenas para o grupo VIP. Dicas de estudo e tudo sobre a Mentoria Individual com o método GPS.</div></div>
<div class="sub">Comenta <b style="color:#22D3B6">GPS</b> e entra no grupo para receber o link.</div>
""", photo="fotos/ludy-bracos-cruzados-clara.jpg")]

render(p4, OUT + "/post-4")
render(p1, OUT + "/post-1")
render(p2, OUT + "/post-2")
render(p3, OUT + "/post-3")
print("ok")
