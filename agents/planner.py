from dataclasses import dataclass
from typing import List
import uuid


@dataclass
class Task:
    id: str
    title: str
    description: str
    status: str = "pending"


class PlannerAgent:
    """
    Creates and manages research tasks.
    """

    def __init__(self):
        self.tasks: List[Task] = []

    def create_task(self, title: str, description: str) -> Task:
        task = Task(
            id=str(uuid.uuid4())[:8],
            title=title,
            description=description,
        )
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id: str):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "completed"
                return task
        return None

    def pending_tasks(self):
        return [t for t in self.tasks if t.status == "pending"]


if __name__ == "__main__":
    planner = PlannerAgent()

    planner.create_task(
        "Literature Review",
        "Search recent papers on AI-assisted cyberattacks."
    )

    planner.create_task(
        "Experiment Design",
        "Create benchmark experiments."
    )

    print("\nPending Tasks\n")

    for task in planner.pending_tasks():
        print(f"{task.id} | {task.title} | {task.status}")
