# ADRs - TaskTracker

Consolidação para Bootcamp III / Entrega 2, 23/10/2026. As decisões da base são preservadas; os refinamentos E2 seguem para homologação no PR #16.

## ADR-001 - Python 3.11+
**Contexto:** equipe necessita CLI simples, biblioteca de datas e testes automatizados.
**Decisão:** Python 3.11+ com biblioteca padrão no runtime.
**Alternativa:** framework web e front-end separado.
**Consequências:** menor número de dependências e execução simples; ausência de interface gráfica e distribuição depende de Python ou Docker.

## ADR-002 - Domínio separado da CLI
**Contexto:** regras precisam ser testadas sem interação manual.
**Decisão:** entidades e enums em models.py; casos de uso e memória em service.py; I/O em main.py.
**Alternativa:** um script único contendo interface e regras.
**Consequências:** testes do domínio independentes de input; é necessário testar também integração do menu. O serviço não impõe imutabilidade aos objetos retornados.

## ADR-003 - Memória e escopo local
**Contexto:** Entrega 1 especificou foco em núcleo funcional e harness, sem persistência.
**Decisão:** manter dicionário por processo e explicitar perda dos registros ao encerrar.
**Alternativa:** SQLite ou arquivo JSON.
**Consequências:** não exige instalação de banco; sem durabilidade, múltiplos usuários ou controle de concorrência. Um volume Docker isolado não torna a aplicação persistente. Persistência exigiria nova especificação e testes.

## ADR-004 - Pytest e regressões
**Contexto:** inspeção sozinha não provou todos os contratos.
**Decisão:** manter suíte inicial e incluir casos reproduzíveis de borda, subprocesso e menu com serviço real.
**Alternativa:** só execução manual ou testes gerados sem revisão de assertivas.
**Consequências:** 39 casos aprovados no snapshot; os resultados são evidência limitada aos cenários exercitados. Há risco de testes confirmarem os mesmos pressupostos errados do código; o revisor deve conferir regra e oráculo.

## ADR-005 - Docker em estágios
**Contexto:** imagem inicial executava apenas testes e faltava interação com CLI.
**Decisão:** runtime separado de tests, stdin/TTY no Compose e usuário UID 10001 no runtime E2.
**Alternativa:** instalar ferramentas de desenvolvimento na imagem de produção e executar como root.
**Consequências:** menor superfície e privilégio no runtime; build de testes depende de rede. Base e dependências sem pinagem integral por hash ainda permitem variação. Docker não é prova de segurança ou isolamento absoluto.

## ADR-006 - Feature / develop / main
**Contexto:** é preciso revisar antes de integrar.
**Decisão:** PR com problema, requisitos, resultados e aceite; aprovação humana de colega diferente do autor e CI no SHA atual.
**Alternativa:** push direto na main.
**Consequências:** rastreabilidade e revisão independente; integração depende de disponibilidade da equipe. A ausência inicial de proteção foi corrigida pelo ruleset ativo 25727805 em main/develop, sem bypass e com PR, revisão e checks obrigatórios. Aprovação antiga não homologa código posterior.

## ADR-007 - Prazos civis locais e timestamps UTC
**Contexto:** datetime herda date; horário sem data era ignorado; referências aware causavam TypeError.
**Decisão E2:** rejeitar datetime como due_date, exigir data para hora e rejeitar tzinfo nos prazos e referências; created_at segue UTC-aware. Sem hora, usar fim do dia, com comparação estritamente maior.
**Alternativa:** converter todos os prazos para UTC com timezone obrigatório.
**Consequências:** comportamento explícito para CLI local e erro de domínio orientado; não atende agendas entre fusos ou regras de horário de verão. Esses casos exigem novo contrato, não conversão silenciosa.

## ADR-008 - IA assistiva e homologação humana
**Contexto:** geração rápida pode reproduzir falhas e produzir explicações sem evidência.
**Decisão E2:** SDD orienta mudanças; IA ajuda a implementar e testar; colega revisa o diff, o significado dos testes e as fontes antes do merge.
**Alternativa:** aceitar automaticamente a saída porque o harness está verde.
**Consequências:** mais esforço de leitura e investigação, com responsabilidade humana explícita. AGENTS.md orienta o agente, mas não substitui sandbox, controle de acesso ou segurança do sistema operacional.
