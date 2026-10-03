"""Gera as colinhas em PDF (pdfs/) a partir de colinhas/*.md.

Cada colinha ocupa 1 página A4 em duas colunas. Também gera um PDF único
com todas as colinhas. Suporta o Markdown usado nas colinhas: títulos,
parágrafos, listas, tabelas, blocos de código, citações (dicas), negrito
e código inline.

Uso: python scripts/gerar_pdfs.py   (requer: pip install reportlab)
"""
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)
from reportlab.platypus.flowables import BalancedColumns

RAIZ = Path(__file__).resolve().parent.parent
COLINHAS = RAIZ / "colinhas"
SAIDA = RAIZ / "pdfs"
TITULO_CURSO = "Curso de T.I. Básico"
URL_SITE = "github.com/GabrielKqw/T.I-Basico"

AZUL = colors.HexColor("#1F4E79")
AZUL_CLARO = colors.HexColor("#EAF1F8")
CINZA_CODIGO = colors.HexColor("#F2F2F2")
AMARELO = colors.HexColor("#FFF4CC")
BORDA = colors.HexColor("#C9D3DD")


def registrar_fontes():
    """Usa Arial/Consolas (acentos completos) se existirem; senão, fontes padrão."""
    fontes = Path("C:/Windows/Fonts")
    try:
        pdfmetrics.registerFont(TTFont("Texto", str(fontes / "arial.ttf")))
        pdfmetrics.registerFont(TTFont("Texto-Negrito", str(fontes / "arialbd.ttf")))
        pdfmetrics.registerFont(TTFont("Texto-Italico", str(fontes / "ariali.ttf")))
        pdfmetrics.registerFont(TTFont("Texto-NegritoItalico", str(fontes / "arialbi.ttf")))
        pdfmetrics.registerFont(TTFont("Mono", str(fontes / "consola.ttf")))
        pdfmetrics.registerFontFamily("Texto", normal="Texto", bold="Texto-Negrito",
                                      italic="Texto-Italico", boldItalic="Texto-NegritoItalico")
        return "Texto", "Texto-Negrito", "Mono"
    except Exception:
        return "Helvetica", "Helvetica-Bold", "Courier"


FONTE, FONTE_NEGRITO, FONTE_MONO = registrar_fontes()

MARGEM = 1.2 * cm
TOPO = 2.3 * cm  # espaço da faixa de título
ESPACO_COLUNAS = 0.6 * cm
LARGURA_COLUNA = (A4[0] - 2 * MARGEM - ESPACO_COLUNAS) / 2

ESTILOS = {}


def definir_escala(e):
    """Tamanho das letras: cada colinha usa a maior escala que ainda cabe em 1 página."""
    ESTILOS.update({
        "h2": ParagraphStyle("h2", fontName=FONTE_NEGRITO, fontSize=10.5 * e, leading=13 * e,
                             textColor=AZUL, spaceBefore=7 * e, spaceAfter=3 * e, keepWithNext=1),
        "p": ParagraphStyle("p", fontName=FONTE, fontSize=8.5 * e, leading=11 * e, spaceAfter=3 * e),
        "li": ParagraphStyle("li", fontName=FONTE, fontSize=8.5 * e, leading=11 * e, leftIndent=10,
                             bulletIndent=2, spaceAfter=1 * e),
        "cell": ParagraphStyle("cell", fontName=FONTE, fontSize=8.2 * e, leading=10 * e),
        "quote": ParagraphStyle("quote", fontName=FONTE, fontSize=8.2 * e, leading=10.5 * e),
        "code": ParagraphStyle("code", fontName=FONTE_MONO, fontSize=7.8 * e, leading=10 * e),
    })


def inline(texto):
    """Converte Markdown inline (negrito e código) para a marcação do ReportLab."""
    saida = []
    for parte in re.split(r"(`[^`]+`)", texto):
        if parte.startswith("`") and parte.endswith("`") and len(parte) > 1:
            codigo = parte[1:-1].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            saida.append(f'<font name="{FONTE_MONO}" color="#B03A2E">{codigo}</font>')
            continue
        parte = parte.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        saida.append(re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", parte))
    return "".join(saida)


def largura_texto(texto):
    """Largura do texto em uma linha só (código em fonte mono, negrito em negrito)."""
    tam = ESTILOS["cell"].fontSize
    total = 0
    for parte in re.split(r"(`[^`]+`)", texto):
        if parte.startswith("`") and parte.endswith("`") and len(parte) > 1:
            total += pdfmetrics.stringWidth(parte[1:-1], FONTE_MONO, tam)
            continue
        for i, trecho in enumerate(parte.split("**")):
            total += pdfmetrics.stringWidth(trecho, FONTE_NEGRITO if i % 2 else FONTE, tam)
    return total + 8  # espaçamento interno da célula


def maior_palavra(celula):
    """Largura da maior palavra: a coluna nunca fica mais estreita que isso."""
    if celula.startswith("`") and celula.endswith("`"):
        return 0  # fórmula comprida pode quebrar
    negrito = celula.startswith("**")
    return max((largura_texto(f"**{p}**" if negrito else p) for p in celula.replace("**", "").split()),
               default=0)


def larguras_colunas(celulas, ncol):
    """Evita quebrar fórmulas no meio: a 1ª coluna ganha o espaço que precisa (até 62%)."""
    precisa = [max(largura_texto(l[i]) for l in celulas) for i in range(ncol)]
    if sum(precisa) <= LARGURA_COLUNA:
        sobra = LARGURA_COLUNA - sum(precisa)
        return [p + sobra * p / sum(precisa) for p in precisa]
    if ncol == 2:
        minimo = max(maior_palavra(l[0]) for l in celulas)
        primeira = max(minimo, min(precisa[0], LARGURA_COLUNA * 0.62))
        return [primeira, LARGURA_COLUNA - primeira]
    return [LARGURA_COLUNA * p / sum(precisa) for p in precisa]


def tabela(linhas):
    celulas = [[c.strip() for c in l.strip().strip("|").split("|")] for l in linhas]
    # tira a linha separadora (---) e o cabeçalho vazio (| | |)
    celulas = [c for c in celulas if not all(re.fullmatch(r":?-{2,}:?", x) for x in c if x)
               and any(c)]
    ncol = max(len(c) for c in celulas)
    celulas = [c + [""] * (ncol - len(c)) for c in celulas]
    larguras = larguras_colunas(celulas, ncol)
    dados = [[Paragraph(inline(x), ESTILOS["cell"]) for x in linha] for linha in celulas]
    t = Table(dados, colWidths=larguras)
    t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, AZUL_CLARO]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, BORDA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return [t, Spacer(1, 3)]


def caixa(conteudo, fundo, borda):
    t = Table([[conteudo]], colWidths=[LARGURA_COLUNA])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fundo),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, borda),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [t, Spacer(1, 4)]


class MarcaTitulo(Flowable):
    """Marcador invisível: avisa ao cabeçalho qual colinha está na página."""

    def __init__(self, numero, titulo):
        super().__init__()
        self.numero, self.titulo = numero, titulo
        self.width = self.height = 0

    def draw(self):
        doc = self.canv._doctemplate
        doc.colinha_atual = (self.numero, self.titulo)
        chave = f"c{self.numero}"
        self.canv.bookmarkPage(chave)
        self.canv.addOutlineEntry(f"{self.numero}. {self.titulo}", chave, level=0)


def markdown_para_flowables(texto, numero):
    elementos, i = [], 0
    linhas = texto.splitlines()
    paragrafo = []

    def fechar_paragrafo():
        if paragrafo:
            elementos.append(Paragraph(inline(" ".join(paragrafo)), ESTILOS["p"]))
            paragrafo.clear()

    while i < len(linhas):
        s = linhas[i].strip()
        if s.startswith("```"):
            fechar_paragrafo()
            bloco = []
            i += 1
            while i < len(linhas) and not linhas[i].strip().startswith("```"):
                bloco.append(linhas[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                i += 1
            elementos += caixa(Paragraph("<br/>".join(bloco), ESTILOS["code"]), CINZA_CODIGO,
                               colors.HexColor("#999999"))
        elif s.startswith("|"):
            fechar_paragrafo()
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                bloco.append(linhas[i])
                i += 1
            elementos += tabela(bloco)
            continue
        elif s.startswith(">"):
            fechar_paragrafo()
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                bloco.append(linhas[i].strip()[1:].strip())
                i += 1
            elementos += caixa(Paragraph(inline(" ".join(bloco)), ESTILOS["quote"]), AMARELO,
                               colors.HexColor("#F4B400"))
            continue
        elif m := re.match(r"# (.*)", s):
            fechar_paragrafo()
            elementos.append(MarcaTitulo(numero, m.group(1)))
        elif m := re.match(r"## (.*)", s):
            fechar_paragrafo()
            elementos.append(Paragraph(inline(m.group(1)), ESTILOS["h2"]))
        elif m := re.match(r"[-*] (.*)", s):
            fechar_paragrafo()
            elementos.append(Paragraph(inline(m.group(1)), ESTILOS["li"], bulletText="•"))
        elif m := re.match(r"(\d+)\. (.*)", s):
            fechar_paragrafo()
            elementos.append(Paragraph(inline(m.group(2)), ESTILOS["li"], bulletText=f"{m.group(1)}."))
        elif not s:
            fechar_paragrafo()
        else:
            paragrafo.append(s)
        i += 1
    fechar_paragrafo()
    return elementos


def grudados(titulo, bloco):
    """Título e o bloco seguinte numa tabela que não se divide entre colunas."""
    t = Table([[titulo], [bloco]], colWidths=[LARGURA_COLUNA])
    t.setStyle(TableStyle([("NOSPLIT", (0, 0), (0, 1)), ("TOPPADDING", (0, 0), (0, 0), titulo.style.spaceBefore),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 1), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t


def duas_colunas(elementos):
    """Distribui o conteúdo em duas colunas de altura parecida."""
    marca = [e for e in elementos if isinstance(e, MarcaTitulo)]
    resto = []
    for e in elementos:
        if isinstance(e, MarcaTitulo):
            continue
        anterior = resto[-1] if resto else None
        if isinstance(anterior, Paragraph) and anterior.style.name == "h2":
            resto[-1] = grudados(anterior, e)  # título nunca fica sozinho no fim da coluna
        else:
            resto.append(e)
    return marca + [BalancedColumns(resto, nCols=2, innerPadding=ESPACO_COLUNAS / 2,
                                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)]


def faixa_titulo(canvas, doc):
    """Desenhada no fim da página, quando já se sabe qual colinha está nela."""
    numero, titulo = getattr(doc, "colinha_atual", ("", ""))
    largura, altura = A4
    canvas.saveState()
    canvas.setFillColor(AZUL)
    canvas.rect(0, altura - 1.8 * cm, largura, 1.8 * cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont(FONTE, 8.5)
    canvas.drawString(MARGEM, altura - 0.75 * cm, f"COLINHA  |  MÓDULO {numero}")
    canvas.setFont(FONTE_NEGRITO, 16)
    canvas.drawString(MARGEM, altura - 1.45 * cm, titulo)
    canvas.setFont(FONTE, 8)
    canvas.drawRightString(largura - MARGEM, altura - 0.75 * cm, TITULO_CURSO)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.setFont(FONTE, 7)
    canvas.drawString(MARGEM, 0.6 * cm, f"{TITULO_CURSO}  |  {URL_SITE}")
    canvas.restoreState()


def gerar(destino, elementos, titulo, avisar=True):
    doc = BaseDocTemplate(str(destino), pagesize=A4, title=titulo, author=TITULO_CURSO,
                          leftMargin=MARGEM, rightMargin=MARGEM, topMargin=TOPO, bottomMargin=MARGEM)
    altura = A4[1] - TOPO - MARGEM
    pagina = Frame(MARGEM, MARGEM, A4[0] - 2 * MARGEM, altura, id="pagina", leftPadding=0, rightPadding=0,
                   topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="colinha", frames=[pagina], onPageEnd=faixa_titulo))
    doc.build(elementos)
    if avisar:
        print(f"Gerado: {destino.relative_to(RAIZ)}  ({doc.page} página{'s' if doc.page > 1 else ''})")
    return doc.page


def main():
    SAIDA.mkdir(exist_ok=True)
    todas, longas = [], []
    for arq in sorted(COLINHAS.glob("*.md")):
        numero = str(int(arq.stem.split("-")[0]))
        texto = arq.read_text(encoding="utf-8")
        titulo = re.search(r"^# (.*)", texto, re.M).group(1)
        destino = SAIDA / f"colinha-{arq.stem}.pdf"
        # testa da letra maior para a menor até caber em 1 página
        for escala in [x / 20 for x in range(36, 19, -1)]:  # de 1.8 até 1.0
            definir_escala(escala)
            if gerar(destino, duas_colunas(markdown_para_flowables(texto, numero)), "", avisar=False) == 1:
                break
        if gerar(destino, duas_colunas(markdown_para_flowables(texto, numero)),
                 f"Colinha {numero} - {titulo}") > 1:
            longas.append(arq.name)
        todas += duas_colunas(markdown_para_flowables(texto, numero)) + [PageBreak()]
    gerar(SAIDA / "Colinhas-TI-Basico.pdf", todas[:-1], f"{TITULO_CURSO} - Todas as colinhas")
    if longas:
        print("ATENÇÃO: passaram de 1 página:", ", ".join(longas))


if __name__ == "__main__":
    main()
