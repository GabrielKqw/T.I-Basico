# 4. PowerShell e Terminal Linux

> **Objetivo:** conhecer o PowerShell (terminal moderno do Windows) e os comandos básicos do Linux, muito usados em servidores e na nuvem.

## 4.1 PowerShell

O PowerShell é mais poderoso que o CMD: trabalha com **objetos** e permite automações completas. Para abrir: `Win + X` > **Terminal** ou `Win + R` > `powershell`.

Os comandos (chamados *cmdlets*) seguem o padrão **Verbo-Substantivo**: `Get-Process`, `Copy-Item`, `Remove-Item`.

> **Boa notícia:** muitos comandos do CMD e do Linux funcionam no PowerShell como apelidos (`cd`, `dir`, `ls`, `cls`, `copy`, `cp`, `mv`, `rm`, `cat`).

### Comandos essenciais

| Comando PowerShell | Apelido | Função |
|---|---|---|
| `Get-Location` | `pwd` | Pasta atual |
| `Set-Location pasta` | `cd` | Entrar em pasta |
| `Get-ChildItem` | `ls`, `dir` | Listar arquivos |
| `New-Item -ItemType Directory nome` | `mkdir` | Criar pasta |
| `New-Item arquivo.txt` | | Criar arquivo |
| `Copy-Item origem destino` | `cp`, `copy` | Copiar |
| `Move-Item origem destino` | `mv`, `move` | Mover |
| `Rename-Item antigo novo` | `ren` | Renomear |
| `Remove-Item arquivo` | `rm`, `del` | Apagar |
| `Get-Content arquivo.txt` | `cat`, `type` | Ler arquivo |
| `Clear-Host` | `cls`, `clear` | Limpar tela |
| `Get-Help comando` | `help` | Ajuda |
| `Get-Command` | | Lista todos os comandos |

### Sistema e processos

| Comando | Função |
|---|---|
| `Get-Process` | Programas em execução |
| `Stop-Process -Name notepad` | Fecha um programa |
| `Get-Service` | Lista serviços |
| `Restart-Service -Name Spooler` | Reinicia o serviço de impressão (resolve fila travada) |
| `Get-ComputerInfo` | Informações do computador |
| `Test-Connection google.com` | Equivalente ao ping |
| `Get-NetIPAddress` | Endereços IP |
| `Restart-Computer` | Reinicia |
| `Stop-Computer` | Desliga |

### Exemplos práticos

```
# Listar todas as planilhas da pasta Documentos e subpastas
Get-ChildItem $HOME\Documents -Recurse -Filter *.xlsx

# Os 5 programas que mais usam memória
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5

# Renomear em massa: trocar espaços por "_" em todos os arquivos da pasta
Get-ChildItem | Rename-Item -NewName { $_.Name -replace ' ', '_' }

# Exportar a lista de arquivos para abrir no Excel
Get-ChildItem | Select-Object Name, Length, LastWriteTime | Export-Csv arquivos.csv -NoTypeInformation

# Ler um CSV (como uma planilha) e filtrar
Import-Csv vendas.csv | Where-Object { [double]$_.Valor -gt 1000 }
```

> **Liga com o Excel:** `Export-Csv` e `Import-Csv` permitem trocar dados entre o PowerShell e o Excel.

## 4.2 Terminal Linux (Bash)

O Linux domina servidores, nuvem e dispositivos. No Windows você pode praticar com o **WSL** (`wsl --install` no PowerShell como administrador) ou com o **Git Bash**.

### Navegação e arquivos

| Comando | Função | Exemplo |
|---|---|---|
| `pwd` | Pasta atual | `pwd` |
| `ls` | Lista arquivos | `ls -la` (detalhado, com ocultos) |
| `cd` | Entra em pasta | `cd /home/maria` |
| `cd ~` | Vai para a pasta do usuário | `cd ~` |
| `mkdir` | Cria pasta | `mkdir -p projetos/2026` |
| `touch` | Cria arquivo vazio | `touch notas.txt` |
| `cp` | Copia | `cp -r pasta backup/` |
| `mv` | Move/renomeia | `mv a.txt b.txt` |
| `rm` | Apaga | `rm arquivo.txt` / `rm -r pasta` |
| `cat` | Mostra conteúdo | `cat notas.txt` |
| `less` | Lê arquivo grande (q para sair) | `less log.txt` |
| `head` / `tail` | Início / fim do arquivo | `tail -f /var/log/syslog` |
| `nano` | Editor de texto simples | `nano config.txt` |
| `find` | Procura arquivos | `find . -name "*.csv"` |
| `grep` | Procura texto dentro de arquivos | `grep -i "erro" log.txt` |
| `clear` | Limpa a tela | `clear` |
| `man` | Manual do comando | `man ls` |

### Sistema, permissões e pacotes

| Comando | Função |
|---|---|
| `sudo comando` | Executa como administrador (root) |
| `sudo apt update && sudo apt upgrade` | Atualiza o sistema (Ubuntu/Debian) |
| `sudo apt install nome` | Instala um programa |
| `top` / `htop` | Monitor de processos |
| `ps aux` | Lista processos |
| `kill PID` | Encerra um processo |
| `df -h` | Espaço em disco |
| `du -sh pasta` | Tamanho de uma pasta |
| `free -h` | Memória RAM |
| `chmod +x script.sh` | Dá permissão de execução |
| `chown usuario arquivo` | Muda o dono do arquivo |
| `ip a` | Endereços IP |
| `ping -c 4 google.com` | Teste de conexão (4 pacotes) |
| `ssh usuario@servidor` | Acessa servidor remoto |
| `history` | Comandos já digitados |

### Combinando comandos

```
ls -la | grep ".csv"           # o | (pipe) envia a saída de um comando para outro
cat vendas.csv | wc -l         # conta as linhas de uma planilha CSV
echo "texto" > arquivo.txt     # > sobrescreve o arquivo
echo "mais" >> arquivo.txt     # >> adiciona ao final
```

## 4.3 Tabela de equivalência

| Tarefa | CMD | PowerShell | Linux |
|---|---|---|---|
| Listar | `dir` | `Get-ChildItem` / `ls` | `ls` |
| Pasta atual | `cd` | `pwd` | `pwd` |
| Criar pasta | `mkdir` | `mkdir` | `mkdir` |
| Copiar | `copy` | `cp` | `cp` |
| Mover | `move` | `mv` | `mv` |
| Apagar | `del` | `rm` | `rm` |
| Ler arquivo | `type` | `cat` | `cat` |
| Limpar tela | `cls` | `cls` | `clear` |
| Processos | `tasklist` | `Get-Process` | `ps aux` |
| Rede | `ipconfig` | `Get-NetIPAddress` | `ip a` |
| Ajuda | `/?` | `Get-Help` | `man` |

## Resumo do módulo

- PowerShell usa Verbo-Substantivo e aceita apelidos do CMD e do Linux.
- No Linux: `ls`, `cd`, `cp`, `mv`, `rm`, `cat`, `grep`, `sudo apt install`.
- O pipe `|` encadeia comandos; `>` e `>>` gravam em arquivos.
