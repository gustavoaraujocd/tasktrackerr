# ADRs — Decisões Arquiteturais

## ADR-001 — Python 3.11
**Status:** aceito. **Decisão:** usar Python 3.11+ no núcleo do TaskTracker.

## ADR-002 — Domínio isolado
**Status:** aceito. **Decisão:** separar entidades (`models.py`) dos casos de uso (`service.py`) para facilitar testes e evolução.

## ADR-003 — Persistência em memória
**Status:** aceito. **Decisão:** usar armazenamento em memória nesta Entrega 1 para manter o foco em especificação e testabilidade.

## ADR-004 — Pytest
**Status:** aceito. **Decisão:** usar pytest como harness de validação.

## ADR-005 — Docker
**Status:** aceito. **Decisão:** usar Docker/Docker Compose para reprodutibilidade.

## ADR-006 — Git Flow simplificado
**Status:** aceito. **Decisão:** `feature/*` -> PR -> `develop` -> PR -> `main`.
