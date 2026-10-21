from render import *

# Plano "rumo aos 10 mil" — 21 a 30/10/2026. Horários de Brasília no nome da pasta.
OUT = "/home/claude/posts/2026-10-plano-10k"

def card(k, t, d=""):
    return f'<div class="card"><div class="k">{k}</div><div class="t">{t}</div>' + (f'<div class="d">{d}</div>' if d else '') + '</div>'

def seguir(extra=""):
    return f'<div class="card"><div class="t">Me siga para mais dicas de concursos e carreira de TI.</div>{extra}</div>'

POSTS = {}

# 1 — 21/10 18h · panorama inscrições abertas
T = 8
POSTS["21-18h"] = [
 page_a(badge() + '<h1><span class="c">5 concursos</span> de TI com inscrições abertas <span class="v">agora</span></h1><div class="sub">Do prazo mais curto ao mais longo. Arrasta →</div>', 1, T, minimal=True),
 page_a('<h2><span class="c">SEFAZ SP</span> · fecha 03/11</h2>' + card("Cargo", "APOFP · Ciência de Dados e TI", "20 vagas · qualquer graduação") + card("Remuneração", "Inicial: R$ 11.359,50", "Final de carreira: R$ 18 mil a R$ 20 mil") + card("Banca e prova", "FCC · 13/12/2026", "Em São Paulo (SP)"), 2, T, minimal=True),
 page_a('<h2><span class="c">CGU</span> · fecha 04/11</h2>' + card("Cargo", "Auditor Federal de Finanças e Controle · TI", "30 vagas · qualquer graduação") + card("Remuneração", "Inicial: R$ 20.000,00", "Final de carreira: R$ 36.694,00") + card("Banca e prova", "Cebraspe · 13/12/2026", "Nas 27 capitais"), 3, T, minimal=True),
 page_a('<h2><span class="c">TRT 8</span> · fecha 05/11</h2>' + card("Analista Judiciário · TI", "Inicial: R$ 18.801,39", "Final de carreira: R$ 26.845,74") + card("Técnico Judiciário · TI", "Inicial: R$ 12.537,22", "Final de carreira: R$ 17.440,22") + card("Banca e prova", "FCC · 17/01/2027", "Belém, Marabá, Santarém e Macapá"), 4, T, minimal=True),
 page_a('<h2><span class="c">TCE-GO</span> · fecha 06/11</h2>' + card("Cargo", "Técnico de Controle Externo · TI", "10 vagas · nível médio") + card("Remuneração", "Inicial: R$ 11.862,19", "Final de carreira: ainda não divulgado") + card("Banca e prova", "FCC · 17/01/2027", "Em Goiânia (GO)"), 5, T, minimal=True),
 page_a('<h2><span class="c">TJ-PB</span> · fecha 18/11</h2>' + card("Cargo", "Analista Judiciário · TI", "20 vagas") + card("Remuneração", "Inicial: R$ 11.526,14", "Final de carreira: R$ 19.212,35") + card("Banca e prova", "FGV · 24/01/2027", "Na Paraíba"), 6, T, minimal=True),
 page_a('<h2>Dá pra fazer <span class="v">mais de um</span>?</h2><p>Sim. CGU e SEFAZ SP caem no <b>mesmo dia (13/12)</b>, então ali é escolher um. Já TRT 8, TCE-GO e TJ-PB ficam em janeiro.</p><p class="sub">Escolha pelo conteúdo que você já domina, não só pelo salário.</p>', 7, T, minimal=True),
 page_a('<h2>Salva pra não perder os <span class="c">prazos</span>.</h2><p>E manda pra aquele amigo de TI que vive dizendo que um dia vai estudar pra concurso.</p>' + seguir(), 8, T, minimal=True),
]

# 2 — 22/10 10h · B: o que do seu dia a dia já cai na CGU
T = 6
POSTS["22-10h"] = [
 page_b('<h1>Você trabalha com TI? Então já estudou parte do edital da <span class="v">CGU</span>.</h1><div class="lead">Quase 70% da nota vem da sua especialidade. Veja o que você talvez já use no trabalho →</div>', 1, T),
 page_b('<span class="tag">DESENVOLVIMENTO</span><h2>Se você é dev…</h2><p>Java e Spring Boot, JavaScript com Vue, APIs REST, OAuth 2 e DevSecOps estão no edital.</p><p>Se isso é o seu dia a dia, você <span class="hl">não começa do zero</span>.</p>', 2, T),
 page_b('<span class="tag">CIÊNCIA DE DADOS</span><h2>Se você é de dados…</h2><p>Python, SQL, Data Lake, machine learning, LLMs e MLOps.</p><p>Quem faz pipeline e modelo no trabalho já tem a base.</p>', 3, T),
 page_b('<span class="tag">INFRAESTRUTURA</span><h2>Se você é de infra…</h2><p>Redes, Linux e Windows, nuvem, contêineres, infraestrutura como código e cibersegurança.</p>', 4, T),
 page_b('<h2>O que muda é o <span class="v">formato</span>.</h2><p>Saber fazer é diferente de acertar questão de certo ou errado do Cebraspe. A prática te dá vantagem, mas o treino em questões é o que vira ponto.</p>', 5, T),
 page_b('<h2>Inscrições até <span class="v">04/11</span>. Prova em 13/12, nas 27 capitais.</h2><div class="box">Salva esse post e manda pro seu colega de time.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 3 — 22/10 18h · B: 5 sinais
T = 7
POSTS["22-18h"] = [
 page_b('<h1>5 sinais de que você deveria estudar pra <span class="v">concurso de TI</span>.</h1><div class="lead">Se você se identificar com 3 ou mais, salva esse post.</div>', 1, T),
 page_b('<span class="tag">SINAL 1</span><h2>Você quer estabilidade</h2><p>Layoff, reestruturação, projeto cancelado. No serviço público, o cargo efetivo não depende do humor do mercado.</p>', 2, T),
 page_b('<span class="tag">SINAL 2</span><h2>Você quer ganhar bem sem esperar anos</h2><p>Em vários concursos de TI, o salário inicial já passa de R$ 11 mil, desde a posse.</p>', 3, T),
 page_b('<span class="tag">SINAL 3</span><h2>Você quer horário definido</h2><p>Jornada fixa, sem plantão eterno no fim de semana (na maioria dos cargos).</p>', 4, T),
 page_b('<span class="tag">SINAL 4</span><h2>Você está vindo de outra área</h2><p>Tem concurso de TI que aceita qualquer graduação. Sua formação não precisa ser em TI.</p>', 5, T),
 page_b('<span class="tag">SINAL 5</span><h2>Você gosta de estudar com método</h2><p>Concurso premia quem planeja, revisa e treina questões. Não quem estuda tudo de qualquer jeito.</p>', 6, T),
 page_b('<h2>Quantos sinais você marcou?</h2><div class="box">Conta aqui nos comentários e manda pra quem precisa ver isso.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 7, T),
]

# 4 — 23/10 10h · A: qualquer graduação
T = 6
POSTS["23-10h"] = [
 page_a(badge() + '<h1>Não é formado em <span class="c">TI</span>? Esses concursos <span class="v">aceitam você</span></h1><div class="sub">3 oportunidades de TI que não exigem graduação na área →</div>', 1, T, photo="fotos/sala-aula.jpg"),
 page_a('<h2><span class="c">CGU</span> · inscrições abertas</h2>' + card("Requisito", "Curso superior em qualquer área") + card("Remuneração", "Inicial: R$ 20.000,00", "Final de carreira: R$ 36.694,00") + card("Prazo", "Inscrições até 04/11/2026", "Cebraspe · prova em 13/12"), 2, T),
 page_a('<h2><span class="c">SEFAZ SP</span> · inscrições abertas</h2>' + card("Requisito", "Curso superior em qualquer área") + card("Remuneração", "Inicial: R$ 11.359,50", "Final de carreira: R$ 18 mil a R$ 20 mil") + card("Prazo", "Inscrições até 03/11/2026", "FCC · prova em 13/12"), 3, T),
 page_a('<h2><span class="c">DPDF</span> · edital iminente</h2>' + card("Requisito", "Graduação em TI ou qualquer graduação + especialização em TI") + card("Remuneração", "Inicial: R$ 11.309,45", "Podendo chegar a R$ 14.733,31") + card("Situação", "Banca contratada: Instituto Access", "Edital pode sair a qualquer momento"), 4, T),
 page_a('<h2>Transição de carreira <span class="v">não é desvantagem</span>.</h2><p>Na prova, ninguém pergunta seu diploma. Pergunta o conteúdo. Com um plano bem feito, dá pra chegar competitivo.</p>', 5, T),
 page_a('<h2>Marca aquele amigo que quer <span class="c">migrar pra TI</span>.</h2><p>Salva esse post pra consultar os prazos.</p>' + seguir(), 6, T),
]

# 5 — 23/10 18h · imagem única: pergunta
POSTS["23-18h"] = [page_a(badge() + '<h1>Qual concurso de <span class="c">TI</span> você vai fazer?</h1>'
    '<div class="sub">CGU, SEFAZ SP, TRT 8, TCE-GO, TJ-PB ou outro? Me conta nos comentários 👇</div>', photo="fotos/ludy-notebook.jpg")]

# 6 — 24/10 18h · A: calendário de provas
T = 5
POSTS["24-18h"] = [
 page_a(badge() + '<h1>Calendário de provas de <span class="c">TI</span>: <span class="v">dez/26 e jan/27</span></h1><div class="sub">Salva pra montar seu planejamento →</div>', 1, T, photo="fotos/ampulheta-1.jpg"),
 page_a('<h2><span class="c">13/12/2026</span> · domingo</h2>' + card("CGU", "Cebraspe · 27 capitais", "Inicial: R$ 20.000,00") + card("SEFAZ SP", "FCC · São Paulo (SP)", "Inicial: R$ 11.359,50") + '<p class="sub">⚠️ Mesmo dia: escolha um dos dois.</p>', 2, T),
 page_a('<h2><span class="c">17/01/2027</span> · domingo</h2>' + card("TRT 8", "FCC · Belém, Marabá, Santarém e Macapá", "Analista: R$ 18.801,39 · Técnico: R$ 12.537,22") + card("TCE-GO", "FCC · Goiânia (GO)", "Técnico (nível médio): R$ 11.862,19") + '<p class="sub">⚠️ Mesmo dia também.</p>', 3, T),
 page_a('<h2><span class="c">24/01/2027</span> · domingo</h2>' + card("TJ-PB", "FGV · Paraíba", "Analista: R$ 11.526,14 inicial · R$ 19.212,35 final") + '<p class="sub">Dá pra encaixar depois da prova de 17/01.</p>', 4, T),
 page_a('<h2>Com <span class="v">8 semanas</span> até a primeira prova, cada semana conta.</h2><p>Salva e manda pra quem vai estudar com você.</p>' + seguir(), 5, T),
]

# 7 — 25/10 18h · imagem única: história
POSTS["25-18h"] = [page_a(badge() + '<h1>14 reprovações antes do <span class="c">sim</span></h1>'
    '<div class="sub">14 domingos de prova, em 4 estados diferentes. Hoje sou analista judiciária de TI. Se eu tivesse parado na 10ª, nada disso teria acontecido.</div>', photo="fotos/ludy-bracos-cruzados.jpg")]

# 8 — 26/10 10h · A: federais previstos
T = 6
POSTS["26-10h"] = [
 page_a(badge() + '<h1>Concursos <span class="c">federais</span> com edital previsto <span class="v">até jan/27</span></h1><div class="sub">Pra quem é de TI começar antes do edital →</div>', 1, T, photo="fotos/estudo-noite-canva.png"),
 page_a('<h2><span class="c">Receita Federal</span></h2>' + card("Analista-Tributário", "116 vagas · R$ 12.735,99") + card("Auditor-Fiscal", "30 vagas · R$ 27.663,52") + card("Previsão", "Edital previsto para dezembro de 2026"), 2, T, src="Fonte: Portal de Prefeitura (12/10/2026)."),
 page_a('<h2><span class="c">Banco Central</span></h2>' + card("Vagas autorizadas", "100 de Auditor e 50 de Técnico", "Remuneração ainda não divulgada") + card("Previsão", "Edital até 03/01/2027"), 3, T, src="Fonte: Portal de Prefeitura (12/10/2026)."),
 page_a('<h2><span class="c">ANPD</span></h2>' + card("Cargo", "Especialista em Regulação de Proteção de Dados", "50 vagas") + card("Remuneração", "R$ 17.726,42") + card("Previsão", "Edital até 24/12/2026"), 4, T, src="Fonte: Portal de Prefeitura (12/10/2026)."),
 page_a('<h2>Ainda sem <span class="v">edital</span>.</h2><p>As áreas e os conteúdos de TI só ficam confirmados quando o edital sair. Mas a base (português, RLM, legislação e TI) você já pode começar.</p>', 5, T),
 page_a('<h2>Salva pra acompanhar.</h2><p>Eu aviso aqui quando cada edital sair.</p>' + seguir(), 6, T),
]

# 9 — 26/10 18h · B: checklist novembro
T = 7
POSTS["26-18h"] = [
 page_b('<h1>Vai começar a estudar pra concurso de TI em <span class="v">novembro</span>? Faz isso primeiro.</h1><div class="lead">Checklist em 5 passos →</div>', 1, T),
 page_b('<span class="tag">PASSO 1</span><h2>Escolha um alvo</h2><p>Um concurso (ou um grupo parecido, como tribunais). Sem alvo, você estuda tudo e não aprofunda nada.</p>', 2, T),
 page_b('<span class="tag">PASSO 2</span><h2>Leia o edital anterior</h2><p>Veja matérias, pesos e banca. É o mapa do que vale ponto.</p>', 3, T),
 page_b('<span class="tag">PASSO 3</span><h2>Monte um ciclo semanal</h2><p>TI + português + legislação desde a primeira semana, com mais horas pro que pesa mais.</p>', 4, T),
 page_b('<span class="tag">PASSO 4</span><h2>Faça questões desde o dia 1</h2><p>Use questões da banca da sua prova. Elas mostram o estilo de cobrança.</p>', 5, T),
 page_b('<span class="tag">PASSO 5</span><h2>Meça seu desempenho</h2><p>Anote acertos por matéria toda semana. Os números mostram onde ajustar a rota.</p>', 6, T),
 page_b('<h2>Salva e começa <span class="v">hoje</span>.</h2><div class="box">Manda pra quem vai estudar com você.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 7, T),
]

# 10 — 27/10 10h · B: o que o dev não estuda
T = 6
POSTS["27-10h"] = [
 page_b('<h1>Dev, o que a prova cobra e o seu trabalho <span class="v">quase nunca</span> te ensina.</h1><div class="lead">É aqui que muita gente boa em tecnologia perde ponto →</div>', 1, T),
 page_b('<span class="tag">REDES</span><h2>Modelo OSI, TCP/IP, roteamento</h2><p>Quem só codifica raramente mexe com isso. A banca adora.</p>', 2, T),
 page_b('<span class="tag">SEGURANÇA E LGPD</span><h2>Criptografia, ataques e proteção de dados</h2><p>Aparece em praticamente todo edital de TI do setor público.</p>', 3, T),
 page_b('<span class="tag">GOVERNANÇA</span><h2>ITIL, COBIT e gestão de projetos</h2><p>Assunto que quase não aparece no dia a dia de quem desenvolve, mas pesa na prova.</p>', 4, T),
 page_b('<span class="tag">FORA DA TI</span><h2>Português, RLM e legislação</h2><p>Essas matérias eliminam muita gente excelente em tecnologia. Entram no estudo desde o início.</p>', 5, T),
 page_b('<h2>Qual desses é o seu <span class="v">ponto fraco</span>?</h2><div class="box">Comenta aqui e salva pra montar seu cronograma.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 11 — 27/10 18h · B: indicadores (pode ser trocado pelo collab)
T = 6
POSTS["27-18h"] = [
 page_b('<h1>Como eu uso <span class="v">dados</span> pra saber se um aluno está no caminho certo.</h1><div class="lead">Eu trabalho com análise de dados. E isso mudou a forma como eu acompanho estudos →</div>', 1, T),
 page_b('<span class="tag">INDICADOR 1</span><h2>% de acertos por matéria</h2><p>Mostra onde você está forte e onde está perdendo ponto. Sem achismo.</p>', 2, T),
 page_b('<span class="tag">INDICADOR 2</span><h2>Evolução semana a semana</h2><p>Mais importante que um bom dia é a tendência. Está subindo, parada ou caindo?</p>', 3, T),
 page_b('<span class="tag">INDICADOR 3</span><h2>Peso no edital × seu desempenho</h2><p>Matéria que pesa muito e você acerta pouco é a prioridade da semana.</p>', 4, T),
 page_b('<h2>É isso que eu chamo de <span class="v">recalcular a rota</span>.</h2><p>É o "S" do método GPS: acompanhar por questões, metas e indicadores, e ajustar o plano quando os números pedem.</p>', 5, T),
 page_b('<h2>Você mede seus estudos?</h2><div class="box">Comenta GPS que eu te mando o link do meu grupo no WhatsApp.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 12 — 28/10 10h · B: bancas
T = 6
POSTS["28-10h"] = [
 page_b('<h1><span class="v">Cebraspe, FCC ou FGV</span>: cada banca cobra TI de um jeito.</h1><div class="lead">E as 3 estão nos concursos abertos agora →</div>', 1, T),
 page_b('<span class="tag">CEBRASPE</span><h2>Certo ou errado</h2><p>Em geral, uma resposta errada anula uma certa. Saber a hora de deixar em branco faz parte da estratégia.</p><p>Exemplo: <b>CGU</b>.</p>', 2, T),
 page_b('<span class="tag">FCC</span><h2>Múltipla escolha, mais direta</h2><p>Costuma cobrar conceitos e a letra da norma com objetividade.</p><p>Exemplos: <b>SEFAZ SP, TRT 8 e TCE-GO</b>.</p>', 3, T),
 page_b('<span class="tag">FGV</span><h2>Múltipla escolha, mais interpretativa</h2><p>Questões com mais contexto e cenários, exigindo raciocínio além da definição.</p><p>Exemplo: <b>TJ-PB</b>.</p>', 4, T),
 page_b('<h2>Resumo: treine no <span class="v">formato da sua prova</span>.</h2><p>Faça questões da banca do seu concurso desde o começo. Elas mostram como o conteúdo é cobrado.</p>', 5, T),
 page_b('<h2>Qual banca você mais teme?</h2><div class="box">Comenta aqui e salva esse post.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 13 — 28/10 18h · B: questões
T = 6
POSTS["28-18h"] = [
 page_b('<h1>Pare de esperar "terminar a teoria" pra começar as <span class="v">questões</span>.</h1><div class="lead">Como eu faria se começasse hoje →</div>', 1, T),
 page_b('<span class="tag">1</span><h2>Estude um tópico curto</h2><p>Um assunto pequeno do edital, não o capítulo inteiro.</p>', 2, T),
 page_b('<span class="tag">2</span><h2>Resolva questões da banca</h2><p>Logo em seguida, sobre o mesmo tópico. Mesmo errando bastante no começo.</p>', 3, T),
 page_b('<span class="tag">3</span><h2>Anote o porquê do erro</h2><p>Faltou conteúdo? Leu rápido? Pegadinha da banca? Cada erro pede um ajuste diferente.</p>', 4, T),
 page_b('<span class="tag">4</span><h2>Revise o que errou</h2><p>Volte nos erros dias depois. É a revisão que fixa o conteúdo.</p>', 5, T),
 page_b('<h2>Questão é <span class="v">ferramenta de estudo</span>, não prova final.</h2><div class="box">Salva e manda pra quem está travado na teoria.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 14 — 29/10 10h · A: analista x técnico
T = 5
POSTS["29-10h"] = [
 page_a(badge() + '<h1><span class="c">Analista</span> ou <span class="v">Técnico</span> de TI: qual escolher?</h1><div class="sub">Usando o TRT 8 como exemplo →</div>', 1, T, photo="fotos/ludy-sentada-azul.jpg"),
 page_a('<h2><span class="c">Analista Judiciário</span> · TI</h2>' + card("Remuneração", "Inicial: R$ 18.801,39", "Final de carreira: R$ 26.845,74") + card("Requisito", "Nível superior", "Confira no edital a formação exigida"), 2, T),
 page_a('<h2><span class="c">Técnico Judiciário</span> · TI</h2>' + card("Remuneração", "Inicial: R$ 12.537,22", "Final de carreira: R$ 17.440,22") + card("Requisito", "Nível médio", "Confira no edital se exige curso técnico na área"), 3, T),
 page_a('<h2>Dá pra fazer <span class="v">os dois</span>?</h2><p>Quando as provas são em turnos diferentes, sim. O conteúdo de TI é parecido, então estudar pra um ajuda no outro.</p><p class="sub">Inscrições do TRT 8 até 05/11/2026.</p>', 4, T),
 page_a('<h2>Qual você vai fazer?</h2><p>Comenta aqui e salva esse post.</p>' + seguir(), 5, T),
]

# 15 — 29/10 18h · B: mitos
T = 6
POSTS["29-18h"] = [
 page_b('<h1>4 mitos sobre concurso de TI que você precisa <span class="v">parar de acreditar</span>.</h1><div class="lead">Manda pra aquele amigo dev cético →</div>', 1, T),
 page_b('<span class="tag">MITO 1</span><h2>"Concurso de TI paga pouco"</h2><p>Só nos abertos agora tem inicial de R$ 11 mil a R$ 20 mil.</p>', 2, T),
 page_b('<span class="tag">MITO 2</span><h2>"No setor público só tem sistema velho"</h2><p>Tem órgão usando nuvem, microsserviços, dados e IA. Depende do órgão, como no privado.</p>', 3, T),
 page_b('<span class="tag">MITO 3</span><h2>"Precisa ser formado em TI"</h2><p>CGU e SEFAZ SP, por exemplo, aceitam graduação em qualquer área.</p>', 4, T),
 page_b('<span class="tag">MITO 4</span><h2>"É só pra quem programa"</h2><p>Tem vaga pra suporte, redes, segurança, dados, governança, projetos e requisitos.</p>', 5, T),
 page_b('<h2>Qual desses você já ouviu?</h2><div class="box">Comenta e manda pra quem precisa ver isso.<br><br>Me siga para mais dicas de <b>concursos</b> e <b>carreira de TI</b>.</div>', 6, T),
]

# 16 — 30/10 10h · imagem única: CGU reta final
POSTS["30-10h"] = [page_a(badge() + '<h1><span class="c">CGU</span>: inscrições fecham <span class="v">04/11</span></h1>'
    + card("Auditor Federal de Finanças e Controle · TI", "Inicial: R$ 20.000,00 · Final: R$ 36.694,00", "30 vagas · qualquer graduação · Cebraspe")
    + card("Prova", "13/12/2026, nas 27 capitais", "Taxa de R$ 170, com isenção para CadÚnico e doadores de medula"), photo="fotos/coding-noite-unsplash.jpg")]

# 17 — 30/10 18h · imagem única: rumo aos 10 mil
POSTS["30-18h"] = [page_a(badge() + '<h1>Rumo aos <span class="c">10 mil</span> 💜</h1>'
    '<div class="sub">Obrigada a cada pessoa que chegou até aqui. Se esse perfil já te ajudou, manda pra um amigo de TI que está pensando em concurso.</div>', photo="fotos/ludy-bracos-cruzados-clara.jpg")]

if __name__ == "__main__":
    import sys
    only = sys.argv[1:]
    for k, pages in POSTS.items():
        if only and k not in only:
            continue
        render(pages, f"{OUT}/{k}")
        print(k, len(pages))
