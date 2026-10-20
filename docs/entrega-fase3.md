# TaskTracker - Entrega final do Bootcamp II

## Identificação

- Estudante: Gustavo Araújo do Carmo
- RA: 22304113
- Curso: Análise e Desenvolvimento de Sistemas (ADS)
- Unidade/Turma: Taguatinga - Noturno

## Repositório

https://github.com/gustavoaraujocd/tasktrackerr

## Projeto

Aplicação de gerenciamento de tarefas por linha de comando em Python.
Permite cadastrar e listar tarefas, com validações de título, prioridade,
data e horário. Os registros são mantidos na memória durante a execução.

## Artefatos disponibilizados

- Código Python em `src/`.
- Testes automatizados em `tests/`.
- `Dockerfile` para construção da imagem e execução da CLI.
- `docker-compose.yml` com terminal interativo e serviço separado de testes.
- `README.md` com instalação, execução e comandos Docker.
- Planejamento e especificação em `docs/`.
- [PDF de identificação e acesso ao projeto](entrega-final.pdf).

## Validação técnica

A suíte contém 13 testes: 11 do domínio e 2 da CLI.
O GitHub Actions validou os testes em Python, a construção da imagem,
a execução do menu e a suíte dentro de um contêiner.

[Consultar as execuções do GitHub Actions](https://github.com/gustavoaraujocd/tasktrackerr/actions)

O PDF de planejamento é uma exportação identificada do Markdown já versionado
no repositório, preservando sua origem.
