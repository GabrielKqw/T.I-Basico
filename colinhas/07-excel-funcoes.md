# Excel: Fórmulas e Funções

## Básicas

| | |
|---|---|
| `=SOMA(E2:E6)` | Soma |
| `=MÉDIA(E2:E6)` | Média |
| `=MÁXIMO(E2:E6)` | Maior valor |
| `=MÍNIMO(E2:E6)` | Menor valor |
| `=CONT.VALORES(A2:A6)` | Conta preenchidas |
| `=ARRED(A1;2)` | Arredonda (2 casas) |

## Decisão: SE

```
=SE(pergunta; se SIM; se NÃO)
```

```
=SE(E2>=1000;"Meta batida";"Abaixo")
```

Três respostas:

```
=SES(E2>=3000;"Ouro";E2>=1000;"Prata";VERDADEIRO;"Bronze")
```

| | |
|---|---|
| `=` / `<>` | Igual / diferente |
| `>` / `<` | Maior / menor |
| `>=` / `<=` | Maior ou igual / menor ou igual |
| `=SEERRO(conta;0)` | Erro vira 0 |

## Com condição

| | |
|---|---|
| `=SOMASE(A:A;"Ana";E:E)` | Soma as vendas da Ana |
| `=CONT.SE(C:C;"Notebook")` | Conta os Notebooks |
| `=MÉDIASE(B:B;"Norte";E:E)` | Média do Norte |
| `=SOMASES(E:E;B:B;"Sul";E:E;">1000")` | Soma com 2 condições |

> SOMASE = (onde procurar; o que procurar; o que somar)

## Procurar em outra tabela

```
=PROCV("Mouse";H2:I5;2;FALSO)
```

Procura na **1ª coluna**, traz a **2ª**. Use sempre **FALSO**.

```
=PROCX("Mouse";H2:H5;I2:I5;"Não achei")
```

## Textos

| | |
|---|---|
| `=ARRUMAR(A2)` | Tira espaços sobrando |
| `=PRI.MAIÚSCULA(A2)` | Maria Silva |
| `=MAIÚSCULA(A2)` | MARIA |
| `=ESQUERDA(A2;4)` | 4 primeiras letras |
| `=TEXTODEPOIS(A2;"@")` | O que vem depois do @ |
| `=A2&" - "&B2` | Junta textos |
| `Ctrl + E` | Dê 1 exemplo, o Excel completa |

## Datas

| | |
|---|---|
| `=HOJE()` | Data de hoje |
| `=MÊS(D2)` | Só o mês |
| `=DATADIF(nasc;HOJE();"y")` | Idade |
| `=D2+90` | 90 dias depois |
| `=D6-D2` | Dias entre datas |

## Erros

| | |
|---|---|
| `#####` | Coluna estreita |
| `#DIV/0!` | Dividiu por zero |
| `#N/D` | Não encontrou |
| `#NOME?` | Função escrita errada |
| `#VALOR!` | Texto no meio da conta |
| `#REF!` | Célula apagada |
