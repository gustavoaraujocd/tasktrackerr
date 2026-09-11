# TaskTracker

Projeto acadêmico do **Bootcamp II — Entrega 1: Ambiente, Especificação Técnica e Test Harness**.

## Visão geral
O TaskTracker é um sistema para organização e acompanhamento de tarefas pessoais, acadêmicas e profissionais. Nesta entrega, o projeto foi evoluído do planejamento inicial para um núcleo funcional em Python, guiado por especificação (SDD), com ambiente reproduzível e suíte automatizada de testes.

## Aluno
- **Nome:** Gustavo Carmo
- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
- **Unidade/Turma:** Taguatinga — Noturno
- **E-mail institucional:** GUSTAVO.CARMO@SEMPRECEUB.COM

> Caso a equipe possua outros integrantes, adicionar aqui os nomes completos e RAs antes da submissão no Moodle.

## Objetivo funcional
Permitir cadastrar, consultar, atualizar, listar e concluir tarefas, controlando prioridade, prazo e status com regras de validação explícitas.

## Arquitetura
- `src/tasktracker/models.py`: entidades, enums e validações do domínio.
- `src/tasktracker/service.py`: casos de uso e armazenamento em memória.
- `tests/test_service.py`: harness de testes automatizados.
- `docs/especificacao-sdd.md`: especificação técnica e contratos.
- `docs/adrs.md`: decisões arquiteturais.
- `AGENTS.md`: regras de contexto para agentes de IA no fluxo SDD.
- `Dockerfile` e `docker-compose.yml`: ambiente reproduzível.

## Fluxo Git e governança
O fluxo adotado é:

`feature/*` -> Pull Request -> `develop` -> Pull Request -> `main`

Não devem ser feitos commits diretos na `main`. O escopo da sprint foi decomposto em Issues independentes no GitHub para especificação, harness/testes e ambiente/IA.

## Fluxo SDD
1. Especificar o comportamento esperado.
2. Decompor em componentes e contratos.
3. Implementar uma unidade pequena.
4. Executar o harness automatizado.
5. Revisar resultado e código.
6. Refinar especificação quando necessário.
7. Integrar via Pull Request.

## Agente de IA
O projeto está preparado para uso de **Codex/ChatGPT** como agente de apoio à geração e revisão de código. O arquivo `AGENTS.md` define o contexto persistente, as regras e o fluxo esperado para evitar alterações que contradigam a especificação.

## Requisitos
- Python 3.11+
- pip
- Docker + Docker Compose (opcional para execução containerizada)

## Instalação local
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -e .[dev]
```

## Executar o test harness
### Local
```bash
pytest -q
```

### Docker
```bash
docker compose build
docker compose run --rm tests
```

## Suíte inicial
A suíte cobre:
- criação com valores padrão;
- rejeição de título vazio;
- rejeição de prioridade inválida;
- rejeição de prazo inválido;
- conclusão de tarefa;
- atualização preservando identificador;
- filtro por status;
- consulta de tarefa inexistente.

## Evidência de execução
Execução validada em 11/09/2026:

```text
........                                                                 [100%]
8 passed in 0.06s
```

Durante a primeira execução foi identificado um aviso de depreciação em `datetime.utcnow()`. O código foi refinado para usar `datetime.now(UTC)`, eliminando a dependência de datetime ingênuo e registrando um exemplo de refinamento técnico orientado pelo harness.

## Decisões arquiteturais resumidas
- Python 3.11 como linguagem-base.
- Domínio separado da camada de casos de uso.
- Persistência em memória nesta entrega para maximizar isolamento e testabilidade.
- Pytest como harness de validação.
- Docker como mecanismo de reprodutibilidade.
- Git Flow simplificado com `main`, `develop` e `feature/*`.

Detalhes: `docs/adrs.md`.

## Especificação técnica
A especificação completa está em `docs/especificacao-sdd.md` e inclui requisitos funcionais e não funcionais, regras de negócio, contratos de entrada/saída, decomposição em unidades, critérios de aceite e registro de refinamentos.

## Estrutura atual
```text
tasktrackerr/
├── AGENTS.md
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
├── docs/
│   ├── adrs.md
│   ├── especificacao-sdd.md
│   ├── algoritmo.md
│   ├── arquitetura.md
│   ├── planejamento-logico.md
│   └── requisitos.md
├── src/
│   └── tasktracker/
│       ├── __init__.py
│       ├── models.py
│       └── service.py
└── tests/
    └── test_service.py
```

## Checklist da Entrega 1
- [x] Repositório público no GitHub.
- [x] Branches `main` e `develop`.
- [x] Trabalho executado em `feature/*`.
- [x] Issues com decomposição da sprint.
- [x] README com instalação, execução e ADRs.
- [x] Especificação técnica SDD.
- [x] Contratos e regras de negócio.
- [x] Arquivo de contexto para agente de IA.
- [x] Dockerfile e Docker Compose.
- [x] Harness automatizado com pytest.
- [x] Casos principais e edge cases.
- [x] Logs de execução documentados.
- [ ] Aprovação de outro integrante no Pull Request, quando aplicável.
- [ ] Adicionar nomes completos e RAs dos demais integrantes, se houver.

## Apresentação em vídeo
https://youtu.be/vuKSPL0uC0U?feature=shared
