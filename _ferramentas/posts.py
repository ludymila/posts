from render import *

OUT = "/home/claude/posts/2026-10-18"

# POST 1 — imagem única, estilo A (15h): concursos de TI no Amazonas
p1 = [page_a(badge() + """
<h1>2 concursos de <span class="c">TI</span> no <span class="v">Amazonas</span> pra ficar de olho</h1>
<div class="card"><div class="k">TCE AM · autorizado</div><div class="t">Auditor de Controle Externo – TI</div><div class="d">Inicial de R$ 11.534,07 · vagas a definir</div></div>
<div class="card"><div class="k">CGE AM · comissão formada</div><div class="t">Auditor de Controle Interno – TI</div><div class="d">5 vagas · R$ 13.700,00</div></div>
""", src="Fonte: Estratégia Concursos (atualização de 09/09/2026). Sem edital publicado até o momento.")]

# POST 2 — carrossel estilo A (17h): TI em tribunal
T2 = 6
p2 = [
 page_a(badge() + '<h1>Como é trabalhar com <span class="c">TI</span> em um <span class="v">tribunal</span>?</h1><div class="sub">O que ninguém te conta antes de escolher esse caminho →</div>', 1, T2),
 page_a('<h2>Primeiro: <span class="c">não</span> é só "dar suporte"</h2><p>Tribunal é órgão com <b>muito sistema</b>: processo eletrônico, portais, bases de dados, integrações. Tudo isso precisa de gente de TI.</p>', 2, T2),
 page_a('<h2>As frentes de trabalho</h2><div class="card"><div class="t">Desenvolvimento</div><div class="d">sistemas internos e serviços pro cidadão</div></div><div class="card"><div class="t">Infra e cloud</div><div class="d">servidores, redes, alta disponibilidade</div></div><div class="card"><div class="t">Segurança e dados</div><div class="d">proteção da informação, LGPD, BI</div></div>', 3, T2),
 page_a('<h2>O que muda em relação à iniciativa privada</h2><p>Projetos de <b>longo prazo</b>, rotina mais previsível e a chance de construir carreira sem trocar de empresa a cada 2 anos.</p>', 4, T2),
 page_a('<h2>O que <span class="v">não</span> muda</h2><p>Você continua estudando tecnologia: IA, nuvem, segurança, arquitetura. Os editais cobram isso, e o dia a dia também.</p>', 5, T2),
 page_a('<h2>Quer seguir esse caminho com um <span class="c">plano</span>?</h2><p>Foi o método <b>GPS</b> que me levou até aqui. Comenta <b class="c">TRIBUNAL</b> que eu te mando o link do meu grupo no WhatsApp.</p>', 6, T2),
]

# POST 3 — carrossel estilo B tweet (19h): 5 erros
T3 = 7
p3 = [
 page_b('<h1>Dev, para de estudar pra concurso de TI como se fosse <span class="v">faculdade</span>.</h1><div class="lead">São 5 erros que eu vejo toda semana na mentoria.</div>', 1, T3),
 page_b('<span class="tag">ERRO 1</span><h2>Estudar todas as matérias do mesmo jeito</h2><p>O edital tem peso. Matéria que vale mais questões merece mais horas. Comece pelo que <span class="hl">mais pontua</span>.</p>', 2, T3),
 page_b('<span class="tag">ERRO 2</span><h2>Ler teoria por semanas antes de fazer questões</h2><p>Questão não é o fim do estudo, é o meio. Ela mostra o que a banca cobra e onde você erra.</p>', 3, T3),
 page_b('<span class="tag">ERRO 3</span><h2>Ignorar a banca</h2><p>Cada banca tem um estilo. Certo/errado é um jogo, múltipla escolha é outro. Treine no formato da sua prova.</p>', 4, T3),
 page_b('<span class="tag">ERRO 4</span><h2>Deixar as matérias "de fora da TI" pro final</h2><p>Português e legislação eliminam muita gente boa em TI. Elas entram no ciclo desde o primeiro dia.</p>', 5, T3),
 page_b('<span class="tag">ERRO 5</span><h2>Não revisar</h2><p>Sem revisão programada, você estuda o mesmo assunto três vezes do zero. Revisão é o que transforma hora estudada em ponto.</p>', 6, T3),
 page_b('<h2>Estudar muito não é o mesmo que estudar <span class="v">na direção certa</span>.</h2><div class="box">É isso que o método <b>GPS</b> resolve.<br>Comenta <b>GPS</b> que eu te mando o link do meu grupo no WhatsApp.</div>', 7, T3),
]

render(p1, OUT + "/post-1")
render(p2, OUT + "/post-2")
render(p3, OUT + "/post-3")
print("ok")
