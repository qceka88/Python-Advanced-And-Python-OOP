from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_obj):
        if task_obj in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task_obj)
        return f"Task {task_obj.details()} is added to the section"

    def complete_task(self, task_name):
        try:

            task = next(filter(lambda t: t.name == task_name, self.tasks))
            task.completed = Task
            return f"Completed task {task.name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                removed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        tasks = '\n'.join(t.details() for t in self.tasks)
        message = f"Section {self.name}:\n{tasks}"
        return message


