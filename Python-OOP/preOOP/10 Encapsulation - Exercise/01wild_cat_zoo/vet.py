from project.worker import Worker


class Vet(Worker):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

