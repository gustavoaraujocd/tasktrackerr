from dataclasses import dataclass, field
from datetime import date, datetime
from enum import StrEnum
from uuid import uuid4


class Priority(StrEnum):
    LOW = "baixa"
    MEDIUM = "media"
    HIGH = "alta"


class Status(StrEnum):
    PENDING = "pendente"
    IN_PROGRESS = "em_andamento"
    DONE = "concluida"


@dataclass(slots=True)
class Task:
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    due_date: date | None = None
    status: Status = Status.PENDING
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        if not self.title:
            raise ValueError("title is required")
        if not isinstance(self.priority, Priority):
            raise ValueError("invalid priority")
        if not isinstance(self.status, Status):
            raise ValueError("invalid status")
        if self.due_date is not None and not isinstance(self.due_date, date):
            raise ValueError("due_date must be a date")
