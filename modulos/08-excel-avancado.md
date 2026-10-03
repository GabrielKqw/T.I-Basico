# 8. Excel: Recursos Avançados

> **Objetivo:** organizar e analisar dados como no trabalho de verdade: filtros, cores automáticas, listas de opções, gráficos e tabela dinâmica.

## 8.1 Antes de tudo: organize os dados

Os recursos deste módulo funcionam bem quando a tabela segue estas regras:

- **A primeira linha é o cabeçalho**, com o nome de cada coluna.
- **Uma informação por coluna:** nome em uma, cidade em outra.
- **Uma linha para cada registro:** cada venda em uma linha.
- **Sem linhas em branco** no meio da tabela.
- **Sem células mescladas** (juntadas) no meio dos dados.

## 8.2 Transformar em Tabela

Clique em qualquer lugar dos dados e aperte `Ctrl + Alt + T` (no Excel em inglês, `Ctrl + T`). Confirme com **OK**.

O que você ganha:

- Cores alternadas nas linhas e filtros prontos no cabeçalho.
- **A tabela cresce sozinha:** digitou uma linha nova embaixo, ela já faz parte da tabela, com as fórmulas.
- **Linha de totais:** guia **Design da Tabela** > marque **Linha de Totais**.

> Dê um nome para a tabela em **Design da Tabela > Nome da Tabela** (ex.: `TabVendas`). Fica mais fácil de achar depois.

## 8.3 Ordenar e filtrar

- **Ordenar:** clique na setinha do cabeçalho > **Classificar de A a Z** (ou do maior para o menor).
- **Filtrar:** clique na setinha do cabeçalho e marque só o que quer ver. Ex.: só a região Sul.
- Sem tabela? Ligue as setinhas com `Ctrl + Shift + L`.
- **Para tirar o filtro:** clique na setinha > **Limpar Filtro**. Seus dados não somem, só ficam escondidos enquanto o filtro está ligado.

## 8.4 Ferramentas que economizam tempo

| Ferramenta | Onde fica | Para que serve |
|---|---|---|
| **Remover Duplicatas** | Guia Dados | Apaga linhas repetidas |
| **Texto para Colunas** | Guia Dados | Separa "Nome;Cidade" em duas colunas |
| **Preenchimento Relâmpago** | `Ctrl + E` | Você dá um exemplo e o Excel completa o resto |
| **Localizar e Substituir** | `Ctrl + U` | Troca uma palavra por outra na planilha toda |
| **Colar Especial** | `Ctrl + Alt + V` | Cola só os valores (sem fórmula) ou só a formatação |

## 8.5 Cores automáticas (Formatação Condicional)

Pinta as células sozinho conforme o valor. Ex.: vendas acima de R$ 1.000 em verde.

1. Selecione as células (ex.: a coluna de valores).
2. Guia **Página Inicial** > **Formatação Condicional** > **Realçar Regras das Células** > **É Maior do que...**
3. Digite `1000` e escolha a cor. **OK**.

Outras opções prontas no mesmo menu:

| Opção | O que faz |
|---|---|
| Valores Duplicados | Pinta o que está repetido (ótimo para achar CPF duplicado) |
| Regras de Primeiros/Últimos | Pinta os 10 maiores, ou os que estão abaixo da média |
| Barras de Dados | Coloca uma barrinha dentro da célula, do tamanho do valor |
| Escalas de Cor | Vai do vermelho (menor) ao verde (maior) |

Para apagar: **Formatação Condicional** > **Limpar Regras**.

## 8.6 Lista de opções (Validação de Dados)

Cria uma setinha na célula para a pessoa **escolher** em vez de digitar. Evita erros como "sul", "Sul" e "SUL" misturados.

1. Selecione as células.
2. Guia **Dados** > **Validação de Dados**.
3. Em **Permitir**, escolha **Lista**.
4. Em **Fonte**, digite as opções separadas por ponto e vírgula: `Sul;Norte;Sudeste;Nordeste;Centro-Oeste`
5. **OK**.

## 8.7 Gráficos

Selecione os dados (com o cabeçalho) > guia **Inserir** > escolha o gráfico. Ou aperte `Alt + F1` para um gráfico rápido.

| Gráfico | Use para |
|---|---|
| Colunas ou Barras | Comparar coisas (vendas de cada vendedor) |
| Linhas | Ver a evolução ao longo do tempo (vendas mês a mês) |
| Pizza | Mostrar partes de um total (use com poucas fatias, até 5) |

> **Gráfico bom é simples:** coloque um título claro, mostre os valores em cima das barras e evite efeitos 3D.

## 8.8 Tabela Dinâmica: o resumo automático

É **o recurso mais valorizado** em vagas de escritório. Ela transforma milhares de linhas em um resumo, **sem você escrever nenhuma fórmula**. Exemplo: o total vendido por cada vendedor em cada região.

1. Clique em qualquer célula dos dados.
2. Guia **Inserir** > **Tabela Dinâmica** > **OK**.
3. À direita aparece a lista com os nomes das colunas. **Arraste** cada um para uma caixinha:

| Caixinha | O que colocar | Exemplo |
|---|---|---|
| **Linhas** | O que vai aparecer de cima para baixo | Vendedor |
| **Colunas** | O que vai aparecer da esquerda para a direita | Região |
| **Valores** | O número que você quer somar | Valor |
| **Filtros** | Um filtro para o resumo todo | Ano |

Pronto: o Excel monta a tabela de resumo.

**Coisas importantes:**

- **Mudou os dados?** Clique com o botão direito na tabela dinâmica > **Atualizar**. Ela não se atualiza sozinha!
- **Quer contar em vez de somar?** Clique na setinha do campo em Valores > **Configurações do Campo de Valor** > **Contagem**.
- **Juntar datas por mês:** botão direito em uma data da tabela dinâmica > **Agrupar** > **Meses**.
- **Dois cliques** em um número mostram as linhas que formaram aquele total.
- **Botões de filtro bonitos:** guia **Análise de Tabela Dinâmica** > **Inserir Segmentação de Dados**.

## 8.9 Proteger e compartilhar

- **Impedir que mexam na planilha:** guia **Revisão** > **Proteger Planilha**.
- **Colocar senha para abrir o arquivo:** Arquivo > Informações > Proteger Pasta de Trabalho > **Criptografar com Senha**. Não esqueça a senha: não tem como recuperar!
- **Comentário em uma célula:** botão direito > **Novo Comentário**.
- **Trabalhar junto com outras pessoas:** salve o arquivo no OneDrive e clique em **Compartilhar**.

## Resumo do módulo

- Dados organizados: cabeçalho na 1ª linha, sem linhas em branco.
- `Ctrl + Alt + T` transforma em Tabela.
- Formatação Condicional pinta sozinha; Validação cria lista de opções.
- **Tabela Dinâmica** resume tudo sem fórmulas. Lembre de **Atualizar**.
