from datetime import date

import pytest

from tasktracker import Priority, Status, Task, TaskService


def test_create_task_with_defaults():
    service = TaskService()
    task = service.create_task("Estudar para o Bootcamp")

    assert task.title == "Estudar para o Bootcamp"
    assert task.priority == Priority.MEDIUM
    assert task.status == Status.PENDING
    assert task.id


def test_create_task_rejects_blank_title():
    service = TaskService()

    with pytest.raises(ValueError, match="title is required"):
        service.create_task("   ")


def test_create_task_rejects_invalid_priority():
    with pytest.raises(ValueError, match="invalid priority"):
        Task(title="Teste", priority="urgente")  # type: ignore[arg-type]


def test_create_task_rejects_invalid_due_date():
    with pytest.raises(ValueError, match="due_date must be a date"):
        Task(title="Teste", due_date="11/09/2026")  # type: ignore[arg-type]


def test_complete_task_changes_status():
    service = TaskService()
    task = service.create_task("Entregar projeto", due_date=date(2026, 9, 11))

    completed = service.complete_task(task.id)

    assert completed.status == Status.DONE


def test_update_task_preserves_id_and_changes_fields():
    service = TaskService()
    task = service.create_task("Versao inicial")

    updated = service.update_task(
        task.id,
        title="Versao revisada",
        priority=Priority.HIGH,
        status=Status.IN_PROGRESS,
    )

    assert updated.id == task.id
    assert updated.title == "Versao revisada"
    assert updated.priority == Priority.HIGH
    assert updated.status == Status.IN_PROGRESS


def test_list_tasks_can_filter_by_status():
    service = TaskService()
    first = service.create_task("Tarefa 1")
    service.create_task("Tarefa 2")
    service.complete_task(first.id)

    done = service.list_tasks(status=Status.DONE)

    assert len(done) == 1
    assert done[0].id == first.id


def test_get_missing_task_raises_key_error():
    service = TaskService()

    with pytest.raises(KeyError, match="task not found"):
        service.get_task("missing-id")
