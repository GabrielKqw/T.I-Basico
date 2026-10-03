# 6. Excel: Primeiros Passos

> **Objetivo:** entender a tela do Excel, digitar e arrumar dados e fazer suas primeiras contas.

## 6.1 Conhecendo a planilha

O Excel é uma grande **tabela** onde você guarda informações e faz contas automáticas.

| Nome | O que é |
|---|---|
| **Coluna** | As "filas em pé", identificadas por **letras**: A, B, C... |
| **Linha** | As "filas deitadas", identificadas por **números**: 1, 2, 3... |
| **Célula** | Cada quadradinho. O nome dela junta a letra da coluna e o número da linha. Ex.: `B3` é a coluna B, linha 3 |
| **Intervalo** | Um grupo de células. `A1:A10` quer dizer "de A1 até A10" |
| **Aba** | As "folhas" lá embaixo (Planilha1, Planilha2). Um arquivo pode ter várias |
| **Barra de fórmulas** | A barra comprida em cima das colunas. Mostra o que está escrito dentro da célula |

## 6.2 Digitando dados

- Clique na célula, digite e aperte `Enter` (desce) ou `Tab` (vai para a direita).
- Para corrigir, clique na célula e aperte `F2`.
- **Texto** fica encostado à esquerda; **números** ficam à direita. Se um número ficou à esquerda, o Excel achou que é texto e não vai conseguir fazer conta com ele.

> **Dica:** para digitar algo que começa com zero (como um CEP), coloque um apóstrofo antes: `'01234-000`.

## 6.3 Fazendo contas

Toda conta no Excel **começa com o sinal de igual** `=`.

| Sinal | Conta | Exemplo |
|---|---|---|
| `+` | Somar | `=A1+B1` |
| `-` | Subtrair | `=A1-B1` |
| `*` | Multiplicar | `=A1*2` |
| `/` | Dividir | `=A1/4` |
| `%` | Porcentagem | `=A1*10%` (10% de A1) |

> **Por que usar o nome da célula e não o número?** Se você escreve `=A1+B1` e depois muda o valor de A1, o resultado se atualiza sozinho. Essa é a mágica do Excel.

Como na matemática da escola, a multiplicação vem antes da soma: `=2+3*4` dá 14. Use parênteses para mudar a ordem: `=(2+3)*4` dá 20.

## 6.4 Sua primeira função: SOMA

Uma **função** é uma conta pronta. A mais usada é a `SOMA`:

```
=SOMA(A1:A10)
```

Lê-se: "some de A1 até A10".

> **Atalho:** clique na célula embaixo dos números e aperte `Alt + =`. O Excel monta a SOMA sozinho.

No Excel em português, quando a função recebe mais de uma informação, elas são separadas por **ponto e vírgula** `;`. Ex.: `=SOMA(A1;C1)` soma só A1 e C1.

## 6.5 Copiar uma conta para as outras linhas

Fez a conta na primeira linha? Não precisa digitar de novo nas outras:

1. Clique na célula com a conta.
2. Repare no **quadradinho** no canto de baixo à direita da célula.
3. **Clique duas vezes** nele. A conta é copiada para todas as linhas de baixo.

O Excel ajusta a conta sozinho: `=B2*C2` vira `=B3*C3` na linha de baixo, `=B4*C4` na outra, e assim por diante.

> **Truque do preenchimento:** digite `Jan` e arraste o quadradinho para baixo: o Excel completa Fev, Mar, Abr... Funciona com dias da semana e números também.

## 6.6 O cifrão `$`: travar uma célula

Às vezes você **não quer** que a célula mude quando copia a conta. Exemplo: todos os preços precisam ser multiplicados pela mesma taxa, que está em `E1`.

```
=B2*$E$1
```

O `$` "tranca" a célula. Ao copiar para baixo, `B2` vira `B3`, `B4`... mas `$E$1` continua sempre E1.

> **Atalho:** enquanto escreve a conta, clique em cima do `E1` e aperte `F4`. O Excel coloca os `$` para você.

## 6.7 Deixando bonito (formatação)

Quase tudo fica na guia **Página Inicial**:

| O que fazer | Onde |
|---|---|
| Negrito, cor da letra, tamanho | Grupo **Fonte** |
| Colocar bordas na tabela | Botão de **Bordas** (grupo Fonte) |
| Mostrar como dinheiro (R$) | Grupo **Número** > Moeda |
| Mostrar como porcentagem | Grupo **Número** > % |
| Mais ou menos casas depois da vírgula | Grupo **Número** > botões ,00 |
| Texto em várias linhas dentro da célula | **Quebrar Texto Automaticamente** |
| Copiar só a aparência de uma célula | **Pincel de Formatação** |
| Todas as opções de uma vez | `Ctrl + 1` |

## 6.8 Linhas, colunas e abas

- **Coluna estreita demais** (aparece `#####`)? Dê dois cliques na linha entre as letras das colunas. Ela se ajusta sozinha.
- **Inserir ou excluir linha/coluna:** botão direito no número da linha (ou na letra da coluna) > Inserir ou Excluir.
- **Nova aba:** clique no `+` ao lado das abas.
- **Mudar o nome da aba:** dois cliques no nome.
- **Deixar o cabeçalho sempre visível ao rolar:** guia **Exibir** > **Congelar Painéis** > Congelar Linha Superior.

## 6.9 Atalhos do Excel (em português)

| Atalho | O que faz |
|---|---|
| `Ctrl + B` | Salvar |
| `Ctrl + N` | Negrito |
| `Ctrl + Z` | Desfazer |
| `Ctrl + C` / `Ctrl + V` | Copiar / colar |
| `Alt + =` | Somar automaticamente |
| `Ctrl + 1` | Formatar células |
| `F2` | Editar a célula |
| `F4` | Colocar o `$` (travar a célula) |
| `Ctrl + ;` | Escrever a data de hoje |
| `Ctrl + setas` | Pular até o fim dos dados |
| `Ctrl + Shift + L` | Ligar/desligar os filtros |
| `Alt + Enter` | Pular linha dentro da mesma célula |

> **Excel em inglês:** salvar é `Ctrl + S` e negrito é `Ctrl + B`.

## 6.10 Salvar e imprimir

- `Ctrl + B` salva. O arquivo do Excel tem a extensão **.xlsx**.
- **Transformar em PDF:** Arquivo > Salvar como > escolha o tipo **PDF**.
- **Antes de imprimir**, aperte `Ctrl + P` para ver como vai ficar. Se a tabela não couber, em **Configurações** escolha **Ajustar todas as colunas em uma página** e a orientação **Paisagem** (folha deitada).

## Resumo do módulo

- Toda conta começa com `=`.
- Use o nome das células (`=A1+B1`) para o resultado se atualizar sozinho.
- Dois cliques no quadradinho copiam a conta para baixo.
- `$` trava a célula (atalho `F4`).
- `Alt + =` soma; `Ctrl + B` salva.
