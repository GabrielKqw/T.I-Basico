# 3. Comandos do Prompt (CMD)

> **Objetivo:** conhecer a "tela preta" do Windows e alguns comandos simples que ajudam a resolver problemas de internet e do computador.

## 3.1 O que é o Prompt de Comando

É uma janela onde, em vez de clicar, você **digita ordens** para o computador. Parece coisa de hacker, mas é só um outro jeito de usar o Windows. O pessoal de suporte usa muito, porque alguns problemas se resolvem mais rápido assim.

**Como abrir:** aperte `Win + R`, digite `cmd` e aperte `Enter`.

Vai aparecer algo assim:

```
C:\Users\Maria>
```

Isso mostra **em qual pasta você está**. Você digita o comando depois do `>` e aperta `Enter`.

> **Fique tranquilo:** os comandos deste módulo só **mostram informações** ou fazem coisas simples. Você não vai estragar nada. Os únicos que apagam coisas estão marcados com aviso.

### Dicas para não se perder

- Errou? Aperte `Esc` para apagar a linha.
- A seta para cima `↑` repete o último comando digitado.
- `cls` limpa a tela.
- `Ctrl + C` para um comando que não acaba nunca.

## 3.2 Andando pelas pastas

| Comando | O que faz | Exemplo |
|---|---|---|
| `dir` | Mostra o que tem na pasta | `dir` |
| `cd nome` | Entra em uma pasta | `cd Documents` |
| `cd ..` | Volta para a pasta anterior | `cd ..` |
| `cls` | Limpa a tela | `cls` |

> Se o nome da pasta tiver espaço, coloque entre aspas: `cd "Meus Arquivos"`.

## 3.3 Criando e organizando

| Comando | O que faz | Exemplo |
|---|---|---|
| `mkdir nome` | Cria uma pasta | `mkdir Relatorios` |
| `copy` | Copia um arquivo | `copy nota.txt D:\` |
| `ren` | Muda o nome de um arquivo | `ren antigo.txt novo.txt` |
| `del` | **Apaga** um arquivo (não vai para a lixeira!) | `del lixo.txt` |
| `start` | Abre um arquivo ou programa | `start planilha.xlsx` |

## 3.4 Informações do computador

| Comando | O que mostra |
|---|---|
| `hostname` | O nome do computador |
| `whoami` | Qual usuário está usando o computador |
| `systeminfo` | Tudo sobre o computador (memória, Windows, data de instalação) |
| `tasklist` | Os programas que estão abertos agora |

> **Útil no trabalho:** quando o suporte pergunta "qual o nome do seu computador?", é só digitar `hostname`.

## 3.5 A internet não funciona? Use estes

| Comando | O que faz |
|---|---|
| `ipconfig` | Mostra o "endereço" do seu computador na rede |
| `ping google.com` | Testa se a internet chega até o Google |
| `ipconfig /flushdns` | Limpa a memória de sites (resolve site que não abre) |

### Passo a passo quando a internet cai

1. Digite `ping google.com` e aperte `Enter`.
   - Se aparecer **"Resposta de..."** quatro vezes: a internet está funcionando. O problema é no site ou no navegador.
   - Se aparecer **"Esgotado o tempo"** ou **"não encontrou o host"**: siga para o passo 2.
2. Digite `ipconfig /flushdns` e tente abrir o site de novo.
3. Ainda não foi? Desligue o roteador da tomada, espere 30 segundos e ligue de novo.
4. Nada resolveu? Chame o suporte e conte o que você já testou. Isso ajuda muito!

## 3.6 Desligar e reiniciar por comando

| Comando | O que faz |
|---|---|
| `shutdown /s /t 0` | Desliga agora |
| `shutdown /r /t 0` | Reinicia agora |
| `shutdown /s /t 3600` | Desliga daqui a 1 hora (3600 segundos) |
| `shutdown /a` | Cancela o desligamento marcado |

## 3.7 Consertar arquivos do Windows

Se o Windows estiver dando erros estranhos, o suporte pode pedir para você rodar:

```
sfc /scannow
```

Ele procura e conserta arquivos do Windows sozinho. Para funcionar, abra o CMD **como administrador**: menu Iniciar > digite `cmd` > clique em **Executar como administrador**. Demora alguns minutos.

## 3.8 Precisa de ajuda?

Digite o comando seguido de `/?` para ver tudo o que ele faz. Exemplo: `copy /?`

## Resumo do módulo

- Abrir: `Win + R` > `cmd` > `Enter`.
- Pastas: `dir` mostra, `cd` entra, `cd ..` volta.
- Internet: `ping google.com` testa, `ipconfig /flushdns` limpa.
- `del` apaga sem lixeira. Cuidado!
