# Refinamento por testes - Entrega 2

Base inspecionada: c946e5781f935f87b51b54c4f0ce56503dae69b3. Issue #14; PR #16.
A suíte de contratos adicionada foi executada antes da correção: 8 falhas e 5 aprovações. Não se alega que a suíte antiga falhava: os casos de borda ainda não eram exercitados.

| Evidência / causa | Antes | Contrato e correção | Teste de regressão |
|---|---|---|---|
| datetime herda date | Validação aceitava valor temporal com hora em campo de data | RN11: rejeitar datetime explicitamente | test_datetime_is_not_a_calendar_due_date |
| Horário isolado | Era aceito e ignorado pelo cálculo de atraso | RN12: horário exige data | test_time_without_date_is_rejected |
| Horário com timezone | Era aceito sem política consistente | RN13: prazo civil local sem tzinfo | test_aware_deadline_time_is_rejected |
| Referência aware | Comparação com deadline naive lançava TypeError | RN13: erro explícito ValueError | test_aware_reference_has_explicit_validation |
| Filtro inválido | Retornava lista vazia silenciosamente | RN15: None ou enum Status | test_invalid_filter_is_not_silently_an_empty_result |
| Texto None: dois casos | AttributeError em strip de título/descrição | RN10: checar tipo antes de normalizar | test_invalid_text_type_uses_domain_error |
| Remoção só da data | Update deixava horário sem efeito | RN12/RN16: validar antes de substituir | test_invalid_update_does_not_change_stored_task |

### Integração por inspeção
O serviço já implementava os casos RF02/RF04/RF05/RF06; o menu não oferecia acesso. As opções 4–7 corrigem essa lacuna e seus testes verificam o resultado no serviço real. A opção 3 continua encerrando, evitando quebrar fluxos anteriores.

### Re-especificação
1. Falha reproduzida com entrada controlada.
2. Ambiguidade do contrato identificada (data, horário, fuso, filtro ou erro).
3. RN10–RN16 documentadas antes da correção.
4. Validação do domínio ajustada; menu integrado; regressões mantidas.
5. Harness ampliado de 13 casos da base para 39 na E2, com nenhuma falha na execução final.

Os 8 casos falhos representam sete grupos de causa, pois o caso de texto é parametrizado em título e descrição. Evidências: [antes.log](evidencias/antes.log), [depois.log](evidencias/depois.log) e [depois.xml](evidencias/depois.xml).

### Limites conhecidos
Objetos do domínio são mutáveis; uso externo pode contornar o serviço. Não há durabilidade, autenticação, concorrência ou calendário entre fusos. A E2 mantém o escopo local da Entrega 1, sem prometer capacidades ausentes.
