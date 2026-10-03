# 4. PowerShell

> **Objetivo:** conhecer o PowerShell, a versão mais moderna da "tela preta" do Windows, e fazer tarefas úteis com poucos comandos.

## 4.1 O que é o PowerShell

É parecido com o Prompt de Comando (Módulo 3), só que mais novo e mais poderoso. A boa notícia: **os comandos que você já aprendeu funcionam aqui também** (`dir`, `cd`, `cls`, `copy`, `mkdir`).

**Como abrir:** clique com o botão direito no menu Iniciar e escolha **Terminal**. Ou aperte `Win + R`, digite `powershell` e `Enter`.

## 4.2 Como os comandos são escritos

Os comandos do PowerShell são em inglês e têm duas partes: **ação-coisa**.

- `Get-Process` = **pegar** os **processos** (programas abertos)
- `Get-Date` = **pegar** a **data**
- `Stop-Process` = **parar** um **processo** (fechar um programa)

> **Dica:** digite as primeiras letras e aperte `Tab`. O PowerShell completa o nome para você.

## 4.3 Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `dir` | Mostra o que tem na pasta |
| `cd Documents` | Entra na pasta Documentos |
| `cd ..` | Volta uma pasta |
| `cls` | Limpa a tela |
| `Get-Date` | Mostra a data e a hora |
| `Get-Process` | Mostra os programas abertos |
| `Stop-Process -Name notepad` | Fecha o Bloco de Notas (troque pelo nome do programa) |
| `Test-Connection google.com` | Testa a internet (igual ao `ping`) |
| `Restart-Computer` | Reinicia o computador |

## 4.4 Tarefas úteis prontas para copiar

Copie a linha, cole no PowerShell (botão direito do mouse cola) e aperte `Enter`.

**Achar todas as suas planilhas, mesmo dentro de outras pastas:**

```
dir $HOME\Documents -Recurse -Filter *.xlsx
```

**Ver quais programas estão usando mais memória (deixando o computador lento):**

```
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5
```

**Destravar a impressora quando a fila de impressão emperra** (abra o PowerShell como administrador):

```
Restart-Service -Name Spooler
```

**Fazer uma lista dos arquivos da pasta para abrir no Excel:**

```
dir | Select-Object Name, Length, LastWriteTime | Export-Csv lista.csv -NoTypeInformation
```

> Depois é só abrir o arquivo `lista.csv` no Excel.

## 4.5 CMD ou PowerShell?

| Tarefa | CMD | PowerShell |
|---|---|---|
| Ver o que tem na pasta | `dir` | `dir` |
| Entrar em pasta | `cd` | `cd` |
| Limpar a tela | `cls` | `cls` |
| Programas abertos | `tasklist` | `Get-Process` |
| Testar a internet | `ping google.com` | `Test-Connection google.com` |

Para o dia a dia, **os dois servem**. Use o que achar mais fácil.

## Resumo do módulo

- Abrir: botão direito no Iniciar > **Terminal**.
- Os comandos do CMD funcionam aqui.
- Comandos novos têm o formato **ação-coisa**: `Get-Process`, `Get-Date`.
- `Tab` completa o que você está digitando.
