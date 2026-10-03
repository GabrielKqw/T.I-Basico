# Curso de T.I. Básico

Curso gratuito de informática para iniciantes: do zero ao uso do computador no trabalho, com Excel, planilhas e ChatGPT. Não precisa saber nada antes de começar.

> **Para quem é este curso?** Para quem está começando na informática, quer conseguir o primeiro emprego em escritório ou quer aprender Excel e usar Inteligência Artificial no dia a dia.

## O que você vai aprender

Cada módulo tem uma **colinha**: um resumo de 1 página para imprimir e deixar do lado do computador.

| Módulo | Conteúdo | Colinha (PDF) |
|---|---|---|
| 1 | Fundamentos de Informática (partes do computador, arquivos) | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-01-fundamentos.pdf) |
| 2 | Windows e Atalhos de Teclado | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-02-windows-atalhos.pdf) |
| 3 | Comandos do Prompt (CMD) | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-03-comandos-cmd.pdf) |
| 4 | PowerShell | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-04-powershell.pdf) |
| 5 | Internet, E-mail e Segurança | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-05-internet-seguranca.pdf) |
| 6 | Excel: Primeiros Passos | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-06-excel-basico.pdf) |
| 7 | Excel: Fórmulas e Funções | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-07-excel-funcoes.pdf) |
| 8 | Excel: Recursos Avançados | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-08-excel-avancado.pdf) |
| 9 | Google Planilhas | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-09-google-planilhas.pdf) |
| 10 | ChatGPT para Excel | [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/colinha-10-chatgpt-excel.pdf) |
| 11 | Exercícios e Gabarito | (online) |

**Todas as colinhas em um só PDF:** [Baixar](https://github.com/GabrielKqw/T.I-Basico/raw/main/pdfs/Colinhas-TI-Basico.pdf)

**Planilha de exercícios (Excel):** [Baixar planilha](https://github.com/GabrielKqw/T.I-Basico/raw/main/planilhas/exercicios-excel.xlsx)

## Como estudar

1. Siga os módulos na ordem: cada um usa o que você aprendeu no anterior.
2. Pratique **no computador** enquanto lê. Informática se aprende fazendo.
3. Ao final de cada módulo, faça os exercícios do Módulo 11.
4. Imprima as colinhas e consulte sempre que precisar.

## Carga horária sugerida

| Parte | Módulos | Tempo estimado |
|---|---|---|
| Informática Essencial | 1 a 5 | 8 horas |
| Excel e Planilhas | 6 a 9 | 14 horas |
| ChatGPT para Excel | 10 | 3 horas |
| Exercícios | 11 | 5 horas |
| **Total** | | **30 horas** |

## Para mantenedores

O conteúdo das páginas fica em `modulos/` e o das colinhas em `colinhas/`. Depois de editar:

```
pip install reportlab openpyxl
python scripts/gerar_pdfs.py
python scripts/gerar_planilha.py
```

O site no **GitBook** é sincronizado com este repositório (Git Sync): a estrutura está em `gitbook-docs.yaml`, `.gitbook.yaml` e `SUMMARY.md`.
