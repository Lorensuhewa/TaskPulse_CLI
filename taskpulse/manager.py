

from typing import List, Optional
from taskpulse.main import Task
from taskpulse.storage import JSONStorage


class TaskManager:
    def __init__(self, storage:Optional[JSONStorage] = None):
        self.tasks: List[Task] = []
        self.storage = storage if storage else JSONStorage()
        self.load()

    def load(self) -> None:
        raw_data = self.storage.load()
        self.tasks = [Task.from_dict(task_data) for task_data in raw_data]

    def save(self) -> bool:
        raw_data = [task.to_dict() for task in self.tasks]
        return self.storage.save(raw_data)

    def add_task(self, title: str, description: str, category: str, priority: str, due_date, status: str = "Pending") -> Task:
        task_id = self._generate_task_id()
        new_task = Task(task_id, title, description, category, priority, due_date, status)
        self.tasks.append(new_task)
        self.save()
        return new_task

    def find_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.find_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            return True
        return False

    def sort_tasks(self, criterion: str) -> List[Task]:
        priority_order = {"High": 1, "Medium": 2, "Low": 3}

        if criterion == "priority":
            return sorted(self.tasks, key=lambda x: priority_order.get(x.priority, 4))
        elif criterion == "due_date":
            return sorted(self.tasks, key=lambda x: x.due_date)
        elif criterion == "status":
            return sorted(self.tasks, key=lambda x: x.status)
        else:
            return self.tasks

    def get_staticstics(self) -> dict:
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        pending_tasks = total_tasks - completed_tasks

        priorities = {
            "High": sum(1 for task in self.tasks if task.priority == "High"),
            "Medium": sum(1 for task in self.tasks if task.priority == "Medium"),
            "Low": sum(1 for task in self.tasks if task.priority == "Low")
        }
        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "priorities": priorities
        }
        