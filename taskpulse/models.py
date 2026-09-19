from datetime import datetime
from typing import Any, Dict

class Task:

    def __init__(self, task_id, title, description, category, priority, due_date, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def mark_completed(self):
        self.status = "Completed"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        due_date = datetime.strptime(data["due_date"], "%Y-%m-%d")
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            priority=data["priority"],
            due_date=due_date,
            status=data["status"]
        )