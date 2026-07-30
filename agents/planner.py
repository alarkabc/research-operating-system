class PlannerAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

if __name__ == "__main__":
    planner = PlannerAgent()
    planner.add_task("Review literature")
    planner.add_task("Generate experiment")
    print(planner.list_tasks())