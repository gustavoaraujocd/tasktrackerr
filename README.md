# TaskTracker

Aplicação acadêmica desenvolvida no **Bootcamp II — Fase 3 (Entrega Final)**, com foco em Engenharia de Software, versionamento profissional com Git/GitHub e implementação das regras de negócio em Python.

**Entrega final individual:** Gustavo Araújo do Carmo - RA 22304113.

## Gravar pelo navegador com GitHub Codespaces

[Abra o TaskTracker no Codespaces](https://codespaces.new/gustavoaraujocd/tasktrackerr).
Entre na conta do GitHub e crie o ambiente na branch `main`. Aguarde a mensagem
“Preparacao concluida” no terminal: a configuração instala as dependências, roda
os testes e constrói as imagens Docker. Isso usa a cota de Codespaces da sua conta.

No terminal do Codespaces, execute os comandos da seção Docker abaixo.
O código roda em uma máquina Linux na nuvem; não é necessário instalar Docker
no computador usado para gravar. Ao terminar, pare o Codespaces pelo menu do GitHub.

Roteiro com os links e a ordem das telas: [docs/roteiro-gravacao.md](docs/roteiro-gravacao.md).

## 1. Visão geral

O **TaskTracker** é uma aplicação para organização e acompanhamento de tarefas pessoais, acadêmicas e profissionais. O projeto transforma o planejamento desenvolvido na Fase 1 em uma solução funcional, executada por linha de comando (CLI), com validações explícitas, código modular e testes automatizados.

## 2. Funcionalidades

A interface CLI disponibiliza um menu contínuo com:

1. **Cadastrar nova tarefa**
2. **Visualizar tarefas cadastradas**
3. **Sair da aplicação**

Cada tarefa possui:

- **Título:** obrigatório e não pode conter apenas espaços;
- **Descrição:** campo livre e opcional;
- **Prioridade:** Alta, Média/Media ou Baixa;
- **Data limite:** opcional, com entrada no formato DD/MM/AAAA;
- **Hora limite:** opcional, com entrada no formato HH:MM;
- **Status:** iniciado automaticamente como Pendente;
- **Identificador único:** gerado automaticamente para cada tarefa.

Quando uma tarefa pendente ultrapassa a data e o horário definidos, o sistema apresenta um **alerta no terminal**, identificando a tarefa pelo título e pelo ID. Tarefas concluídas não geram esse alerta.

Entradas inválidas são rejeitadas com mensagens orientativas e nova solicitação de dados.

## 3. Arquitetura

```text
TaskTracker/
├── .github/
├── docs/
│   ├── planejamento_logico.pdf
│   ├── adrs.md
│   └── especificacao-sdd.md
├── src/
│   ├── main.py
│   └── tasktracker/
│       ├── __init__.py
│       ├── models.py
│       └── service.py
├── tests/
│   └── test_service.py
├── AGENTS.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

### Responsabilidades

- `src/main.py`: interface de linha de comando, menu, entrada de dados, apresentação das tarefas e alertas de prazo.
- `src/tasktracker/models.py`: entidades, enums, identificador e validações do domínio.
- `src/tasktracker/service.py`: casos de uso, armazenamento em memória e identificação de tarefas atrasadas.
- `tests/test_service.py`: testes automatizados das regras e casos de uso.
- `docs/especificacao-sdd.md`: requisitos, regras de negócio, contratos e critérios de aceite.
- `docs/adrs.md`: decisões arquiteturais do projeto.
- `AGENTS.md`: contexto e regras para apoio de agentes de IA.

## 4. Regras de negócio

As principais regras implementadas são:

- O título é obrigatório;
- A prioridade aceita somente `baixa`, `media` ou `alta`;
- O status utiliza os estados `pendente`, `em_andamento` e `concluida`;
- O prazo, quando utilizado pelo núcleo de domínio, deve ser uma data válida;
- O horário limite, quando informado, deve ser válido;
- Cada tarefa recebe um identificador único;
- O identificador permanece o mesmo durante atualizações;
- Tarefas pendentes com prazo ultrapassado são identificadas como atrasadas e geram alerta no terminal;
- Tarefas concluídas não são consideradas atrasadas;
- Consultas de tarefas inexistentes geram erro explícito.

## 5. Tecnologias

- **Python 3.11+**
- **Pytest**
- **Git/GitHub**
- **Docker e Docker Compose**
- **SDD (Spec-Driven Development)**

## 6. Instalação

### Pré-requisitos

- Python 3.11 ou superior;
- pip;
- Git;
- Docker e Docker Compose (opcional para execução via container).

### Ambiente virtual

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências de desenvolvimento:

```bash
pip install -e ".[dev]"
```

## 7. Execução da aplicação

Na raiz do projeto:

```bash
python src/main.py
```

Exemplo de fluxo:

```text
==================================================
              TASKTRACKER
==================================================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
==================================================
Escolha uma opção:
```

Durante o cadastro, o sistema solicita título, descrição, prioridade, data limite e hora limite. Se existir uma tarefa pendente fora do prazo, um alerta é exibido no terminal.

## Execução com Docker — Fase 3

Pré-requisitos: Git, Docker Engine ou Docker Desktop iniciado e Docker Compose v2
(`docker compose version`). O computador hospedeiro não precisa ter Python instalado.

Na raiz do repositório, valide a configuração e construa a imagem:

```bash
docker compose config
docker build -t tasktracker:phase3 .
```

Execute a imagem em terminal interativo:

```bash
docker run --rm -it tasktracker:phase3
```

Execute a aplicação pelo Compose (recomendado), após o build acima:

```bash
docker compose run --rm tasktracker-app
```

Para construir e executar pelo próprio Compose:

```bash
docker compose run --build --rm tasktracker-app
```

O serviço `tasktracker-app` usa `stdin_open: true` para manter a entrada aberta
e `tty: true` para alocar um terminal. A opção 3 encerra a aplicação; `--rm`
remove o contêiner após o encerramento. Use `run` em um terminal para interagir com
`input()`. A imagem contém o código copiado no build, sem montar a pasta local.

### Como a imagem é organizada

- `python:3.11-slim`: base com Python 3.11.
- `WORKDIR /app`: diretório da aplicação.
- `PYTHONUNBUFFERED=1`: mostra a saída imediatamente.
- `COPY src/ /app/src/`: inclui a CLI e os módulos de domínio.
- `CMD ["python", "src/main.py"]`: inicia o menu por padrão.
- O estágio `tests` instala as dependências de desenvolvimento; a imagem final
  `runtime` executa somente a CLI, usando a biblioteca padrão do Python.
- `.dockerignore` exclui histórico Git, caches, ambientes virtuais e arquivos de documentação.

### Testes em contêiner

```bash
docker compose build tests
docker compose run --rm tests
```

O serviço de testes usa um perfil separado. A suíte existente do domínio é mantida,
e os testes da CLI verificam cadastro, validações, listagem e saída em um processo real.

### Limites e diagnóstico

As tarefas permanecem apenas na memória do processo. Ao sair, os registros são
perdidos; um volume não acrescentaria persistência a esta implementação.
Este deploy executa uma CLI local em contêiner e não disponibiliza um site ou uma API.

Se o Docker não responder, inicie o Docker Desktop e confirme `docker version`.
Se o menu não aceitar digitação, execute os comandos interativos acima em um terminal.
Após alterações no código, reconstrua a imagem.
Os alertas de prazo usam o relógio local do processo; o fuso do contêiner pode
diferir do hospedeiro.

### Rastreabilidade do planejamento

O arquivo `docs/planejamento_logico.pdf` é uma exportação fiel do conteúdo
já versionado em `docs/planejamento-logico.md`, gerada para esta preparação.
Ele não foi recuperado como PDF original da entrega da Fase 1.

### Entrega individual da Fase 3

- Manter o repositório público e preservar o histórico das fases anteriores.
- Gravar vídeo de 5 minutos, horizontal 16:9, com rosto e voz próprios.
- Mostrar GitHub, Dockerfile, Compose, build e uso real do menu no contêiner.
- Publicar no YouTube como público ou não listado.
- Inserir aqui o link do vídeo da Fase 3 quando estiver disponível.
- Enviar ao AVA um PDF com nome e links ativos do repositório e do novo vídeo.

**Vídeo da Fase 3: pendente de gravação/publicação.**
O link da Fase 2 abaixo é mantido como histórico e não substitui o novo vídeo.

Referências técnicas:
[Dockerfile](https://docs.docker.com/reference/dockerfile/),
[serviços Compose](https://docs.docker.com/reference/compose-file/services/),
[docker compose run](https://docs.docker.com/reference/cli/docker/compose/run/).

## 8. Testes automatizados

Execute a suíte com:

```bash
pytest -q
```

Execução com Docker:

```bash
docker compose build
docker compose run --rm tests
```

A suíte cobre criação, validação de título, prioridade, prazo, horário, conclusão, atualização, filtro por status, identificação de tarefas atrasadas e consulta de tarefa inexistente.

## 9. Fluxo de desenvolvimento

O projeto utiliza um fluxo baseado em branches e Pull Requests:

```text
feature/*
    ↓
Pull Request
    ↓
develop
    ↓
Pull Request
    ↓
main
```

A evolução do projeto deve ser registrada em commits pequenos e descritivos, permitindo acompanhar a implementação da estrutura, do menu, das regras de validação e dos alertas de prazo.

## 10. SDD e uso de IA

O desenvolvimento utiliza **Spec-Driven Development (SDD)**. O comportamento esperado é definido antes da implementação e utilizado como referência para desenvolvimento, testes e revisão.

A ferramenta de IA utilizada no projeto foi o **Codex**, com apoio do ChatGPT para organização técnica, documentação e revisão. A IA foi utilizada como ferramenta de apoio, enquanto requisitos, regras de negócio e critérios de aceite permanecem definidos pela equipe.

## 11. Evolução do projeto

### Fase 1 — Planejamento

Planejamento lógico, arquitetura de dados, decomposição do problema, algoritmo em português e mapeamento para Git/GitHub.

### Fase 2 — Entrega intermediária

Estruturação do repositório, versionamento, implementação da aplicação CLI em Python e validação das regras de negócio.

### Fase 3 — Entrega final

Empacotamento da CLI em imagem Docker, execução interativa com Docker Compose e documentação dos comandos. A validação no Docker e o vídeo da Fase 3 devem ser concluídos antes do envio ao AVA.

## 12. Vídeo de apresentação

🎥 **Apresentação da Fase 2 — TaskTracker**

[Assistir ao vídeo de apresentação no YouTube](https://youtu.be/D5hFhHNIHJI)

## 13. Equipe registrada nas fases anteriores

| Integrante | RA |
|---|---:|
| Jonathan Rodrigues Silva Corrêa | 22450356 |
| Matheus Couto Nogueira | 22505474 |
| Esther Diniz Bastos | 22505492 |
| Cauã Gonçalves Xavier Mrad | 22452326 |
| Rillary Lorranne de Souza Portilho | 22450936 |
| Gustavo Araújo do Carmo | 22304113 |

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Unidade/Turma:** Taguatinga — Noturno

## 14. Pendências para concluir a entrega final

- Executar o build e a demonstração interativa no Docker.
- Gravar e publicar o vídeo individual da Fase 3.
- Preencher o link do vídeo no README e no PDF de envio ao AVA.
