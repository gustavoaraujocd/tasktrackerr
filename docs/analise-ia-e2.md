# Análise comparativa e ético-técnica de agentes de IA

Bootcamp III - Entrega 2 | TaskTracker | 23/10/2026.

## Método e limites da comparação

Uso comprovado neste projeto: Codex, com apoio do ChatGPT na organização técnica. O responsável confirmou que não utilizou Claude Code, Cursor ou Antigravity. A matriz abaixo é uma avaliação documental de capacidades e adequação ao fluxo; não é experimento controlado, ranking de qualidade ou medição de produtividade. Não foram medidos tempo economizado, custo, taxa de acerto ou comparação entre modelos. A interface Codex utilizada no trabalho é a aplicação integrada; não se afirma que todos os comandos foram executados especificamente pelo produto Codex CLI.

As fontes dos fabricantes foram consultadas em 23/10/2026. Suas afirmações descrevem recursos, não uma auditoria independente de segurança. A configuração efetiva varia por versão, sistema operacional, plano e política da organização.

## Matriz comparativa

| Ferramenta / evidência | Pontos fortes relevantes | Limitações e riscos | Impacto no TaskTracker |
|---|---|---|---|
| Codex / Codex CLI - uso real do ecossistema Codex; CLI analisada documentalmente | Pode editar arquivos e executar testes; separa sandbox de política de aprovação. Adequado para ciclos especificar, alterar, testar e inspecionar diff. [S1] | A geração pode manter premissas erradas. Permissões amplas, rede e conectores precisam de controle. Harness verde não significa contrato completo. | Apoio verificável à CLI, harness, Docker, README e refinamentos. A suíte cresceu de 8 casos registrados na Entrega 1 para 39 no snapshot E2; esse aumento é evidência de cobertura de cenários, não prova causal de superioridade da IA. |
| Claude Code - apenas documentação | Arquitetura de permissões e sandbox para comandos; políticas permitem ajustar o nível de autonomia. [S2] | Aprovação de comando e isolamento do SO são camadas diferentes. Saídas continuam exigindo revisão; não há qualidade local medida. | Poderia executar o mesmo fluxo SDD e testar mudanças. O impacto real neste código não foi avaliado. |
| Cursor - apenas documentação | Ferramentas de leitura, edição e terminal integradas; revisão pode ser associada ao contexto do código. [S3] | A documentação alerta que alterações podem executar por auto-reload e que guardrails são melhores esforços. Edição salva em disco exige versionamento e revisão. | Potencial para revisão contextual das regras; nenhum resultado experimental ou ganho de qualidade é atribuído ao projeto. |
| Antigravity - apenas documentação | Permissões Deny/Ask/Allow e mecanismos para revisar mudanças e comentar diffs. [S4, S5] | A autonomia e o isolamento dependem do preset. Permissões amplas aumentam exposição; capacidade de apresentar artefatos não prova correção. | Poderia tornar planos e alterações inspecionáveis. Nenhuma execução comparativa foi feita neste repositório. |

A decisão de continuar com Codex se apoia no histórico e contexto já disponíveis. Para comparar desempenho no futuro: usar a mesma especificação e base imutável, os mesmos casos de teste independentes, registrar versões, tempo humano de revisão, falhas introduzidas e custo. Variar apenas a ferramenta, repetir execuções e publicar resultados negativos também.

## Alucinação e confiança indevida

Uma IA pode inventar métodos de bibliotecas, formatos de API, resultados de testes, aprovações ou requisitos. Código sintaticamente válido também pode ser logicamente errado. Neste projeto, a aceitação de datetime como date e o horário sem data demonstraram como uma implementação plausível pode contrariar o contrato. Não há evidência suficiente para atribuir a autoria de cada defeito exclusivamente à IA.

O controle adotado é transformar a alegação em cenário verificável: entrada, saída ou erro esperado e invariante. O teste deve expressar a regra de negócio e falhar na implementação defeituosa. Na E2, os novos contratos produziram 8 falhas antes dos ajustes. Preservar a suíte original evita substituir testes incômodos por outros que só confirmem o código novo. O revisor humano precisa conferir o oráculo, porque agente e testes podem compartilhar o mesmo erro.

## Código inseguro, comandos destrutivos e prompt injection

O risco do agente excede o texto que ele gera: comandos podem apagar arquivos, expor tokens, alterar permissões ou instalar dependências maliciosas. Um README ou log de terceiro pode conter instruções maliciosas para executar comandos ou enviar arquivos. Esse conteúdo é dado de análise, não autorização para mudar o objetivo da tarefa.

Para o TaskTracker: trabalhar em branch, inspecionar diffs, limitar escrita ao workspace, reduzir rede e evitar credenciais de produção. Comandos irreversíveis precisam de revisão explícita do alvo e do efeito. Não desabilitar verificações de assinatura para contornar falhas de instalação. O episódio documentado de chave GPG ausente no Codespaces foi tratado pela troca da imagem de desenvolvimento, sem desativar a validação; o rebuild completo não foi homologado após o cancelamento do ambiente.

O runtime E2 usa UID 10001; o CI tem contents:read e tempo limite. Esses controles reduzem privilégio e exposição, mas não tornam Docker uma fronteira absoluta. Dependências e imagens sem pinagem integral continuam sendo risco de cadeia de suprimentos. Não se executou pentest ou auditoria de dependências nesta entrega.

## Privacidade e confidencialidade

Prompts, arquivos selecionados, diffs e logs podem conter dados pessoais, segredos ou propriedade de terceiros. Rodar comandos localmente não implica que o contexto enviado a um serviço de IA permaneça local. Políticas de retenção, treinamento e subprocessadores precisam ser verificadas no contrato e nas configurações vigentes; não se presume sigilo só porque o repositório é privado.

Como prática do projeto: utilizar tarefas fictícias, selecionar apenas os arquivos necessários, remover tokens de logs e não inserir .env, chaves privadas, credenciais ou dados de clientes em prompts e commits. Nomes e RAs são dados de identificação exigidos pela atividade; o relatório não adiciona contatos, documentos ou credenciais. Os textos livres de tarefas podem conter dados sensíveis: isso deve ser evitado mesmo com armazenamento apenas em memória.

Se houver exposição, interromper o compartilhamento, revogar o segredo, avaliar os acessos e tratar o incidente com o responsável; apagar um commit recente não revoga uma credencial nem elimina cópias. O princípio de necessidade e as medidas de segurança da LGPD são referências para minimizar exposição. [S6] Esta análise não certifica conformidade jurídica ou contratual.

## Propriedade intelectual e direitos autorais

Código gerado não deve ser tratado como automaticamente original, livre de restrições ou de titularidade garantida. É necessário separar as contribuições humanas, saídas do modelo, bibliotecas e trechos de terceiros. Verificar semelhanças relevantes, origem, licenças e avisos; manter atribuições de dependências e decisões sobre reutilização.

O INPI referencia a Lei de Software e a Lei de Direitos Autorais para a proteção de programas no Brasil. [S7] A discussão do U.S. Copyright Office sobre autoria e IA é referência comparativa estrangeira, não regra brasileira aplicada automaticamente. [S8] Não se atribui titularidade jurídica conclusiva à ferramenta ou à equipe sem análise da origem e dos contratos.

Não há LICENSE explícita na árvore inspecionada. Um repositório público permite consulta, mas a publicidade, por si, não demonstra autorização irrestrita para redistribuir ou comercializar o código. A equipe precisa deliberar uma licença compatível com todas as contribuições; o agente não escolhe uma em nome dos demais titulares.

## Homologação humana obrigatória no SDD

1. Responsável humano confirma o problema, o escopo e os contratos.
2. Agente propõe implementação vinculada à issue e à especificação.
3. Harness e inspeção verificam cenários normais, bordas e regressões.
4. Revisor independente lê o diff, executa testes e verifica segurança e fontes.
5. Equipe aprova o comportamento e os trade-offs, resolve observações e registra decisão no PR.
6. Merge em develop e depois em main exige novo aceite compatível com o SHA integrado.

AGENTS.md é orientação textual; sandbox e permissões são controles técnicos distintos. IA não pode emitir a aprovação de um colega, fabricar colaboração ou converter resultado de teste em homologação de produto. No snapshot E2 o PR #16 está aberto, sem aprovação humana independente confirmada. A condição será atendida somente com revisão real, mantendo a rastreabilidade.

## Critério de responsabilidade

A gestão de riscos proposta é contínua: definir responsáveis, mapear os dados e ações expostos, medir por testes e inspeção e tratar riscos residuais. Essa organização se alinha às funções Govern, Map, Measure e Manage do NIST AI RMF. [S9] Na prática, o critério é conseguir explicar uma mudança sem depender da autoridade do modelo e reproduzir a evidência que a sustenta.

## Fontes oficiais

- [S1 - OpenAI: Agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security).
- [S2 - Anthropic: Claude Code Security](https://code.claude.com/docs/en/security).
- [S3 - Cursor: Agent Security](https://cursor.com/docs/agent/security).
- [S4 - Google: Antigravity Permissions](https://antigravity.google/docs/permissions/).
- [S5 - Google: Review changes](https://antigravity.google/docs/ide/review-changes-editor/).
- [S6 - Brasil: Lei 13.709/2018 (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).
- [S7 - INPI: legislação sobre programas de computador](https://www.gov.br/inpi/pt-br/servicos/programas-de-computador/legislacao-programa-de-computador).
- [S8 - U.S. Copyright Office: Copyright and Artificial Intelligence](https://www.copyright.gov/ai/).
- [S9 - NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Consulta documental: 23/10/2026. Recursos e políticas dos produtos podem mudar.
