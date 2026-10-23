# Governança, sprints e experiência - Entrega 2

## Histórico comprovado

- Sprint 1: issues [#1](https://github.com/gustavoaraujocd/tasktrackerr/issues/1), [#2](https://github.com/gustavoaraujocd/tasktrackerr/issues/2) e [#3](https://github.com/gustavoaraujocd/tasktrackerr/issues/3), fechadas, documentam especificação, harness e ambiente.
- [PR #4](https://github.com/gustavoaraujocd/tasktrackerr/pull/4): aprovado por estherbastos em 12/09/2026 22:26 UTC e JON4TH4NRSC às 23:09 UTC; integrado em develop às 23:51 UTC. A aprovação de cauamrad em 13/09 16:10 UTC ocorreu depois da integração e não é apresentada como aprovação prévia.
- [PR #5](https://github.com/gustavoaraujocd/tasktrackerr/pull/5): encerrado sem merge por conflito histórico.
- [PR #6](https://github.com/gustavoaraujocd/tasktrackerr/pull/6): integração recomposta a partir da main; harness inicial de 8 testes.
- [PR #8](https://github.com/gustavoaraujocd/tasktrackerr/pull/8): runtime interativo, testes CLI e Docker; 13 casos.
- [PR #10](https://github.com/gustavoaraujocd/tasktrackerr/pull/10): ajuste de imagem de desenvolvimento por falha de chave GPG; não se afirma homologação final do Codespaces.
- Sprint 2: issues [#14](https://github.com/gustavoaraujocd/tasktrackerr/issues/14) e [#15](https://github.com/gustavoaraujocd/tasktrackerr/issues/15), abertas para aceite de código, documentação e análise ética.
- [PR #16](https://github.com/gustavoaraujocd/tasktrackerr/pull/16): feature/bootcamp3-entrega2 para develop; testes de regressão, integração e relatório desta etapa.

As fases acadêmicas anteriores compartilham o mesmo repositório. Os nomes históricos de PRs e commits são preservados; eles não alteram a identificação desta Entrega 2 do Bootcamp III.

## Estado e critérios de aceite

Na inspeção de 23/10/2026, main e develop estavam sem proteção automática. Não é correto afirmar que o GitHub impede tecnicamente merge sem revisão. A equipe deve configurar proteção se quiser transformar a política em bloqueio obrigatório; esta entrega não altera permissões administrativas.

O PR #16 deve receber revisão real de um integrante diferente do autor. O revisor verifica: RF01–RF08 no menu, contratos RN10–RN16, atualização atômica, 39 testes e CI no SHA atual, comandos Docker, fontes do relatório e ausência de dados indevidos.
Comentários devem ser resolvidos antes do aceite. Alterações relevantes posteriores exigem nova revisão. A promoção para main ocorre via outro PR após a integração em develop.

As aprovações do PR #4 comprovam colaboração histórica, mas não são reutilizadas como homologação do PR #16. Os checklists e issues da Sprint 2 só devem ser encerrados após o aceite real, sem simular participação ou retroagir datas.

## Relato de experiência técnica

Síntese baseada no histórico inspecionado e nas execuções desta preparação; não é entrevista nem depoimento atribuído a cada integrante.

O principal aprendizado foi separar um núcleo testável de uma aplicação acessível: a existência de métodos no serviço não garantia que o usuário pudesse executar todos os casos pelo terminal. A integração do menu tornou esse descompasso visível e verificável.

Outro desafio foi especificar o significado de prazo. A tipagem aparente de Python não impediu datetime em campo date; timestamps com fuso e horários sem data também exigiram uma decisão explícita. Testar casos de borda antes de corrigir produziu evidências mais fortes do que apenas mostrar uma suíte verde.

No versionamento, o conflito histórico entre branches mostrou a importância de preservar conteúdo revisado e registrar como a integração foi recomposta. No ambiente, uma chave de pacote ausente mostrou que empacotar o código não elimina falhas externas. A governança precisa distinguir código testado, infraestrutura preparada e ambiente efetivamente homologado.

O apoio da IA ampliou a capacidade de produzir código, testes e documentação, mas exigiu leitura crítica. A equipe continua responsável por entender os contratos, revisar o que publica e comprovar participação por registros reais. Não há medição que permita afirmar ganho percentual de produtividade.

## Próxima ação humana concreta

Revisar o diff do PR #16, executar os comandos do README e registrar aprovação ou solicitações de ajuste no GitHub com a conta de um colega. Depois, integrar por PR em develop e main e atualizar o estado desta documentação. Este registro descreve o snapshot atual e não antecipa aprovações futuras.

## Complemento após recebimento do guia

O aceite não depende apenas do review. A apostila detalha experimento empírico de IA, marco da sprint, participação dos integrantes, evidências visuais e conferências. Consulte auditoria-guia-e2.md. Não há afirmação de que essas atividades já ocorreram. Líder para submissão: Gustavo Araújo do Carmo.
