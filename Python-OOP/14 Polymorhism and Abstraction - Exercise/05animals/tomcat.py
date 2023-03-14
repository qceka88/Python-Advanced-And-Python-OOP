from project.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Tomcat.GENDER)

    @staticmethod
    def make_sound():
        return "Hiss"
