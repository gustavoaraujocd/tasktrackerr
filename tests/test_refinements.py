"""Contratos de borda refinados na Entrega 2 do Bootcamp III."""
from datetime import UTC, date, datetime, time

import pytest

from tasktracker import Priority, Status, TaskService


def test_datetime_is_not_a_calendar_due_date():
    with pytest.raises(ValueError, match="data"):
        TaskService().create("Prazo", due_date=datetime(2026, 10, 23, 10))


def test_time_without_date_is_rejected():
    with pytest.raises(ValueError, match="data"):
        TaskService().create("Prazo", due_time=time(10))


def test_aware_deadline_time_is_rejected():
    with pytest.raises(ValueError, match="fuso"):
        TaskService().create("Prazo", due_date=date(2026, 10, 23), due_time=time(10, tzinfo=UTC))


def test_aware_reference_has_explicit_validation():
    task = TaskService().create("Prazo", due_date=date(2026, 10, 23))
    with pytest.raises(ValueError, match="fuso"):
        task.is_overdue(datetime(2026, 10, 24, tzinfo=UTC))


def test_invalid_filter_is_not_silently_an_empty_result():
    with pytest.raises(ValueError, match="Status"):
        TaskService().list("inexistente")


@pytest.mark.parametrize("changes", [{"title": None}, {"description": None}])
def test_invalid_text_type_uses_domain_error(changes):
    values = {"title": "Válida", **changes}
    with pytest.raises(ValueError):
        TaskService().create(**values)


def test_due_date_without_time_expires_only_after_end_of_day():
    task = TaskService().create("Prazo", due_date=date(2026, 10, 23))
    assert not task.is_overdue(datetime(2026, 10, 23, 23, 59, 59, 999999))
    assert task.is_overdue(datetime(2026, 10, 24))


def test_exact_deadline_is_not_overdue():
    task = TaskService().create("Prazo", due_date=date(2026, 10, 23), due_time=time(10))
    assert not task.is_overdue(datetime(2026, 10, 23, 10))
    assert task.is_overdue(datetime(2026, 10, 23, 10, 0, 0, 1))


def test_no_deadline_and_completed_task_do_not_alert():
    service = TaskService()
    service.create("Sem prazo")
    task = service.create("Feita", due_date=date(2026, 10, 22))
    service.complete(task.id)
    assert service.overdue(datetime(2026, 10, 23)) == []


def test_invalid_update_does_not_change_stored_task():
    service = TaskService()
    task = service.create("Original", due_date=date(2026, 10, 23), due_time=time(10))
    with pytest.raises(ValueError):
        service.update(task.id, title="Outra", due_date=None)
    assert service.get(task.id).title == "Original"
    assert service.get(task.id).due_date == date(2026, 10, 23)


def test_update_rejects_unknown_fields_and_preserves_creation_time():
    service = TaskService()
    task = service.create("Original")
    with pytest.raises(ValueError):
        service.update(task.id, id="outro")
    updated = service.update(task.id, title="Atualizada", priority=Priority.HIGH, status=Status.IN_PROGRESS)
    assert updated.id == task.id
    assert updated.created_at == task.created_at
    assert updated.status is Status.IN_PROGRESS


def test_invalid_status_update_keeps_original():
    service = TaskService()
    task = service.create("Original")
    with pytest.raises(ValueError):
        service.update(task.id, status="qualquer")
    assert service.get(task.id).status is Status.PENDING


def test_in_progress_task_still_alerts_when_overdue():
    service = TaskService()
    task = service.create("Em execução", due_date=date(2026, 10, 22))
    service.update(task.id, status=Status.IN_PROGRESS)
    assert [t.id for t in service.overdue(datetime(2026, 10, 23))] == [task.id]


def test_non_datetime_reference_is_rejected():
    task = TaskService().create("Prazo", due_date=date(2026, 10, 23))
    with pytest.raises(ValueError):
        task.is_overdue("2026-10-24")
