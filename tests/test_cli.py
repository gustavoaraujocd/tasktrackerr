"""Verifica o fluxo real do terminal usado na demonstração da Fase 3."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_cli(lines):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [sys.executable, str(ROOT / "src" / "main.py")],
        input="\n".join(lines) + "\n",
        text=True,
        encoding="utf-8",
        capture_output=True,
        cwd=ROOT,
        env=env,
        timeout=10,
    )


def test_empty_list_invalid_option_and_exit():
    result = run_cli(["9", "2", "3"])
    assert result.returncode == 0, result.stderr
    assert "Opção inválida" in result.stdout
    assert "Nenhuma tarefa cadastrada" in result.stdout
    assert "Encerrando o TaskTracker" in result.stdout


def test_registration_recovers_from_invalid_input_and_lists_task():
    result = run_cli([
        "1", "   ", "Entrega final Docker", "Validar container",
        "urgente", "Alta", "31/02/2026", "31/12/2099",
        "25:61", "18:30", "2", "3",
    ])
    assert result.returncode == 0, result.stderr
    for expected in [
        "Este campo é obrigatório", "Prioridade inválida",
        "Data inválida", "Horário inválido", "Tarefa cadastrada com sucesso",
        "Entrega final Docker", "Validar container", "Alta",
        "31/12/2099 às 18:30", "Pendente", "Encerrando o TaskTracker",
    ]:
        assert expected in result.stdout


def test_registration_without_deadline_and_eof():
    result = run_cli(["1", "Sem prazo", "", "Média", "", "2"])
    assert result.returncode == 0, result.stderr
    assert "Sem prazo" in result.stdout
    assert "Não informada" in result.stdout
    assert "Entrada encerrada" in result.stdout
