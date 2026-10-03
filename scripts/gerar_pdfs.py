"""Converte os módulos em Markdown (modulos/*.md) em PDFs (pdfs/).

Gera um PDF por módulo e a apostila completa. Suporta o subconjunto de
Markdown usado no curso: títulos, parágrafos, listas, tabelas, blocos de
código, citações (dicas), negrito, código inline e links.

Uso: python scripts/gerar_pdfs.py   (requer: pip install reportlab)
"""
import re
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (PageBreak, Paragraph, Preformatted,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

RAIZ = Path(__file__).resolve().parent.parent
MODULOS = RAIZ / "modulos"
SAIDA = RAIZ / "pdfs"
TITULO_CURSO = "Curso de T.I. Básico"
URL_REPO = "https://github.com/GabrielKqw/T.I-Basico"

AZUL = colors.HexColor("#1F4E79")
AZUL_CLARO = colors.HexColor("#EAF1F8")
CINZA_CODIGO = colors.HexColor("#F4F4F4")
AMARELO = colors.HexColor("#FFF8E1")
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

ESTILOS = {
    "h1": ParagraphStyle("h1", fontName=FONTE_NEGRITO, fontSize=22, leading=27, textColor=AZUL, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName=FONTE_NEGRITO, fontSize=15, leading=19, textColor=AZUL, spaceBefore=12, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName=FONTE_NEGRITO, fontSize=12, leading=15, textColor=colors.HexColor("#2E75B6"), spaceBefore=8, spaceAfter=4),
    "p": ParagraphStyle("p", fontName=FONTE, fontSize=10, leading=14, spaceAfter=6),
    "li": ParagraphStyle("li", fontName=FONTE, fontSize=10, leading=14, leftIndent=14, bulletIndent=4, spaceAfter=2),
    "cell": ParagraphStyle("cell", fontName=FONTE, fontSize=8.5, leading=11),
    "cellh": ParagraphStyle("cellh", fontName=FONTE_NEGRITO, fontSize=8.5, leading=11, textColor=colors.white),
    "quote": ParagraphStyle("quote", fontName=FONTE, fontSize=9.5, leading=13.5),
    "code": ParagraphStyle("code", fontName=FONTE_MONO, fontSize=8.5, leading=11.5),
    "capa_t": ParagraphStyle("capa_t", fontName=FONTE_NEGRITO, fontSize=34, leading=40, textColor=AZUL, alignment=TA_CENTER),
    "capa_s": ParagraphStyle("capa_s", fontName=FONTE, fontSize=14, leading=20, alignment=TA_CENTER, textColor=colors.HexColor("#444444")),
    "sum": ParagraphStyle("sum", fontName=FONTE, fontSize=12, leading=22),
}
LARGURA = A4[0] - 4 * cm


def inline(texto):
    """Converte Markdown inline (negrito, código, links) para a marcação do ReportLab."""
    partes = re.split(r"(`[^`]+`)", texto)
    saida = []
    for parte in partes:
        if parte.startswith("`") and parte.endswith("`") and len(parte) > 1:
            codigo = parte[1:-1].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            saida.append(f'<font name="{FONTE_MONO}" color="#B03A2E">{codigo}</font>')
            continue
        parte = parte.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        parte = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", parte)
        parte = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, parte)
        saida.append(parte)
    return "".join(saida)


def _link(m):
    rotulo, url = m.group(1), m.group(2)
    if not url.startswith("http"):  # links internos: apontar para o repositório
        url = f"{URL_REPO}/blob/main/{url.lstrip('./')}"
    return f'<link href="{url}" color="#2E75B6"><u>{rotulo}</u></link>'


def tabela(linhas):
    celulas = [[c.strip() for c in l.strip().strip("|").split("|")] for l in linhas]
    celulas = [c for c in celulas if not all(re.fullmatch(r":?-{2,}:?", x) for x in c if x)]
    ncol = max(len(c) for c in celulas)
    celulas = [c + [""] * (ncol - len(c)) for c in celulas]
    # largura das colunas proporcional ao conteúdo
    pesos = [max(11, min(45, max(len(l[i]) for l in celulas))) ** 0.8 for i in range(ncol)]
    # garante que a maior palavra de cada coluna caiba sem ser quebrada
    minimos = [max(len(w) for l in celulas for w in (l[i].replace("`", "").split() or [""])) * 6.3 + 10
               for i in range(ncol)]
    minimos = [min(m, LARGURA / ncol) for m in minimos]  # palavras enormes (fórmulas) podem quebrar
    larguras = [LARGURA * p / sum(pesos) for p in pesos]
    fixas = set()
    for _ in range(ncol):
        fixas |= {i for i in range(ncol) if larguras[i] < minimos[i]}
        resto = LARGURA - sum(minimos[i] for i in fixas)
        livres = sum(pesos[i] for i in range(ncol) if i not in fixas)
        larguras = [minimos[i] if i in fixas else resto * pesos[i] / livres for i in range(ncol)]
    dados = [[Paragraph(inline(x), ESTILOS["cellh" if r == 0 else "cell"]) for x in linha]
             for r, linha in enumerate(celulas)]
    t = Table(dados, colWidths=larguras, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, AZUL_CLARO]),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [t, Spacer(1, 8)]


def caixa(conteudo, fundo, borda):
    t = Table([[conteudo]], colWidths=[LARGURA])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fundo),
        ("LINEBEFORE", (0, 0), (0, -1), 3, borda),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [t, Spacer(1, 8)]


def markdown_para_flowables(texto):
    elementos, i = [], 0
    linhas = texto.splitlines()
    paragrafo = []

    def fechar_paragrafo():
        if paragrafo:
            elementos.append(Paragraph(inline(" ".join(paragrafo)), ESTILOS["p"]))
            paragrafo.clear()

    while i < len(linhas):
        linha = linhas[i]
        s = linha.strip()
        if s.startswith("```"):
            fechar_paragrafo()
            bloco = []
            i += 1
            while i < len(linhas) and not linhas[i].strip().startswith("```"):
                bloco.append(linhas[i])
                i += 1
            elementos += caixa(Preformatted("\n".join(bloco), ESTILOS["code"], maxLineLength=95), CINZA_CODIGO, colors.HexColor("#888888"))
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
            elementos += caixa(Paragraph(inline(" ".join(bloco)), ESTILOS["quote"]), AMARELO, colors.HexColor("#F4B400"))
            continue
        elif m := re.match(r"(#{1,3}) (.*)", s):
            fechar_paragrafo()
            nivel = len(m.group(1))
            elementos.append(Paragraph(inline(m.group(2)), ESTILOS[f"h{nivel}"]))
            if nivel == 1:
                elementos[-1].outline = m.group(2)
        elif m := re.match(r"[-*] (.*)", s):
            fechar_paragrafo()
            elementos.append(Paragraph(inline(m.group(1)), ESTILOS["li"], bulletText="•"))
        elif m := re.match(r"(\d+)\. (.*)", s):
            fechar_paragrafo()
            elementos.append(Paragraph(inline(m.group(2)), ESTILOS["li"], bulletText=f"{m.group(1)}."))
        elif s == "---":
            fechar_paragrafo()
            elementos.append(PageBreak())
        elif not s:
            fechar_paragrafo()
        else:
            paragrafo.append(s)
        i += 1
    fechar_paragrafo()
    return elementos


class Documento(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        titulo = getattr(flowable, "outline", None)
        if titulo:  # marcadores (bookmarks) no leitor de PDF
            chave = f"m{id(flowable)}"
            self.canv.bookmarkPage(chave)
            self.canv.addOutlineEntry(titulo, chave, level=0)


def rodape(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONTE, 8)
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.drawString(2 * cm, 1.2 * cm, f"{TITULO_CURSO}  |  {URL_REPO}")
    canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Página {doc.page}")
    canvas.setStrokeColor(BORDA)
    canvas.line(2 * cm, 1.5 * cm, A4[0] - 2 * cm, 1.5 * cm)
    canvas.restoreState()


def capa(subtitulo):
    return [Spacer(1, 6 * cm), Paragraph(TITULO_CURSO, ESTILOS["capa_t"]), Spacer(1, 1 * cm),
            Paragraph(subtitulo, ESTILOS["capa_s"]), Spacer(1, 0.6 * cm),
            Paragraph(f"Atualizado em {date.today():%d/%m/%Y}", ESTILOS["capa_s"]), Spacer(1, 0.4 * cm),
            Paragraph(f'<link href="{URL_REPO}" color="#2E75B6">{URL_REPO}</link>', ESTILOS["capa_s"]),
            PageBreak()]


def gerar(destino, elementos, titulo):
    doc = Documento(str(destino), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                    topMargin=2 * cm, bottomMargin=2 * cm, title=titulo, author=TITULO_CURSO)
    doc.build(elementos, onFirstPage=rodape, onLaterPages=rodape)
    print("Gerado:", destino.relative_to(RAIZ))


def main():
    SAIDA.mkdir(exist_ok=True)
    arquivos = sorted(MODULOS.glob("*.md"))
    apostila = capa("Apostila completa: Informática, Comandos, Excel, Planilhas e ChatGPT para Excel")
    sumario = [Paragraph("Sumário", ESTILOS["h1"])]
    for arq in arquivos:
        texto = arq.read_text(encoding="utf-8")
        titulo = re.search(r"^# (.*)", texto, re.M).group(1)
        sumario.append(Paragraph(inline(titulo), ESTILOS["sum"]))
        gerar(SAIDA / f"{arq.stem}.pdf", markdown_para_flowables(texto), f"{TITULO_CURSO} - {titulo}")
    apostila += sumario + [PageBreak()]
    for arq in arquivos:
        apostila += markdown_para_flowables(arq.read_text(encoding="utf-8")) + [PageBreak()]
    gerar(SAIDA / "Apostila-Completa-TI-Basico.pdf", apostila[:-1], f"{TITULO_CURSO} - Apostila Completa")


if __name__ == "__main__":
    main()
