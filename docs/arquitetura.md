# Arquitetura Planejada — TaskTracker

## Organização prevista

```text
tasktrackerr/
├── README.md
├── .gitignore
├── docs/
│   ├── planejamento-logico.md
│   ├── requisitos.md
│   ├── algoritmo.md
│   └── arquitetura.md
├── src/
│   └── README.md
├── tests/
│   └── README.md
└── data/
    └── .gitkeep
```

## Responsabilidade das pastas

- `docs/`: documentação de requisitos, lógica e arquitetura.
- `src/`: futura implementação em Python.
- `tests/`: futuros testes automatizados e manuais.
- `data/`: arquivos de dados usados pelo sistema em fases posteriores.

## Estratégia Git/GitHub

- `main`: versão estável e documentada.
- `develop`: linha de desenvolvimento para próximas etapas.
- branches futuras de funcionalidade poderão seguir o padrão `feature/nome-da-funcionalidade`.

## Estratégia de commits

Os commits devem ser pequenos e descritivos, por exemplo:

- `docs: adiciona planejamento lógico`
- `docs: adiciona requisitos do sistema`
- `feat: implementa cadastro de tarefas`
- `test: adiciona testes de validação`

## Evolução prevista

Na próxima fase, a documentação servirá de guia para transformar o algoritmo em Python. Em fase posterior, o projeto poderá ser containerizado com Docker conforme o cronograma do Bootcamp.
