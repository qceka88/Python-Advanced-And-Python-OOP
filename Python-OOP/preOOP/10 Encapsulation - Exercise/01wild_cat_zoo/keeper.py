from project.worker import Worker


class Keeper(Worker):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
