from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
        self.money_for_care = 60
