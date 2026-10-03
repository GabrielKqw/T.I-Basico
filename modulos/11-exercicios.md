# 11. Exercícios e Gabarito

> **Como usar:** tente fazer sozinho antes de olhar as respostas. Os exercícios de Excel usam a planilha [exercicios-excel.xlsx](https://github.com/GabrielKqw/T.I-Basico/raw/main/planilhas/exercicios-excel.xlsx). As respostas estão no final.

## Parte A - Informática e Windows

1. Qual a diferença entre a memória RAM e o SSD?
2. Uma internet de 200 Mbps baixa mais ou menos quantos MB por segundo?
3. Que tipo de arquivo é um `.pdf`? E um `.xlsx`?
4. Qual atalho bloqueia o computador?
5. Qual atalho tira um print de só um pedaço da tela?
6. Como apagar um arquivo sem mandar para a lixeira? Por que tomar cuidado com isso?
7. Um programa travou. Qual atalho abre o Gerenciador de Tarefas para fechá-lo?
8. Qual atalho reabre uma aba do navegador fechada sem querer?

## Parte B - Comandos (CMD e PowerShell)

1. Como abrir o Prompt de Comando?
2. No CMD, crie uma pasta chamada `Curso` e entre nela.
3. Qual comando mostra o nome do computador?
4. Qual comando testa se a internet está chegando até o Google?
5. Um site não abre, mas a internet funciona. Qual comando pode ajudar?
6. Marque o desligamento do computador para daqui a 30 minutos. Como cancelar?
7. No PowerShell, qual comando mostra os programas que estão abertos?

## Parte C - Segurança

1. Cite três sinais de que um e-mail é falso.
2. O que é a verificação em duas etapas e por que ativar?
3. Alguém liga dizendo ser do banco e pede o código que chegou por SMS. O que fazer?

## Parte D - Excel básico (aba **Notas**)

1. Na coluna F, calcule a **média** das 4 notas de cada aluno.
2. Na coluna G, mostre "Aprovado" se a média for 7 ou mais, "Recuperação" se for 5 ou mais e "Reprovado" nos outros casos.
3. Na célula J2, mostre a maior média da turma; em J3, a menor; em J4, a média geral.
4. Na célula J5, conte quantos alunos foram aprovados.
5. Deixe as médias com 1 casa depois da vírgula.
6. Pinte de vermelho as médias abaixo de 5 (Formatação Condicional).

## Parte E - Funções (abas **Vendas**, **Produtos** e **Pedidos**)

1. (Vendas) Calcule o total geral vendido (coluna H).
2. (Vendas) Calcule o total vendido pela vendedora "Ana".
3. (Vendas) Calcule o total vendido na região "Sul" só das vendas acima de R$ 1.000.
4. (Vendas) Conte quantas vendas foram de "Notebook".
5. (Pedidos) Usando o código da coluna B, traga o **nome do produto** (coluna D) e o **preço** (coluna E) da aba Produtos com `PROCV` ou `PROCX`.
6. (Pedidos) Calcule o total do pedido na coluna F (Quantidade x Preço).
7. (Vendas) Crie uma coluna "Comissão": 5% se o Total for maior que R$ 2.000; se não, 2%.
8. (Vendas) Faça a lista de vendedores sem repetir e, ao lado, o total de cada um.

## Parte F - Arrumando textos (aba **Limpeza**)

1. Coluna A: nomes com espaços sobrando e letras bagunçadas. Deixe-os arrumados na coluna D.
2. Pegue só o primeiro nome na coluna E.
3. Coluna B: e-mails. Pegue só o que vem depois do @ na coluna F.
4. Coluna C: CPFs só com números. Deixe no formato `000.000.000-00` na coluna G.

## Parte G - Datas (aba **Datas**)

1. Calcule a idade de cada funcionário na coluna D.
2. Calcule há quantos anos cada um trabalha na empresa na coluna E.
3. Calcule a data do fim da experiência (90 dias depois da admissão) na coluna F.

## Parte H - Recursos avançados (aba **Vendas**)

1. Transforme os dados em uma **Tabela** com o nome `TabVendas`.
2. Crie uma **lista de opções** na coluna Região com Sul, Norte, Sudeste, Nordeste e Centro-Oeste.
3. Crie uma **Tabela Dinâmica** com o total por Vendedor (linhas) e por Região (colunas).
4. Na tabela dinâmica, junte as datas por mês.
5. Crie um **gráfico de colunas** com o total por vendedor.
6. Coloque botões de filtro (**Segmentação de Dados**) por Produto.

## Parte I - ChatGPT

1. Escreva um pedido completo para o ChatGPT pedindo a fórmula do exercício E3.
2. Peça ao ChatGPT que explique a fórmula `=PROCV(B2;Produtos!$A$2:$D$9;2;FALSO)`.
3. Por que é importante dizer "Excel em português" no pedido?
4. Por que você não deve colar a lista de clientes da empresa no ChatGPT?

---

## Gabarito

### Parte A

1. A RAM guarda o que está aberto agora e esvazia quando desliga (é a "mesa"). O SSD guarda os arquivos de vez (é o "armário").
2. 200 ÷ 8 = **25 MB por segundo**.
3. `.pdf` é um documento pronto para ler e imprimir; `.xlsx` é uma planilha do Excel.
4. `Win + L`.
5. `Win + Shift + S`.
6. `Shift + Delete`. Cuidado porque o arquivo não vai para a lixeira e não dá para recuperar.
7. `Ctrl + Shift + Esc`.
8. `Ctrl + Shift + T`.

### Parte B

1. `Win + R`, digitar `cmd` e apertar `Enter`.
2. `mkdir Curso` e depois `cd Curso`.
3. `hostname`.
4. `ping google.com`.
5. `ipconfig /flushdns` (limpa a memória de sites do computador).
6. `shutdown /s /t 1800` (30 minutos = 1800 segundos). Para cancelar: `shutdown /a`.
7. `Get-Process`.

### Parte C

1. Pressa exagerada, endereço de quem enviou esquisito, erros de português, links que levam para outro site, anexos que você não esperava.
2. É um código extra (que chega no celular) pedido além da senha. Mesmo que roubem sua senha, não conseguem entrar.
3. **Não passar o código**, desligar e ligar você mesmo para o número oficial do banco. Banco não pede esse código.

### Parte D

```
F2:  =MÉDIA(B2:E2)
G2:  =SES(F2>=7;"Aprovado";F2>=5;"Recuperação";VERDADEIRO;"Reprovado")
J2:  =MÁXIMO(F2:F16)
J3:  =MÍNIMO(F2:F16)
J4:  =MÉDIA(F2:F16)
J5:  =CONT.SE(G2:G16;"Aprovado")
```

5. Selecione F2:F16 > `Ctrl + 1` > Número > 1 casa decimal.
6. Selecione F2:F16 > Formatação Condicional > Realçar Regras das Células > É Menor do que > `5` > cor vermelha.

### Parte E

```
Ex.1: =SOMA(H2:H41)
Ex.2: =SOMASE(C2:C41;"Ana";H2:H41)
Ex.3: =SOMASES(H2:H41;D2:D41;"Sul";H2:H41;">1000")
Ex.4: =CONT.SE(E2:E41;"Notebook")
Ex.5: D2: =PROCV(B2;Produtos!$A$2:$D$9;2;FALSO)
      E2: =PROCV(B2;Produtos!$A$2:$D$9;4;FALSO)
Ex.6: F2: =C2*E2
Ex.7: I2: =SE(H2>2000;H2*5%;H2*2%)
Ex.8: K2: =ÚNICO(C2:C41)
      L2: =SOMASE($C$2:$C$41;K2;$H$2:$H$41)   (copie para baixo)
```

> No Ex.8, outro jeito (sem fórmula) é criar uma Tabela Dinâmica com Vendedor em Linhas e Total em Valores.

### Parte F

O jeito mais fácil é o **Preenchimento Relâmpago**: digite o primeiro resultado à mão na linha 2 e aperte `Ctrl + E`. O Excel completa o resto.

Com fórmulas:

```
D2:  =PRI.MAIÚSCULA(ARRUMAR(A2))
E2:  =TEXTOANTES(D2;" ")
F2:  =TEXTODEPOIS(B2;"@")
```

### Parte G

```
D2:  =DATADIF(C2;HOJE();"y")
E2:  =DATADIF(B2;HOJE();"y")
F2:  =B2+90
```

### Parte H

1. Clique nos dados > `Ctrl + Alt + T` > OK > Design da Tabela > Nome da Tabela: `TabVendas`.
2. Selecione a coluna Região > Dados > Validação de Dados > Lista > `Sul;Norte;Sudeste;Nordeste;Centro-Oeste`.
3. Inserir > Tabela Dinâmica > arraste Vendedor para Linhas, Região para Colunas e Total para Valores.
4. Arraste Data para Linhas > botão direito em uma data > Agrupar > Meses.
5. Clique na tabela dinâmica > Inserir > Gráfico de Colunas.
6. Análise de Tabela Dinâmica > Inserir Segmentação de Dados > Produto.

### Parte I

1. Exemplo: "Uso Excel em português. Na aba Vendas, a coluna D tem a Região e a coluna H o Total, da linha 2 até a 41. Quero na célula K10 o total vendido na região Sul, só das vendas acima de R$ 1.000. Me dê a fórmula e explique de um jeito simples."
2. A fórmula procura o código que está em B2 na primeira coluna da aba Produtos e traz o que está na 2ª coluna (o nome do produto). O `FALSO` quer dizer que só aceita se achar exatamente igual.
3. Porque, se não disser, ele pode responder com os nomes das funções em inglês, e o Excel em português mostra o erro `#NOME?`.
4. Porque são dados pessoais dos clientes. Pela LGPD, não podem ser enviados para outro serviço sem autorização. Use dados inventados ou só descreva as colunas.
