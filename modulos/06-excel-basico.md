# 6. Excel: Primeiros Passos

> **Objetivo:** entender a interface do Excel, digitar e formatar dados, criar as primeiras fórmulas e dominar os atalhos.

## 6.1 Conceitos básicos

| Termo | O que é |
|---|---|
| **Pasta de trabalho** | O arquivo do Excel (.xlsx) |
| **Planilha (aba)** | Cada folha dentro do arquivo (Planilha1, Planilha2...) |
| **Coluna** | Identificada por letras (A, B, C ... XFD) |
| **Linha** | Identificada por números (1, 2, 3 ... 1.048.576) |
| **Célula** | Encontro de coluna e linha. Ex.: `B3` |
| **Intervalo** | Grupo de células. Ex.: `A1:C10` |
| **Caixa de Nome** | Mostra o endereço da célula selecionada (à esquerda da barra de fórmulas) |
| **Barra de fórmulas** | Mostra/edita o conteúdo da célula |
| **Faixa de Opções** | Menu superior com as guias Página Inicial, Inserir, Fórmulas, Dados... |

## 6.2 Tipos de dados

- **Texto:** alinha à esquerda. Ex.: `Nome`, `Rua A`.
- **Número:** alinha à direita. Ex.: `150`, `3,14`.
- **Data/Hora:** são números por baixo (1 = 01/01/1900). Ex.: `03/10/2026`.
- **Fórmula:** sempre começa com `=`. Ex.: `=A1+B1`.

> **Dica:** para digitar um número como texto (ex.: CEP com zero à esquerda), comece com apóstrofo: `'01234`.

## 6.3 Operadores

| Operador | Função | Exemplo |
|---|---|---|
| `+` | Soma | `=A1+B1` |
| `-` | Subtração | `=A1-B1` |
| `*` | Multiplicação | `=A1*2` |
| `/` | Divisão | `=A1/4` |
| `^` | Potência | `=2^3` (resultado 8) |
| `%` | Porcentagem | `=A1*10%` |
| `&` | Junta textos | `=A1&" "&B1` |
| `=` `>` `<` `>=` `<=` `<>` | Comparação | `=A1>100` (VERDADEIRO/FALSO) |

O Excel respeita a ordem matemática: parênteses, potência, multiplicação/divisão, soma/subtração. `=2+3*4` dá 14; `=(2+3)*4` dá 20.

> **Separador de argumentos:** no Excel em português usa-se **ponto e vírgula** `;` . Ex.: `=SOMA(A1;B1)`. Nas versões em inglês usa-se vírgula: `=SUM(A1,B1)`.

## 6.4 Referências: relativa, absoluta e mista

Quando você **arrasta** uma fórmula, as referências mudam automaticamente.

| Tipo | Escrita | Ao arrastar |
|---|---|---|
| Relativa | `A1` | Muda linha e coluna |
| Absoluta | `$A$1` | Não muda nunca |
| Mista (coluna fixa) | `$A1` | Só a linha muda |
| Mista (linha fixa) | `A$1` | Só a coluna muda |

**Pressione F4** enquanto edita a referência para alternar entre os tipos.

Exemplo: preço em `B2:B10` e a taxa de imposto em `E1`:

```
=B2*$E$1
```

Arraste para baixo: `B2` vira `B3, B4...`, mas `$E$1` continua fixo.

Referência a outra aba: `=Vendas!B2`. A outro arquivo: `=[Orcamento.xlsx]Plan1!A1`.

## 6.5 Preenchimento e alça de preenchimento

O quadradinho no canto inferior direito da célula é a **alça de preenchimento**:

- Arraste para copiar uma fórmula para as células vizinhas.
- **Duplo clique** na alça preenche até o fim dos dados.
- Digite `Jan` e arraste: Fev, Mar, Abr... (também funciona com dias da semana, datas e números).
- Digite `1` e `2`, selecione os dois e arraste: sequência 3, 4, 5...

## 6.6 Formatação

| Recurso | Onde | Uso |
|---|---|---|
| Formato de número | Página Inicial > Número | Moeda (R$), Porcentagem, Data, Contábil |
| Casas decimais | Página Inicial > Número | Aumentar/Diminuir casas |
| Mesclar e centralizar | Página Inicial > Alinhamento | Títulos (use com moderação) |
| Quebrar texto | Página Inicial > Alinhamento | Texto em várias linhas na célula |
| Bordas | Página Inicial > Fonte | Linhas da tabela |
| Pincel de formatação | Página Inicial > Área de transferência | Copia só o formato |
| Estilos de célula | Página Inicial > Estilos | Formatos prontos |
| Formatar como Tabela | Página Inicial > Estilos | Tabela com filtros e cores (veja Módulo 8) |
| Formatar células | `Ctrl + 1` | Todas as opções de formato |

### Formatos personalizados úteis (Ctrl + 1 > Personalizado)

| Código | Resultado |
|---|---|
| `000.000.000-00` | CPF: 123.456.789-00 |
| `00000-000` | CEP: 01234-000 |
| `"R$" #.##0,00` | R$ 1.250,00 |
| `0,0%` | 12,5% |
| `dd/mm/aaaa` | 03/10/2026 |
| `dddd` | sexta-feira (dia da semana) |
| `mmmm/aaaa` | outubro/2026 |
| `[h]:mm` | Soma de horas acima de 24h (ex.: 37:30) |

## 6.7 Linhas, colunas e planilhas

- **Inserir linha/coluna:** botão direito no cabeçalho > Inserir (ou `Ctrl + +`).
- **Excluir:** botão direito > Excluir (ou `Ctrl + -`).
- **Ajustar largura:** duplo clique na divisa entre as letras das colunas.
- **Ocultar/Reexibir:** botão direito no cabeçalho.
- **Nova planilha:** `Shift + F11` ou o botão `+` ao lado das abas.
- **Renomear aba:** duplo clique no nome da aba.
- **Congelar painéis:** Exibir > Congelar Painéis (mantém o cabeçalho visível ao rolar).

## 6.8 Atalhos essenciais do Excel

> Os atalhos com `Ctrl + letra` variam entre o Excel em **português** e em **inglês**. A tabela mostra as duas versões quando são diferentes.

### Navegação e seleção

| Atalho | Função |
|---|---|
| `Ctrl + Seta` | Vai até o fim dos dados naquela direção |
| `Ctrl + Shift + Seta` | Seleciona até o fim dos dados |
| `Ctrl + Home` | Vai para A1 |
| `Ctrl + End` | Vai para a última célula usada |
| `Ctrl + Page Down/Up` | Próxima / anterior aba |
| `Ctrl + Espaço` | Seleciona a coluna inteira |
| `Shift + Espaço` | Seleciona a linha inteira |
| `Ctrl + T` (pt) / `Ctrl + A` (en) | Seleciona tudo |
| `F5` ou `Ctrl + G` | Ir para (célula ou Ir para Especial) |
| `Ctrl + Backspace` | Volta a tela para a célula ativa |

### Edição

| Atalho | Função |
|---|---|
| `F2` | Editar a célula |
| `Enter` / `Tab` | Confirma e desce / vai para a direita |
| `Esc` | Cancela a edição |
| `Alt + Enter` | Quebra de linha dentro da célula |
| `Ctrl + Enter` | Preenche todas as células selecionadas com o mesmo valor |
| `Ctrl + D` | Copia a célula de cima (preencher para baixo) |
| `Ctrl + R` | Copia a célula da esquerda (preencher para a direita) |
| `Ctrl + ;` | Insere a data de hoje |
| `Ctrl + Shift + ;` | Insere a hora atual |
| `Ctrl + E` | Preenchimento Relâmpago |
| `Ctrl + +` / `Ctrl + -` | Inserir / excluir linhas ou colunas |
| `Ctrl + Z` / `Ctrl + Y` | Desfazer / refazer |
| `Ctrl + Alt + V` | Colar especial (valores, formatos, transpor) |
| `Delete` | Apaga o conteúdo |

### Fórmulas

| Atalho | Função |
|---|---|
| `Alt + =` | AutoSoma |
| `F4` | Alterna referência relativa/absoluta (e repete a última ação) |
| `Shift + F3` | Inserir função |
| `F9` | Recalcula (ou avalia parte da fórmula selecionada) |
| `Ctrl + '` (crase/acento) | Mostra as fórmulas em vez dos resultados |
| `Ctrl + Shift + Enter` | Fórmula matricial (versões antigas) |
| `Ctrl + Shift + U` | Expande a barra de fórmulas |

### Formatação

| Atalho (pt-BR) | Atalho (inglês) | Função |
|---|---|---|
| `Ctrl + N` | `Ctrl + B` | Negrito |
| `Ctrl + I` | `Ctrl + I` | Itálico |
| `Ctrl + S` | `Ctrl + U` | Sublinhado |
| `Ctrl + 1` | `Ctrl + 1` | Formatar células |
| `Ctrl + Shift + $` | `Ctrl + Shift + $` | Formato moeda |
| `Ctrl + Shift + %` | `Ctrl + Shift + %` | Formato porcentagem |
| `Ctrl + Shift + #` | `Ctrl + Shift + #` | Formato data |
| `Ctrl + Shift + !` | `Ctrl + Shift + !` | Número com 2 casas e milhar |

### Arquivo e dados

| Atalho (pt-BR) | Atalho (inglês) | Função |
|---|---|---|
| `Ctrl + B` | `Ctrl + S` | Salvar |
| `F12` | `F12` | Salvar como |
| `Ctrl + O` | `Ctrl + N` | Nova pasta de trabalho |
| `Ctrl + A` | `Ctrl + O` | Abrir |
| `Ctrl + L` | `Ctrl + F` | Localizar |
| `Ctrl + U` | `Ctrl + H` | Substituir |
| `Ctrl + Alt + T` | `Ctrl + T` | Criar Tabela (com dados selecionados) |
| `Ctrl + Shift + L` | `Ctrl + Shift + L` | Ligar/desligar filtros |
| `Alt + F1` | `Alt + F1` | Gráfico instantâneo |
| `F11` | `F11` | Gráfico em nova aba |
| `F7` | `F7` | Verificar ortografia |
| `Alt` | `Alt` | Mostra as letras de atalho da faixa de opções |

> **Truque universal:** pressione `Alt` e siga as letras que aparecem na faixa de opções. Você não precisa decorar: o Excel mostra as letras na tela, e depois de alguns dias elas viram memória muscular.

## 6.9 Salvar e imprimir

- Formatos: `.xlsx` (padrão), `.xlsm` (com macros), `.csv` (texto separado por `;`), `.pdf`.
- **Exportar para PDF:** Arquivo > Salvar como > tipo PDF.
- **Imprimir bem:** Layout da Página > Orientação (Paisagem), **Dimensionar para Ajustar** (1 página de largura), **Imprimir Títulos** (repete o cabeçalho em todas as páginas), **Área de Impressão**.
- Use `Ctrl + P` para visualizar antes de imprimir.

## Resumo do módulo

- Fórmulas começam com `=`; no Excel em português o separador é `;`.
- `$` fixa referências (tecla F4).
- Duplo clique na alça de preenchimento copia a fórmula até o fim.
- `Ctrl + 1` formata, `Alt + =` soma, `Ctrl + Seta` navega.
