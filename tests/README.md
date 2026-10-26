# Harness automatizado
Execute `python -m pytest -q --cov --cov-report=term-missing --cov-report=html`.
Domínio: test_service.py e test_refinements.py. Processo real da CLI: test_cli.py.
Integração do menu, atualização atômica e regressões do PR #17: test_cli_workflows.py.
Cobertura mede src inteiro, incluindo a CLI. Limite combinado de linhas e ramos: 90%.
Resultados da Entrega 3: docs/relatorio-testes-e3.md. Evidências E2 são históricas.
