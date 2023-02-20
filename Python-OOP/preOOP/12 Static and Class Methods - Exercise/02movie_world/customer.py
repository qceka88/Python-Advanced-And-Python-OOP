class Customer:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        dvd = ', '.join(i.name for i in self.rented_dvds)
        count_dvds = len(self.rented_dvds)
        message = f"{self.id}: {self.name} of age {self.age} has {count_dvds} rented DVD's ({dvd})"
        return message
