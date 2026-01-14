
class TaskManager:
def __init__(self):
self.tasks = []


def create_task(self, title, priority):
task = {
"id": len(self.tasks) + 1,
"title": title,
"priority": priority,
"status": "A Fazer"
}
self.tasks.append(task)
return task


def list_tasks(self):
return self.tasks


def update_task(self, task_id, new_status):
for task in self.tasks:
if task["id"] == task_id:
task["status"] = new_status
return task
return None


def delete_task(self, task_id):
self.tasks = [t for t in self.tasks if t["id"] != task_id]
