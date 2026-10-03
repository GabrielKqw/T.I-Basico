# 7. Excel: Fórmulas e Funções

> **Objetivo:** aprender as funções que mais aparecem no trabalho e em testes de emprego, com exemplos prontos para copiar.

## 7.1 Como se escreve uma função

```
=NOME(o que a função precisa)
```

- Comece com `=` e digite as primeiras letras do nome. O Excel mostra uma lista: aperte `Tab` para escolher.
- O que vai dentro dos parênteses é separado por **ponto e vírgula** `;`.
- Textos vão **entre aspas**: `"Ana"`. Números e células, sem aspas.

### Tabela usada nos exemplos

| | A | B | C | D | E |
|---|---|---|---|---|---|
| **1** | Vendedor | Região | Produto | Data | Valor |
| **2** | Ana | Sul | Notebook | 05/09/2026 | 3500 |
| **3** | Bruno | Norte | Mouse | 06/09/2026 | 80 |
| **4** | Ana | Sul | Monitor | 10/09/2026 | 1200 |
| **5** | Carla | Sudeste | Notebook | 12/09/2026 | 3700 |
| **6** | Bruno | Norte | Teclado | 15/09/2026 | 150 |

## 7.2 As básicas

| Função | O que faz | Exemplo | Resultado |
|---|---|---|---|
| `SOMA` | Soma tudo | `=SOMA(E2:E6)` | 8630 |
| `MÉDIA` | Calcula a média | `=MÉDIA(E2:E6)` | 1726 |
| `MÁXIMO` | Mostra o maior valor | `=MÁXIMO(E2:E6)` | 3700 |
| `MÍNIMO` | Mostra o menor valor | `=MÍNIMO(E2:E6)` | 80 |
| `CONT.VALORES` | Conta quantas células estão preenchidas | `=CONT.VALORES(A2:A6)` | 5 |
| `ARRED` | Arredonda (aqui, para 2 casas) | `=ARRED(3,14159;2)` | 3,14 |

## 7.3 SE: o Excel tomando decisões

O `SE` faz uma pergunta e dá uma resposta para "sim" e outra para "não":

```
=SE(pergunta; resposta se SIM; resposta se NÃO)
```

```
=SE(E2>=1000;"Meta batida";"Abaixo da meta")
```

Lê-se: "se o valor em E2 for maior ou igual a 1000, escreva *Meta batida*; se não, escreva *Abaixo da meta*".

### Sinais para as perguntas

| Sinal | Significa |
|---|---|
| `=` | igual a |
| `<>` | diferente de |
| `>` / `<` | maior que / menor que |
| `>=` / `<=` | maior ou igual / menor ou igual |

### Mais de duas respostas

Para três faixas (Ouro, Prata, Bronze), use `SES`:

```
=SES(E2>=3000;"Ouro";E2>=1000;"Prata";VERDADEIRO;"Bronze")
```

O Excel testa na ordem: se for 3000 ou mais é Ouro; se não, se for 1000 ou mais é Prata; **senão** (o `VERDADEIRO` no final), é Bronze.

### Esconder erros: SEERRO

```
=SEERRO(E2/F2;0)
```

Se a conta der erro (como dividir por zero), mostra 0 em vez do erro.

## 7.4 Somar e contar só o que interessa

Estas são **as mais pedidas em testes de emprego**.

| Função | O que faz | Exemplo | Resultado |
|---|---|---|---|
| `SOMASE` | Soma só o que bate com uma condição | `=SOMASE(A2:A6;"Ana";E2:E6)` | 4700 |
| `CONT.SE` | Conta só o que bate com uma condição | `=CONT.SE(C2:C6;"Notebook")` | 2 |
| `MÉDIASE` | Média só do que bate com uma condição | `=MÉDIASE(B2:B6;"Norte";E2:E6)` | 115 |
| `SOMASES` | Soma com **várias** condições | `=SOMASES(E2:E6;B2:B6;"Sul";E2:E6;">1000")` | 4700 |
| `CONT.SES` | Conta com **várias** condições | `=CONT.SES(A2:A6;"Ana";E2:E6;">1000")` | 2 |

**Como ler o `SOMASE`:** `=SOMASE(onde procurar; o que procurar; o que somar)`. No exemplo: procure "Ana" na coluna de vendedores e some os valores dela.

> **Condições com números** vão entre aspas: `">1000"` (maior que mil), `"<>Sul"` (diferente de Sul).

## 7.5 Procurar uma informação: PROCV e PROCX

Servem para **buscar um dado em outra tabela**. Exemplo: você tem o nome do produto e quer achar o preço dele numa lista de preços.

Lista de preços em `H2:I5`:

| H | I |
|---|---|
| Produto | Preço |
| Mouse | 80 |
| Teclado | 150 |
| Monitor | 1200 |

### PROCV

```
=PROCV("Mouse";H2:I5;2;FALSO)
```

Lê-se: "procure **Mouse** na tabela **H2:I5** e me traga o que está na **2ª coluna** (o preço), mas só se achar **exatamente** igual (FALSO)".

> **Regras do PROCV:** o que você procura tem que estar na **primeira coluna** da tabela, e no final use sempre `FALSO`.

### PROCX (mais fácil, Excel 365 e 2021)

```
=PROCX("Mouse";H2:H5;I2:I5;"Não encontrado")
```

Lê-se: "procure **Mouse** na coluna H e me traga o que está na mesma linha da coluna I. Se não achar, escreva *Não encontrado*".

> **Deu `#N/D`?** O Excel não encontrou o que você procurou. Normalmente é um espaço sobrando ou o nome escrito diferente.

## 7.6 Arrumando textos

| Função | O que faz | Exemplo | Resultado |
|---|---|---|---|
| `ARRUMAR` | Tira espaços sobrando | `=ARRUMAR("  Ana  ")` | Ana |
| `PRI.MAIÚSCULA` | Primeira letra de cada palavra maiúscula | `=PRI.MAIÚSCULA("maria silva")` | Maria Silva |
| `MAIÚSCULA` | Tudo em maiúsculas | `=MAIÚSCULA("ana")` | ANA |
| `ESQUERDA` | Pega as primeiras letras | `=ESQUERDA("Notebook";4)` | Note |
| `DIREITA` | Pega as últimas letras | `=DIREITA("12345";2)` | 45 |
| `TEXTOANTES` | Pega o que vem antes de um sinal | `=TEXTOANTES("ana@email.com";"@")` | ana |
| `TEXTODEPOIS` | Pega o que vem depois de um sinal | `=TEXTODEPOIS("ana@email.com";"@")` | email.com |

**Juntar textos:** use o `&`.

```
=A2&" - "&B2
```

Resultado: `Ana - Sul`.

> **Atalho mágico (`Ctrl + E`):** na coluna ao lado, digite o primeiro resultado que você quer (ex.: só o primeiro nome) e aperte `Ctrl + E`. O Excel entende o padrão e completa o resto sozinho, sem fórmula!

## 7.7 Datas

| Função | O que faz | Exemplo |
|---|---|---|
| `HOJE` | Data de hoje (atualiza todo dia) | `=HOJE()` |
| `DIA` / `MÊS` / `ANO` | Pega só o dia, o mês ou o ano | `=MÊS(D2)` dá 9 |
| `DATADIF` | Diferença em anos completos (ex.: idade) | `=DATADIF(nascimento;HOJE();"y")` |
| `DIATRABALHOTOTAL` | Quantos dias úteis entre duas datas | `=DIATRABALHOTOTAL(D2;D6)` |

> **Conta com datas:** subtrair uma data de outra dá os dias entre elas (`=D6-D2` dá 10). Somar números a uma data anda para frente: `=D2+90` é 90 dias depois.

## 7.8 Os erros e o que eles querem dizer

| Erro | O que aconteceu | Como resolver |
|---|---|---|
| `#####` | A coluna está estreita demais | Aumente a largura da coluna |
| `#DIV/0!` | Divisão por zero (ou por célula vazia) | Confira os números ou use `SEERRO` |
| `#N/D` | O PROCV/PROCX não encontrou | Confira se está escrito igual |
| `#NOME?` | Nome da função escrito errado | Confira a escrita (acentos contam!) |
| `#VALOR!` | Conta com texto no meio | Veja se tem texto onde deveria ter número |
| `#REF!` | Uma célula usada na conta foi apagada | `Ctrl + Z` ou refaça a fórmula |

## 7.9 Bônus: lista sem repetição (Excel 365)

```
=ÚNICO(A2:A6)
```

Mostra a lista de vendedores sem repetir: Ana, Bruno, Carla.

## Resumo do módulo

- Básicas: `SOMA`, `MÉDIA`, `MÁXIMO`, `MÍNIMO`, `CONT.VALORES`.
- Decisão: `SE` e `SES`.
- Com condição: `SOMASE`, `CONT.SE`, `SOMASES`.
- Procurar: `PROCV` (sempre com `FALSO`) ou `PROCX`.
- Textos: `ARRUMAR`, `PRI.MAIÚSCULA`, `&` e o atalho `Ctrl + E`.
