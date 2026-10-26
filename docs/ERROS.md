# Registro de erros lógicos - TaskTracker

Evidências reais da Sprint 2, issue #14 e PR #16. Base inspecionada c946e57; correção inicial no commit 5f34096. Logs de diagnóstico em [evidencias/antes.log](evidencias/antes.log); contratos em [especificacao-sdd.md](especificacao-sdd.md). Não se atribui cada defeito exclusivamente à IA.

## E-01 - datetime aceito no campo de data
- Detecção: test_datetime_is_not_a_calendar_due_date falhou antes da correção.
- Causa: datetime é subclasse de date e passava em isinstance.
- Correção: excluir datetime explicitamente da validação de due_date.
- Prevenção: manter o teste de tipo de borda.
- Classificação: contrato de entrada incompleto; refinamento R-E2-01 / RN11.

## E-02 - Horário sem data era aceito e ignorado
- Detecção: test_time_without_date_is_rejected.
- Causa: o cálculo retornava False sem due_date, mesmo havendo due_time.
- Correção: exigir data quando um horário é fornecido.
- Prevenção: testar cadastro e remoção parcial do prazo.
- Classificação: omissão da especificação; R-E2-02 / RN12.

## E-03 - Mistura de referência com fuso e prazo local
- Detecção: test_aware_reference_has_explicit_validation revelou TypeError; test_aware_deadline_time_is_rejected não recebia o erro esperado.
- Causa: ausência de política explícita para datetime/time aware.
- Correção: rejeitar tzinfo no prazo e na referência com ValueError orientado.
- Prevenção: fronteiras exatas do prazo, fim do dia e tipos de referência testados.
- Classificação: ambiguidade temporal; R-E2-03 / RN13-RN14.

## E-04 - Filtro inválido ocultava erro de chamada
- Detecção: test_invalid_filter_is_not_silently_an_empty_result.
- Causa: status arbitrário era comparado ao enum e retornava lista vazia.
- Correção: aceitar somente None ou Status.
- Prevenção: manter teste com status inexistente.
- Classificação: contrato insuficiente; R-E2-04 / RN15.

## E-05 - Texto de tipo incorreto causava AttributeError
- Detecção: test_invalid_text_type_uses_domain_error, dois casos: título e descrição.
- Causa: strip era chamado antes de validar o tipo.
- Correção: validar strings antes de normalizar; usar ValueError.
- Prevenção: parametrização dos dois campos.
- Classificação: contrato de erro incompleto; R-E2-05 / RN10.

## E-06 - Atualização removia data mantendo horário sem efeito
- Detecção: test_invalid_update_does_not_change_stored_task.
- Causa: a combinação final de campos não era rejeitada pelo modelo.
- Correção: validar o novo objeto antes da substituição no serviço.
- Prevenção: testar que título e prazo originais permanecem após falha.
- Classificação: refinamento da invariância e atomicidade; R-E2-02 / RN12-RN16.

## E-07 - Casos de uso existiam sem acesso no menu
- Detecção: inspeção técnica da CLI nesta preparação; não foi uma revisão por pares e não deve ser registrada como tal.
- Causa: menu oferecia apenas cadastro e listagem, embora o serviço tivesse consulta, atualização, conclusão e filtro.
- Correção: opções 4-7, mantendo opção 3 para sair.
- Prevenção: teste integrado do menu com TaskService real.
- Classificação: lacuna de integração em relação aos RFs existentes, sem redução de escopo.

Oito testes falharam no diagnóstico de 13 casos; dois deles correspondem aos campos de E-05. E-07 foi identificado por inspeção, não pelo harness inicial. Não há relato inventado de erro encontrado por um colega.
