# 8. Excel: Recursos Avançados

> **Objetivo:** organizar e analisar dados como um profissional: tabelas, filtros, formatação condicional, validação, gráficos, tabela dinâmica, Power Query e macros.

## 8.1 Regras de uma base de dados bem feita

Antes de qualquer recurso avançado, organize os dados assim:

- **Uma linha de cabeçalho** com nomes únicos (sem células mescladas).
- **Uma informação por coluna** (Nome em uma coluna, Sobrenome em outra).
- **Um registro por linha** (cada venda em uma linha).
- **Sem linhas ou colunas em branco** no meio dos dados.
- **Sem totais no meio** da base: calcule em outra área ou use tabela dinâmica.

## 8.2 Tabelas (Formatar como Tabela)

Selecione os dados e pressione `Ctrl + Alt + T` (pt-BR) ou `Ctrl + T` (inglês).

Vantagens:

- Filtros automáticos e linhas zebradas.
- **Crescem sozinhas:** fórmulas, gráficos e tabelas dinâmicas acompanham os novos dados.
- **Colunas calculadas:** digite a fórmula em uma linha e ela é aplicada à coluna inteira.
- **Linha de totais:** Design da Tabela > Linha de Totais.
- **Referências estruturadas:** em vez de `E2:E100`, use o nome da coluna.

```
=SOMA(TabVendas[Valor])
=[@Valor]*0,1          (o @ significa "nesta linha")
```

> Renomeie a tabela em **Design da Tabela > Nome da Tabela** (ex.: `TabVendas`).

## 8.3 Classificar e filtrar

- **Classificar:** Dados > Classificar (permite vários níveis: Região, depois Valor decrescente).
- **Filtro:** `Ctrl + Shift + L`. Clique na setinha do cabeçalho para filtrar por texto, número, data ou cor.
- **Filtros de número:** Maior que, Entre, 10 Primeiros, Acima da Média.
- **Filtro avançado:** Dados > Avançado (critérios complexos e copiar resultado para outro local).
- **Segmentação de dados:** em tabelas e tabelas dinâmicas, botões visuais para filtrar (Inserir > Segmentação de Dados).

## 8.4 Ferramentas de dados

| Ferramenta | Onde | Para que serve |
|---|---|---|
| **Remover Duplicatas** | Dados > Remover Duplicatas | Apaga linhas repetidas |
| **Texto para Colunas** | Dados > Texto para Colunas | Divide "Nome;Cidade" em colunas separadas |
| **Preenchimento Relâmpago** | `Ctrl + E` | Digite 1 ou 2 exemplos e o Excel completa o padrão (ex.: extrair primeiro nome) |
| **Localizar e Substituir** | `Ctrl + U` (pt) / `Ctrl + H` (en) | Troca textos em massa |
| **Ir para Especial** | `F5` > Especial | Seleciona só vazias, fórmulas, constantes... |
| **Colar Especial** | `Ctrl + Alt + V` | Cola só valores, formatos, transpõe, soma |
| **Atingir Meta** | Dados > Teste de Hipóteses | Descobre o valor de entrada para chegar a um resultado |
| **Consolidar** | Dados > Consolidar | Junta dados de várias abas |
| **Subtotal** | Dados > Subtotal | Totais por grupo (dados classificados) |
| **Agrupar** | Dados > Agrupar | Recolhe/expande linhas e colunas |

> **Truque: preencher células vazias com o valor de cima.** Selecione a coluna > `F5` > Especial > Em branco > digite `=` e a seta para cima > `Ctrl + Enter`.

## 8.5 Formatação condicional

Página Inicial > **Formatação Condicional**. Destaca células automaticamente.

| Tipo | Exemplo de uso |
|---|---|
| Realçar regras das células | Valores maiores que 1000 em verde |
| Regras de primeiros/últimos | Os 10 maiores, abaixo da média |
| Barras de dados | Barras dentro da célula, proporcionais ao valor |
| Escalas de cor | Mapa de calor (vermelho a verde) |
| Conjuntos de ícones | Setas, semáforos |
| Valores duplicados | Destacar CPFs repetidos |
| **Usar fórmula** | Pintar a linha inteira com base em uma coluna |

### Pintar a linha inteira quando o status for "Atrasado"

1. Selecione `A2:F100`.
2. Formatação Condicional > Nova Regra > **Usar uma fórmula**.
3. Fórmula: `=$F2="Atrasado"` (coluna fixa com `$`, linha livre).
4. Escolha o formato (preenchimento vermelho claro).

Outras fórmulas úteis:

```
=$D2<HOJE()                     (data vencida)
=E2>MÉDIA($E$2:$E$100)          (acima da média)
=MOD(LIN();2)=0                 (linhas zebradas)
=CONT.SE($A$2:$A$100;$A2)>1     (duplicados)
```

Gerencie em Formatação Condicional > **Gerenciar Regras**.

## 8.6 Validação de dados

Dados > **Validação de Dados**. Controla o que pode ser digitado.

| Permitir | Exemplo |
|---|---|
| Lista | Lista suspensa: `Sul;Norte;Sudeste` ou um intervalo `=$H$2:$H$10` |
| Número inteiro | Quantidade entre 1 e 100 |
| Decimal | Valor maior que 0 |
| Data | Datas a partir de hoje: `>= =HOJE()` |
| Comprimento do texto | CPF com exatamente 11 caracteres |
| Personalizado | `=CONT.SE($A:$A;A2)=1` (impede duplicados) |

Use as abas **Mensagem de Entrada** (dica ao selecionar) e **Alerta de Erro** (mensagem ao digitar errado).

> **Lista dependente:** a lista de "Cidade" muda conforme o "Estado". Crie nomes para cada lista (ex.: intervalo `SP` com as cidades de SP) e use `=INDIRETO(A2)` na validação da coluna Cidade.

## 8.7 Gráficos

Selecione os dados > Inserir > Gráficos (ou `Alt + F1` para gráfico rápido).

| Gráfico | Quando usar |
|---|---|
| Colunas / Barras | Comparar categorias (vendas por vendedor) |
| Linhas | Evolução no tempo (vendas por mês) |
| Pizza / Rosca | Partes de um todo (poucas categorias, até 5) |
| Dispersão | Relação entre duas variáveis |
| Combinado | Duas medidas com escalas diferentes (valor e %) |
| Cascata | Entradas e saídas (fluxo de caixa) |
| Mapa | Valores por estado/país |
| Minigráficos (Sparklines) | Mini gráfico dentro da célula (Inserir > Minigráficos) |

Boas práticas: título claro, rótulos de dados, remover enfeites desnecessários (3D, sombras) e ordenar as barras do maior para o menor.

## 8.8 Tabela Dinâmica (o recurso mais valorizado do mercado)

Resume milhares de linhas em segundos, **sem fórmulas**.

1. Clique em qualquer célula dos dados.
2. **Inserir > Tabela Dinâmica** > Nova Planilha > OK.
3. Arraste os campos para as áreas:

| Área | Função | Exemplo |
|---|---|---|
| **Linhas** | Categorias na vertical | Vendedor |
| **Colunas** | Categorias na horizontal | Região |
| **Valores** | O que calcular | Soma de Valor |
| **Filtros** | Filtro geral do relatório | Ano |

Recursos importantes:

- **Configurações do Campo de Valor:** trocar Soma por Contagem, Média, Máximo, ou **Mostrar Valores Como** % do total.
- **Agrupar datas:** botão direito em uma data > Agrupar > Meses, Trimestres, Anos.
- **Atualizar:** quando os dados mudam, botão direito > Atualizar (ou `Alt + F5`). Use dados em formato de Tabela para incluir novas linhas automaticamente.
- **Segmentação de Dados e Linha do Tempo:** filtros visuais clicáveis.
- **Gráfico Dinâmico:** Analisar Tabela Dinâmica > Gráfico Dinâmico.
- **Duplo clique** em um valor mostra as linhas que o compõem.
- **Campo calculado:** Analisar > Campos, Itens e Conjuntos.

> **Dashboard em 10 minutos:** crie 3 tabelas dinâmicas + 3 gráficos dinâmicos em uma aba, adicione uma Segmentação de Dados e conecte-a a todas (botão direito > Conexões de Relatório).

## 8.9 Power Query (limpeza e automação de dados)

**Dados > Obter Dados**. Importa e trata dados de Excel, CSV, pastas, bancos de dados e web, gravando cada passo para repetir automaticamente.

O que dá para fazer sem fórmulas:

- Remover colunas, linhas em branco e duplicadas.
- Dividir colunas, trocar tipos (texto, número, data), substituir valores.
- **Combinar todos os arquivos de uma pasta** (ex.: 12 planilhas mensais em uma só).
- **Mesclar consultas** (como um PROCV entre tabelas).
- **Transformar colunas em linhas** (Despivotar).

Depois de configurar, basta clicar em **Atualizar Tudo** quando chegarem novos dados.

## 8.10 Proteção e colaboração

- **Proteger planilha:** Revisão > Proteger Planilha (antes, desbloqueie as células editáveis: `Ctrl + 1` > Proteção > desmarcar Bloqueada).
- **Proteger pasta de trabalho:** impede inserir/excluir abas.
- **Senha para abrir:** Arquivo > Informações > Proteger Pasta de Trabalho > Criptografar com Senha.
- **Comentários e anotações:** botão direito > Novo Comentário (`Ctrl + Shift + F2` para anotação).
- **Coautoria:** salve no OneDrive/SharePoint e compartilhe; várias pessoas editam ao mesmo tempo.
- **Histórico de versões:** Arquivo > Informações > Histórico de Versões.

## 8.11 Nomes, LET e LAMBDA

- **Gerenciador de Nomes:** `Ctrl + F3`.
- `LET` deixa fórmulas longas legíveis:

```
=LET(vendas;SOMA(E2:E6); meta;10000; SE(vendas>=meta;"Bateu";"Faltam "&meta-vendas))
```

- `LAMBDA` cria funções próprias. Em Fórmulas > Definir Nome, crie `COMISSAO` com:

```
=LAMBDA(valor; SE(valor>=3000; valor*5%; valor*2%))
```

Depois use em qualquer célula: `=COMISSAO(E2)`.

## 8.12 Macros e VBA (introdução)

Macros automatizam tarefas repetitivas.

1. Habilite a guia **Desenvolvedor**: Arquivo > Opções > Personalizar Faixa de Opções > marque Desenvolvedor.
2. **Gravar Macro:** Desenvolvedor > Gravar Macro, faça as ações, Parar Gravação.
3. Veja o código: `Alt + F11` (editor VBA).
4. Salve como **.xlsm** (pasta habilitada para macro).

Exemplo de macro que formata o cabeçalho:

```
Sub FormatarCabecalho()
    With Range("A1").CurrentRegion.Rows(1)
        .Font.Bold = True
        .Interior.Color = RGB(31, 78, 121)
        .Font.Color = RGB(255, 255, 255)
    End With
    Columns.AutoFit
End Sub
```

> **Segurança:** só habilite macros de arquivos de origem confiável. Macros em anexos de e-mail são uma forma comum de vírus.

> **Alternativa moderna:** o **Office Scripts** (guia Automatizar, Excel para web) usa TypeScript e funciona na nuvem.

## Resumo do módulo

- Organize os dados em formato de banco de dados e transforme em **Tabela**.
- Formatação condicional com fórmula usa `$` na coluna: `=$F2="Atrasado"`.
- Validação cria listas suspensas e impede erros de digitação.
- **Tabela Dinâmica** resume dados sem fórmulas; Power Query automatiza a limpeza.
