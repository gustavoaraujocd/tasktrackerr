from dataclasses import dataclass, field
from datetime import UTC, date, datetime, time
from enum import StrEnum
from uuid import uuid4


class Priority(StrEnum):
    """Níveis de prioridade disponíveis para uma tarefa."""

    LOW = "baixa"
    MEDIUM = "media"
    HIGH = "alta"


class Status(StrEnum):
    """Estados possíveis de uma tarefa."""

    PENDING = "pendente"
    IN_PROGRESS = "em_andamento"
    DONE = "concluida"


@dataclass(slots=True)
class Task:
    """Representa uma tarefa e aplica as validações do domínio."""

    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    due_date: date | None = None
    due_time: time | None = None
    status: Status = Status.PENDING
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        self.description = self.description.strip()

        if not self.title:
            raise ValueError("O título da tarefa é obrigatório.")

        if not isinstance(self.priority, Priority):
            raise ValueError("Prioridade inválida.")

        if not isinstance(self.status, Status):
            raise ValueError("Status inválido.")

        if self.due_date is not None and not isinstance(self.due_date, date):
            raise ValueError("A data limite deve ser uma data válida.")

        if self.due_time is not None and not isinstance(self.due_time, time):
            raise ValueError("O horário limite deve ser um horário válido.")

    def is_overdue(self, reference: datetime | None = None) -> bool:
        """Informa se uma tarefa pendente já passou do prazo definido."""
        if self.status == Status.DONE or self.due_date is None:
            return False

        reference = reference or datetime.now()
        deadline_time = self.due_time or time.max
        deadline = datetime.combine(self.due_date, deadline_time)
        return reference > deadline
