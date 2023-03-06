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

    @staticmethod
    def collect_data(some_dict, some_list):
        message = [f"You have {len(some_list)} {some_list[0].__class__.__base__.__name__.lower()}s"]

        for data in some_list:
            some_dict[data.__class__.__name__].append(data.__repr__())

        for type_data, data in some_dict.items():
            message.append(f"----- {len(data)} {type_data}s:")
            message.extend(data)

        return message

    def animals_status(self):
        dict_animals = {"Lion": [], "Tiger": [], "Cheetah": []}

        result = self.collect_data(dict_animals, self.animals)

        return "\n".join(result)

    def workers_status(self):
        dict_workers = {"Keeper": [], "Caretaker": [], "Vet": []}

        result = self.collect_data(dict_workers, self.workers)

        return "\n".join(result)
