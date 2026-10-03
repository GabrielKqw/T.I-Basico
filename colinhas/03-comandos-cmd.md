# Comandos do Prompt (CMD)

**Abrir:** `Win + R` > digite `cmd` > `Enter`

## Andar pelas pastas

| | |
|---|---|
| `dir` | Mostra o que tem na pasta |
| `cd Pasta` | Entra na pasta |
| `cd ..` | Volta uma pasta |
| `cd "Meus Arquivos"` | Nome com espaço: use aspas |
| `cls` | Limpa a tela |

## Arquivos e pastas

| | |
|---|---|
| `mkdir Nome` | Cria pasta |
| `copy a.txt D:\` | Copia arquivo |
| `ren velho.txt novo.txt` | Muda o nome |
| `start arquivo.xlsx` | Abre o arquivo |
| `del arquivo.txt` | **Apaga sem lixeira!** |

## Informações do PC

| | |
|---|---|
| `hostname` | Nome do computador |
| `whoami` | Usuário logado |
| `systeminfo` | Tudo sobre o PC |
| `tasklist` | Programas abertos |

## Internet

| | |
|---|---|
| `ping google.com` | Testa a internet |
| `ipconfig` | Endereço do PC na rede |
| `ipconfig /flushdns` | Resolve site que não abre |

> **"Resposta de..."** = internet OK. **"Esgotado o tempo"** = sem internet.

## Internet caiu? Nesta ordem

1. `ping google.com`
2. `ipconfig /flushdns`
3. Desligue o roteador da tomada, espere 30 s, ligue
4. Chame o suporte e conte o que já testou

## Desligar

| | |
|---|---|
| `shutdown /s /t 0` | Desliga agora |
| `shutdown /r /t 0` | Reinicia agora |
| `shutdown /s /t 3600` | Desliga em 1 hora |
| `shutdown /a` | Cancela |

## Consertar o Windows

`sfc /scannow` (abra o CMD como **administrador**)

## Dicas

| | |
|---|---|
| Seta para cima | Repete o último comando |
| `Tab` | Completa o nome |
| `Esc` | Apaga a linha |
| `Ctrl + C` | Para o comando |
| `comando /?` | Ajuda do comando |
