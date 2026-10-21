from render import *

OUT = "/home/claude/posts/2026-10-21"

# POST 1 — 11h (Brasília) · carrossel estilo A: áreas de atuação de TI em um tribunal, 1 card por área com foto
AREAS = [
 ("🛠️", "Suporte de TI", "Atende servidores e magistrados no dia a dia: equipamentos, acessos, sistemas e incidentes.", "suporte"),
 ("📋", "Gerenciamento de projetos", "Planeja e acompanha projetos de tecnologia: prazos, custos, riscos e entregas.", "projetos"),
 ("🧭", "Governança de TI", "Alinha a tecnologia aos objetivos do órgão: planejamento, contratações, políticas e indicadores.", "governanca"),
 ("🔐", "Segurança da informação", "Protege dados e sistemas: gestão de riscos, controle de acessos, resposta a incidentes e LGPD.", "seguranca"),
 ("🌐", "Redes e infraestrutura", "Mantém servidores, redes, data center e nuvem funcionando com alta disponibilidade.", "redes"),
 ("💻", "Desenvolvimento de sistemas", "Cria e mantém os sistemas usados pelo órgão e pelos cidadãos.", "dev"),
 ("🧪", "Testes de software", "Garante a qualidade dos sistemas antes de chegarem ao usuário, com testes manuais e automatizados.", "testes"),
 ("📝", "Análise de requisitos", "Entende a necessidade das áreas e transforma em requisitos claros para o time de desenvolvimento.", "requisitos"),
]
T = len(AREAS) + 2
p1 = [page_a(badge() + '<h1>Como é o trabalho de quem é de <span class="c">TI</span> em um <span class="v">tribunal</span>?</h1>'
             '<div class="sub">Não é só com programação. Conheça as 8 áreas de atuação&nbsp;→</div>', 1, T, photo="fotos/ludy-trabalho-tribunal.jpg", panel=True)]
for i, (icon, nome, desc, f) in enumerate(AREAS, 2):
    p1.append(page_a(f'<span style="font-size:26px;letter-spacing:2px;color:#22D3B6;font-weight:700">ÁREA {i-1} DE 8</span>'
                     f'<h2 style="margin-top:14px">{icon} {nome}</h2><p>{desc}</p>', i, T, top_photo=f"fotos/areas/{f}.jpg", top_h=800))
LAST = ('<h2>Comenta o <span class="c">número</span> da área que mais te interessa <span class="v">(1 a 8)</span>!</h2>'
        '<p>Se estiver em dúvida, me conta que eu te ajudo a escolher. 🚀</p>'
        '<p style="margin-top:28px">Vamos ver qual a área mais interessante 👀</p>')
p1.append(page_a(LAST +
                 '<div class="card"><div class="t">Me siga para mais dicas de concursos e carreira de TI.</div></div>', T, T))

render(p1, OUT + "/post-1")  # atenção: slide_01 foi substituído pela capa do Canva; renderize só o que mudar
print("ok")
