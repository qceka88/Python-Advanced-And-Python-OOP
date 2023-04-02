from project.driver import Driver


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers: [Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

