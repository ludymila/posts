"""Reel 9:16 — "Passei no meu 1º concurso federal com 18 anos".
Gera reel_18anos.mp4 (1080x1920, 30fps, sem áudio: o áudio em alta é escolhido no app do Instagram).
Uso: python3 reel_18anos.py <pasta_saida>   (rodar a partir de _ferramentas/)"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, subprocess, sys, re, os

W, H, FPS = 1080, 1920, 30
BG = (20, 17, 43); TXT = (246, 245, 251); MINT = (34, 211, 182); VIOLET = (108, 76, 241)
FD = '/usr/share/fonts/opentype/inter/'
def F(w, s): return ImageFont.truetype(FD + f'Inter-{w}.otf', s)

CARD_W, CARD_TOP, CARD_MAX_H = 940, 290, 860
TEXT_SIZE = 66
XFADE = 0.35

P = 'fotos/'
SCENES = [
 # (foto, foco_x, foco_y, texto, duração)
 (P+'ludy-posse-primeiro-concurso.jpg', .60, .40, "Passei no meu 1º concurso federal com **18 anos.**", 3.2),
 (P+'ludy-posse-primeiro-concurso.jpg', .58, .30, "Edital com **1 vaga.** Fiquei em **10º.**\nAchei que nunca iam me chamar.", 3.4),
 (P+'eua-campus.jpg', .55, .55, "Continuei estudando e ganhei uma **bolsa de 100%** pra estudar nos EUA", 3.4),
 (P+'eua-brooklyn-noite.jpg', .53, .55, "1 ano de **Ciência da Computação** em Massachusetts", 3.0),
 (P+'eua-ny-noite.jpg', .55, .45, "Aquele concurso?\n**Nem lembrava mais.**", 2.8),
 (P+'eua-brooklyn-comemorando.jpg', .48, .45, "Até que o telefone tocou:\n**fui nomeada!**", 3.0),
 (P+'eua-nasa.jpg', .45, .78, "No **4º e último ano** de validade do concurso", 3.0),
 (P+'eua-brooklyn-dia.jpg', .62, .50, "Eu carregava **10 reprovações.**\nNenhuma delas me parou.", 3.2),
 (P+'ludy-trabalho-tribunal.jpg', .50, .00, "E isso foi só o **começo.**", 2.6),
 (None, 0, 0, "Não se limite pela **idade,** pelo **número de vagas** ou pela **sua colocação.**", 3.4),
 (None, 0, 0, "Segue **@ludy.dev** para mais dicas de Concursos de TI", 3.0),
]

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

def text_layer(text, size, maxw, center=False):
    f = F('ExtraBold', size)
    sp = f.getlength(' ')
    lines, cur, cw = [], [], 0
    for w, hl in tokens(text):
        if w == '\n':
            lines.append((cur, cw)); cur, cw = [], 0; continue
        ww = f.getlength(w); add = ww + (sp if cur else 0)
        if cur and cw + add > maxw:
            lines.append((cur, cw)); cur, cw = [], 0; add = ww
        cur.append((w, hl)); cw += add
    lines.append((cur, cw))
    lh = int(size * 1.18)
    img = Image.new('RGBA', (W, lh * len(lines) + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i, (ln, lw) in enumerate(lines):
        x = (W - lw) / 2 if center else 70
        for j, (w, hl) in enumerate(ln):
            if j: x += sp
            d.text((x, i * lh), w, font=f, fill=MINT if hl else TXT)
            x += f.getlength(w)
    return img

def rounded_mask(w, h, r=36, ss=3):
    m = Image.new('L', (w * ss, h * ss), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w * ss - 1, h * ss - 1), r * ss, fill=255)
    return m.resize((w, h), Image.LANCZOS)

def handle_chip():
    av = Image.open('avatar.png').convert('RGB').resize((64, 64), Image.LANCZOS)
    m = Image.new('L', (256, 256), 0); ImageDraw.Draw(m).ellipse((4, 4, 251, 251), fill=255)
    av.putalpha(m.resize((64, 64), Image.LANCZOS))
    f = F('SemiBold', 32)
    w = 64 + 16 + int(f.getlength('@ludy.dev')) + 30
    chip = Image.new('RGBA', (w + 8, 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(chip)
    d.rounded_rectangle((0, 0, w + 6, 78), 40, fill=(20, 17, 43, 200))
    chip.paste(av, (8, 7), av)
    d.text((88, 20), '@ludy.dev', font=f, fill=TXT)
    return chip

def minimal_bg():
    img = Image.new('RGB', (W, H), BG)
    ss = 2
    ov = Image.new('RGBA', (W * ss, H * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    cx, cy = 980 * ss, 260 * ss
    for r, a in [(420, 140), (290, 80)]:
        d.ellipse((cx - r * ss, cy - r * ss, cx + r * ss, cy + r * ss), outline=(108, 76, 241, a), width=3 * ss)
    d.ellipse((cx - 300 * ss - 12 * ss, cy + 296 * ss - 12 * ss, cx - 300 * ss + 12 * ss, cy + 296 * ss + 12 * ss), fill=MINT + (255,))
    ov = ov.resize((W, H), Image.LANCZOS)
    img.paste(ov, (0, 0), ov)
    return img

def scene_assets(photo, fx, fy, text):
    if photo is None:
        bg = minimal_bg()
        tl = text_layer(text, 78, W - 140, center=True)
        return dict(kind='end', bg=bg, text=tl, ty=(H - tl.height) // 2 - 40)
    src = Image.open(photo).convert('RGB')
    # fundo: a própria foto, desfocada e escurecida
    s = max(W / src.width, H / src.height)
    bg = src.resize((int(src.width * s) + 1, int(src.height * s) + 1), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(38))
    bg = Image.blend(bg, Image.new('RGB', (W, H), BG), 0.62)
    native = int(CARD_W * src.height / src.width)
    ch = CARD_MAX_H if native >= CARD_MAX_H else max(native, 760)
    tl = text_layer(text, TEXT_SIZE, W - 140)
    top = max(260, (H - (ch + 70 + tl.height)) // 2 - 60)
    return dict(kind='photo', src=src, fx=fx, fy=fy, bg=bg, ch=ch, top=top, mask=rounded_mask(CARD_W, ch), text=tl,
                ty=top + ch + 70)

def card_frame(a, t):
    """Ken Burns: zoom 1.00 -> 1.08 ao longo da cena, centrado no foco."""
    src, ch = a['src'], a['ch']
    z = 1.0 + 0.08 * t
    # janela base com a proporção do card, o maior possível dentro da foto
    ar = CARD_W / ch
    bw = min(src.width, src.height * ar); bh = bw / ar
    ww, wh = bw / z, bh / z
    cx = min(max(a['fx'] * src.width, ww / 2), src.width - ww / 2)
    cy = min(max(a['fy'] * src.height, wh / 2), src.height - wh / 2)
    box = (cx - ww / 2, cy - wh / 2, cx + ww / 2, cy + wh / 2)
    return src.resize((CARD_W, ch), Image.BICUBIC, box=box, reducing_gap=2.0)

CHIP = None
def render_frame(a, t, tt):
    """t: progresso 0..1 da cena; tt: segundos desde o início da cena."""
    if a['kind'] == 'end':
        fr = a['bg'].copy()
    else:
        fr = a['bg'].copy()
        card = card_frame(a, t)
        fr.paste(card, ((W - CARD_W) // 2, a['top']), a['mask'])
    # texto: entra com fade + leve subida nos primeiros 0,35 s
    k = min(1.0, tt / 0.35); k = 1 - (1 - k) ** 3
    tl = a['text']
    if k < 1:
        al = tl.getchannel('A').point(lambda v: int(v * k))
        tl = tl.copy(); tl.putalpha(al)
    fr.paste(tl, (0, int(a['ty'] + 30 * (1 - k))), tl)
    fr.paste(CHIP, ((W - CHIP.width) // 2, 150), CHIP)
    return fr

def main(out_dir):
    global CHIP
    CHIP = handle_chip()
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'reel_18anos.mp4')
    assets = [scene_assets(p, fx, fy, t) for p, fx, fy, t, _ in SCENES]
    durs = [d for *_, d in SCENES]
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                           '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium',
                           '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out],
                          stdin=subprocess.PIPE)
    xf = int(XFADE * FPS)
    for i, (a, d) in enumerate(zip(assets, durs)):
        n = int(d * FPS)
        for f in range(n):
            fr = render_frame(a, f / n, (f / FPS) if i else 9.0)  # 1ª cena: texto já visível no 1º quadro (gancho)
            # crossfade com a próxima cena nos últimos quadros
            if i + 1 < len(assets) and f >= n - xf:
                k = (f - (n - xf) + 1) / (xf + 1)
                nxt = render_frame(assets[i + 1], 0, 0.0)
                fr = Image.blend(fr, nxt, k)
            ff.stdin.write(np.asarray(fr, dtype=np.uint8).tobytes())
        if i == 0:
            render_frame(a, 0.9, 2.0).save(os.path.join(out_dir, 'reel_capa.png'))
    ff.stdin.close(); ff.wait()
    print(out, sum(durs), 's')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
