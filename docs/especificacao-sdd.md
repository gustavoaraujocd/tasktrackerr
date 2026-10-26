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
- RF07 informar horário limite opcional.
- RF08 identificar tarefas pendentes fora do prazo e apresentar alerta no terminal.

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
- RN05 horário limite, quando informado, deve ser um horário válido.
- RN06 IDs são únicos e não mudam durante atualizações.
- RN07 tarefa pendente com prazo ultrapassado é identificada como atrasada.
- RN08 tarefa concluída não gera alerta de atraso.
- RN09 tarefa inexistente gera erro explícito.

## Contrato de entrada — criação
Campos: `title` obrigatório; `description` opcional; `priority` opcional; `due_date` opcional; `due_time` opcional.

## Contrato de saída
Uma tarefa possui `id`, `title`, `description`, `priority`, `due_date`, `due_time`, `status` e `created_at`.

## Componentes
- `models.py`: entidades, identificador e validações do domínio.
- `service.py`: casos de uso, armazenamento em memória e identificação de tarefas atrasadas.
- `tests/test_service.py`: harness automatizado.

## Critérios de aceite
A entrega é aceita quando criação, atualização, conclusão, listagem, filtro, validações principais e identificação de tarefas atrasadas passam no harness automatizado.

## Refinamento por feedback
Durante a primeira execução do harness foi identificado uso de `datetime.utcnow()`. A implementação foi refinada para `datetime.now(UTC)`, mantendo timestamps com timezone explícito.

## Infraestrutura da Fase 3
- RNF06: a imagem final deve iniciar a CLI com `python src/main.py`.
- RNF07: o serviço `tasktracker-app` deve manter stdin aberto e alocar TTY.
- RNF08: os testes devem continuar executáveis em serviço separado.
- RNF09: o README deve documentar build, execução com `docker run -it` e Compose.
- RNF10: a imagem deve conter o código sem depender de bind mount do hospedeiro.
- Não há alteração dos contratos do domínio ou inclusão de persistência.
- Aceite: build sem erros; cadastro, rejeição de entrada inválida, listagem e saída
  dentro do contêiner; suíte de domínio e da CLI aprovada.

- RNF11: o Codespaces deve preparar Python, Docker, testes e imagens para a demonstracao no navegador.

## Refinamento E2 - Bootcamp III (23/10/2026)

Proposta implementada para homologação no PR da Sprint 2, vinculada à issue #14.
Os RF01-RF08 permanecem; todos os casos de uso devem ser acessíveis pela CLI.
As opções 1 (cadastro), 2 (listagem) e 3 (saída) são preservadas. As opções
4, 5, 6 e 7 oferecem consulta por ID, atualização, conclusão e filtro por status.
Erros de domínio ou ID inexistente são informados sem encerrar o menu.

### Contratos refinados por testes

- RN10: título e descrição são strings; tipos incompatíveis geram ValueError.
- RN11: due_date aceita date, mas rejeita datetime (subclasse de date).
- RN12: due_time exige due_date. Remover a data exige remover o horário no mesmo update.
- RN13: prazos são horários civis locais sem tzinfo. due_time e reference com
  tzinfo são rejeitados com ValueError; não há conversão implícita entre fusos.
  created_at continua UTC-aware e não participa da comparação de prazo.
- RN14: sem horário, a data vence após 23:59:59.999999. No instante exato do
  prazo, a tarefa não está atrasada; após esse instante, está. Apenas concluídas
  são excluídas do alerta entre as tarefas com prazo, inclusive em andamento.
- RN15: list(status) aceita None ou Status; filtros inválidos geram ValueError.
- RN16: update valida antes de substituir o registro. Se falhar, nenhum campo
  armazenado muda; id e created_at não podem ser alterados.

Na CLI, Enter mantém campos durante atualização; '-' limpa descrição/data/hora.
Status aceita pendente, em_andamento ou concluida. Identificadores são completos.
Ao receber EOF ou Ctrl+C, a CLI encerra de forma orientada sem traceback.

### Evidência do loop

Os novos testes de contrato foram executados contra a base c946e57:
8 falhas e 5 aprovações. Evidenciaram data/hora ambíguas, TypeError em comparação
timezone-aware, AttributeError em texto inválido, filtro silencioso e atualização
que removia data deixando horário. O log antes da correção é preservado em
docs/evidencias/antes.log. A execução posterior e o JUnit são publicados ao lado.

Persistência em memória e domínio local monousuário são mantidos da Entrega 1.
Não há autenticação, banco, API ou promessa de uso em produção. Esses limites
devem aparecer no README e na defesa das decisões.

## Registro de re-especificações E2 (rastreabilidade)

| ID | Origem | Decisão | Evidência |
|---|---|---|---|
| R-E2-01 | E-01 | RN11 rejeita datetime como data civil | test_datetime_is_not_a_calendar_due_date |
| R-E2-02 | E-02 / E-06 | RN12 exige data para horário; RN16 mantém atualização atômica | test_time_without_date_is_rejected; test_invalid_update_does_not_change_stored_task |
| R-E2-03 | E-03 | RN13 explicita fuso; RN14 define fronteira do prazo | test_aware_reference_has_explicit_validation; test_exact_deadline_is_not_overdue |
| R-E2-04 | E-04 | RN15 rejeita filtro inválido | test_invalid_filter_is_not_silently_an_empty_result |
| R-E2-05 | E-05 | RN10 define texto e ValueError | test_invalid_text_type_uses_domain_error |

Origem: [ERROS.md](ERROS.md), issue #14 e PR #16. Contratos foram refinados antes da correção, na preparação de 23/10/2026, sem atribuir homologação à equipe. A ordem numérica de seções do StudyRoom é um modelo de organização; os contratos do TaskTracker permanecem neste arquivo.

## Refinamento E3 - revisão do PR #17 (26/10/2026)

- RN17: filtro sem resultados informa ausência de correspondências; não afirma que o cadastro está vazio.
- RN18: alertas de atraso são apresentados uma vez por ciclo do menu, antes da entrada; a listagem não duplica alertas.
- A especificação consolidada da candidata à release está em `sdd-as-built.md`.
