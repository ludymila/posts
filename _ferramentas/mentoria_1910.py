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

# POST 2 — 12h · carrossel · estilo B (tweet): o que ela mostra na live (baseado nos slides da Mentoria Individual GPS)
T2 = 5
p2 = [
 page_b('<span class="tag">LIVE HOJE · 20H (BRASÍLIA)</span><h1>Hoje eu abro tudo sobre a <span class="v">Mentoria Individual GPS</span>.</h1><div class="lead">E por que um plano genérico não te leva até a aprovação →</div>', 1, T2),
 page_b('<span class="tag">O PROBLEMA</span><h2>O que mais atrasa a aprovação em TI</h2><p><b>01.</b> Perder tempo decidindo o que estudar</p><p><b>02.</b> Estudar muito o que <span class="hl">quase não cai</span></p><p><b>03.</b> Não saber onde está errando</p>', 2, T2),
 page_b('<span class="tag">O MÉTODO GPS</span><h2>Autoconhecimento é o que separa quem passa</h2><p>🔍 <b>Onde você está:</b> seus pontos fortes e, principalmente, os fracos</p><p>🧭 <b>Para onde vai:</b> a rota até o seu concurso e a sua meta</p><p>⚙️ <b>Recalculando:</b> seu desempenho mostra o desvio, e a gente <span class="hl">ajusta a rota</span></p>', 3, T2),
 page_b('<span class="tag">NA PRÁTICA</span><h2>Na Mentoria Individual você recebe:</h2><p>🗺️ Cronograma personalizado, montado por mim para o seu concurso</p><p>📊 Análise mensal + relatório na minha plataforma, a aprova.dev</p><p>💬 Meu acompanhamento pessoal</p><p>👥 Grupo exclusivo de mentorados</p>', 4, T2),
 page_b('<h2>É hoje.</h2><div class="box">📅 <b>Live:</b> hoje, 19/10, às 20h (horário de Brasília), exclusiva para o grupo VIP<br><br>⏳ <b>Mentoria Individual e bônus:</b> encerram hoje<br><br>Comenta <b>GPS</b> que eu te mando o link do grupo VIP.</div>', 5, T2),
]

# POST 3 — 17h · imagem única · estilo A (foto câmera): a live é hoje
p3 = [page_a(badge() + """
<h1>A live é <span class="c">hoje</span>, às <span class="v">20h</span> de Brasília</h1>
<div class="sub" style="margin-top:20px">Exclusiva para o grupo VIP</div>
<div class="card"><div class="t">Tudo sobre a Mentoria Individual GPS: o método, o acompanhamento e a plataforma</div>
<div class="d">E hoje é o último dia das inscrições e do bônus.</div></div>
<div class="sub">Comenta <b style="color:#22D3B6">GPS</b> e entra no grupo agora para receber o link.</div>
""", photo="fotos/ludy-sentada-azul.jpg")]

render(p1, OUT + "/post-1")
render(p2, OUT + "/post-2")
render(p3, OUT + "/post-3")
print("ok")
