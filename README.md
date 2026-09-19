
# TaskPulse CLI

A modular, dependency-free command-line personal task manager written purely in vanilla Python. Built without external frameworks, databases, or third-party packages, relying entirely on the Python Standard Library.

---
# Getting Started

- **Prerequisites**: 
    - Python 3.10+ installed on your system.
    - No external packages (pip install) are required

- **Installation & Execution**

1. Clone or download the repository to your local machine:

```text 
    git clone [https://github.com/your-username/TaskPulse_CLI.git](https://github.com/your-username/TaskPulse_CLI.git)
    cd TaskPulse_CLI
```

2. Run the application as a Python module from the project root:

```text 
    python -m taskpulse.main
```
--- 

## Features

- **CRUD Operations**: Add, inspect, search, edit, and delete tasks.
- **Task Attributes**: Manage titles, descriptions, categories, strict priority levels (`High`, `Medium`, `Low`), due dates (`YYYY-MM-DD`), and dynamic statuses (`Pending`, `Completed`).
- **Data Filtering & Analytics**:
  - Substring search across title, description, and category.
  - Multi-criterion sorting (by priority, due date, or status).
  - Statistical summaries including completion percentage and priority breakdown.
- **Persistence**: Automatic JSON file serialization (`tasks.json`) with error handling for empty or malformed files.
- **Input Validation**: Safe date parsing, input bounds checking, and graceful fallbacks.

---
 

## Project Structure

```text
TaskPulse_CLI/
├── tasks.json              # Persistent data store (auto-generated)
├── README.md               # Project documentation
└── taskpulse/
    ├── __init__.py         # Package marker
    ├── main.py             # CLI interactive loop & menu dispatchers
    ├── models.py           # Task data model & serialization logic
    ├── manager.py          # TaskManager business logic, search & aggregation
    ├── storage.py          # Atomic JSON read/write persistence
    └── utils.py            # Input validation, date parsing & formatting
   
```
---

# Interactive Menu Overview

```text

================================
       MY TASK MANAGER          
================================
1. Add Task
2. View Tasks
3. Search Tasks
4. Update Task
5. Mark Task as Completed
6. View Statistics
7. Sort Tasks
8. Exit
================================

```

