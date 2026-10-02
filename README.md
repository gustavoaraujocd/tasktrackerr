# TaskTracker

Aplicação acadêmica desenvolvida no **Bootcamp II — Fase 2 (Entrega Intermediária)**, com foco em Engenharia de Software, versionamento profissional com Git/GitHub e implementação das regras de negócio em Python.

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
.venv\\Scripts\\activate
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

Evolução prevista para empacotamento, containerização com Docker, testes e deploy.

## 12. Vídeo de apresentação

🎥 **Apresentação da Fase 2 — TaskTracker**

[Assistir ao vídeo de apresentação no YouTube](https://youtu.be/D5hFhHNIHJI)

## 13. Equipe

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

## 14. Próximos passos

- Refinar os testes da interface CLI;
- Evoluir os casos de uso conforme os critérios da próxima etapa;
- Consolidar a execução em Docker;
- Preparar a apresentação técnica e a demonstração da solução.
