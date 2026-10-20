# Roteiro de gravação - entrega final

Grave na horizontal 16:9, com seu rosto em uma webcam no canto e voz própria.
Duração de 5 minutos. Publique no YouTube como público ou não listado.

## Preparação

1. Abra o repositório: https://github.com/gustavoaraujocd/tasktrackerr
2. Crie ou retome o Codespaces na branch main.
3. Aguarde a mensagem “Preparacao concluida”.
4. Abra dois separadores: GitHub e editor do Codespaces.
5. No terminal do Codespaces, execute `clear` antes de começar a demonstração.

## Telas e tempo

| Tempo | Tela | Ação |
|---|---|---|
| 0:00-0:30 | Página inicial do repositório | Nome, RA, curso, unidade e objetivo |
| 0:30-1:30 | GitHub | Pastas, histórico, arquivos e comandos do README |
| 1:30-2:30 | Dockerfile e Compose | Explique base Python, WORKDIR, COPY, CMD, stdin e TTY |
| 2:30-4:30 | Terminal do Codespaces | Build, docker run, Compose, erro, cadastro e listagem |
| 4:30-5:00 | README | Explique a evolução e encerre |

Links para deixar abertos:

- Pastas: https://github.com/gustavoaraujocd/tasktrackerr
- Histórico: https://github.com/gustavoaraujocd/tasktrackerr/commits/main/
- Dockerfile: https://github.com/gustavoaraujocd/tasktrackerr/blob/main/Dockerfile
- Compose: https://github.com/gustavoaraujocd/tasktrackerr/blob/main/docker-compose.yml
- README: https://github.com/gustavoaraujocd/tasktrackerr#readme

## Comandos do terminal

Execute um por vez, aguardando terminar:

```bash
docker build -t tasktracker:phase3 .
docker run --rm -it tasktracker:phase3
```

Mostre o menu e escolha 3 para sair. Depois:

```bash
docker compose run --rm tasktracker-app
```

## Entradas para demonstrar o menu

1. Opção: 1.
2. Título: apenas Enter para mostrar a validação.
3. Título corrigido: Entrega final Docker.
4. Descrição: Demonstrar a aplicação no container.
5. Prioridade: urgente para mostrar a validação.
6. Prioridade corrigida: Alta.
7. Data e hora: apenas Enter em cada campo.
8. Opção: 2 para mostrar a tarefa.
9. Opção: 3 para encerrar.

Os dados ficam em memória e são descartados ao sair. O Docker executa a CLI
no Codespaces; o navegador mostra o terminal da máquina Linux remota.

Depois de gravar, pare o Codespaces para encerrar o consumo de computação.
O envio ao AVA continua pendente do PDF com o link do novo vídeo.
