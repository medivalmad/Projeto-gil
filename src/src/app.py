from task_manager import TaskManager


manager = TaskManager()
manager.create_task("Implementar login", "Alta")
manager.create_task("Criar dashboard", "Média")


for task in manager.list_tasks():
print(task)
