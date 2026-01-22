# Task Manager CLI

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A clean, well-structured command-line task management application built with Python. Features object-oriented design, data persistence, and an intuitive user interface.

## Features

- **Add Tasks**: Create tasks with titles, descriptions, and priority levels
- **View Tasks**: Display all tasks or filter by completion status
- **Task Management**: Mark tasks as complete/incomplete, delete tasks
- **Priority Filtering**: Filter tasks by priority (low, medium, high)
- **Data Persistence**: Automatic saving to JSON file
- **Clean Interface**: Intuitive CLI with formatted output

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/kevin-vasilescu/task-manager-cli.git
cd task-manager-cli
```

2. No additional dependencies required! Uses only Python standard library.

## Usage

Run the application:

```bash
python task_manager.py
```

### Menu Options

1. **Add Task** - Create a new task with title, description, and priority
2. **View All Tasks** - Display all tasks (completed and pending)
3. **View Pending Tasks** - Show only incomplete tasks
4. **Mark Task Complete** - Mark a task as done
5. **Mark Task Incomplete** - Revert a completed task
6. **Delete Task** - Remove a task permanently
7. **Filter by Priority** - View tasks of specific priority level
8. **Exit** - Save and close the application

### Example Workflow

```
Task Manager CLI
================

1. Add Task
   Title: Complete project documentation
   Description: Write README and code comments
   Priority: high
   ✓ Task added successfully!

2. View All Tasks
   ID              Status   Priority   Title
   ----------------------------------------------
   123456789      ✗ Pending  high      Complete project documentation

3. Mark Task Complete
   Enter task ID: 123456789
   ✓ Task marked as complete!
```

## Project Structure

```
task-manager-cli/
│
├── task_manager.py      # Main application file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies (none required)
├── .gitignore          # Git ignore patterns
└── tasks.json          # Data persistence file (auto-generated)
```

## Code Architecture

### Class: `Task`
Represents individual tasks with properties:
- `id`: Unique identifier
- `title`: Task title
- `description`: Optional description
- `priority`: Priority level (low/medium/high)
- `completed`: Completion status
- `created_at`: Timestamp of creation
- `completed_at`: Timestamp of completion

### Class: `TaskManager`
Manages task collection with methods:
- `add_task()`: Create new task
- `remove_task()`: Delete task by ID
- `get_task()`: Retrieve specific task
- `list_tasks()`: List all/pending tasks
- `list_by_priority()`: Filter by priority
- `save_tasks()`: Persist to JSON
- `load_tasks()`: Load from JSON

## Data Persistence

Tasks are automatically saved to `tasks.json` in the following format:

```json
[
  {
    "id": 123456789,
    "title": "Complete project",
    "description": "Finish the task manager",
    "priority": "high",
    "completed": false,
    "created_at": "2026-01-22T23:09:00",
    "completed_at": null
  }
]
```

## Best Practices Demonstrated

- **Object-Oriented Programming**: Clean class design with encapsulation
- **Type Hints**: Full type annotations for better code clarity
- **Documentation**: Comprehensive docstrings for all classes and methods
- **Error Handling**: Graceful handling of invalid inputs and file operations
- **Data Persistence**: JSON-based storage for reliability
- **Separation of Concerns**: Clear division between data models and business logic
- **User Experience**: Intuitive CLI with formatted output

## Future Enhancements

- [ ] Add due dates and reminders
- [ ] Implement task categories/tags
- [ ] Export tasks to CSV/PDF
- [ ] Search functionality
- [ ] Task statistics and analytics
- [ ] Color-coded priority display
- [ ] Undo/redo functionality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**Kevin Vasilescu**
- GitHub: [@kevin-vasilescu](https://github.com/kevin-vasilescu)

## Acknowledgments

Built as a demonstration of clean software engineering principles and Python best practices.
