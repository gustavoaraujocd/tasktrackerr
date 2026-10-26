"""Interface de linha de comando do TaskTracker.

Bootcamp III: casos de uso do domínio acessíveis em menu contínuo.
"""

from datetime import datetime

from tasktracker import Priority, Status, TaskService


PRIORITY_OPTIONS = {
    "alta": Priority.HIGH,
    "media": Priority.MEDIUM,
    "média": Priority.MEDIUM,
    "baixa": Priority.LOW,
}


def read_required_text(prompt: str) -> str:
    """Solicita um texto obrigatório até que uma entrada válida seja informada."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("[ERRO] Este campo é obrigatório. Digite uma informação válida.")


def read_priority() -> Priority:
    """Solicita uma prioridade válida."""
    while True:
        value = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        priority = PRIORITY_OPTIONS.get(value)
        if priority is not None:
            return priority
        print("[ERRO] Prioridade inválida. Escolha Alta, Média ou Baixa.")


def read_due_date():
    """Solicita uma data no formato DD/MM/AAAA ou permite deixar em branco."""
    while True:
        value = input("Data limite (DD/MM/AAAA, opcional): ").strip()
        if not value:
            return None
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            print("[ERRO] Data inválida. Use o formato DD/MM/AAAA.")


def read_due_time():
    """Solicita um horário no formato HH:MM ou permite deixar em branco."""
    while True:
        value = input("Hora limite (HH:MM, opcional): ").strip()
        if not value:
            return None
        try:
            return datetime.strptime(value, "%H:%M").time()
        except ValueError:
            print("[ERRO] Horário inválido. Use o formato HH:MM.")


def format_due_date(task) -> str:
    """Formata a data e o horário para apresentação no terminal."""
    if task.due_date is None:
        return "Não informada"
    if task.due_time is None:
        return task.due_date.strftime("%d/%m/%Y")
    return f"{task.due_date.strftime('%d/%m/%Y')} às {task.due_time.strftime('%H:%M')}"


def show_overdue_notifications(service: TaskService) -> None:
    """Exibe alerta para tarefas pendentes que ultrapassaram o prazo."""
    overdue_tasks = service.overdue()
    if not overdue_tasks:
        return

    print("\n[ALERTA] Você possui tarefas fora do prazo:")
    for task in overdue_tasks:
        print(f"- {task.title} (ID: {task.id})")


def create_task(service: TaskService) -> None:
    """Executa o fluxo de cadastro de uma nova tarefa."""
    print("\n=== CADASTRAR NOVA TAREFA ===")
    title = read_required_text("Título: ")
    description = input("Descrição: ").strip()
    priority = read_priority()
    due_date = read_due_date()
    due_time = read_due_time() if due_date is not None else None

    task = service.create(
        title=title,
        description=description,
        priority=priority,
        due_date=due_date,
        due_time=due_time,
    )

    print("\n[SUCESSO] Tarefa cadastrada com sucesso!")
    print(f"ID: {task.id}")


def list_tasks(service: TaskService) -> None:
    """Exibe todas as tarefas cadastradas de forma organizada."""
    print("\n=== TAREFAS CADASTRADAS ===")
    display_tasks(service.list())
    show_overdue_notifications(service)


def display_tasks(tasks) -> None:
    """Apresenta uma coleção de tarefas, inclusive consultas filtradas."""

    if not tasks:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"\nTarefa {index}")
        print("-" * 50)
        print(f"ID:          {task.id}")
        print(f"Título:      {task.title}")
        print(f"Descrição:   {task.description or 'Não informada'}")
        print(f"Prioridade:  {task.priority.value.capitalize()}")
        print(f"Prazo:       {format_due_date(task)}")
        print(f"Status:      {task.status.value.replace('_', ' ').capitalize()}")



def consult_task(service: TaskService) -> None:
    task_id = read_required_text("ID da tarefa: ")
    display_tasks([service.get(task_id)])


def complete_task(service: TaskService) -> None:
    task_id = read_required_text("ID da tarefa: ")
    service.complete(task_id)
    print("[SUCESSO] Tarefa concluída.")


def read_status() -> Status:
    while True:
        value = input("Status (pendente/em_andamento/concluida): ").strip().lower()
        try:
            return Status(value)
        except ValueError:
            print("[ERRO] Status inválido.")


def filter_tasks(service: TaskService) -> None:
    display_tasks(service.list(read_status()))


def update_task(service: TaskService) -> None:
    task_id = read_required_text("ID da tarefa: ")
    service.get(task_id)
    print("Enter mantém o valor. '-' limpa descrição, data ou hora.")
    changes = {}
    for label, field in [("Título", "title"), ("Descrição", "description")]:
        value = input(f"{label}: ").strip()
        if value:
            changes[field] = "" if value == "-" and field == "description" else value
    value = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
    if value:
        if value not in PRIORITY_OPTIONS:
            raise ValueError("Prioridade inválida. Nenhuma alteração aplicada.")
        changes["priority"] = PRIORITY_OPTIONS[value]
    for label, field, fmt, converter in [
        ("Data (DD/MM/AAAA)", "due_date", "%d/%m/%Y", datetime.date),
        ("Hora (HH:MM)", "due_time", "%H:%M", datetime.time),
    ]:
        value = input(f"{label}: ").strip()
        if value:
            if value == "-":
                changes[field] = None
            else:
                try:
                    changes[field] = converter(datetime.strptime(value, fmt))
                except ValueError:
                    raise ValueError(f"{label} inválida. Nenhuma alteração aplicada.") from None
    value = input("Status (pendente/em_andamento/concluida): ").strip().lower()
    if value:
        try:
            changes["status"] = Status(value)
        except ValueError:
            raise ValueError("Status inválido. Nenhuma alteração aplicada.") from None
    service.update(task_id, **changes)
    print("[SUCESSO] Tarefa atualizada.")


def show_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("\n" + "=" * 50)
    print("              TASKTRACKER")
    print("=" * 50)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("4. Consultar tarefa por ID")
    print("5. Atualizar tarefa")
    print("6. Concluir tarefa")
    print("7. Filtrar tarefas por status")
    print("=" * 50)


def main() -> None:
    """Inicializa a aplicação e mantém o menu em execução."""
    service = TaskService()

    print("\nBem-vindo ao TaskTracker!")

    while True:
        show_menu()
        show_overdue_notifications(service)
        try:
            option = input("Escolha uma opção: ").strip()
            if option == "3":
                print("\nAté logo! Encerrando o TaskTracker.")
                break
            actions = {
                "1": create_task, "2": list_tasks, "4": consult_task,
                "5": update_task, "6": complete_task, "7": filter_tasks,
            }
            action = actions.get(option)
            if action is None:
                print("[ERRO] Opção inválida. Escolha uma opção de 1 a 7.")
            else:
                action(service)
        except KeyError:
            print("[ERRO] Tarefa não encontrada. Copie o ID completo da listagem.")
        except ValueError as exc:
            print(f"[ERRO] {exc}")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada encerrada. Encerrando o TaskTracker.")
            break


if __name__ == "__main__":
    main()
