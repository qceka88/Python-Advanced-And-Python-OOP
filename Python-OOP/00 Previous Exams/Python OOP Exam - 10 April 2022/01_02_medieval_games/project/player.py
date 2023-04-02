class Player:
    players_list = []

    # TODO: check is the stamina int or float
    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_sustenance: bool = None

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        if value in Player.players_list:
            raise Exception(f"Name {value} is already used!")

        Player.players_list.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

# player1 = Player("Gosho", 15, 75)
# player2 = Player("Ivan", 15)
# player3 = Player("Robert", 15, 75)
