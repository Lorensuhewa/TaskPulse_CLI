from datetime import datetime
from typing import Any, Dict, Optional, Optional

class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        category: str,
        priority: str,
        due_date: str,
        status: str = "Pending",
        created_at: Optional[str] = None,
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.status = status          
        self.created_at = created_at

    def mark_completed(self):
        self.status = "Completed"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            category=data.get("category", "General"),
            priority=data.get("priority", "Medium"),
            due_date=data.get("due_date", "N/A"),
            status=data.get("status", "Pending"),       
            created_at=data.get("created_at"),
        )