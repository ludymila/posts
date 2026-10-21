"""Carrossel 21/10 18h: história do primeiro concurso (versão com fotos dos EUA).
Uso: python3 render2.py  (rodar na pasta que contém avatar.png e fotos/)"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import re

W, H = 1080, 1350
MX = 88
BG = (20, 17, 43)        # #14112B
TXT = (246, 245, 251)    # #F6F5FB
MUTED = (164, 158, 200)
VIOLET = (108, 76, 241)  # #6C4CF1
MINT = (34, 211, 182)    # #22D3B6
FONT_DIR = '/usr/share/fonts/opentype/inter/'
def F(w, s): return ImageFont.truetype(FONT_DIR + f'Inter-{w}.otf', s)

PAD_V = 84   # margem mínima topo/base
GAP_HEAD = 36
GAP_PHOTO = 36

def circ_avatar(size, ss=4):
    im = Image.open('avatar.png').convert('RGB').resize((size*ss, size*ss), Image.LANCZOS).convert('RGBA')
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
    out = []
    for line in text.split('\n'):
        for p in re.split(r'(\*\*.+?\*\*)', line):
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

def cover_crop(path, w, h, fx=0.5, fy=0.5, sharpen=False):
    im = Image.open(path).convert('RGB')
    sw, sh = im.size
    scale = max(w/sw, h/sh)
    nw, nh = round(sw*scale), round(sh*scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    if sharpen:
        im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    left = min(max(0, int(nw*fx - w/2)), nw - w)
    top = min(max(0, int(nh*fy - h/2)), nh - h)
    return im.crop((left, top, left+w, top+h))

def rounded(im, r=28, ss=4):
    w, h = im.size
    m = Image.new('L', (w*ss, h*ss), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w*ss-1, h*ss-1), radius=r*ss, fill=255)
    im = im.convert('RGBA'); im.putalpha(m.resize((w, h), Image.LANCZOS))
    return im

def photo_block(photos, w, h):
    """photos: lista de (path, fx, fy, sharpen). 1 foto = largura cheia; 2 = lado a lado."""
    if len(photos) == 1:
        p, fx, fy, sh = photos[0]
        return [(rounded(cover_crop(p, w, h, fx, fy, sh)), 0)]
    gap = 16
    cw = (w - gap)//2
    out = []
    for i, (p, fx, fy, sh) in enumerate(photos):
        out.append((rounded(cover_crop(p, cw, h, fx, fy, sh)), i*(cw+gap)))
    return out

def slide(text, out, size=48, photos=None, photo_max=560, fit=False):
    img = Image.new('RGB', (W, H), BG)
    glow = Image.new('RGBA', (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    for r, a in [(520, 10), (380, 14), (240, 18)]:
        gd.ellipse((W-r, -r//1.6, W+r, r), fill=(108, 76, 241, a))
    img.paste(glow, (0,0), glow)
    d = ImageDraw.Draw(img)

    maxw = W - 2*MX
    lines, space = layout(text, size, maxw)
    lh = int(size*1.38)
    text_h = len(lines)*lh - (lh - size)  # sem sobra da última linha
    av = 96
    ph_h = 0
    if photos:
        avail = H - 2*PAD_V - av - GAP_HEAD - text_h - GAP_PHOTO
        ph_h = max(260, min(photo_max, avail))
        assert avail >= 260, f'{out}: texto longo demais para a foto ({avail}px livres)'
    total = av + GAP_HEAD + text_h + ((GAP_PHOTO + ph_h) if photos else 0)
    y = (H - total)//2

    a = circ_avatar(av)
    img.paste(a, (MX, y), a)
    nx = MX + av + 22
    fn, fh = F('Bold', 36), F('Regular', 28)
    d.text((nx, y+12), 'Ludymila Lobo', font=fn, fill=TXT)
    badge(img, nx + fn.getlength('Ludymila Lobo') + 12, y+16)
    d.text((nx, y+56), '@ludy.dev', font=fh, fill=MUTED)

    ty = y + av + GAP_HEAD
    for ln in lines:
        x = MX
        for i, (w, hl, f) in enumerate(ln):
            if i: x += space
            d.text((x, ty), w, font=f, fill=MINT if hl else TXT)
            x += f.getlength(w)
        ty += lh
    if photos:
        py = y + av + GAP_HEAD + text_h + GAP_PHOTO
        for ph, dx in photo_block(photos, maxw, ph_h):
            img.paste(ph, (MX + dx, py), ph)
    img.save(out, 'PNG', optimize=True)

P = 'fotos/'
SLIDES = [
 # 1 capa
 ("**Passei no meu primeiro concurso federal com 18 anos.**\n\nE eu tinha certeza de que nunca iam me chamar.",
  54, [(P+'posse.jpg', 0.64, 0.6, False)], 560),
 # 2
 ("Eu ainda estava na graduação quando fiz a prova.\n\nO edital tinha **só 1 vaga.**\n\nFiquei em **10º lugar.**\n\nFiz as contas e pensei: esquece, nunca vão me chamar.",
  50, None, 0),
 # 3 bolsa
 ("Mas eu não fiquei parada esperando.\n\nContinuei estudando. E esses estudos me levaram a passar em uma seletiva pra cursar parte da graduação nos EUA, com **bolsa de 100%.**",
  46, [(P+'eua-campus.jpg', 0.5, 0.55, True)], 520),
 # 4 Massachusetts
 ("Passei um ano estudando **Ciência da Computação em Massachusetts.**\n\nE ainda fui destaque como **estudante do mês.**",
  46, [(P+'eua-student-of-the-month.jpg', 0.5, 0.5, True)], 337),
 # 5 ano de portas abertas
 ("Foi um ano de muito código, eventos de tecnologia e portas abertas.\n\nAquele concurso em que eu fiquei em 10º? **Nem passava mais pela minha cabeça.**",
  46, [(P+'eua-startup-weekend.jpg', 0.55, 0.42, False), (P+'eua-microsoft.jpg', 0.5, 0.5, False)], 520),
 # 6 ligação
 ("Até que, ainda nos EUA, o telefone tocou.\n\nEra o aviso da **minha nomeação.**\n\nNo mês seguinte eu já precisava voltar pro Brasil. Era justamente o fim do intercâmbio.",
  46, [(P+'eua-brooklyn-comemorando.jpg', 0.47, 0.45, False)], 520),
 # 7 validade
 ("Um detalhe que muita gente não sabe:\n\nconcurso costuma valer **2 anos, prorrogáveis por mais 2.**\n\nFui nomeada no **4º e último ano** de validade. Junto com o último período da minha graduação.",
  46, [(P+'eua-ny-noite.jpg', 0.52, 0.5, False)], 460),
 # 8 tempo de Deus
 ("As coisas acontecem no tempo de Deus.\n\nO resultado, ninguém controla. A gente controla o próprio comportamento: **desistir ou continuar estudando.**",
  46, [(P+'eua-brooklyn-dia.jpg', 0.58, 0.45, False)], 520),
 # 9 reprovações / queria mais
 ("Nessa época eu carregava **10 reprovações.** Nenhuma delas me parou.\n\nE nem a aprovação me fez parar. Eu queria mais. Veio a aprovação pra **analista de TI,** mas essa é história pra outro post.",
  46, [(P+'eua-google-android.jpg', 0.4, 0.6, False)], 480),
 # 10 não se limite
 ("Então não se limite.\n\nNem pela **idade,** pra mais ou pra menos. Nem pelo **número de vagas.** Nem pela **sua colocação.**\n\nQuem continua estudando chega mais longe do que imaginava.",
  46, [(P+'eua-nasa.jpg', 0.5, 0.86, False)], 500),
 # 11 CTA
 ("Se essa história te deu um gás, salva pra reler no dia em que bater a vontade de desistir.\n\nE manda pra aquele amigo que acha que \"não tem chance\".\n\nE já segue **@ludy.dev** para mais dicas de Concursos de TI.",
  50, None, 0),
]

if __name__ == '__main__':
    import glob, os
    for f in glob.glob('slide_*.png'): os.remove(f)
    for i, (t, s, ph, pm) in enumerate(SLIDES, 1):
        slide(t, f'slide_{i:02d}.png', size=s, photos=ph, photo_max=pm)
    print('ok', len(SLIDES))
