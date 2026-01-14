from src.task_manager import TaskManager


def test_create_task():
manager = TaskManager()
task = manager.create_task("Teste", "Alta")
assert task["title"] == "Teste"
assert task["priority"] == "Alta"
