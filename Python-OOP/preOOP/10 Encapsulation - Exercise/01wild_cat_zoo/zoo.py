class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if self.__budget - price < 0:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum([w.salary for w in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needed_money = sum([a.money_for_care for a in self.animals])
        if self.__budget - total_needed_money >= 0:
            self.__budget -= total_needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = f"You have {len(self.animals)} animals"
        zoo_animals = {'Lions': [], 'Tigers': [], 'Cheetahs': []}
        for animal in self.animals:
            type_of_animal = str(type(animal).__name__) + 's'
            zoo_animals[type_of_animal].append(animal.__repr__())
        for animal_type, data in zoo_animals.items():
            message += f"\n----- {len(data)} {animal_type}:"
            if data:
                message += '\n' + '\n'.join(data)
        return message

    def workers_status(self):
        message = f"You have {len(self.workers)} workers"
        zoo_workers = {'Keepers': [], 'Caretakers': [], 'Vets': []}

        for worker in self.workers:
            type_of_worker = str(type(worker).__name__) + 's'
            zoo_workers[type_of_worker].append(worker.__repr__())
        for worker_type, data in zoo_workers.items():
            message += f"\n----- {len(data)} {worker_type}:"
            if data:
                message += '\n' + '\n'.join(data)
        return message

