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
O fluxo adotado é:

`feature/*` -> Pull Request -> `develop` -> Pull Request -> `main`

Não devem ser feitos commits diretos na `main`. O escopo da sprint foi decomposto em Issues independentes no GitHub para especificação, harness/testes e ambiente/IA.

Todo merge relevante deve ocorrer por Pull Request. O PR da Entrega 1 precisa ser revisado por outro integrante da equipe antes do merge em `develop`, mantendo evidência de comentário/revisão e aprovação no próprio GitHub.

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
A IA foi usada como agente de apoio ao desenvolvimento, sem substituir a especificação. O fluxo adotado foi orientado por SDD: primeiro foram definidos requisitos, regras de negócio, contratos e critérios de aceite; somente depois o agente foi utilizado para apoiar a geração, revisão e refinamento dos artefatos de código e documentação.

### Tarefas em que a IA foi utilizada
- organização da estrutura inicial do repositório;
- apoio à decomposição do problema em componentes testáveis;
- geração assistida do modelo de domínio e do serviço de tarefas;
- criação e refinamento da suíte inicial de testes com `pytest`;
- apoio na criação do `Dockerfile` e `docker-compose.yml`;
- revisão de documentação técnica, ADRs e README;
- análise dos resultados do harness e refinamento após feedback dos testes;
- apoio à preparação de Issues, branches e Pull Request seguindo a governança definida.

### Como a especificação controlou a geração
A geração de código não foi feita de forma livre. O documento `docs/especificacao-sdd.md` define os requisitos funcionais e não funcionais, regras de negócio, entradas, saídas e critérios de aceite. O arquivo `AGENTS.md` fornece ao agente o contexto persistente e estabelece que qualquer código gerado deve respeitar essa especificação.

Assim, o agente deve:
1. consultar a especificação antes de propor alterações;
2. não criar comportamentos que não estejam previstos nos requisitos;
3. manter as regras de negócio definidas no domínio;
4. criar ou atualizar testes quando houver alteração de comportamento;
5. usar o resultado dos testes como feedback para refinamento;
6. registrar decisões arquiteturais relevantes nos ADRs.

Esse processo caracteriza o uso de IA dentro do fluxo **Spec-Driven Development**, em que a especificação é a fonte de verdade e o agente atua como mecanismo de implementação e revisão controlada.

### Evidência para o PDF
O PDF final deve conter pelo menos um print real do uso do Codex/ChatGPT durante o desenvolvimento. A captura recomendada deve mostrar uma interação relacionada à geração ou revisão de código, testes ou documentação. O PDF deve explicar que a interação foi orientada pelos arquivos `docs/especificacao-sdd.md` e `AGENTS.md`.

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
- [x] Ferramenta de IA identificada e uso documentado.
- [x] Arquivo de contexto para agente de IA.
- [x] Dockerfile e Docker Compose.
- [x] Harness automatizado com pytest.
- [x] Casos principais e edge cases.
- [x] Logs de execução documentados.
- [x] Integrantes e RAs registrados.
- [ ] Aprovação real de outro integrante no Pull Request #4.
- [ ] Inserir no PDF final um print real do uso do Codex/ChatGPT.
- [ ] Inserir no PDF final um print/log do harness/pipeline executando com sucesso.

## Apresentação em vídeo
https://youtu.be/vuKSPL0uC0U?feature=shared
