

import json
import os
from typing import Any, Dict, List


class JSONStorage:
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath

    def load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, tasks: List[Dict[str, Any]]) -> bool:
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(tasks, file, indent=4)
            return True
        except IOError:
            return False