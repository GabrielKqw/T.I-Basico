# Curso de T.I. Básico

Curso gratuito e completo de informática para iniciantes: do zero ao uso profissional do computador, comandos de terminal, Excel/planilhas e uso do ChatGPT para turbinar suas planilhas.

> **Para quem é este curso?** Para quem está começando na informática, quer conseguir o primeiro emprego em escritório/administrativo, ou quer dominar o Excel e usar Inteligência Artificial no dia a dia.

## O que você vai aprender

| Módulo | Conteúdo | PDF |
|---|---|---|
| 1 | Fundamentos de Informática (hardware, software, arquivos) | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/01-fundamentos.pdf) |
| 2 | Windows e Atalhos de Teclado | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/02-windows-atalhos.pdf) |
| 3 | Comandos do Prompt (CMD) | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/03-comandos-cmd.pdf) |
| 4 | PowerShell e Terminal Linux | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/04-powershell-linux.pdf) |
| 5 | Internet, E-mail e Segurança | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/05-internet-seguranca.pdf) |
| 6 | Excel: Primeiros Passos | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/06-excel-basico.pdf) |
| 7 | Excel: Fórmulas e Funções | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/07-excel-funcoes.pdf) |
| 8 | Excel: Recursos Avançados | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/08-excel-avancado.pdf) |
| 9 | Google Planilhas | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/09-google-planilhas.pdf) |
| 10 | ChatGPT para Excel | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/10-chatgpt-excel.pdf) |
| 11 | Exercícios e Gabarito | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/11-exercicios.pdf) |

**Apostila completa (todos os módulos em um só PDF):** [Baixar apostila](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/Apostila-Completa-TI-Basico.pdf)

**Planilha de exercícios (Excel):** [Baixar planilha](https://github.com/GabrielKqw/T.I-Basico/raw/main/planilhas/exercicios-excel.xlsx)

## Como estudar

1. Siga os módulos na ordem: cada um usa o que foi visto no anterior.
2. Pratique **no computador** enquanto lê. Informática se aprende fazendo.
3. Ao final de cada módulo, faça os exercícios do Módulo 11.
4. Baixe os PDFs para estudar offline ou imprimir.

## Carga horária sugerida

| Parte | Módulos | Tempo estimado |
|---|---|---|
| Informática Essencial | 1 a 5 | 10 horas |
| Excel e Planilhas | 6 a 9 | 16 horas |
| ChatGPT para Excel | 10 | 4 horas |
| Exercícios | 11 | 6 horas |
| **Total** | | **36 horas** |

## Para mantenedores

Os PDFs são gerados a partir dos arquivos Markdown em `modulos/`. Depois de editar o conteúdo:

```
pip install reportlab openpyxl
python scripts/gerar_pdfs.py
python scripts/gerar_planilha.py
```

O repositório está pronto para o **GitBook** (Git Sync): a estrutura é definida em `.gitbook.yaml` e `SUMMARY.md`.
