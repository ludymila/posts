from render import *
T = 5
p = [
 page_b('<span class="tag">ÚLTIMA CHAMADA</span><h1>As inscrições da minha <span class="v">Mentoria Individual</span> foram prorrogadas até amanhã.</h1><div class="lead">E amanhã às 20h (Brasília) tem live explicando tudo →</div>', 1, T),
 page_b('<h2>Na live eu vou te mostrar:</h2><p>✅ Como funciona a <span class="hl">Mentoria Individual</span>, do primeiro dia até a prova</p><p>✅ Como eu monto um <span class="hl">cronograma de estudos</span> para concursos de TI</p><p>✅ O método que usei para ser aprovada como <b>analista de TI em um tribunal federal</b></p>', 2, T),
 page_b('<h2>O método <span class="v">GPS</span></h2><p><b>G · Guia</b>: definir o objetivo e o tipo de concurso certo pra você</p><p><b>P · Planejamento</b>: cronograma personalizado, no seu ritmo</p><p><b>S · Sucesso</b>: acompanhamento por questões, metas e indicadores, recalculando a rota sempre que precisar</p>', 3, T),
 page_b('<h2>Na Mentoria Individual você tem:</h2><p>🎯 Preparatório personalizado para a <b>sua</b> meta</p><p>🗺️ Cronograma estratégico com o método GPS</p><p>📊 Plataforma com relatório mensal de desempenho</p><p>💬 Grupo exclusivo de mentorados</p>', 4, T),
 page_b('<h2>Anota aí:</h2><div class="box">📅 <b>Live:</b> segunda, 19/10, às 20h (Brasília) · 19h (Manaus)<br><br>⏳ <b>Inscrições:</b> só até segunda, 19/10<br><br>Comenta <b>MENTORIA</b> que eu te mando o link da live e das inscrições.</div>', 5, T),
]
render(p, "/home/claude/posts/2026-10-18/post-4")
print("ok")
