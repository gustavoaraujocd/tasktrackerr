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

Na inspeção inicial de 23/10/2026, main e develop estavam sem proteção automática. Durante esta preparação, o líder confirmou a autenticação do GitHub e foi ativado o ruleset 25727805 para ambas. Agora são exigidos PR, uma aprovação independente, aprovação do último push, resolução de conversas e checks test/docker do GitHub Actions, com base atualizada. Aprovações antigas são descartadas quando o diff muda. Force push e exclusão são bloqueados; não há atores com bypass.

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

## Preparação de fechamento confirmada

- [Proteção ativa - ruleset 25727805](https://github.com/gustavoaraujocd/tasktrackerr/rules/25727805).
- [Milestone Sprint 2 - Entrega 2](https://github.com/gustavoaraujocd/tasktrackerr/milestone/1), criado em 23/10/2026, reunindo #14, #15 e PR #16. Continua aberto; não representa sprint já encerrada.
- Convites de colaboração com escrita enviados, a pedido do líder, para estherbastos, JON4TH4NRSC e cauamrad. Todos estavam pendentes no momento da conferência. Matheus e Rillary ficaram para depois por decisão do responsável.
- O PR #16 permanece sem aprovação humana confirmada e bloqueado pela regra. Revisão automatizada do bot em commit anterior não é aceite de colega.
- Sem merge em develop/main, sem fechamento de issues e sem tag de entrega antes do aceite.
- [Registro verificável da configuração](evidencias/governanca.json).

## Participação observada e limites da evidência

| Integrante | Registro localizado | Estado desta etapa |
|---|---|---|
| Gustavo Araújo do Carmo | Autor dos PRs consultados e dos commits do PR #16 | Líder e autor da preparação; não pode aprovar o próprio PR |
| Esther Diniz Bastos / estherbastos | Aprovação histórica no PR #4 antes do merge | Convite de colaboração pendente; sem revisão do PR #16 |
| Jonathan Rodrigues Silva Corrêa / JON4TH4NRSC | Aprovação histórica no PR #4 antes do merge | Convite de colaboração pendente; sem revisão do PR #16 |
| Cauã Gonçalves Xavier Mrad / cauamrad | Aprovação histórica no PR #4 após o merge | Convite de colaboração pendente; sem revisão do PR #16 |
| Matheus Couto Nogueira | Nenhuma conta confirmada nesta preparação | Convite adiado; participação não demonstrada pelos registros consultados |
| Rillary Lorranne de Souza Portilho | Nenhuma conta confirmada nesta preparação | Convite adiado; participação não demonstrada pelos registros consultados |

A consulta encontrou 64 commits na história retornada da main, todos associados à conta gustavoaraujocd, e todos os PRs retornados também estavam nessa conta. Isso descreve o histórico consultado; não prova ausência de contribuições fora do GitHub. O critério de todos aparecerem como autores e revisores na sprint ainda não foi demonstrado. Convidar agora não recria participação histórica.

## Sequência após a revisão real

1. Um convidado aceita o acesso e revisa o SHA final do PR #16 com comentário substantivo e aprovação, ou solicita correções.
2. Com CI e critérios de aceite satisfeitos, integrar o PR #16 em develop.
3. Abrir PR de develop para main, conferir CI e obter o aceite exigido pela proteção.
4. Integrar em main, validar o resultado, fechar as issues com registro do aceite e concluir o milestone.
5. Atualizar o PDF com os links e SHAs finais e marcar a versão submetida com tag/release. Não marcar v2.0 antecipadamente.

A autorização do líder permite preparar e executar essa sequência após o aceite; não substitui a revisão independente exigida.
