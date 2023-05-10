from abc import ABC, abstractmethod


class Musician(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")

        self.__age = value

    @property
    @abstractmethod
    def valid_skills(self):
        ...

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."
