from render import *

OUT = "/home/claude/posts/2026-10-19"

# POST 1 — 10h · imagem única · estilo A (foto ampulheta): último dia
p1 = [page_a(badge() + """
<h1>Último dia: <span class="v">Mentoria Individual</span> e bônus <span class="c">encerram hoje</span></h1>
<div class="card"><div class="k">Só até hoje, 19/10</div>
<div class="d">📲 Acompanhamento direto comigo pelo WhatsApp<br>
📚 Português, Inglês, RLM, Constitucional e Administrativo<br>
💳 Condições especiais no pagamento, com bônus exclusivos</div></div>
<div class="sub">Live hoje às 20h (Brasília) no grupo VIP · Comenta <b style="color:#22D3B6">GPS</b> que eu te mando o link</div>
""", photo="fotos/ampulheta-1.jpg")]

# POST 2 — 12h · carrossel · estilo B (tweet): o que vou mostrar na live / GPS na prática
T2 = 5
p2 = [
 page_b('<span class="tag">LIVE HOJE · 20H (BRASÍLIA)</span><h1>Hoje eu vou abrir como monto um <span class="v">cronograma de estudos</span> do zero.</h1><div class="lead">O mesmo método que me aprovou como analista de TI em um tribunal federal →</div>', 1, T2),
 page_b('<span class="tag">G · GUIA</span><h2>Antes de estudar, escolher o destino</h2><p>Tribunais, controle, bancos ou área fiscal? Cada caminho cobra coisas diferentes. Na live eu mostro como escolher o seu <span class="hl">a partir do edital</span>, e não do achismo.</p>', 2, T2),
 page_b('<span class="tag">P · PLANEJAMENTO</span><h2>Um cronograma que cabe na sua rotina</h2><p>Peso de cada matéria, horas que você realmente tem e revisões programadas. Vou montar um <span class="hl">exemplo ao vivo</span>.</p>', 3, T2),
 page_b('<span class="tag">S · SUCESSO</span><h2>Medir para não estudar no escuro</h2><p>Percentual de acertos por assunto, metas semanais e o momento certo de <span class="hl">recalcular a rota</span>.</p>', 4, T2),
 page_b('<h2>É hoje.</h2><div class="box">📅 <b>Live:</b> hoje, 19/10, às 20h (Brasília) · 19h (Manaus), exclusiva para o grupo VIP<br><br>⏳ <b>Mentoria Individual e bônus:</b> encerram hoje<br><br>Comenta <b>GPS</b> que eu te mando o link do grupo VIP.</div>', 5, T2),
]

# POST 3 — 17h · imagem única · estilo A (foto câmera): a live é hoje
p3 = [page_a(badge() + """
<h1>A live é <span class="c">hoje</span>, às <span class="v">20h</span> de Brasília</h1>
<div class="sub" style="margin-top:20px">19h em Manaus · exclusiva para o grupo VIP</div>
<div class="card"><div class="t">Como funciona a Mentoria Individual + como eu monto o cronograma com o método GPS</div>
<div class="d">E hoje é o último dia das inscrições e do bônus.</div></div>
<div class="sub">Comenta <b style="color:#22D3B6">GPS</b> e entra no grupo agora para receber o link.</div>
""", photo="fotos/camera-tripe.jpg")]

render(p1, OUT + "/post-1")
render(p2, OUT + "/post-2")
render(p3, OUT + "/post-3")
print("ok")
