from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Kitten.GENDER)

    @staticmethod
    def make_sound():
        return "Meow"
