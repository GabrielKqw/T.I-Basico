# 10. ChatGPT para Excel

> **Objetivo:** usar o ChatGPT (e outras IAs como Copilot, Gemini e Claude) como um assistente de Excel: criar fórmulas, entender planilhas prontas, limpar dados, gerar macros e analisar dados.

## 10.1 O que o ChatGPT faz por você no Excel

| Tarefa | Exemplo |
|---|---|
| Criar fórmulas | "Fórmula para somar as vendas da Ana na região Sul" |
| Explicar fórmulas | "O que faz `=ÍNDICE(B:B;CORRESP(MAIOR(C:C;1);C:C;0))`?" |
| Corrigir erros | "Meu PROCV dá #N/D, o que pode ser?" |
| Escrever macros VBA | "Macro que salva cada aba como PDF separado" |
| Montar planilhas | "Crie a estrutura de um controle de estoque" |
| Analisar dados | Enviar um arquivo e pedir gráficos e conclusões |
| Ensinar | "Me explique tabela dinâmica como se eu fosse iniciante" |
| Gerar dados de teste | "Gere 30 linhas fictícias de vendas em formato de tabela" |

## 10.2 Começando

1. Acesse **chatgpt.com** e crie uma conta (há versão gratuita).
2. Digite seu pedido (o *prompt*) na caixa de mensagem.
3. Copie a fórmula da resposta e cole na célula.
4. **Teste sempre** o resultado com poucos dados conhecidos.

## 10.3 A fórmula do prompt perfeito

Um bom pedido tem 5 partes. Use o modelo **C.E.D.O.F.**:

| Parte | O que informar | Exemplo |
|---|---|---|
| **C**ontexto | Versão e idioma do Excel | "Uso Excel 365 em português, separador ;" |
| **E**strutura | Colunas e onde estão os dados | "A = Vendedor, B = Região, E = Valor, dados de A2 a E500" |
| **D**esejo | O que você quer | "Quero o total vendido por região" |
| **O**nde | Onde o resultado vai ficar | "Na célula H2, com a região escrita em G2" |
| **F**ormato | Como quer a resposta | "Só a fórmula e uma explicação curta" |

### Prompt ruim x prompt bom

**Ruim:**

```
faz uma formula de soma com condicao
```

**Bom:**

```
Uso Excel 365 em português (separador ponto e vírgula).
Minha planilha tem: coluna A = Vendedor, B = Região, D = Data, E = Valor,
com dados de A2 até E500.
Quero, na célula H2, o total vendido pela região que está escrita em G2,
somente no mês de setembro de 2026.
Me dê a fórmula e explique cada parte em uma linha.
```

Resposta esperada:

```
=SOMASES(E2:E500;B2:B500;G2;D2:D500;">="&DATA(2026;9;1);D2:D500;"<="&DATA(2026;9;30))
```

> **Importante:** diga sempre que o Excel está em **português**. Se não disser, o ChatGPT costuma responder com nomes em inglês (`SUMIFS`) e vírgula, que darão erro `#NOME?` no Excel pt-BR.

## 10.4 Biblioteca de prompts prontos

Copie, troque o que está entre colchetes e use.

### Fórmulas

```
Excel 365 em português. Tenho [descreva as colunas e o intervalo].
Preciso de uma fórmula para [objetivo] na célula [célula].
Se houver mais de uma forma, mostre a mais simples e a mais moderna.
```

```
Converta esta fórmula do Excel em inglês para o Excel em português,
com ponto e vírgula: [cole a fórmula]
```

```
Crie uma fórmula que classifique o valor da célula E2 em:
"Ouro" se for maior ou igual a 3000, "Prata" se for maior ou igual a 1000
e "Bronze" nos outros casos. Excel em português.
```

### Explicar e corrigir

```
Explique passo a passo, para um iniciante, o que esta fórmula faz:
[cole a fórmula]
```

```
Esta fórmula está retornando [erro, ex.: #VALOR!]:
[cole a fórmula]
Os dados da coluna X são [descreva: ex.: números importados de um sistema].
Quais as causas possíveis e como corrijo?
```

```
Simplifique esta fórmula mantendo o mesmo resultado: [cole a fórmula]
```

### Limpeza de dados

```
Na coluna A tenho nomes completos como "  maria DA silva ".
Quero na coluna B o nome limpo, sem espaços extras e com as iniciais maiúsculas.
Excel em português.
```

```
Na coluna A tenho textos como "Pedido 4587 - Cliente: João - SP".
Quero extrair só o número do pedido na coluna B e a sigla do estado na coluna C.
```

```
Tenho CPFs na coluna A, alguns com pontos e traço e outros sem.
Crie uma fórmula que deixe todos no formato 000.000.000-00.
```

### Estrutura de planilhas

```
Monte a estrutura de uma planilha de [controle de estoque / fluxo de caixa /
controle de horas / orçamento doméstico] para uma [pequena loja].
Liste as abas, as colunas de cada aba, as fórmulas principais (Excel em português),
as validações de dados e as formatações condicionais recomendadas.
```

```
Quero um dashboard de vendas no Excel. Tenho as colunas [liste].
Quais tabelas dinâmicas, gráficos e segmentações devo criar? Passo a passo.
```

### Macros VBA

```
Escreva uma macro VBA comentada em português que [ação, ex.: salve cada aba
desta pasta como um PDF separado na mesma pasta do arquivo, com o nome da aba].
Explique como instalar e executar a macro.
```

```
Explique linha por linha o que esta macro faz e se ela tem algum risco: [cole o código]
```

### Tabela dinâmica e análise

```
Tenho uma base com [colunas]. Quero descobrir [ex.: qual produto mais vende
por região em cada trimestre]. Como monto a tabela dinâmica? Quais campos
vão em Linhas, Colunas, Valores e Filtros?
```

### Aprender

```
Seja meu professor de Excel. Me explique [PROCX] com um exemplo do dia a dia,
depois me passe 3 exercícios de dificuldade crescente e corrija minhas respostas.
```

## 10.5 Analisando planilhas enviadas ao ChatGPT

O ChatGPT permite **anexar arquivos** (.xlsx, .csv) pelo ícone de clipe. Ele lê os dados, faz cálculos com Python e devolve tabelas, gráficos e até um arquivo novo para baixar.

Exemplos de pedidos após anexar:

```
Analise esta planilha de vendas e me diga:
1. Total por mês e por vendedor.
2. Os 5 produtos mais vendidos.
3. Alguma tendência ou anomalia.
Crie um gráfico de linhas com a evolução mensal.
```

```
Limpe esta base: remova duplicados, padronize os nomes das cidades,
corrija as datas para dd/mm/aaaa e me devolva um arquivo .xlsx.
```

```
Compare as duas planilhas anexadas e liste os clientes que estão
na primeira e não estão na segunda.
```

> **Confira os resultados:** peça "mostre como você calculou" e valide alguns números manualmente no Excel.

## 10.6 Fluxo de trabalho recomendado

1. **Descreva** a planilha (colunas, intervalo, versão do Excel em português).
2. **Peça** a fórmula com um objetivo claro.
3. **Teste** em poucas linhas com resultado conhecido.
4. **Itere:** se não funcionar, cole o erro e o que esperava. "Deu #N/D na linha 5, onde o valor é X."
5. **Entenda:** peça a explicação. O objetivo é aprender, não só copiar.

## 10.7 IA dentro das planilhas

| Ferramenta | Onde | O que faz |
|---|---|---|
| **Microsoft Copilot no Excel** | Botão Copilot no Excel 365 (planos com Copilot) | Cria fórmulas, destaca dados, gera gráficos e análises por comando de texto |
| **Função COPILOT** | Excel 365 (em liberação gradual) | `=COPILOT("classifique o sentimento deste comentário";A2)` usa IA dentro da célula |
| **Gemini no Google Planilhas** | Painel lateral do Google Workspace | Cria tabelas, fórmulas e resumos |
| **Analisar Dados** | Excel > Página Inicial > Analisar Dados | Sugere gráficos e tabelas dinâmicas automaticamente (gratuito no 365) |

## 10.8 Cuidados importantes

- **A IA erra.** Fórmulas podem ter referências erradas ou funções que não existem na sua versão. Sempre teste.
- **Privacidade e LGPD:** nunca envie dados pessoais (CPF, telefones, salários, dados de clientes) ou informações confidenciais da empresa. Use dados fictícios ou anonimizados, ou só descreva as colunas.
- **Verifique a política da empresa** sobre uso de IA antes de usar com dados de trabalho.
- **Macros geradas por IA:** leia o código (ou peça para a IA explicar) antes de rodar, e teste em uma cópia do arquivo.
- **Não terceirize o raciocínio:** use a IA para aprender. Em entrevistas e testes práticos, você precisará saber fazer.

## 10.9 Desafio prático

Abra a planilha de exercícios (`planilhas/exercicios-excel.xlsx`), aba **Vendas**, e use o ChatGPT para:

1. Criar uma fórmula que mostre o total vendido por cada vendedor.
2. Criar uma coluna "Comissão": 5% para vendas acima de R$ 2.000 e 2% para as demais.
3. Criar uma formatação condicional que pinte de verde as vendas acima da média.
4. Escrever uma macro que copie a aba Vendas para uma nova pasta de trabalho.
5. Pedir uma explicação de cada resposta e conferir os resultados manualmente.

## Resumo do módulo

- Diga sempre: **Excel em português, separador ;**, colunas e intervalos.
- Use o modelo C.E.D.O.F.: Contexto, Estrutura, Desejo, Onde, Formato.
- Teste, itere e peça explicações.
- Não envie dados pessoais ou confidenciais.
