from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if task.name == new_task.name:
                return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        removed_tasks_count = len(self.tasks)

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                del task

        return f'Cleared {removed_tasks_count} tasks.'

    def view_section(self):
        info = [f'Section {self.name}:'] + [t.details() for t in self.tasks]

        return '\n'.join(info)
