Pokemon Battle   problem conditions
               8.	Pokemon Battle*
Note: For this problem, please submit a zip file, containing a separate file for each of the classes,
with the class names provided in the problem description and include them in a module named project.
![img_7.png](img_7.png)
You are tasked to create two classes: a Pokemon class in the pokemon.py file and 
a Trainer class in the trainer.py file. 
The Pokemon class should receive a name (string) and health (int) upon initialization. 
It should also have a method called pokemon_details that returns the information 
about the pokemon: "{pokemon_name} with health {pokemon_health}"
The Trainer class should receive a name (string). The Trainer should also have an 
attribute pokemons (list, empty by default). The Trainer has three methods:
-	add_pokemon(pokemon: Pokemon)
o	Add the pokemon to the collection and return "Caught {pokemon_name} with health
- {pokemon_health}". Note: use the pokemon's details method.
o	If the pokemon is already in the collection, it should return "This pokemon is already caught"
o	Hint: to import the Pokemon class you should add "from project.pokemon import Pokemon"
-	release_pokemon(pokemon_name: String) 
o	Check if you have a pokemon with that name and remove it from the collection.
- It should return "You have released {pokemon_name}"
o	If there is no pokemon with that name in the collection, return "Pokemon is not caught"
-	trainer_data()
o	The method returns the information about the trainer and his pokemon collection in this format:
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details}
 ...
 - {pokemon_details}"
Examples
Test Code	Output
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())	Pikachu with health 90
Caught Pikachu with health 90
Caught Charizard with health 110
This pokemon is already caught
You have released Pikachu
Pokemon is not caught
Pokemon Trainer Ash
Pokemon count 1
- Charizard with health 110
