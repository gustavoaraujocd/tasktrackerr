#!/usr/bin/env bash
set -euo pipefail
python -m pip install -e '.[dev]'
python -m pytest -q
docker compose config --quiet
docker build -t tasktracker:phase3 .
docker compose build tests
docker compose run --rm -T tests
saida=$(printf '2\n3\n' | docker run --rm -i tasktracker:phase3)
printf '%s\n' "$saida"
grep -q 'Nenhuma tarefa cadastrada' <<< "$saida"
grep -q 'Encerrando o TaskTracker' <<< "$saida"
printf '\nPreparacao concluida. Execute: docker compose run --rm tasktracker-app\n'
