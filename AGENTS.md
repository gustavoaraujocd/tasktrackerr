# Diretrizes para Agentes de IA — TaskTracker

## Objetivo
Usar IA como apoio ao fluxo SDD (Spec-Driven Development), mantendo a especificação como fonte de verdade.

## Regras obrigatórias
1. Ler `docs/especificacao-sdd.md` antes de propor alterações de código.
2. Não criar comportamento novo sem requisito ou regra de negócio correspondente.
3. Toda alteração funcional deve incluir ou atualizar testes automatizados.
4. Preservar os contratos públicos do domínio (`Task`, `TaskService`, `Priority`, `Status`).
5. Preferir mudanças pequenas, rastreáveis e associadas a Issues.
6. Nunca commitar diretamente em `main`; usar `feature/*` -> PR -> `develop` -> PR -> `main`.
7. Antes de concluir uma tarefa, executar `pytest -q` ou `docker compose run --rm tests`.
8. Em caso de conflito entre código e especificação, corrigir o código ou registrar formalmente o refinamento da especificação.

## Fluxo SDD esperado
Especificar -> decompor -> gerar/editar -> testar -> revisar -> refinar -> integrar.

## Agente documentado
Ferramenta principal: **Codex**, com apoio do ChatGPT para organização, documentação e revisão técnica.
