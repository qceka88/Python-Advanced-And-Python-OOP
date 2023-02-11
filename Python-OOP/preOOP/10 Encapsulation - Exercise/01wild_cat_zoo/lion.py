from project.animal import Animal


class Lion(Animal):

    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
        self.money_for_care = 50
