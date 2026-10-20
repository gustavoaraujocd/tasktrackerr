"""Interface de linha de comando do TaskTracker.

Fase 2 — Bootcamp II: aplicação das regras de negócio em Python,
com menu contínuo para cadastro, visualização e alerta de tarefas atrasadas.
"""

from datetime import datetime

from tasktracker import Priority, TaskService


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
    due_time = read_due_time()

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
    tasks = service.list()

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

    show_overdue_notifications(service)


def show_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("\n" + "=" * 50)
    print("              TASKTRACKER")
    print("=" * 50)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 50)


def main() -> None:
    """Inicializa a aplicação e mantém o menu em execução."""
    service = TaskService()

    print("\nBem-vindo ao TaskTracker!")

    while True:
        show_menu()
        show_overdue_notifications(service)
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            create_task(service)
        elif option == "2":
            list_tasks(service)
        elif option == "3":
            print("\nAté logo! Encerrando o TaskTracker.")
            break
        else:
            print("[ERRO] Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
