# Especificação Técnica SDD — TaskTracker

## Problema
Organizar e acompanhar tarefas pessoais, acadêmicas e profissionais com prioridade, prazo e status definidos de forma consistente.

## Requisitos funcionais
- RF01 cadastrar tarefa.
- RF02 consultar tarefa por ID.
- RF03 listar tarefas.
- RF04 atualizar dados da tarefa.
- RF05 concluir tarefa.
- RF06 filtrar tarefas por status.

## Requisitos não funcionais
- RNF01 execução em Python 3.11+.
- RNF02 suíte automatizada de testes.
- RNF03 ambiente reproduzível com Docker.
- RNF04 código modular e testável.
- RNF05 fluxo de integração via branches e Pull Requests.

## Regras de negócio
- RN01 título é obrigatório.
- RN02 prioridade aceita: baixa, media ou alta.
- RN03 status aceita: pendente, em_andamento ou concluida.
- RN04 prazo, quando informado, deve ser uma data válida.
- RN05 IDs são únicos e não mudam durante atualizações.
- RN06 tarefa inexistente gera erro explícito.

## Contrato de entrada — criação
Campos: `title` obrigatório; `description` opcional; `priority` opcional; `due_date` opcional.

## Contrato de saída
Uma tarefa possui `id`, `title`, `description`, `priority`, `due_date`, `status` e `created_at`.

## Componentes
- `models.py`: entidades e validações do domínio.
- `service.py`: casos de uso e armazenamento em memória.
- `tests/test_service.py`: harness automatizado.

## Critérios de aceite
A entrega é aceita quando criação, atualização, conclusão, listagem, filtro e validações principais passam no harness automatizado.

## Refinamento por feedback
Durante a primeira execução do harness foi identificado uso de `datetime.utcnow()`. A implementação foi refinada para `datetime.now(UTC)`, mantendo timestamps com timezone explícito.
