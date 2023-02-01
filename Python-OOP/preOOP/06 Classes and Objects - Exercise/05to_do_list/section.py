'''The Section class should receive a name (string) upon initialization.
The task also has one instance attribute: tasks (empty list)
The Section class should also have four methods:
-	add_task(new_task: Task)
o	Adds a new task to the collection and returns "Task {task details} is added to the section"
o	If the task is already in the collection, returns "Task is already in the section {section_name}"
-	complete_task(task_name: str)
o	Changes the task to completed (True) and returns "Completed task {task_name}"
o	If the task is not found, returns "Could not find task with the name {task_name}"
-	clean_section()
o	Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
-	view_section()
o	Returns information about the section and its tasks in this format:
    "Section {section_name}:
     {details of the first task}
     {details of the second task}
     …
     {details of the n task}"

'''

from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def clean_section(self):
        amount = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                amount += 1

        return f"Cleared {amount} tasks."

    def complete_task(self, task_name):
        if task_name not in [x.name for x in self.tasks]:
            return f"Could not find task with the name {task_name}"
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
        return f"Completed task {task_name}"

    def view_section(self):
        message = f'Section {self.name}:\n'
        message += '\n'.join(x.details() for x in self.tasks)
        return message

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.complete_task(second_task))
# print(section.clean_section())
# print(section.view_section())
