# 7. Excel: Fórmulas e Funções

> **Objetivo:** conhecer as funções do Excel por categoria, com sintaxe e exemplos prontos para usar. Os nomes estão em **português** (Excel pt-BR) e, entre parênteses, em **inglês**.

## 7.1 Como funciona uma função

```
=NOME_DA_FUNÇÃO(argumento1; argumento2; ...)
```

- Comece com `=`, digite as primeiras letras e use `Tab` para aceitar a sugestão.
- Argumentos entre colchetes `[ ]` na ajuda são **opcionais**.
- Clique em **fx** (ao lado da barra de fórmulas) para abrir o assistente de funções.

### Planilha de exemplo usada neste módulo

| | A | B | C | D | E |
|---|---|---|---|---|---|
| **1** | Vendedor | Região | Produto | Data | Valor |
| **2** | Ana | Sul | Notebook | 05/09/2026 | 3500 |
| **3** | Bruno | Norte | Mouse | 06/09/2026 | 80 |
| **4** | Ana | Sul | Monitor | 10/09/2026 | 1200 |
| **5** | Carla | Sudeste | Notebook | 12/09/2026 | 3700 |
| **6** | Bruno | Norte | Teclado | 15/09/2026 | 150 |

## 7.2 Matemáticas e estatísticas básicas

| Função (pt-BR) | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `SOMA` | SUM | Soma valores | `=SOMA(E2:E6)` = 8630 |
| `MÉDIA` | AVERAGE | Média aritmética | `=MÉDIA(E2:E6)` = 1726 |
| `MÁXIMO` | MAX | Maior valor | `=MÁXIMO(E2:E6)` = 3700 |
| `MÍNIMO` | MIN | Menor valor | `=MÍNIMO(E2:E6)` = 80 |
| `CONT.NÚM` | COUNT | Conta células com números | `=CONT.NÚM(E2:E6)` = 5 |
| `CONT.VALORES` | COUNTA | Conta células não vazias | `=CONT.VALORES(A2:A6)` = 5 |
| `CONTAR.VAZIO` | COUNTBLANK | Conta células vazias | `=CONTAR.VAZIO(A2:A100)` |
| `ARRED` | ROUND | Arredonda | `=ARRED(3,14159;2)` = 3,14 |
| `ARREDONDAR.PARA.CIMA` | ROUNDUP | Arredonda para cima | `=ARREDONDAR.PARA.CIMA(2,1;0)` = 3 |
| `ARREDONDAR.PARA.BAIXO` | ROUNDDOWN | Arredonda para baixo | `=ARREDONDAR.PARA.BAIXO(2,9;0)` = 2 |
| `INT` | INT | Parte inteira | `=INT(7,8)` = 7 |
| `TRUNCAR` | TRUNC | Corta as casas decimais | `=TRUNCAR(7,89;1)` = 7,8 |
| `MOD` | MOD | Resto da divisão | `=MOD(10;3)` = 1 |
| `ABS` | ABS | Valor absoluto | `=ABS(-5)` = 5 |
| `POTÊNCIA` | POWER | Potência | `=POTÊNCIA(2;10)` = 1024 |
| `RAIZ` | SQRT | Raiz quadrada | `=RAIZ(81)` = 9 |
| `MULT` | PRODUCT | Multiplica valores | `=MULT(2;3;4)` = 24 |
| `SOMARPRODUTO` | SUMPRODUCT | Soma de multiplicações | `=SOMARPRODUTO(B2:B5;C2:C5)` |
| `MED` | MEDIAN | Mediana | `=MED(E2:E6)` = 1200 |
| `MODO` | MODE | Valor mais frequente | `=MODO(1;2;2;3)` = 2 |
| `MAIOR` | LARGE | k-ésimo maior | `=MAIOR(E2:E6;2)` = 3500 |
| `MENOR` | SMALL | k-ésimo menor | `=MENOR(E2:E6;1)` = 80 |
| `ORDEM.EQ` | RANK.EQ | Posição no ranking | `=ORDEM.EQ(E2;$E$2:$E$6)` |
| `DESVPAD.A` | STDEV.S | Desvio padrão (amostra) | `=DESVPAD.A(E2:E6)` |
| `ALEATÓRIOENTRE` | RANDBETWEEN | Número aleatório | `=ALEATÓRIOENTRE(1;100)` |
| `SUBTOTAL` | SUBTOTAL | Cálculo que ignora linhas filtradas | `=SUBTOTAL(9;E2:E6)` (9 = soma) |
| `AGREGAR` | AGGREGATE | Como SUBTOTAL, ignorando erros | `=AGREGAR(9;6;E2:E6)` |

## 7.3 Funções condicionais (as mais pedidas em entrevistas)

| Função | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `SOMASE` | SUMIF | Soma com 1 condição | `=SOMASE(A2:A6;"Ana";E2:E6)` = 4700 |
| `SOMASES` | SUMIFS | Soma com várias condições | `=SOMASES(E2:E6;B2:B6;"Norte";E2:E6;">100")` = 150 |
| `CONT.SE` | COUNTIF | Conta com 1 condição | `=CONT.SE(C2:C6;"Notebook")` = 2 |
| `CONT.SES` | COUNTIFS | Conta com várias condições | `=CONT.SES(A2:A6;"Ana";E2:E6;">1000")` = 2 |
| `MÉDIASE` | AVERAGEIF | Média com condição | `=MÉDIASE(B2:B6;"Norte";E2:E6)` = 115 |
| `MÉDIASES` | AVERAGEIFS | Média com várias condições | `=MÉDIASES(E2:E6;B2:B6;"Sul";C2:C6;"Monitor")` |
| `MÁXIMOSES` | MAXIFS | Maior valor com condição | `=MÁXIMOSES(E2:E6;B2:B6;"Sul")` = 3500 |
| `MÍNIMOSES` | MINIFS | Menor valor com condição | `=MÍNIMOSES(E2:E6;A2:A6;"Bruno")` = 80 |

### Critérios que você pode usar

| Critério | Significado |
|---|---|
| `"Ana"` | Igual a Ana |
| `">1000"` | Maior que 1000 |
| `"<>Sul"` | Diferente de Sul |
| `"*book"` | Termina com "book" (`*` = qualquer texto) |
| `"A?a"` | `?` = um caractere qualquer |
| `">"&H1` | Maior que o valor da célula H1 |
| `">="&DATA(2026;9;10)` | Data a partir de 10/09/2026 |

## 7.4 Funções lógicas

| Função | Inglês | O que faz |
|---|---|---|
| `SE` | IF | Testa uma condição |
| `E` | AND | Verdadeiro se **todas** as condições forem verdadeiras |
| `OU` | OR | Verdadeiro se **pelo menos uma** for verdadeira |
| `NÃO` | NOT | Inverte o resultado |
| `SES` | IFS | Várias condições sem aninhar SE |
| `PARÂMETRO` | SWITCH | Compara um valor com uma lista |
| `SEERRO` | IFERROR | Valor alternativo se der erro |
| `SENÃODISP` | IFNA | Valor alternativo para #N/D |
| `XOU` | XOR | Ou exclusivo |

### Exemplos

```
=SE(E2>=1000;"Meta batida";"Abaixo da meta")

=SE(E(B2="Sul";E2>1000);"Bônus";"Sem bônus")

=SE(OU(C2="Notebook";C2="Monitor");"Eletrônico grande";"Acessório")

=SES(E2>=3000;"Ouro";E2>=1000;"Prata";VERDADEIRO;"Bronze")

=PARÂMETRO(B2;"Sul";"Equipe 1";"Norte";"Equipe 2";"Outras")

=SEERRO(E2/F2;0)
```

> **SE aninhado:** `=SE(E2>=3000;"Ouro";SE(E2>=1000;"Prata";"Bronze"))` funciona em qualquer versão, mas `SES` é mais fácil de ler (Excel 2019+).

## 7.5 Funções de procura e referência

| Função | Inglês | O que faz |
|---|---|---|
| `PROCV` | VLOOKUP | Procura na 1ª coluna e retorna uma coluna à direita |
| `PROCH` | HLOOKUP | Procura na 1ª linha e retorna uma linha abaixo |
| `PROCX` | XLOOKUP | Procura em qualquer direção (substitui PROCV/PROCH) |
| `ÍNDICE` | INDEX | Retorna o valor de uma posição |
| `CORRESP` | MATCH | Retorna a posição de um valor |
| `CORRESPX` | XMATCH | CORRESP moderno |
| `ESCOLHER` | CHOOSE | Escolhe de uma lista pelo número |
| `DESLOC` | OFFSET | Referência deslocada |
| `INDIRETO` | INDIRECT | Converte texto em referência |
| `LIN` / `COL` | ROW / COLUMN | Número da linha / coluna |
| `LINS` / `COLS` | ROWS / COLUMNS | Quantidade de linhas / colunas |
| `HIPERLINK` | HYPERLINK | Cria link clicável |
| `TRANSPOR` | TRANSPOSE | Troca linhas por colunas |

### PROCV passo a passo

```
=PROCV(valor_procurado; tabela; número_da_coluna; [FALSO])
```

Tabela de produtos em `H2:I5` (H = Produto, I = Preço):

```
=PROCV("Mouse";H2:I5;2;FALSO)
```

- `"Mouse"`: o que procurar.
- `H2:I5`: onde procurar (o valor tem que estar na **primeira coluna**).
- `2`: retornar a 2ª coluna da tabela (Preço).
- `FALSO` (ou `0`): correspondência **exata**. Use quase sempre!

> **Erro #N/D?** O valor não foi encontrado. Verifique espaços extras (use `ARRUMAR`), números armazenados como texto ou se a tabela está fixa com `$`.

### PROCX: o substituto moderno (Excel 365/2021+)

```
=PROCX(valor_procurado; coluna_procura; coluna_retorno; [se_não_encontrado])
```

```
=PROCX("Mouse";H2:H5;I2:I5;"Não cadastrado")
```

Vantagens: procura à esquerda, não quebra ao inserir colunas, já trata "não encontrado" e procura do último para o primeiro.

### ÍNDICE + CORRESP (funciona em todas as versões)

```
=ÍNDICE(I2:I5;CORRESP("Mouse";H2:H5;0))
```

## 7.6 Funções de texto

| Função | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `CONCAT` | CONCAT | Junta textos | `=CONCAT(A2;" - ";B2)` = Ana - Sul |
| `CONCATENAR` | CONCATENATE | Junta textos (versão antiga) | `=CONCATENAR(A2;B2)` |
| `UNIRTEXTO` | TEXTJOIN | Junta com separador | `=UNIRTEXTO(", ";VERDADEIRO;A2:A6)` |
| `ESQUERDA` | LEFT | Primeiros caracteres | `=ESQUERDA("Notebook";4)` = Note |
| `DIREITA` | RIGHT | Últimos caracteres | `=DIREITA("12345";2)` = 45 |
| `EXT.TEXTO` | MID | Caracteres do meio | `=EXT.TEXTO("ABC-123";5;3)` = 123 |
| `NÚM.CARACT` | LEN | Quantidade de caracteres | `=NÚM.CARACT("Excel")` = 5 |
| `MAIÚSCULA` | UPPER | Tudo maiúsculo | `=MAIÚSCULA("ana")` = ANA |
| `MINÚSCULA` | LOWER | Tudo minúsculo | `=MINÚSCULA("ANA")` = ana |
| `PRI.MAIÚSCULA` | PROPER | Primeira letra maiúscula | `=PRI.MAIÚSCULA("maria silva")` = Maria Silva |
| `ARRUMAR` | TRIM | Remove espaços extras | `=ARRUMAR("  Ana  ")` = Ana |
| `TIRAR` | CLEAN | Remove caracteres invisíveis | `=TIRAR(A2)` |
| `PROCURAR` | FIND | Posição de um texto (diferencia maiúsculas) | `=PROCURAR("@";"a@b.com")` = 2 |
| `LOCALIZAR` | SEARCH | Posição de um texto (não diferencia) | `=LOCALIZAR("book";C2)` |
| `SUBSTITUIR` | SUBSTITUTE | Troca um texto por outro | `=SUBSTITUIR("1.234";".";"")` = 1234 |
| `MUDAR` | REPLACE | Troca por posição | `=MUDAR("ABC";2;1;"X")` = AXC |
| `TEXTO` | TEXT | Formata número/data como texto | `=TEXTO(D2;"dd/mm/aaaa")` |
| `VALOR` | VALUE | Converte texto em número | `=VALOR("150")` = 150 |
| `REPT` | REPT | Repete texto | `=REPT("*";5)` = ***** |
| `EXATO` | EXACT | Compara textos exatamente | `=EXATO("a";"A")` = FALSO |
| `TEXTOANTES` | TEXTBEFORE | Texto antes de um delimitador (365) | `=TEXTOANTES("ana@email.com";"@")` = ana |
| `TEXTODEPOIS` | TEXTAFTER | Texto depois de um delimitador (365) | `=TEXTODEPOIS("ana@email.com";"@")` = email.com |
| `DIVIDIRTEXTO` | TEXTSPLIT | Divide texto em várias células (365) | `=DIVIDIRTEXTO("a;b;c";";")` |

> **Concatenar com `&`:** `=A2&" vendeu R$ "&TEXTO(E2;"#.##0,00")` resulta em "Ana vendeu R$ 3.500,00".

## 7.7 Funções de data e hora

| Função | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `HOJE` | TODAY | Data de hoje | `=HOJE()` |
| `AGORA` | NOW | Data e hora atuais | `=AGORA()` |
| `DATA` | DATE | Monta uma data | `=DATA(2026;10;3)` |
| `DIA` / `MÊS` / `ANO` | DAY / MONTH / YEAR | Extrai partes da data | `=MÊS(D2)` = 9 |
| `HORA` / `MINUTO` / `SEGUNDO` | HOUR / MINUTE / SECOND | Partes da hora | `=HORA(AGORA())` |
| `DIA.DA.SEMANA` | WEEKDAY | Dia da semana (1 = domingo) | `=DIA.DA.SEMANA(D2)` |
| `NÚMSEMANA` | WEEKNUM | Número da semana no ano | `=NÚMSEMANA(D2)` |
| `DIATRABALHO` | WORKDAY | Data após N dias úteis | `=DIATRABALHO(D2;10)` |
| `DIATRABALHOTOTAL` | NETWORKDAYS | Dias úteis entre datas | `=DIATRABALHOTOTAL(D2;D6)` |
| `DATAM` | EDATE | Soma meses | `=DATAM(D2;3)` (3 meses depois) |
| `FIMMÊS` | EOMONTH | Último dia do mês | `=FIMMÊS(D2;0)` = 30/09/2026 |
| `DATADIF` | DATEDIF | Diferença em anos/meses/dias | `=DATADIF(nascimento;HOJE();"y")` (idade) |
| `DATA.VALOR` | DATEVALUE | Texto em data | `=DATA.VALOR("03/10/2026")` |

> Subtrair datas dá a diferença em dias: `=D6-D2` = 10.

## 7.8 Funções de informação e erros

| Função | Inglês | O que faz |
|---|---|---|
| `ÉCÉL.VAZIA` | ISBLANK | Célula está vazia? |
| `ÉNÚM` | ISNUMBER | É número? |
| `ÉTEXTO` | ISTEXT | É texto? |
| `ÉERRO` / `ÉERROS` | ISERR / ISERROR | É erro? |
| `É.NÃO.DISP` | ISNA | É #N/D? |
| `ÉFÓRMULA` | ISFORMULA | Contém fórmula? |
| `NÃO.DISP` | NA | Gera #N/D |

### Erros comuns

| Erro | Causa | Solução |
|---|---|---|
| `#DIV/0!` | Divisão por zero | `=SEERRO(A1/B1;0)` |
| `#N/D` | Valor não encontrado (PROCV/PROCX) | Conferir o valor; usar SEERRO ou o 4º argumento do PROCX |
| `#NOME?` | Nome de função digitado errado | Verificar a grafia (ou usar nome em inglês no Excel pt-BR) |
| `#VALOR!` | Tipo errado (texto em conta) | Converter com VALOR, limpar espaços |
| `#REF!` | Referência apagada | Desfazer ou refazer a fórmula |
| `#NÚM!` | Número inválido | Revisar o cálculo |
| `#DESPEJAR!` (#SPILL!) | Fórmula dinâmica sem espaço livre | Limpar as células abaixo/ao lado |
| `#####` | Coluna estreita | Aumentar a largura da coluna |

## 7.9 Funções financeiras

| Função | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `PGTO` | PMT | Valor da parcela | `=PGTO(2%;12;-10000)` = parcela de 10 mil em 12x a 2% a.m. |
| `VF` | FV | Valor futuro | `=VF(1%;24;-500)` (guardar 500/mês por 2 anos) |
| `VP` | PV | Valor presente | `=VP(1%;12;-1000)` |
| `TAXA` | RATE | Taxa de juros | `=TAXA(12;-950;10000)` |
| `NPER` | NPER | Número de parcelas | `=NPER(2%;-500;5000)` |
| `VPL` | NPV | Valor presente líquido | `=VPL(10%;B2:B6)` |
| `TIR` | IRR | Taxa interna de retorno | `=TIR(B1:B6)` |

## 7.10 Funções de matriz dinâmica (Excel 365 / 2021+)

Estas funções "despejam" o resultado em várias células automaticamente.

| Função | Inglês | O que faz | Exemplo |
|---|---|---|---|
| `FILTRO` | FILTER | Filtra dados por condição | `=FILTRO(A2:E6;B2:B6="Sul";"Nada")` |
| `CLASSIFICAR` | SORT | Ordena | `=CLASSIFICAR(A2:E6;5;-1)` (por Valor, decrescente) |
| `CLASSIFICARPOR` | SORTBY | Ordena por outra coluna | `=CLASSIFICARPOR(A2:A6;E2:E6;-1)` |
| `ÚNICO` | UNIQUE | Lista sem repetições | `=ÚNICO(A2:A6)` = Ana, Bruno, Carla |
| `SEQUÊNCIA` | SEQUENCE | Gera sequência | `=SEQUÊNCIA(10)` = 1 a 10 |
| `MATRIZALEATÓRIA` | RANDARRAY | Números aleatórios | `=MATRIZALEATÓRIA(5)` |
| `EMPILHARV` | VSTACK | Empilha tabelas | `=EMPILHARV(Jan!A2:C10;Fev!A2:C10)` |
| `ESCOLHERCOLS` | CHOOSECOLS | Escolhe colunas | `=ESCOLHERCOLS(A2:E6;1;5)` |
| `LET` | LET | Cria variáveis na fórmula | `=LET(total;SOMA(E2:E6);total*0,1)` |
| `LAMBDA` | LAMBDA | Cria sua própria função | Ver Módulo 8 |

Combinação poderosa: total vendido por vendedor, ordenado:

```
=CLASSIFICAR(ÚNICO(A2:A6))          (lista de vendedores em G2)
=SOMASE(A2:A6;G2#;E2:E6)             (total de cada um; G2# = todo o resultado despejado)
```

## 7.11 Dicas de ouro

1. Use `F9` em um pedaço selecionado da fórmula para ver o resultado parcial (depois `Esc`).
2. **Fórmulas > Avaliar Fórmula** mostra o cálculo passo a passo.
3. **Fórmulas > Rastrear Precedentes** mostra de onde vêm os dados.
4. Dê **nomes** a intervalos (Caixa de Nome ou Fórmulas > Definir Nome): `=SOMA(Vendas)` é mais claro que `=SOMA(E2:E6)`.
5. Não sabe o nome de uma função? Peça ao ChatGPT (Módulo 10)!

## Resumo do módulo

- Básicas: `SOMA`, `MÉDIA`, `MÁXIMO`, `MÍNIMO`, `CONT.VALORES`.
- Condicionais: `SE`, `SOMASES`, `CONT.SES`, `SEERRO`.
- Procura: `PROCV` (com FALSO), `PROCX`, `ÍNDICE`+`CORRESP`.
- Texto: `ARRUMAR`, `ESQUERDA`, `TEXTO`, `&`.
- Datas: `HOJE`, `DATADIF`, `DIATRABALHOTOTAL`.
- Modernas: `FILTRO`, `ÚNICO`, `CLASSIFICAR`.
