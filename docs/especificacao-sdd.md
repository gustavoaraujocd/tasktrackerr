# Especificação Técnica SDD — TaskTracker

## 1. Problema
Pessoas que conciliam atividades acadêmicas, pessoais e profissionais precisam registrar tarefas, prioridade, prazo e andamento sem depender de controles dispersos. O TaskTracker centraliza esse acompanhamento em um domínio simples, testável e evolutivo.

## 2. Escopo da Entrega 1
Entregar o núcleo de domínio e um test harness automatizado. Interface gráfica, autenticação, banco de dados e integrações externas ficam fora desta etapa.

## 3. Requisitos funcionais
- RF01: cadastrar tarefa com título obrigatório.
- RF02: registrar descrição opcional.
- RF03: definir prioridade baixa, média ou alta.
- RF04: definir prazo opcional como data válida.
- RF05: listar tarefas cadastradas.
- RF06: consultar tarefa por identificador.
- RF07: atualizar dados da tarefa.
- RF08: alterar tarefa para concluída.
- RF09: filtrar listagem por status.

## 4. Requisitos não funcionais
- RNF01: Python 3.11 ou superior.
- RNF02: suíte automatizada com pytest.
- RNF03: execução reproduzível via Docker.
- RNF04: código de domínio independente de UI e persistência.
- RNF05: fluxo Git baseado em `main`, `develop` e `feature/*`.

## 5. Regras de negócio
- RN01: título vazio ou somente espaços é inválido.
- RN02: prioridade aceita somente `baixa`, `media` e `alta`.
- RN03: status aceita somente `pendente`, `em_andamento` e `concluida`.
- RN04: prazo, quando informado, deve ser um objeto de data válido.
- RN05: cada tarefa recebe identificador único.
- RN06: concluir uma tarefa altera seu status para `concluida` sem remover o registro.
- RN07: consulta de ID inexistente retorna erro controlado.

## 6. Contratos de entrada e saída
### create_task
Entrada: `title: str`, `description: str`, `priority: Priority`, `due_date: date | None`.
Saída: `Task` criada com `id`, `created_at` e status inicial `pendente`.
Erros: `ValueError` para dados inválidos.

### get_task
Entrada: `task_id: str`.
Saída: `Task` correspondente.
Erro: `KeyError("task not found")` quando o ID não existe.

### list_tasks
Entrada: `status: Status | None`.
Saída: lista de tarefas, opcionalmente filtrada.

### update_task
Entrada: ID e campos opcionais de atualização.
Saída: tarefa atualizada preservando o ID.

### complete_task
Entrada: `task_id: str`.
Saída: tarefa com status `concluida`.

## 7. Decomposição em unidades
- `models.py`: entidades, enums e validações locais.
- `service.py`: casos de uso do domínio e armazenamento em memória.
- `tests/test_service.py`: harness de validação executável.
- `Dockerfile`/`docker-compose.yml`: ambiente reproduzível.
- `AGENTS.md`: regras de contexto para agente de IA.

## 8. Critérios de aceite
A Entrega 1 é aceita quando a suíte cobre fluxo principal e casos de borda, todos os testes passam no ambiente local/container e a documentação permite reproduzir a execução.

## 9. Refinamentos por feedback
A especificação inicial previa apenas planejamento. Para atender à Entrega 1, foi refinada para incluir núcleo executável, contratos explícitos, validação de entradas, filtro por status, Docker e harness automatizado. A persistência foi mantida em memória nesta sprint para preservar isolamento e testabilidade.
