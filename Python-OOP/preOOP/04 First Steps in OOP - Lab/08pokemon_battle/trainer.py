from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        current_pokemon = pokemon.pokemon_details().split()
        name, health = current_pokemon[0], int(current_pokemon[-1])
        if name not in [p[0] for p in self.pokemons]:
            self.pokemons.append([name, health])
            return f'Caught {name} with health {health}'
        return 'This pokemon is already caught'

    def release_pokemon(self, name):
        for name_pokemon, health in self.pokemons:
            if name == name_pokemon:
                self.pokemons.remove([name, health])
                return f'You have released {name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        count = len(self.pokemons)
        message = f'Pokemon Trainer {self.name}\nPokemon count {count}'
        for name, health in self.pokemons:
            result = Pokemon(name, health).pokemon_details()
            message += f"\n- {result}"
        return message


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
