

from typing import List, Optional
from taskpulse.models import Task
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

    def add_task(
        self,
        title: str,
        description: str,
        category: str,
        priority: str,
        due_date: str,
    ) -> Task:
        next_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(next_id, title, description, category, priority, due_date)
        self.tasks.append(task)
        return task

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

    def get_statistics(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.status == "Completed")
        pending = total - completed
        rate = (completed / total * 100) if total > 0 else 0.0

        priorities = {
            "High": sum(1 for t in self.tasks if t.priority == "High"),
            "Medium": sum(1 for t in self.tasks if t.priority == "Medium"),
            "Low": sum(1 for t in self.tasks if t.priority == "Low"),
        }

        return {
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "priorities": priorities,
            "completed_percentage": rate,
        }
        