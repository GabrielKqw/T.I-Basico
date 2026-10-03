# 11. Exercícios e Gabarito

> **Como usar:** faça os exercícios antes de olhar o gabarito. Os exercícios de Excel usam a planilha [exercicios-excel.xlsx](https://github.com/GabrielKqw/T.I-Basico/raw/main/planilhas/exercicios-excel.xlsx). O gabarito está no final.

## Parte A - Informática e Windows

1. Qual a diferença entre memória RAM e SSD?
2. Uma internet de 200 Mbps baixa aproximadamente quantos MB por segundo?
3. Qual extensão indica uma planilha do Excel com macros?
4. Qual atalho bloqueia o computador?
5. Qual atalho captura apenas uma parte da tela?
6. Como excluir um arquivo sem enviá-lo para a lixeira?
7. Qual comando do `Win + R` abre o Gerenciador de Dispositivos?
8. Qual atalho reabre uma aba do navegador fechada sem querer?

## Parte B - Comandos (CMD, PowerShell e Linux)

1. No CMD, crie uma pasta chamada `Curso` e entre nela.
2. No CMD, liste apenas os arquivos `.pdf` da pasta atual.
3. Qual comando mostra o endereço IP do computador?
4. Um site não abre, mas o `ping 8.8.8.8` funciona. Qual o provável problema e qual comando ajuda?
5. Qual comando repara arquivos corrompidos do Windows?
6. Agende o desligamento do computador para daqui a 30 minutos. Como cancelar?
7. No PowerShell, liste todos os arquivos `.xlsx` da pasta Documentos, incluindo subpastas.
8. No Linux, qual comando instala o programa `htop` no Ubuntu?
9. No Linux, como procurar a palavra "erro" dentro do arquivo `log.txt`?

## Parte C - Segurança

1. Cite três sinais de que um e-mail é falso.
2. O que é verificação em duas etapas e por que usar?
3. O que significa a regra de backup 3-2-1?

## Parte D - Excel básico (aba **Notas**)

1. Na coluna F, calcule a **média** das 4 notas de cada aluno.
2. Na coluna G, mostre "Aprovado" se a média for maior ou igual a 7, "Recuperação" se for maior ou igual a 5 e "Reprovado" nos outros casos.
3. Na célula J2, calcule a maior média da turma; em J3, a menor; em J4, a média geral.
4. Na célula J5, conte quantos alunos foram aprovados.
5. Formate as médias com 1 casa decimal.
6. Aplique formatação condicional: médias abaixo de 5 em vermelho.

## Parte E - Funções (abas **Vendas**, **Produtos** e **Pedidos**)

1. (Vendas) Calcule o total geral vendido (coluna H).
2. (Vendas) Calcule o total vendido pelo vendedor "Ana".
3. (Vendas) Calcule o total vendido na região "Sul" com valor acima de R$ 1.000.
4. (Vendas) Conte quantas vendas foram de "Notebook".
5. (Pedidos) Usando o código da coluna B, traga o **nome do produto** (coluna D) e o **preço** (coluna E) da aba Produtos com `PROCV` ou `PROCX`.
6. (Pedidos) Calcule o total do pedido na coluna F (Quantidade x Preço).
7. (Vendas) Crie uma coluna "Comissão": 5% se o Total for maior que R$ 2.000, senão 2%.
8. (Vendas) Liste os vendedores sem repetição usando `ÚNICO` e, ao lado, o total de cada um.

## Parte F - Limpeza de dados (aba **Limpeza**)

1. Coluna A: nomes com espaços extras e letras bagunçadas. Deixe-os padronizados na coluna D.
2. Extraia o primeiro nome na coluna E.
3. Coluna B: e-mails. Extraia o domínio (depois do @) na coluna F.
4. Coluna C: CPFs só com números. Formate como `000.000.000-00` na coluna G.

## Parte G - Datas (aba **Datas**)

1. Calcule a idade de cada funcionário na coluna D.
2. Calcule há quantos anos completos cada um trabalha na empresa na coluna E.
3. Calcule a data do fim do período de experiência (90 dias após a admissão) na coluna F.

## Parte H - Recursos avançados (aba **Vendas**)

1. Transforme os dados em uma **Tabela** chamada `TabVendas`.
2. Crie uma **lista suspensa** para a coluna Região com Sul, Norte, Sudeste, Nordeste, Centro-Oeste.
3. Crie uma **Tabela Dinâmica** com o total por Vendedor (linhas) e Região (colunas).
4. Agrupe as datas da tabela dinâmica por mês.
5. Crie um **gráfico de colunas** com o total por vendedor.
6. Adicione uma **Segmentação de Dados** por Produto.

## Parte I - ChatGPT

1. Escreva um prompt completo (modelo C.E.D.O.F.) pedindo a fórmula do exercício E3.
2. Peça ao ChatGPT que explique a fórmula `=ÍNDICE(Produtos!B:B;CORRESP(B2;Produtos!A:A;0))`.
3. Peça uma macro que formate em negrito e fundo azul o cabeçalho da aba ativa. Teste em uma cópia do arquivo.
4. Por que você não deve colar a base de clientes real da empresa no ChatGPT?

---

## Gabarito

### Parte A

1. RAM é memória temporária e rápida, usada pelos programas abertos (apaga ao desligar); o SSD armazena os arquivos permanentemente.
2. 200 / 8 = **25 MB/s**.
3. `.xlsm`.
4. `Win + L`.
5. `Win + Shift + S`.
6. `Shift + Delete`.
7. `devmgmt.msc`.
8. `Ctrl + Shift + T`.

### Parte B

1. `mkdir Curso` e depois `cd Curso`.
2. `dir *.pdf`.
3. `ipconfig`.
4. Problema de **DNS**. Use `ipconfig /flushdns` (e teste com `nslookup site.com`).
5. `sfc /scannow` (como administrador).
6. `shutdown /s /t 1800`; cancelar com `shutdown /a`.
7. `Get-ChildItem $HOME\Documents -Recurse -Filter *.xlsx`.
8. `sudo apt install htop`.
9. `grep "erro" log.txt` (ou `grep -i` para ignorar maiúsculas).

### Parte C

1. Urgência exagerada, remetente com domínio estranho, erros de português, links que apontam para outro endereço, anexos suspeitos.
2. É uma segunda confirmação além da senha (código no celular/app). Mesmo que roubem a senha, não conseguem entrar.
3. 3 cópias dos dados, em 2 mídias diferentes, sendo 1 fora do local (ex.: nuvem).

### Parte D

```
F2:  =MÉDIA(B2:E2)
G2:  =SES(F2>=7;"Aprovado";F2>=5;"Recuperação";VERDADEIRO;"Reprovado")
     ou =SE(F2>=7;"Aprovado";SE(F2>=5;"Recuperação";"Reprovado"))
J2:  =MÁXIMO(F2:F16)
J3:  =MÍNIMO(F2:F16)
J4:  =MÉDIA(F2:F16)
J5:  =CONT.SE(G2:G16;"Aprovado")
```

5. Selecione F2:F16 > `Ctrl + 1` > Número > 1 casa decimal.
6. Formatação Condicional > Realçar Regras > É Menor do que > 5 > Preenchimento vermelho.

### Parte E

```
Ex.1: =SOMA(Vendas!H2:H41)
Ex.2: =SOMASE(C2:C41;"Ana";H2:H41)
Ex.3: =SOMASES(H2:H41;D2:D41;"Sul";H2:H41;">1000")
Ex.4: =CONT.SE(E2:E41;"Notebook")
Ex.5: D2: =PROCV(B2;Produtos!$A$2:$D$9;2;FALSO)
     E2: =PROCV(B2;Produtos!$A$2:$D$9;4;FALSO)
     ou  =PROCX(B2;Produtos!$A$2:$A$9;Produtos!$B$2:$B$9;"Não encontrado")
Ex.6: F2: =C2*E2
Ex.7: I2: =SE(H2>2000;H2*5%;H2*2%)
Ex.8: K2: =ÚNICO(C2:C41)
     L2: =SOMASE($C$2:$C$41;K2#;$H$2:$H$41)
```

### Parte F

```
D2:  =PRI.MAIÚSCULA(ARRUMAR(A2))
E2:  =ESQUERDA(D2;PROCURAR(" ";D2)-1)     ou =TEXTOANTES(D2;" ")
F2:  =EXT.TEXTO(B2;PROCURAR("@";B2)+1;100) ou =TEXTODEPOIS(B2;"@")
G2:  =TEXTO(C2;"000\.000\.000-00")
```

> Dica: o Preenchimento Relâmpago (`Ctrl + E`) também resolve E e F: digite o primeiro resultado e pressione `Ctrl + E`.

### Parte G

```
D2:  =DATADIF(C2;HOJE();"y")
E2:  =DATADIF(B2;HOJE();"y")
F2:  =B2+90
```

### Parte H

1. Clique nos dados > `Ctrl + Alt + T` (pt-BR) > OK > Design da Tabela > Nome: `TabVendas`.
2. Selecione a coluna Região > Dados > Validação de Dados > Lista > `Sul;Norte;Sudeste;Nordeste;Centro-Oeste`.
3. Inserir > Tabela Dinâmica > Vendedor em Linhas, Região em Colunas, Total em Valores.
4. Arraste Data para Linhas > botão direito em uma data > Agrupar > Meses.
5. Selecione a tabela dinâmica > Analisar > Gráfico Dinâmico > Colunas.
6. Analisar Tabela Dinâmica > Inserir Segmentação de Dados > Produto.

### Parte I

1. Exemplo: "Uso Excel 365 em português, separador ponto e vírgula. Na aba Vendas, D = Região e H = Total, dados de D2 a H41. Quero na célula K10 o total vendido na região Sul apenas das vendas acima de R$ 1.000. Me dê só a fórmula e uma explicação curta."
2. A fórmula procura o código de B2 na coluna A da aba Produtos (`CORRESP` retorna a posição) e `ÍNDICE` devolve o nome do produto que está na mesma posição da coluna B. É uma alternativa ao PROCV.
3. Resposta livre. Confira se a macro usa `Font.Bold = True` e `Interior.Color`.
4. Por causa da **LGPD** e da confidencialidade: os dados pessoais dos clientes seriam enviados a um serviço externo sem autorização. Use dados fictícios ou anonimizados.
