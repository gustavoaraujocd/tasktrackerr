from datetime import date

from .models import Priority, Status, Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def create_task(
        self,
        title: str,
        description: str = "",
        priority: Priority = Priority.MEDIUM,
        due_date: date | None = None,
    ) -> Task:
        task = Task(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
        )
        self._tasks[task.id] = task
        return task

    def list_tasks(self, status: Status | None = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if status is None:
            return tasks
        return [task for task in tasks if task.status == status]

    def get_task(self, task_id: str) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise KeyError("task not found") from exc

    def update_task(
        self,
        task_id: str,
        *,
        title: str | None = None,
        description: str | None = None,
        priority: Priority | None = None,
        due_date: date | None = None,
        status: Status | None = None,
    ) -> Task:
        task = self.get_task(task_id)
        if title is not None:
            clean_title = title.strip()
            if not clean_title:
                raise ValueError("title is required")
            task.title = clean_title
        if description is not None:
            task.description = description
        if priority is not None:
            if not isinstance(priority, Priority):
                raise ValueError("invalid priority")
            task.priority = priority
        if due_date is not None:
            if not isinstance(due_date, date):
                raise ValueError("due_date must be a date")
            task.due_date = due_date
        if status is not None:
            if not isinstance(status, Status):
                raise ValueError("invalid status")
            task.status = status
        return task

    def complete_task(self, task_id: str) -> Task:
        task = self.get_task(task_id)
        task.status = Status.DONE
        return task
