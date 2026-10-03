# 9. Google Planilhas

> **Objetivo:** usar o Google Planilhas, o "Excel gratuito do Google", que funciona direto no navegador.

## 9.1 Por que usar

- **De graça:** só precisa de uma conta Google (a mesma do Gmail).
- **Salva sozinho:** não existe "esqueci de salvar".
- **Abre em qualquer lugar:** no computador do trabalho, de casa ou no celular.
- **Várias pessoas ao mesmo tempo:** cada um vê o que o outro está digitando.
- **Conversa com o Excel:** abre arquivos `.xlsx` e salva como `.xlsx`.

**Como começar:** entre em **sheets.google.com** ou, no Google Drive, clique em **Novo > Planilhas Google**.

## 9.2 O que muda em relação ao Excel

| Item | Excel | Google Planilhas |
|---|---|---|
| Salvar | Você salva (`Ctrl + B`) | Salva sozinho |
| Onde fica o arquivo | No computador (ou OneDrive) | No Google Drive |
| Compartilhar | Pelo OneDrive | Botão verde **Compartilhar** |
| Funções | `SOMA`, `SE`, `PROCV`... | **As mesmas**, com os mesmos nomes |

> Tudo o que você aprendeu de fórmulas nos módulos 6 e 7 funciona aqui do mesmo jeito.

## 9.3 Compartilhando do jeito certo

Clique em **Compartilhar** (canto de cima, à direita), digite o e-mail da pessoa e escolha o que ela pode fazer:

| Permissão | A pessoa pode... |
|---|---|
| **Leitor** | Só ver |
| **Comentarista** | Ver e deixar comentários |
| **Editor** | Ver e mudar tudo |

> **Cuidado com "Qualquer pessoa com o link":** quem receber o link (mesmo encaminhado) consegue abrir. Não use isso para planilhas com dados de clientes.

## 9.4 Recursos úteis

- **Voltar uma versão antiga:** Arquivo > **Histórico de versões**. Dá para ver quem mudou o quê e desfazer.
- **Caixa de seleção (checklist ✓):** Inserir > **Caixa de seleção**.
- **Lista de opções:** Inserir > **Menu suspenso**.
- **Cores automáticas:** Formatar > **Formatação condicional**.
- **Tabela dinâmica:** Inserir > **Tabela dinâmica** (funciona igual à do Excel).
- **Ver todos os atalhos:** `Ctrl + /`.

## 9.5 Funções que só o Google tem

| Função | O que faz | Exemplo |
|---|---|---|
| `GOOGLETRANSLATE` | Traduz um texto | `=GOOGLETRANSLATE(A2;"pt";"en")` |
| `GOOGLEFINANCE` | Mostra a cotação do dólar e de outras moedas | `=GOOGLEFINANCE("CURRENCY:USDBRL")` |
| `IMAGE` | Mostra uma imagem dentro da célula | `=IMAGE("endereço da imagem")` |

## 9.6 Levando um arquivo do Excel para o Google

1. Abra o **Google Drive** (drive.google.com).
2. Clique em **Novo** > **Upload de arquivo** e escolha o `.xlsx`.
3. Dê dois cliques no arquivo e escolha **Abrir com Planilhas Google**.

E o caminho de volta: no Google Planilhas, **Arquivo > Fazer download > Microsoft Excel (.xlsx)**.

## Resumo do módulo

- Gratuito, salva sozinho e abre em qualquer lugar.
- As fórmulas são as mesmas do Excel.
- Compartilhe escolhendo Leitor, Comentarista ou Editor.
- Errou? **Histórico de versões** volta atrás.
