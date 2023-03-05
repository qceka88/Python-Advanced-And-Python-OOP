from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if price > self.__budget:
                return "Not enough budget"

            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum(w.salary for w in self.workers)
        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = sum(a.money_for_care for a in self.animals)
        if needed_money > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = [f"You have {len(self.animals)} animals"]
        counted_animals = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            counted_animals[animal.__class__.__name__].append(animal.__repr__())

        for type_animal, data in counted_animals.items():
            message.append(f"----- {len(data)} {type_animal}s:")
            message.extend(data)

        return "\n".join(message)

    def workers_status(self):
        message = [f"You have {len(self.workers)} workers"]
        counted_workers = {"Keeper": [], "Caretaker": [], "Vet": []}

        for worker in self.workers:
            counted_workers[worker.__class__.__name__].append(worker.__repr__())

        for type_worker, data in counted_workers.items():
            message.append(f"----- {len(data)} {type_worker}s:")
            message.extend(data)

        return "\n".join(message)
