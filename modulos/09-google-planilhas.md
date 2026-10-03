# 9. Google Planilhas

> **Objetivo:** usar o Google Planilhas (Google Sheets), a alternativa gratuita e online ao Excel, e conhecer suas funções exclusivas.

## 9.1 Por que usar

- **Gratuito:** basta uma conta Google (sheets.google.com).
- **Na nuvem:** salva automaticamente e abre em qualquer computador ou celular.
- **Colaboração em tempo real:** várias pessoas editando juntas, com comentários e histórico.
- **Compatível com Excel:** abre e exporta `.xlsx`.

## 9.2 Diferenças em relação ao Excel

| Item | Excel | Google Planilhas |
|---|---|---|
| Salvar | Manual (`Ctrl + B`/`Ctrl + S`) ou AutoSalvamento no OneDrive | Automático |
| Compartilhar | OneDrive/SharePoint | Botão **Compartilhar** (leitor, comentarista, editor) |
| Histórico | Histórico de Versões | Arquivo > Histórico de versões |
| Automação | VBA / Office Scripts | Apps Script (JavaScript) |
| Funções | A maioria igual | Iguais + funções exclusivas (abaixo) |
| Tabela dinâmica | Inserir > Tabela Dinâmica | Inserir > Tabela dinâmica |
| Limite | 1.048.576 linhas | 10 milhões de células por arquivo |

> As funções têm os **mesmos nomes** em português: `SOMA`, `SE`, `PROCV`, `SOMASES`, `PROCX`, `FILTER`... O separador também é `;` quando a planilha está em português (Arquivo > Configurações > Localidade: Brasil).

## 9.3 Funções exclusivas do Google Planilhas

| Função | O que faz | Exemplo |
|---|---|---|
| `QUERY` | Consulta os dados com linguagem parecida com SQL | `=QUERY(A1:E100;"select A, sum(E) group by A";1)` |
| `IMPORTRANGE` | Traz dados de outra planilha | `=IMPORTRANGE("URL_da_planilha";"Vendas!A1:E100")` |
| `GOOGLETRANSLATE` | Traduz texto | `=GOOGLETRANSLATE(A2;"pt";"en")` |
| `GOOGLEFINANCE` | Cotações de ações e moedas | `=GOOGLEFINANCE("CURRENCY:USDBRL")` |
| `IMAGE` | Insere imagem pela URL | `=IMAGE("https://.../logo.png")` |
| `SPARKLINE` | Minigráfico na célula | `=SPARKLINE(B2:M2)` |
| `ARRAYFORMULA` | Aplica a fórmula à coluna inteira | `=ARRAYFORMULA(B2:B*C2:C)` |
| `IMPORTHTML` | Importa tabela de um site | `=IMPORTHTML("URL";"table";1)` |
| `SPLIT` | Divide texto | `=SPLIT(A2;",")` |
| `REGEXEXTRACT` | Extrai texto por padrão | `=REGEXEXTRACT(A2;"\d+")` (números) |
| `DETECTLANGUAGE` | Detecta o idioma | `=DETECTLANGUAGE(A2)` |

### QUERY na prática

Com os dados de vendas (A = Vendedor, B = Região, C = Produto, D = Data, E = Valor):

```
=QUERY(A1:E100;"select A, sum(E) where B = 'Sul' group by A order by sum(E) desc";1)
```

Resultado: total vendido por vendedor da região Sul, do maior para o menor.

## 9.4 Recursos úteis

- **Filtros e visualizações de filtro:** cada pessoa filtra sem atrapalhar os outros.
- **Validação de dados:** Dados > Validação de dados (listas suspensas, caixas de seleção).
- **Caixa de seleção:** Inserir > Caixa de seleção (ótimo para checklists).
- **Formatação condicional:** Formatar > Formatação condicional.
- **Proteger intervalos:** Dados > Proteger páginas e intervalos.
- **Formulários:** Ferramentas > Criar um formulário (as respostas caem direto na planilha).
- **Explorar / Gemini:** botão no canto inferior direito ou painel lateral sugere gráficos e análises por IA.
- **Atalhos:** `Ctrl + /` mostra todos os atalhos.

## 9.5 Apps Script (automação)

Extensões > **Apps Script**. Exemplo que envia um e-mail com o total de vendas:

```
function enviarResumo() {
  const aba = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Vendas");
  const total = aba.getRange("E2:E").getValues().flat()
                   .filter(Number).reduce((a, b) => a + b, 0);
  MailApp.sendEmail("gestor@empresa.com", "Resumo de vendas",
                    "Total vendido: R$ " + total.toFixed(2));
}
```

Em **Acionadores** (ícone de relógio) você agenda o script para rodar todo dia.

## Resumo do módulo

- Google Planilhas é gratuito, online e colaborativo.
- As funções do Excel funcionam quase todas iguais.
- Exclusivas poderosas: `QUERY`, `IMPORTRANGE`, `GOOGLETRANSLATE`, `ARRAYFORMULA`.
