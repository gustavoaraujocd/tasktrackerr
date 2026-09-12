# ADRs — Decisões Arquiteturais

## ADR-001 — Python 3.11
**Status:** aceito.
**Decisão:** usar Python 3.11+ no núcleo do TaskTracker.
**Motivo:** linguagem prevista no planejamento inicial, simples para prototipação e ampla compatibilidade com pytest e Docker.

## ADR-002 — Arquitetura de domínio isolado
**Status:** aceito.
**Decisão:** separar entidades (`models.py`) dos casos de uso (`service.py`).
**Motivo:** facilitar evolução iterativa, testes unitários e futura troca da camada de persistência.

## ADR-003 — Persistência em memória na Entrega 1
**Status:** aceito.
**Decisão:** usar um dicionário interno no serviço em vez de banco de dados.
**Motivo:** a entrega avalia especificação, testabilidade e harness; banco adicionaria complexidade sem benefício para os critérios atuais.

## ADR-004 — Pytest como test harness
**Status:** aceito.
**Decisão:** usar pytest para cenários principais e edge cases.
**Motivo:** execução simples, saída legível e integração direta com automação.

## ADR-005 — Docker para reprodutibilidade
**Status:** aceito.
**Decisão:** empacotar a execução dos testes em imagem Python slim.
**Motivo:** reduzir diferenças entre máquinas dos integrantes e ambiente de avaliação.

## ADR-006 — Git Flow simplificado
**Status:** aceito.
**Decisão:** `main` recebe integração final, `develop` recebe trabalho da sprint e alterações são produzidas em `feature/*` por Pull Request.
**Motivo:** impedir trabalho direto na principal e tornar revisão/rastreabilidade explícitas.
