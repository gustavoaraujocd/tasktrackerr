# Relatório de execução dos testes - Entrega 2

Snapshot: 23/10/2026. Base: c946e57. Revisão técnica: 984ed48daad1fd83ca9c0b7727b67e843adf5301.

## Resultado consolidado

| Grupo | Casos | Resultado |
|---|---|---|
| Domínio inicial - test_service.py | 11 | Aprovados |
| Regressões E2 - test_refinements.py | 15 | Aprovados |
| CLI em subprocesso - test_cli.py | 3 | Aprovados |
| Menu integrado - test_cli_workflows.py | 10 | Aprovados |
| Total coletado | 39 | 39 aprovados; 0 falhas; 0 erros; 0 ignorados |

Passagem: 39/39 = 100%. Não se mediu cobertura de linhas ou ramos. Passagem integral não significa ausência de defeitos, auditoria de segurança ou homologação de produto.

## Ambiente e comandos

Execução local: Windows, Python 3.12.14, pytest 9.1.1. A saída final registrou 39 passed in 1.84s; duração é informativa e varia entre ambientes.

```bash
python -m pip install -e ".[dev]"
python -m pytest -q --junitxml=test-results.xml
docker compose build tests
docker compose run --rm tests
```

O Docker foi validado no GitHub Actions em Linux, com job Python 3.11 e job Docker separados. Não foi executado Docker neste Windows.

## Ciclo antes e depois

A suíte de novos contratos, aplicada à base anterior, registrou 8 failed, 5 passed in 1.36s. Após as correções e a ampliação da integração, a suíte completa registrou 39 passed. Não são os mesmos denominadores: o primeiro resultado corresponde a 13 casos de diagnóstico; o segundo inclui os 39 casos finais.

Os resultados locais estão em docs/evidencias/antes.log, depois.log e depois.xml. O hostname foi removido da cópia pública do JUnit; resultados e casos foram preservados.

## Evidência automatizada

GitHub Actions run #27 (39957156921), head 984ed48: jobs test e docker concluídos com sucesso. O checkout executado foi o merge ref 832c6ecf9f0b546984b58039311707f292ba206d, combinando esta revisão com develop. Python 3.11.17: 39 passed in 0.20s. Contêiner: 39 passed in 0.50s. O smoke test também verificou UID 10001 e o menu. Trechos reais estão em docs/evidencias/ci-resumo.log.

[Execução do CI](https://github.com/gustavoaraujocd/tasktrackerr/actions/runs/39957156921).
O artefato pytest-results contém o JUnit do job Python. O job Docker valida Compose, build, UID 10001, menu na imagem runtime e suíte em contêiner.

Limites: testes não cobrem concorrência, durabilidade, integração multiusuário ou calendários entre fusos, capacidades que não fazem parte da solução local especificada.
