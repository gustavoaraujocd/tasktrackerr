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

## ADR - Containerização da CLI na Fase 3
A imagem final passa a iniciar o menu. Um estágio e um serviço separados mantêm
os testes, sem instalar Pytest na imagem final. O Compose fornece stdin e TTY;
o comando de uso recomendado é `docker compose run --rm tasktracker-app`.
Mantemos o armazenamento em memória e o menu da entrega anterior. Não há serviço
web, porta publicada ou banco de dados nesta etapa.
