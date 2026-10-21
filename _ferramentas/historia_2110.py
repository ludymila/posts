from PIL import Image, ImageDraw, ImageFont
import re, sys

W, H = 1080, 1350
MX = 88
BG = (20, 17, 43)        # #14112B
TXT = (246, 245, 251)    # #F6F5FB
MUTED = (164, 158, 200)
VIOLET = (108, 76, 241)  # #6C4CF1
MINT = (34, 211, 182)    # #22D3B6

FONT_DIR = '/usr/share/fonts/opentype/inter/'
def F(w, s): return ImageFont.truetype(FONT_DIR + f'Inter-{w}.otf', s)

PHOTO = 'fotos/ludy-posse-primeiro-concurso.jpg'

def circ_avatar(size, ss=4):
    im = Image.open('avatar.png').convert('RGB')
    im = im.resize((size*ss, size*ss), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', (size*ss, size*ss), 0)
    ImageDraw.Draw(m).ellipse((ss, ss, size*ss-1-ss, size*ss-1-ss), fill=255)
    im.putalpha(m)
    return im.resize((size, size), Image.LANCZOS)

def badge(img, x, y, size=34, ss=4):
    b = Image.new('RGBA', (size*ss, size*ss), (0,0,0,0))
    d = ImageDraw.Draw(b)
    d.ellipse((ss, ss, size*ss-1-ss, size*ss-1-ss), fill=VIOLET)
    lw = 3*ss
    pts = [(9*ss, 17*ss), (15*ss, 23*ss), (25*ss, 11*ss)]
    d.line(pts, fill='white', width=lw, joint='curve')
    for cx, cy in pts:
        d.ellipse((cx-lw//2, cy-lw//2, cx+lw//2, cy+lw//2), fill='white')
    b = b.resize((size, size), Image.LANCZOS)
    img.paste(b, (int(x), int(y)), b)

def tokens(text):
    """Parse **mint** markup into (word, highlighted) tokens, keeping line breaks."""
    out = []
    for line in text.split('\n'):
        parts = re.split(r'(\*\*.+?\*\*)', line)
        for p in parts:
            hl = p.startswith('**') and p.endswith('**')
            p = p[2:-2] if hl else p
            for w in p.split(' '):
                if w: out.append((w, hl))
        out.append(('\n', False))
    return out[:-1]

def layout(text, size, maxw):
    fr, fb = F('Regular', size), F('SemiBold', size)
    lines, cur, curw = [], [], 0
    space = fr.getlength(' ')
    for w, hl in tokens(text):
        if w == '\n':
            lines.append(cur); cur, curw = [], 0; continue
        f = fb if hl else fr
        ww = f.getlength(w)
        add = ww + (space if cur else 0)
        if cur and curw + add > maxw:
            lines.append(cur); cur, curw = [], 0; add = ww
        cur.append((w, hl, f)); curw += add
    lines.append(cur)
    return lines, space

def slide(text, out, size=48, photo=None, kicker=None):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    # subtle glow
    glow = Image.new('RGBA', (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    for r, a in [(520, 10), (380, 14), (240, 18)]:
        gd.ellipse((W-r, -r//1.6, W+r, r), fill=(108, 76, 241, a))
    img.paste(glow, (0,0), glow)
    d = ImageDraw.Draw(img)

    maxw = W - 2*MX
    lines, space = layout(text, size, maxw)
    lh = int(size*1.38)
    text_h = len(lines)*lh
    av = 96
    head_h = av
    ph = None
    if photo:
        ph = Image.open(PHOTO).convert('RGB')
        pw = maxw
        # crop to 4:3-ish centered on her
        c = ph.crop((560, 0, 2368, 1356))
        hh = int(pw * c.height / c.width)
        if hh > photo:
            hh = photo
        c = c.resize((pw, int(pw*c.height/c.width)), Image.LANCZOS)
        top = max(0, int((c.height-hh)*0.62))
        c = c.crop((0, top, pw, top+hh))
        ss = 4
        m = Image.new('L', (pw*ss, hh*ss), 0)
        ImageDraw.Draw(m).rounded_rectangle((0,0,pw*ss-1,hh*ss-1), radius=28*ss, fill=255)
        c.putalpha(m.resize((pw, hh), Image.LANCZOS))
        ph = c
    kick_h = 0
    total = head_h + 40 + text_h + ((44 + ph.height) if ph else 0)
    y = (H - total)//2

    a = circ_avatar(av)
    img.paste(a, (MX, y), a)
    nx = MX + av + 22
    fn, fh = F('Bold', 36), F('Regular', 28)
    d.text((nx, y+12), 'Ludymila Lobo', font=fn, fill=TXT)
    badge(img, nx + fn.getlength('Ludymila Lobo') + 12, y+16)
    d.text((nx, y+56), '@ludy.dev', font=fh, fill=MUTED)

    ty = y + head_h + 40
    for ln in lines:
        x = MX
        for i, (w, hl, f) in enumerate(ln):
            if i: x += space
            d.text((x, ty), w, font=f, fill=MINT if hl else TXT)
            x += f.getlength(w)
        ty += lh
    if ph:
        img.paste(ph, (MX, ty + 44 - (lh - size)), ph)
    img.save(out, 'PNG', optimize=True)

SLIDES = [
 ("**Passei no meu primeiro concurso federal com 18 anos.**\n\nE eu tinha certeza de que nunca iam me chamar.", 54, 560),
 ("Eu ainda estava na graduação quando fiz a prova.\n\nO edital tinha **só 1 vaga.**\n\nFiquei em **10º lugar.**\n\nFiz as contas e pensei: esquece, nunca vão me chamar.", 50, None),
 ("Mas eu não fiquei parada esperando.\n\nContinuei estudando.\n\nE esses estudos me levaram a passar em uma seletiva pra cursar parte da graduação nos Estados Unidos, com **bolsa de 100%.**", 50, None),
 ("Passei um ano estudando **Ciência da Computação em Massachusetts.**\n\nAquele concurso em que eu fiquei em 10º?\n\nNem passava mais pela minha cabeça.", 50, None),
 ("Até que, ainda nos EUA, o telefone tocou.\n\nEra o aviso da **minha nomeação.**\n\nNo mês seguinte eu já precisava voltar pro Brasil. Era justamente o fim do intercâmbio.", 50, None),
 ("Um detalhe que muita gente não sabe:\n\nconcurso costuma valer **2 anos, prorrogáveis por mais 2.**\n\nFui nomeada no **4º e último ano** de validade. Junto com o último período da minha graduação.", 50, None),
 ("As coisas acontecem no tempo de Deus.\n\nMuitas vezes a gente não entende um resultado ou uma reprovação.\n\nO resultado, ninguém controla. A gente controla o próprio comportamento: **desistir ou continuar estudando.**", 48, None),
 ("Nessa época eu carregava **10 reprovações.**\n\nNenhuma delas me parou.\n\nE nem a aprovação me fez parar. Eu queria mais. Veio a aprovação pra **analista de TI,** mas essa é história pra outro post.", 50, None),
 ("Então não se limite.\n\nNem pela **idade,** pra mais ou pra menos.\n\nNem pelo **número de vagas.**\n\nNem pela **sua colocação.**\n\nVocê não controla quando vão te chamar. Controla se vai estar pronto(a) quando chamarem.", 48, None),
 ("Se essa história te deu um gás, salva pra reler no dia em que bater a vontade de desistir.\n\nE manda pra aquele amigo que acha que \"não tem chance\".\n\n**Comenta GPS** que eu te mando o link do meu grupo no WhatsApp.", 50, None),
]

if __name__ == '__main__':
    for i, (t, s, p) in enumerate(SLIDES, 1):
        slide(t, f'slide_{i:02d}.png', size=s, photo=p)
    print('ok')
