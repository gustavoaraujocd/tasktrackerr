# Protocolo de comparação empírica de IA - A EXECUTAR

O guia do professor pede resultados próprios. A matriz documental em analise-ia-e2.md não conclui esse requisito. Nenhuma taxa, custo ou intervenção abaixo foi medida ainda.

## Desenho preferido
Usar Codex e uma segunda ferramenta à qual a equipe tenha acesso, verificando previamente as condições de uso. Não é necessário adquirir assinatura para esta tarefa.

Se o acesso a outra ferramenta for inviável, a apostila admite duas configurações da mesma ferramenta. Nesse caso, registrar a indisponibilidade e comparar Codex com e sem AGENTS.md. Não apresentar isso como comparação entre fabricantes.

## Insumo fixo
- Base: 2e1d12ef0e52e12088cf1fcebcdc50b42c4370e0, commit da regressão antes da correção, identificado no PR #16 como "test: especifica regressões de prazo e validação (#14)".
- SPEC: docs/especificacao-sdd.md desse commit.
- Tarefa: ajustar validação de data, horário, fuso, texto e filtro conforme RN10-RN16.
- Harness congelado: tests/test_refinements.py e suíte original desse commit.
- Não carregar a conversa atual nem oferecer a solução corrigida. Usar sessões novas e cópias independentes da mesma base.
- Anotar ferramenta, interface, versão/modelo visível, plano utilizado e data. Se um dado não estiver disponível, registrar "não informado".

## Prompt comum
> Implemente os contratos RN10-RN16 da especificação do TaskTracker, alterando somente models.py e service.py. Preserve a API pública e os testes existentes. Não crie funcionalidades extras. Ao terminar a primeira proposta, pare antes de corrigir falhas do harness; a pessoa responsável executará os testes e registrará esse primeiro resultado.

## Condições e execução
1. Criar duas cópias limpas da mesma base, fora de pastas que injetem outros arquivos de contexto.
2. Com duas ferramentas, fornecer o mesmo contexto, adaptado ao formato de cada uma.
3. No desenho alternativo A/B, A recebe AGENTS.md e B não recebe esse arquivo; a SPEC e o prompt permanecem idênticos. Registrar a configuração efetiva: remover só um arquivo não elimina regras globais ou memória da sessão.
4. Guardar prompt e saída da primeira proposta; executar pytest sem alterar testes e registrar aprovados/total.
5. Continuar a correção e contar as intervenções humanas adicionais (cada mensagem com instrução corretiva é uma intervenção; não contar o prompt inicial).
6. Conferir arquitetura, alterações fora do escopo e respeito aos contratos. Guardar diff, logs e identificação das sessões.
7. Publicar em branches exp/* separadas, sem merge do código experimental no produto.
8. Uma rodada por condição é observação limitada, sem inferência de superioridade estatística ou causal.

## Matriz a preencher com evidência

| Critério | Condição A | Condição B |
|---|---|---|
| Ferramenta/interface/modelo/plano | Não executado | Não executado |
| Configuração e contexto efetivos | Não executado | Não executado |
| Testes aprovados na primeira proposta / total | Não medido | Não medido |
| Intervenções humanas até aprovação | Não medido | Não medido |
| Arquitetura e escopo respeitados | Não avaliado | Não avaliado |
| Ambiguidades da SPEC detectadas | Não observado | Não observado |
| Limitação concreta observada | Não observado | Não observado |
| Links de sessões/diffs/logs | Pendente | Pendente |

Depois do experimento: substituir os campos pelos fatos, preservar resultados negativos, explicar limites e atualizar a síntese e o PDF. Não reutilizar as 8 falhas do diagnóstico como se fossem resultados das duas condições: elas foram produzidas por outro procedimento.
