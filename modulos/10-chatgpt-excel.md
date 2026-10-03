# 10. ChatGPT para Excel

> **Objetivo:** usar o ChatGPT como um "professor particular" de Excel: ele cria fórmulas, explica o que você não entendeu e ajuda a resolver erros.

## 10.1 O que é o ChatGPT

É uma **inteligência artificial** com quem você conversa por escrito, como numa conversa de WhatsApp. Você pede algo e ele responde. Existem outras parecidas (Gemini, do Google; Copilot, da Microsoft; Claude), e as dicas deste módulo servem para todas.

**Como começar:** entre em **chatgpt.com** e crie uma conta (tem versão gratuita). Escreva seu pedido na caixa de mensagem e aperte `Enter`.

## 10.2 O que ele faz por você

| Você pede | Exemplo de pedido |
|---|---|
| Uma fórmula | "Fórmula para somar as vendas da Ana" |
| Explicação | "O que essa fórmula faz? `=PROCV(B2;H:I;2;FALSO)`" |
| Ajuda com erro | "Meu PROCV está dando #N/D, o que pode ser?" |
| Montar uma planilha | "Que colunas devo ter numa planilha de controle de gastos?" |
| Aprender | "Me explique tabela dinâmica como se eu nunca tivesse usado Excel" |

## 10.3 Como pedir do jeito certo

Quanto **mais detalhes** você der, melhor a resposta. Sempre conte:

1. **Qual Excel:** "Uso Excel em português."
2. **Como está a planilha:** o que tem em cada coluna e até que linha vão os dados.
3. **O que você quer:** o resultado que espera.
4. **Onde:** em qual célula a fórmula vai ficar.

### Pedido ruim x pedido bom

**Ruim:**

```
faz uma formula de soma
```

**Bom:**

```
Uso Excel em português.
Na coluna A tenho o nome do vendedor e na coluna E o valor da venda,
da linha 2 até a linha 500.
Quero, na célula H2, o total vendido pelo vendedor que eu escrever em G2.
Me dê a fórmula e explique de um jeito simples.
```

Resposta que ele vai dar:

```
=SOMASE(A2:A500;G2;E2:E500)
```

> **Sempre diga "Excel em português".** Se não disser, ele pode responder com o nome da função em inglês (`SUMIF` em vez de `SOMASE`), e aí o seu Excel mostra o erro `#NOME?`.

## 10.4 Pedidos prontos para copiar

Troque o que está entre colchetes `[ ]` pelo seu caso.

**Criar uma fórmula:**

```
Uso Excel em português. Na minha planilha, [coluna A tem X, coluna B tem Y],
da linha 2 até a [500]. Quero [o que você quer] na célula [H2].
Me dê a fórmula e explique de um jeito simples.
```

**Entender uma fórmula:**

```
Explique, para quem está começando, o que esta fórmula faz: [cole a fórmula]
```

**Resolver um erro:**

```
Esta fórmula está dando o erro [#N/D]: [cole a fórmula]
O que pode ser e como eu arrumo? Uso Excel em português.
```

**Arrumar nomes bagunçados:**

```
Na coluna A tenho nomes como "  maria DA silva ". Quero na coluna B o nome
sem espaços sobrando e com as iniciais maiúsculas. Uso Excel em português.
```

**Montar uma planilha do zero:**

```
Quero montar uma planilha de [controle de gastos da casa / estoque de uma loja].
Quais colunas devo criar e quais fórmulas usar? Uso Excel em português.
Explique passo a passo, para iniciante.
```

**Estudar:**

```
Seja meu professor de Excel. Me explique [PROCV] com um exemplo do dia a dia,
depois me passe 3 exercícios fáceis e corrija minhas respostas.
```

## 10.5 O jeito certo de trabalhar com a IA

1. **Explique** sua planilha com detalhes.
2. **Copie** a fórmula da resposta e cole na célula.
3. **Confira** se o resultado está certo em uma ou duas linhas que você consegue calcular de cabeça.
4. **Não funcionou?** Conte para ele o que aconteceu: "Deu #N/D na linha 5". Ele corrige.
5. **Peça para explicar.** O objetivo é aprender, não só copiar.

## 10.6 Cuidados importantes

- **A IA erra.** Às vezes com muita confiança. Sempre confira o resultado.
- **Nunca envie dados pessoais** (CPF, telefone, endereço, salário) ou informações sigilosas da empresa. É proibido pela LGPD. Em vez de mandar a planilha, **descreva** as colunas, ou use dados inventados.
- **Pergunte se a empresa permite** usar IA no trabalho.
- **Não dependa só dela:** em testes de emprego você vai precisar saber fazer sozinho.

## 10.7 Desafio prático

Abra a planilha de exercícios (aba **Vendas**) e peça ao ChatGPT:

1. Uma fórmula que mostre o total vendido por um vendedor.
2. Uma coluna "Comissão": 5% para vendas acima de R$ 2.000 e 2% para as outras.
3. Como pintar de verde as vendas acima da média.
4. Uma explicação de cada resposta. Depois, confira os resultados você mesmo.

## Resumo do módulo

- Diga sempre: **Excel em português**, o que tem em cada coluna e onde quer o resultado.
- Teste a fórmula e peça explicação.
- Nunca envie dados pessoais ou sigilosos.
