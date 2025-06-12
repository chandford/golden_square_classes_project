class TaskTracker:

    def __init__(self):
        self.tasks = []
        self.task_count = 0

    def add_task(self, task):
        self.tasks.append(task)
        self.task_count += 1
        print(f"Task added: {task}. Task count is {self.task_count}.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.task_count -= 1
            print(f"Task removed: {task}. Task count is {self.task_count}.")

        else:
            raise Exception("Task not found.")