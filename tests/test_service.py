from datetime import date, datetime, time

import pytest

from tasktracker import Priority, Status, TaskService


def test_create_task_with_defaults():
    service = TaskService()
    task = service.create("Estudar")
    assert task.title == "Estudar"
    assert task.priority == Priority.MEDIUM
    assert task.status == Status.PENDING


def test_empty_title_is_rejected():
    with pytest.raises(ValueError):
        TaskService().create("   ")


def test_invalid_priority_is_rejected():
    with pytest.raises(ValueError):
        TaskService().create("Teste", priority="urgente")


def test_invalid_due_date_is_rejected():
    with pytest.raises(ValueError):
        TaskService().create("Teste", due_date="2026-09-12")


def test_invalid_due_time_is_rejected():
    with pytest.raises(ValueError):
        TaskService().create("Teste", due_time="18:00")


def test_complete_task():
    service = TaskService()
    task = service.create("Entregar trabalho")
    completed = service.complete(task.id)
    assert completed.status == Status.DONE


def test_update_preserves_id():
    service = TaskService()
    task = service.create("Original", due_date=date(2026, 9, 20))
    updated = service.update(task.id, title="Atualizada")
    assert updated.id == task.id
    assert updated.title == "Atualizada"


def test_filter_by_status():
    service = TaskService()
    first = service.create("A")
    service.create("B")
    service.complete(first.id)
    assert [task.title for task in service.list(Status.DONE)] == ["A"]
    assert [task.title for task in service.list(Status.PENDING)] == ["B"]


def test_overdue_task_is_identified():
    service = TaskService()
    task = service.create(
        "Prazo vencido",
        due_date=date(2026, 9, 30),
        due_time=time(18, 0),
    )

    overdue = service.overdue(datetime(2026, 10, 1, 10, 0))

    assert [item.id for item in overdue] == [task.id]


def test_completed_task_is_not_overdue():
    service = TaskService()
    task = service.create(
        "Concluida",
        due_date=date(2026, 9, 30),
        due_time=time(18, 0),
    )
    service.complete(task.id)

    assert service.overdue(datetime(2026, 10, 1, 10, 0)) == []


def test_missing_task_raises_key_error():
    with pytest.raises(KeyError):
        TaskService().get("missing")
