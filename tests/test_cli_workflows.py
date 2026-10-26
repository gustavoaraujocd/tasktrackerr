"""Integração do menu com serviço real, entrada simulada e saída capturada."""
from datetime import date, time
import importlib.util
from pathlib import Path

import pytest

from tasktracker import Status, TaskService


def run_menu(monkeypatch, service, values):
    spec = importlib.util.spec_from_file_location("tasktracker_cli", Path(__file__).resolve().parents[1] / "src/main.py")
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    monkeypatch.setattr(cli, "TaskService", lambda: service)
    stream = iter(values)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(stream))
    cli.main()


def test_consult_update_complete_and_filter(monkeypatch, capsys):
    service = TaskService()
    task = service.create("Original")
    run_menu(monkeypatch, service, [
        "4", task.id, "5", task.id, "Atualizada", "Descrição", "Alta",
        "31/12/2099", "18:30", "em_andamento", "6", task.id,
        "7", "inexistente", "concluida", "3",
    ])
    output = capsys.readouterr().out
    assert "Tarefa atualizada" in output and "Tarefa concluída" in output
    assert "Status inválido" in output and "Atualizada" in output
    updated = service.get(task.id)
    assert updated.status is Status.DONE
    assert updated.due_date == date(2099, 12, 31)


def test_unknown_id_does_not_end_menu(monkeypatch, capsys):
    run_menu(monkeypatch, TaskService(), ["4", "missing", "6", "missing", "2", "3"])
    output = capsys.readouterr().out
    assert output.count("Tarefa não encontrada") == 2
    assert "Nenhuma tarefa" in output and "Encerrando" in output


@pytest.mark.parametrize("invalid", ["priority", "date", "time", "status"])
def test_invalid_edit_is_atomic_and_menu_recovers(monkeypatch, capsys, invalid):
    service = TaskService()
    task = service.create("Original")
    # O menu aborta o formulário no primeiro campo inválido.
    values = ["5", task.id, "Outra", "Desc"]
    fields = {"priority": ["urgente"], "date": ["Alta", "31/02/2026"],
              "time": ["Alta", "31/12/2099", "25:61"],
              "status": ["Alta", "31/12/2099", "18:00", "inexistente"]}
    run_menu(monkeypatch, service, values + fields[invalid] + ["3"])
    assert service.get(task.id).title == "Original"
    assert "[ERRO]" in capsys.readouterr().out


def test_clear_deadline_and_description(monkeypatch):
    service = TaskService()
    task = service.create("Original", description="Desc", due_date=date(2099, 12, 31), due_time=time(10))
    run_menu(monkeypatch, service, ["5", task.id, "", "-", "", "-", "-", "", "3"])
    updated = service.get(task.id)
    assert updated.description == "" and updated.due_date is None and updated.due_time is None


def test_eof_closes_cleanly(monkeypatch, capsys):
    def end_input(prompt=""):
        raise EOFError
    monkeypatch.setattr("builtins.input", end_input)
    spec = importlib.util.spec_from_file_location("cli_eof", Path(__file__).resolve().parents[1] / "src/main.py")
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    cli.main()
    assert "Entrada encerrada" in capsys.readouterr().out


def test_blank_edit_keeps_fields(monkeypatch):
    service = TaskService()
    task = service.create("Original", description="Desc")
    run_menu(monkeypatch, service, ["5", task.id, "", "", "", "", "", "", "3"])
    assert service.get(task.id).title == "Original"
    assert service.get(task.id).description == "Desc"


def test_removing_only_date_is_rejected_in_menu(monkeypatch, capsys):
    service = TaskService()
    task = service.create("Original", due_date=date(2099, 12, 31), due_time=time(10))
    run_menu(monkeypatch, service, ["5", task.id, "Outra", "", "", "-", "", "", "3"])
    assert service.get(task.id).title == "Original"
    assert "exige uma data" in capsys.readouterr().out


def test_empty_filter_does_not_claim_tracker_is_empty(monkeypatch, capsys):
    service = TaskService()
    service.create("Continua pendente")
    run_menu(monkeypatch, service, ["7", "concluida", "3"])
    output = capsys.readouterr().out
    assert "Nenhuma tarefa encontrada para este status" in output
    assert "Nenhuma tarefa cadastrada" not in output
    assert len(service.list()) == 1


def test_overdue_listing_has_one_alert_per_menu_cycle(monkeypatch, capsys):
    service = TaskService()
    service.create("Vencida", due_date=date(2000, 1, 1))
    run_menu(monkeypatch, service, ["2", "3"])
    output = capsys.readouterr().out
    assert output.count("[ALERTA]") == 2
    listing = output.split("=== TAREFAS CADASTRADAS ===", 1)[1].split("TASKTRACKER", 1)[0]
    assert "[ALERTA]" not in listing
