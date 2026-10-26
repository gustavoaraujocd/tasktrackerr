# TaskTracker | Testes e cobertura E3
## Execução observada em 26/10/2026
41 testes aprovados, 0 falhas, 0 erros e 0 ignorados: 100% de passagem dos testes coletados. Tempo reportado pelo pytest: 18,85 segundos. Python 3.12.14, Windows, pytest 8.3.5, pytest-cov 6.1.1 e coverage 7.17.0, em ambiente virtual novo.
Base develop b54839dba345e164e2cfcd8473627a9af96e9733 com alterações E3. A identidade dos arquivos exercitados está em evidencias/e3/tested-files-sha256.json. O commit da candidata será acessível no PR; os hashes permitem verificar o código sem inserir um SHA circular em seu próprio commit.
## Método e comando
python -m pytest -q --cov --cov-report=term-missing --cov-report=json:coverage.json --cov-report=xml:coverage.xml --cov-report=html:htmlcov --junitxml=junit.xml
Os destinos usados na execução local foram work/coverage.json, work/coverage.xml, work/htmlcov e work/junit.xml, a partir da raiz da candidata. O log integral está em evidencias/e3/pytest.log; JUnit e relatórios são cópias dessa execução. A configuração em pyproject mede todo src com branch=true, sem omitir CLI ou módulos críticos; gate de 90% combinado. pytest-cov também acompanha os subprocessos dos testes da CLI.
## Métricas
Total: 244/245 linhas (99.59%); 67/68 ramos (98.53%); cobertura combinada 99.36%.
src/main.py: 156/157 linhas; 41/42 ramos; combinado 98.99%.
src/tasktracker/__init__.py: 3/3 linhas; 0/0 ramos; combinado 100.00%.
src/tasktracker/models.py: 51/51 linhas; 22/22 ramos; combinado 100.00%.
src/tasktracker/service.py: 34/34 linhas; 4/4 ramos; combinado 100.00%.
Lacuna observada: retorno None da leitura de horário vazio em src/main.py:55 e seu ramo correspondente. Nenhuma exclusão artificial foi adicionada para elevar métricas. Cobertura de 100% nos módulos do domínio não prova ausência de defeitos.
## Escopo dos testes
Domínio: criação, título, prioridade, data/hora, identidade, atualização, filtro e atraso. Refinamentos: texto inválido, datetime como data, referência aware, prazo exato, hora sem data e atualização atômica. CLI: subprocesso real com entrada inválida, cadastro/listagem, EOF; integração com consulta, update, conclusão, filtro, limpeza e recuperação de erros.
Novas regressões do PR #17: filtro sem correspondências preserva cadastro e informa mensagem específica; listagem não duplica alertas por ciclo. Suíte anterior: 39; candidata E3: 41.
## Docker, CI e homologação
Docker não está instalado localmente; não houve build ou execução local em contêiner nesta sessão. O workflow mantém build runtime, UID não root, smoke de listagem/saída e suíte em contêiner, além de Compose config. O novo serviço coverage exporta XML/HTML/JUnit para reports/.
A CI do PR #17 na base b54839d passou em test e docker (run 40261694716), mas isso é evidência da base, não desta alteração. A validação da candidata deve ser consultada no PR de Entrega 3 e no arquivo CI-e3.json do pacote quando disponível. A aprovação humana e o vídeo não foram realizados nesta execução.
## Limites e repetição
Não foram executados testes de carga, fuzzing, persistência ou múltiplos usuários; esses recursos não pertencem ao produto. Não há promessa de cobertura integral do espaço de entradas ou de ambiente Docker local. Para repetir com contêiner: docker compose run --build --rm -T tests. Para exportar cobertura: docker compose run --build --rm -T coverage.
