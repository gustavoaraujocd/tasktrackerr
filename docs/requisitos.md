# Requisitos — TaskTracker

## Requisitos funcionais

- RF01 — Cadastrar uma nova tarefa.
- RF02 — Informar título e descrição da tarefa.
- RF03 — Definir prioridade para a tarefa.
- RF04 — Definir prazo para conclusão.
- RF05 — Listar tarefas cadastradas.
- RF06 — Atualizar dados de uma tarefa.
- RF07 — Marcar tarefa como concluída.
- RF08 — Exibir o status atual da tarefa.
- RF09 — Permitir futura filtragem por prioridade e status.

## Regras de negócio

- RN01 — O título é obrigatório.
- RN02 — A prioridade deve pertencer ao conjunto definido pelo sistema.
- RN03 — O status deve ser controlado pelo sistema.
- RN04 — O prazo precisa utilizar formato válido.
- RN05 — Tarefas concluídas devem permanecer identificadas como concluídas.
- RN06 — Alterações devem manter a consistência dos dados.

## Dados previstos

| Campo | Descrição |
|---|---|
| id | Identificador único |
| titulo | Nome da tarefa |
| descricao | Detalhamento da atividade |
| prioridade | Nível de prioridade |
| prazo | Data prevista |
| status | Situação da tarefa |
| data_criacao | Data de cadastro |
