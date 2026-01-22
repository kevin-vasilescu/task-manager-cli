#!/usr/bin/env python3
"""
Task Manager CLI Application
A clean, object-oriented task management system with data persistence.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Task:
    """Represents a single task with properties and methods."""
    
    def __init__(self, title: str, description: str = "", priority: str = "medium", task_id: Optional[int] = None):
        self.id = task_id if task_id else id(self)
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a Task instance from a dictionary."""
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            task_id=data['id']
        )
        task.completed = data.get('completed', False)
        task.created_at = data.get('created_at', datetime.now().isoformat())
        task.completed_at = data.get('completed_at')
        return task
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = '✓' if self.completed else '✗'
        return f"[{status}] {self.title} (Priority: {self.priority})"


class TaskManager:
    """Manages a collection of tasks with persistence."""
    
    def __init__(self, data_file: str = 'tasks.json'):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> Task:
        """Add a new task to the manager."""
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def remove_task(self, task_id: int) -> bool:
        """Remove a task by its ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        """List all tasks, optionally filtering out completed ones."""
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if not task.completed]
    
    def list_by_priority(self, priority: str) -> List[Task]:
        """List tasks filtered by priority level."""
        return [task for task in self.tasks if task.priority.lower() == priority.lower()]
    
    def save_tasks(self) -> None:
        """Persist tasks to JSON file."""
        data = [task.to_dict() for task in self.tasks]
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_tasks(self) -> None:
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError):
                print(f"Warning: Could not load tasks from {self.data_file}")
                self.tasks = []


def print_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*50)
    print("Task Manager CLI".center(50))
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. Mark Task Complete")
    print("5. Mark Task Incomplete")
    print("6. Delete Task")
    print("7. Filter by Priority")
    print("8. Exit")
    print("="*50)


def display_tasks(tasks: List[Task]) -> None:
    """Display a list of tasks in a formatted manner."""
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print(f"\n{'ID':<15} {'Status':<8} {'Priority':<10} {'Title':<30}")
    print("-" * 70)
    for task in tasks:
        status = '✓ Done' if task.completed else '✗ Pending'
        print(f"{task.id:<15} {status:<8} {task.priority:<10} {task.title:<30}")
        if task.description:
            print(f"{'':15} Description: {task.description}")


def main():
    """Main application loop."""
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            title = input("Enter task title: ").strip()
            description = input("Enter description (optional): ").strip()
            priority = input("Enter priority (low/medium/high): ").strip() or "medium"
            task = manager.add_task(title, description, priority)
            print(f"\n✓ Task added successfully! (ID: {task.id})")
        
        elif choice == '2':
            tasks = manager.list_tasks(show_completed=True)
            display_tasks(tasks)
        
        elif choice == '3':
            tasks = manager.list_tasks(show_completed=False)
            display_tasks(tasks)
        
        elif choice == '4':
            task_id = input("Enter task ID to mark complete: ").strip()
            try:
                task = manager.get_task(int(task_id))
                if task:
                    task.mark_complete()
                    manager.save_tasks()
                    print("\n✓ Task marked as complete!")
                else:
                    print("\n✗ Task not found.")
            except ValueError:
                print("\n✗ Invalid task ID.")
        
        elif choice == '5':
            task_id = input("Enter task ID to mark incomplete: ").strip()
            try:
                task = manager.get_task(int(task_id))
                if task:
                    task.mark_incomplete()
                    manager.save_tasks()
                    print("\n✓ Task marked as incomplete!")
                else:
                    print("\n✗ Task not found.")
            except ValueError:
                print("\n✗ Invalid task ID.")
        
        elif choice == '6':
            task_id = input("Enter task ID to delete: ").strip()
            try:
                if manager.remove_task(int(task_id)):
                    print("\n✓ Task deleted successfully!")
                else:
                    print("\n✗ Task not found.")
            except ValueError:
                print("\n✗ Invalid task ID.")
        
        elif choice == '7':
            priority = input("Enter priority level (low/medium/high): ").strip()
            tasks = manager.list_by_priority(priority)
            display_tasks(tasks)
        
        elif choice == '8':
            print("\nThank you for using Task Manager CLI! Goodbye!")
            break
        
        else:
            print("\n✗ Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
