# PowerShell

**Abrir:** botão direito no Iniciar > **Terminal** (ou `Win + R` > `powershell`)

> Os comandos do CMD (`dir`, `cd`, `cls`, `copy`, `mkdir`) **funcionam aqui também**.

## Como se lê

Formato **ação-coisa**, em inglês:

| | |
|---|---|
| `Get` | Pegar / mostrar |
| `Stop` | Parar / fechar |
| `Restart` | Reiniciar |
| `Test` | Testar |

## Comandos do dia a dia

| | |
|---|---|
| `dir` | O que tem na pasta |
| `cd Documents` | Entra em Documentos |
| `cd ..` | Volta uma pasta |
| `cls` | Limpa a tela |
| `Get-Date` | Data e hora |
| `Get-Process` | Programas abertos |
| `Stop-Process -Name notepad` | Fecha um programa |
| `Test-Connection google.com` | Testa a internet |
| `Restart-Computer` | Reinicia o PC |

## Prontos para copiar

**Achar todas as planilhas:**

```
dir $HOME\Documents -Recurse -Filter *.xlsx
```

**O que está deixando o PC lento:**

```
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5
```

**Destravar a impressora** (como administrador):

```
Restart-Service -Name Spooler
```

**Lista de arquivos para abrir no Excel:**

```
dir | Select-Object Name, Length | Export-Csv lista.csv
```

## CMD x PowerShell

| | |
|---|---|
| `tasklist` | `Get-Process` |
| `ping` | `Test-Connection` |
| `dir`, `cd`, `cls` | Iguais nos dois |

## Dicas

| | |
|---|---|
| `Tab` | Completa o nome |
| Seta para cima | Último comando |
| Botão direito | Cola o que copiou |
| `Get-Help comando` | Ajuda |
