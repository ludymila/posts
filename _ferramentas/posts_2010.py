from render import *

OUT = "/home/claude/posts/2026-10-20"

# POST 1 — 13h (Brasília) · imagem única · estilo A: TCE-GO inscrições abertas (nível médio, TI)
p1 = [page_a(badge() + """
<h1>Inscrições abertas: <span class="c">TCE-GO</span> com <span class="v">10 vagas de TI</span></h1>
<div class="card"><div class="k">Técnico de Controle Externo · nível médio</div>
<div class="t">Inicial: R$ 11.862,19</div>
<div class="d">Final de carreira: ainda não divulgado<br>Banca FCC · taxa de R$ 100</div></div>
<div class="card"><div class="k">Prazos</div>
<div class="d">Inscrições até 06/11/2026 · prova em 17/01/2027, em Goiânia</div></div>
""", photo="fotos/sala-aula.jpg", src="Fonte: JC Concursos (25/08/2026).")]

# POST 2 — 19h (Brasília) · carrossel · estilo B: benefícios no Judiciário federal além do salário
T2 = 5
p2 = [
 page_b('<h1>O salário não é tudo: os <span class="v">auxílios</span> de quem trabalha no Judiciário federal.</h1><div class="lead">Valores de referência do Poder Judiciário da União (TRTs, TREs, TST etc.) →</div>', 1, T2),
 page_b('<span class="tag">AUXÍLIO-ALIMENTAÇÃO</span><h2>R$ 1.860,51 por mês</h2><p>Pago a todos os servidores, independentemente do cargo.</p>', 2, T2),
 page_b('<span class="tag">ADICIONAL DE QUALIFICAÇÃO</span><h2 style="margin-bottom:28px">Estudar vira aumento de salário</h2><p>🎓 Duas pós-graduações: <b>R$ 1.428,80</b> por mês</p><p>📚 Cursos de capacitação (treinamento): <b>R$ 428,64</b> por mês</p><p>🎓 Mestrado: <b>R$ 2.700,43</b> por mês</p><p>🎓 Doutorado: <b>R$ 3.857,76</b> por mês</p>', 3, T2),
 page_b('<span class="tag">AUXÍLIO-SAÚDE</span><h2>Até R$ 900,00 por mês</h2><p>Ajuda no custo do plano de saúde.</p><span class="tag" style="margin-top:30px">AUXÍLIO-CRECHE</span><h2>R$ 1.288,47 por mês</h2><p>Por filho pequeno, como assistência pré-escolar.</p>', 4, T2),
 page_b('<h2>Somando só esses itens:</h2><div class="box"><b>R$ 4.617,95 por mês</b> além do vencimento, no exemplo de um analista com 2 pós.<br><br>Me siga para mais dicas de concursos e carreira de TI.</div>', 5, T2),
]

# POST 3 — 13h (Brasília) · imagem única · estilo A: TJ-PB inscrições abertas (substitui o TCE-GO nesse horário)
p3 = [page_a(badge() + """
<h1>Inscrições abertas: <span class="c">TJ-PB</span> com <span class="v">20 vagas de TI</span></h1>
<div class="card"><div class="k">Analista Judiciário · TI</div>
<div class="t">Inicial: R$ 11.526,14 · Final: R$ 19.212,35</div>
<div class="d">Vencimento + auxílio-alimentação + auxílio-saúde</div></div>
<div class="card"><div class="k">Prazos</div>
<div class="d">Inscrições de 20/10 a 18/11/2026 · prova em 24/01/2027<br>Banca FGV</div></div>
""", photo="fotos/tjpb-sede.jpg")]

render(p3, OUT + "/post-3")
render(p1, OUT + "/post-1")
render(p2, OUT + "/post-2")
print("ok")
