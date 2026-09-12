from dataclasses import replace
from datetime import date

from .models import Priority, Status, Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def create(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM, due_date: date | None = None) -> Task:
        task = Task(title=title, description=description, priority=priority, due_date=due_date)
        self._tasks[task.id] = task
        return task

    def get(self, task_id: str) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise KeyError("task not found") from exc

    def list(self, status: Status | None = None) -> list[Task]:
        tasks = list(self._tasks.values())
        return [task for task in tasks if task.status == status] if status else tasks

    def update(self, task_id: str, **changes) -> Task:
        current = self.get(task_id)
        allowed = {"title", "description", "priority", "due_date", "status"}
        invalid = set(changes) - allowed
        if invalid:
            raise ValueError(f"unsupported fields: {sorted(invalid)}")
        updated = replace(current, **changes)
        self._tasks[task_id] = updated
        return updated

    def complete(self, task_id: str) -> Task:
        return self.update(task_id, status=Status.DONE)
