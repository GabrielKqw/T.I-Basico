# 3. Comandos do Prompt (CMD)

> **Objetivo:** usar o Prompt de Comando do Windows para navegar em pastas, gerenciar arquivos e diagnosticar problemas de rede e sistema, como um técnico de suporte.

## 3.1 Abrindo o Prompt de Comando

- Pressione `Win + R`, digite `cmd` e Enter.
- Ou: menu Iniciar > digite "cmd" > **Executar como administrador** (para comandos que exigem permissão).

A tela mostra algo como:

```
C:\Users\Maria>
```

Isso é o **prompt**: indica a pasta atual. Você digita o comando e pressiona Enter.

> **Dica:** use a tecla `Tab` para completar nomes de pastas e as setas `Cima/Baixo` para repetir comandos anteriores. `Ctrl + C` cancela um comando em execução.

## 3.2 Navegação entre pastas

| Comando | Função | Exemplo |
|---|---|---|
| `cd` | Mostra a pasta atual | `cd` |
| `cd pasta` | Entra em uma pasta | `cd Documentos` |
| `cd ..` | Volta uma pasta | `cd ..` |
| `cd \` | Vai para a raiz do disco | `cd \` |
| `D:` | Troca de unidade | `D:` |
| `dir` | Lista arquivos e pastas | `dir` |
| `dir /a` | Lista inclusive ocultos | `dir /a` |
| `dir *.xlsx` | Lista só planilhas | `dir *.xlsx` |
| `dir /s nome` | Procura em subpastas | `dir /s relatorio.docx` |
| `tree` | Mostra a árvore de pastas | `tree /f` |
| `cls` | Limpa a tela | `cls` |

> Se o nome tiver espaços, use aspas: `cd "Meus Documentos"`.

## 3.3 Arquivos e pastas

| Comando | Função | Exemplo |
|---|---|---|
| `mkdir` ou `md` | Cria pasta | `mkdir Relatorios` |
| `rmdir` ou `rd` | Remove pasta vazia | `rd Antiga` |
| `rd /s /q` | Remove pasta e tudo dentro | `rd /s /q Temp` |
| `copy` | Copia arquivo | `copy nota.txt D:\Backup` |
| `xcopy /e` | Copia pasta inteira | `xcopy Docs D:\Backup\Docs /e /i` |
| `robocopy` | Cópia robusta (backup) | `robocopy C:\Docs D:\Backup /e` |
| `move` | Move ou renomeia | `move nota.txt Arquivo\` |
| `ren` | Renomeia | `ren antigo.txt novo.txt` |
| `del` | Apaga arquivo | `del lixo.txt` |
| `del *.tmp` | Apaga por padrão | `del *.tmp` |
| `type` | Mostra conteúdo de texto | `type leia-me.txt` |
| `echo` | Escreve texto | `echo Olá > arquivo.txt` |
| `echo >>` | Adiciona ao final | `echo linha2 >> arquivo.txt` |
| `start` | Abre arquivo/programa | `start planilha.xlsx` |
| `attrib` | Atributos (oculto, somente leitura) | `attrib -h -s -r E:\*.* /s /d` |

> **Cuidado:** `del` e `rd /s /q` não enviam para a lixeira. Confira antes de apagar.

> **Dica de suporte:** `attrib -h -s -r E:\*.* /s /d` recupera arquivos que um vírus "escondeu" em um pendrive (troque `E:` pela letra do pendrive).

## 3.4 Informações do sistema

| Comando | Função |
|---|---|
| `systeminfo` | Informações completas do computador |
| `hostname` | Nome do computador |
| `whoami` | Usuário logado |
| `ver` | Versão do Windows |
| `tasklist` | Lista os programas em execução |
| `taskkill /im nome.exe /f` | Força o fechamento de um programa |
| `date` / `time` | Data e hora |
| `wmic bios get serialnumber` | Número de série do computador |

## 3.5 Rede (os mais usados no suporte)

| Comando | Função |
|---|---|
| `ipconfig` | Mostra IP, máscara e gateway |
| `ipconfig /all` | Detalhes completos (inclui endereço MAC e DNS) |
| `ipconfig /release` | Libera o IP atual |
| `ipconfig /renew` | Pede um novo IP ao roteador |
| `ipconfig /flushdns` | Limpa o cache de DNS (resolve sites que não abrem) |
| `ping google.com` | Testa se há comunicação com um endereço |
| `ping -t 8.8.8.8` | Ping contínuo (pare com `Ctrl + C`) |
| `tracert google.com` | Mostra o caminho até o destino |
| `nslookup google.com` | Consulta o DNS |
| `netstat -an` | Conexões de rede ativas |
| `getmac` | Endereço físico (MAC) da placa de rede |
| `netsh wlan show profiles` | Redes Wi-Fi salvas |
| `netsh wlan show profile name="MinhaRede" key=clear` | Mostra a senha de uma rede Wi-Fi salva |

### Roteiro de diagnóstico "a internet não funciona"

```
ipconfig              (tem IP? se começar com 169.254, não pegou IP do roteador)
ping 192.168.0.1      (responde o roteador? use o "Gateway padrão" do ipconfig)
ping 8.8.8.8          (chega na internet?)
ping google.com       (o DNS funciona? se o anterior funcionou e este não, é DNS)
ipconfig /flushdns    (limpa o DNS)
ipconfig /release
ipconfig /renew       (renova o IP)
```

## 3.6 Disco e manutenção (executar como administrador)

| Comando | Função |
|---|---|
| `chkdsk C:` | Verifica erros no disco |
| `chkdsk C: /f` | Verifica e corrige (pode pedir reinício) |
| `sfc /scannow` | Verifica e repara arquivos do Windows |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repara a imagem do Windows |
| `cleanmgr` | Limpeza de disco |
| `defrag C: /o` | Otimiza o disco |
| `shutdown /s /t 0` | Desliga agora |
| `shutdown /r /t 0` | Reinicia agora |
| `shutdown /s /t 3600` | Desliga em 1 hora |
| `shutdown /a` | Cancela o desligamento agendado |
| `gpupdate /force` | Atualiza políticas de grupo (empresas) |

## 3.7 Ajuda

Todo comando tem ajuda embutida:

```
comando /?
```

Exemplo: `copy /?` mostra todas as opções do `copy`. O comando `help` lista os comandos disponíveis.

## 3.8 Seu primeiro script (.bat)

Crie no Bloco de Notas um arquivo `backup.bat` com:

```
@echo off
echo Iniciando backup...
robocopy "%USERPROFILE%\Documents" "D:\Backup\Documentos" /e
echo Backup concluido!
pause
```

Dê dois cliques no arquivo e ele copiará seus Documentos para `D:\Backup`. Pronto: você automatizou uma tarefa!

## Resumo do módulo

- Navegação: `cd`, `dir`, `cls`.
- Arquivos: `mkdir`, `copy`, `move`, `ren`, `del`.
- Rede: `ipconfig`, `ping`, `tracert`, `nslookup`.
- Reparos: `sfc /scannow`, `chkdsk`, `DISM`.
- Dúvida? `comando /?`.
