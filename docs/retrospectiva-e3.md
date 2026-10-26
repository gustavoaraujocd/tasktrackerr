# TaskTracker | Retrospectiva da Entrega 3
## Natureza do registro
Síntese técnica baseada em código, documentos e histórico visíveis em 26/10/2026. Não representa reunião realizada, depoimento da equipe, aprovação humana ou pesquisa de satisfação.
## Evolução e decisões
A base acadêmica evoluiu para uma CLI com sete opções, domínio isolado e testes de refinamento. Memória e interface local mantiveram execução simples e escopo verificável. Em troca, não há continuidade dos dados ou colaboração entre usuários.
A Entrega 2 registrou refinamento de contratos por falhas reproduzidas: data/hora sem ambiguidade, erro de tipo orientado e atualização atômica. A Entrega 3 fecha documentação As-Built, cobertura do src inteiro, comandos de execução e empacotamento rastreável.
## O que funcionou
Especificar invariantes antes de alterar o domínio permitiu testar fronteiras do prazo e manter identidade. Testes de integração do menu verificam o serviço real; testes subprocess verificam entrada/saída e encerramento. Checks separados de Python e Docker mostram problemas em ambientes distintos.
A proteção ativa evita tratar revisão automática ou aprovações de PRs antigos como homologação da entrega atual.
## Problemas observados e resposta
O PR #17 mostrou que funções reutilizadas de apresentação ainda confundiam filtro vazio com cadastro vazio e repetiam alertas. Foram refinadas RN17/RN18 e adicionadas regressões. README também apontava para uma branch antiga; foi corrigido com caminho de distribuição e explicação da candidata.
A ausência de colaboradores habilitados impediu pedidos de revisão anteriores (relato recebido). A ação organizacional restante é habilitar/aceitar acesso de revisores e obter revisão independente do último push. Desativar regras não é parte da solução.
Docker não está instalado no ambiente local desta execução. O CI deve executar build, smoke e suíte em contêiner antes da integração. Vídeo real ainda precisa ser gravado pelo responsável.
## Uso de IA e responsabilidade
Codex foi empregado na inspeção, documentação, código e automação, com contexto histórico do ChatGPT. Afirmações são restritas aos logs e consultas disponíveis. Não houve benchmark empírico com Claude Code, Cursor ou Antigravity; a comparação documental anterior não atende um experimento medido.
A revisão automática apoia a qualidade; não substitui validação humana, aprovação de PR, reunião ou demonstração funcional gravada. Nenhuma fala ou participação foi atribuída aos colegas.
## Ações de encerramento e próximo ciclo
1. Revisores habilitados: revisar a candidata, resolver conversas e aprovar o último push; responsabilidade de mantenedor/revisor humano.
2. Integrar feature em develop e develop em main, com test/docker verdes no SHA atual; responsabilidade do mantenedor, conforme regras.
3. Após aceite, normalizar versão para 1.0.0 em PR revisado, testar o commit final, criar tag/release e anexar pacote correspondente à main.
4. Responsável pela apresentação: gravar demonstração real, publicar link acessível e registrar no README/material de submissão.
5. Para evolução: decidir persistência e contratos de mutabilidade antes de novos recursos; documentar fuso/configuração e fixação completa de dependências conforme necessidade.
