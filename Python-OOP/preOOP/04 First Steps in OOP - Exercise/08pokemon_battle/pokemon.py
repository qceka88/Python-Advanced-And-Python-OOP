'''The Pokemon class should receive a name (string) and health (int) upon initialization.
It should also have a method called pokemon_details
that returns the information about the pokemon: "{pokemon_name} with health {pokemon_health}
'''


class Pokemon:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"
