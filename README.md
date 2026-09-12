# TaskTracker

Projeto acadêmico do **Bootcamp II — Entrega 1: Ambiente, Especificação Técnica e Test Harness**.

## Visão geral
O TaskTracker é um sistema para organização e acompanhamento de tarefas pessoais, acadêmicas e profissionais. Nesta entrega, o projeto foi evoluído do planejamento inicial para um núcleo funcional em Python, guiado por especificação (SDD), com ambiente reproduzível e suíte automatizada de testes.

## Equipe

| Integrante | RA |
|---|---:|
| Jonathan Rodrigues Silva Corrêa | 22450356 |
| Matheus Couto Nogueira | 22505474 |
| Esther Diniz Bastos | 22505492 |
| Cauã Gonçalves Xavier Mrad | 22452326 |
| Rillary Lorranne de Souza Portilho | 22450936 |
| Gustavo Araújo do Carmo | 22304113 |

- **Curso:** Análise e Desenvolvimento de Sistemas (ADS)
- **Unidade/Turma:** Taguatinga — Noturno
- **E-mail institucional de referência:** GUSTAVO.CARMO@SEMPRECEUB.COM

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
`feature/*` -> Pull Request -> `develop` -> Pull Request -> `main`

Não devem ser feitos commits diretos na `main`. O escopo da sprint foi decomposto em Issues independentes no GitHub para especificação, harness/testes e ambiente/IA. O PR #4 foi revisado e aprovado por dois integrantes antes do merge em `develop`.

## Fluxo SDD
1. Especificar o comportamento esperado.
2. Decompor em componentes e contratos.
3. Implementar uma unidade pequena.
4. Executar o harness automatizado.
5. Revisar resultado e código.
6. Refinar especificação quando necessário.
7. Integrar via Pull Request.

## Ferramenta de IA utilizada
**Ferramenta utilizada:** Codex, com apoio do ChatGPT para organização técnica, documentação e revisão do fluxo.

### Como a IA foi utilizada
A IA foi usada como agente de apoio ao desenvolvimento, sem substituir a especificação. Primeiro foram definidos requisitos, regras de negócio, contratos e critérios de aceite; depois o agente foi utilizado para apoiar geração, revisão e refinamento dos artefatos.

### Tarefas em que a IA foi utilizada
- organização da estrutura inicial do repositório;
- decomposição do problema em componentes testáveis;
- geração assistida do modelo de domínio e serviço de tarefas;
- criação e refinamento da suíte de testes com `pytest`;
- apoio na criação do `Dockerfile` e `docker-compose.yml`;
- revisão de ADRs e documentação técnica;
- análise dos resultados do harness e refinamento após feedback dos testes;
- apoio à preparação de Issues, branches e Pull Requests.

### Como a especificação controlou a geração
O documento `docs/especificacao-sdd.md` define requisitos, regras de negócio, entradas, saídas e critérios de aceite. O arquivo `AGENTS.md` estabelece que qualquer código gerado deve respeitar essa especificação. A especificação funciona como fonte de verdade do fluxo SDD.

## Requisitos
- Python 3.11+
- pip
- Docker + Docker Compose

## Instalação local
```bash
python -m venv .venv
source .venv/bin/activate
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
A suíte cobre criação, validações de título/prioridade/prazo, conclusão, atualização, filtro por status e consulta inexistente.

## Evidência de execução
```text
........                                                                 [100%]
8 passed in 0.06s
```

Durante a primeira execução foi identificado um aviso de depreciação em `datetime.utcnow()`. O código foi refinado para usar `datetime.now(UTC)`.

## Decisões arquiteturais resumidas
- Python 3.11.
- Domínio separado dos casos de uso.
- Persistência em memória nesta entrega.
- Pytest como harness.
- Docker para reprodutibilidade.
- Git Flow simplificado com `main`, `develop` e `feature/*`.

## Especificação técnica
A especificação completa está em `docs/especificacao-sdd.md`.

## Checklist da Entrega 1
- [x] Repositório público no GitHub.
- [x] Branches `main` e `develop`.
- [x] Trabalho executado em `feature/*`.
- [x] Issues com decomposição da sprint.
- [x] README com instalação, execução e ADRs.
- [x] Especificação técnica SDD.
- [x] Contratos e regras de negócio.
- [x] Ferramenta de IA identificada e uso documentado.
- [x] Arquivo de contexto para agente de IA.
- [x] Dockerfile e Docker Compose.
- [x] Harness automatizado com pytest.
- [x] Casos principais e edge cases.
- [x] Logs de execução documentados.
- [x] Integrantes e RAs registrados.
- [x] Aprovação de integrantes no PR #4.

## Apresentação em vídeo
https://youtu.be/vuKSPL0uC0U?feature=shared
