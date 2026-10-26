# TaskTracker | Release e bloqueios da Entrega 3
## Situação em 26/10/2026
Candidata 1.0.0rc1 preparada na branch feature/entrega3-final a partir de develop b54839d. Main permanece c946e5781f935f87b51b54c4f0ce56503dae69b3 no levantamento inicial. Não foi criada tag ou release v1.0.0. O pacote é uma entrega técnica candidata, com pendências de homologação e publicação explicitadas.
## Proteções verificadas
Ruleset 25727805 ativo em main/develop, sem bypass, uma aprovação independente, aprovação do último push, conversas resolvidas, checks test e docker e base atualizada. PR #17 aberto, zero APPROVED e três conversas de revisão abertas na consulta. A revisão COMMENTED do bot não é aprovação humana. As aprovações anteriores do PR #16 não se transferem.
O responsável informa que pedidos de revisão a Esther/Cauã falharam por colaboradores não habilitados. Não foram repetidos nem inventadas aprovações. É preciso que um mantenedor habilite revisores/que aceitem acesso e que um colega revise o último push. Não alterar o ruleset para contornar a condição.
## Artefatos preparados
SDD As-Built, refinamento RN17/RN18, correções de apresentação, suíte com 41 aprovados e cobertura, Docker/Compose/CI, README, retrospectiva técnica e roteiro de demonstração. PDFs e ZIP identificam candidatura, sem afirmar produto homologado.
## Sequência restante
1. Revisar e integrar PR feature/entrega3-final -> develop com checks test/docker verdes e aprovação independente. Corrigir achados, se houver.
2. O PR #17 develop -> main incorporará as mudanças; conferir diff, base, CI, resolver conversas e obter aprovação no head final. Aprovações antigas podem ser descartadas pelo ruleset.
3. Antes da release estável, atualizar version de 1.0.0rc1 para 1.0.0 por PR no mesmo fluxo, executar novamente testes/coverage e validar o commit que efetivamente chegar à main.
4. Somente após main conter o código aprovado: criar tag v1.0.0 no commit final, publicar release com notas e artefatos gerados desse mesmo commit. Confirmar que não restam PRs da entrega pendentes e que a tag coincide com main. Se a tag já existir, verificar antes de criar ou substituir; nunca mover tag publicada silenciosamente.
5. Gravar vídeo real e publicar link verificável. Atualizar README/submissão. Roteiro, log ou CI não substituem o vídeo.
## Notas de release preparadas
TaskTracker 1.0.0 (proposta, não publicada): CLI com cadastro, listagem, consulta, atualização atômica, conclusão, filtro e alertas. Contratos de data/hora explicitados, mensagens de filtro corrigidas e alertas sem duplicação de listagem. Runtime não root, serviço de testes e exportação de cobertura. Limites: memória volátil, monousuário e prazos civis locais.
As métricas da candidata não devem ser reaproveitadas como evidência do commit final se código/configuração mudarem.
## Materiais e origem
Inspecionados o clone GitHub atual, documentos e evidências E1/E2 do repositório, pacotes TaskTracker_Entrega_Final e Bootcamp III locais, o guia anterior Guia_Fase3_TaskTracker.pdf e o rascunho AVA que declara ausência de vídeo. Esses materiais são históricos e não demonstram a Entrega 3 concluída.
A conversa referenciada só estava disponível em prévia; read_thread não está disponível nesta sessão. Nenhum arquivo anexado exclusivo dessa conversa foi presumido lido. O enunciado visível fornecido pelo responsável orientou a preparação. A formatação de vídeo do guia anterior é sugestão e exige conferência com a regra específica atual.
