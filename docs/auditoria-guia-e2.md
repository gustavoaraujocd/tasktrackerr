# Conferência com o guia do professor - 23/10/2026

Fontes fornecidas: Apostila_Bootcamp_III_Entrega_02.pdf (26 páginas), Tutorial_StudyRoom_Bootcamp_III.pdf (21 páginas) e studyroom-api.zip. O ZIP foi lido como exemplo, sem executar código, hooks ou reaproveitar histórico Git do StudyRoom.

## O projeto permanece TaskTracker
O tutorial orienta transpor o método, não copiar o sistema StudyRoom. A completude é determinada pela SPEC do projeto. Não é necessário converter a CLI em API de reservas, adotar FastAPI ou reproduzir os 23 testes do exemplo.

## Preparado no TaskTracker
- RF01-RF08 acessíveis no menu e 39 testes aprovados.
- README, diagrama, oito ADRs e análise ético-técnica.
- ERROS.md com sete entradas reais e rastreabilidade E/RN/testes/PR.
- Registro R-E2-01 a R-E2-05 na especificação.
- DEMO.md com fluxo completo e critérios de observação.
- Logs antes/depois, JUnit e extrato de CI; log integral do job Docker anexado como logs_testes_final.txt.
- Líder identificado: Gustavo Araújo do Carmo, RA 22304113.
- Protocolo de experimento preparado em experimento-ia.md.

## Limitação assumida

O responsável decidiu não realizar o experimento de IA. A comparação permanece documental; esse requisito do guia não foi atendido e não integra mais a lista de atividades a executar.

## Conferência dos itens do guia

| Item | Estado e ação necessária |
|---|---|
| Participação e revisão da equipe (p.11-12) | PR #16 sem aprovação independente confirmada. Não fabricar autores, comentários ou aprovações. Conferir a participação efetiva de todos. |
| Publicação estável (p.3 e 23) | Código E2 está na feature. Integrar via develop e main após aceite. |
| Milestone, fechamento e proteção (p.5-6 e 23) | Issues #14/#15 seguem abertas; milestone da Sprint 2 e proteção de branches não foram configurados nesta preparação. O registro atual não deve afirmar que existem. |
| Evidência visual do harness (p.21) | Concluída: captura autêntica do GitHub Actions, run #29, comando e 39 passed in 0.23s visíveis; incluída no PDF. |
| Versão submetida (p.21-23) | Commit técnico está identificado, mas tag/release de submissão deve ser criada após a homologação final; não marcar versão ainda incompleta como v2.0. |
| Conferência externa e em equipe (p.14, 16 e 22) | Falta confirmar clone limpo por pessoa externa e leitura final do PDF por outro integrante. O relato atual é síntese técnica dos registros, não depoimento coletivo. |
| Termos da ferramenta efetivamente usada (p.19) | Identificar o plano/contrato efetivo para conferir retenção, treinamento e titularidade aplicáveis; a documentação genérica de segurança não prova as condições da conta. |

A apostila acrescenta detalhamento que não estava explícito no enunciado anterior. A captura do harness foi concluída. Permanecem os itens de governança e conferência acima. O experimento foi retirado da lista por decisão do responsável; o requisito de comparação empírica não foi atendido e a matriz permanece documental.

## Histórico e autenticidade
Os números de reservas e resultados do StudyRoom são ilustrativos ou relativos àquele exemplo. Não pertencem ao TaskTracker. Nenhuma reunião, função dos colegas, execução de outra IA ou revisão por pares deve ser inventada para preencher o checklist.
