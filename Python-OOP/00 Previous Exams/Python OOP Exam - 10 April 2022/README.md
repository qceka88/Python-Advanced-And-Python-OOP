Problem description 

Python OOP Exam - Medieval Games
You and your friends gathered to play Medieval Games in your backyard!
You will be provided with a skeleton that includes all the folders and files you will need. 
Note: You are not allowed to change the folder and file structure and change their names!


![img_1.png](img_1.png)

Judge Upload
For the first 2 problems, create a zip file with the project folder and upload it to the judge system.
For the last problem, create a zip file with the tests folder and upload it to the judge system.
You do not need to include in the zip file your venv, .idea, pycache, and __MACOSX (for Mac users), so you do not exceed the maximum allowed size of 16.00 KB.
Structure (Problem 1) and Functionality (Problem 2)
Our first task is to implement the structure and functionality of all the classes (properties, methods, inheritance, etc.)
You are free to add additional attributes (instance attributes, class attributes, methods, dunder methods, etc.) to simplify your code and increase readability as long as it does not change the project's final result according to the requirements and the program works properly.
1.	Class Supply
In the file supply.py, the class Supply should be implemented. It is a base class of any type of supply, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	name: str
o	If it is an empty string, raise ValueError with the message "Name cannot be an empty string."
•	energy: int
o	If it is a negative number, raise ValueError with the message "Energy cannot be less than zero."
Methods
__init__(name: str, energy: int)
The __init__ method should receive a name and energy.
details()
Return the supply's type, name and energy in the format: "{type}: {name}, {energy}".
The type of the supply is either "Food" or "Drink".
Hint: override the method in the child classes.
2.	Class Food
In the food.py file, the class Food should be implemented. The food is a type of supply. A food has 25 units of energy as an optional parameter.
3.	Class Drink
In the drink.py file, the class Drink should be implemented. The drink is a type of supply. Each drink has 15 initial units of energy.
4.	Class Player
In the player.py file, the class Player should be implemented. It will store the info of each player.
Structure
The class should have the following attributes:
•	name: str
o	If it's set to an empty string, raise ValueError with the message "Name not valid!"
o	There should not be two players with the same name (they all should be unique). If a second player is created with the same name, raise Exception with the message "Name {name} is already used!"
•	age: int
o	If the player is under 12 years old, raise ValueError with the message "The player cannot be under 12 years old!"
•	stamina: int
o	An optional parameter, 100 by default
o	Stamina's max value is 100, and its min value is 0
o	If it is less than zero or more than 100, raise ValueError with the message "Stamina not valid!"
•	need_sustenance: bool
o	Returns if the player's stamina is less than 100. It is read-only, and it should not be able to be set
Methods
__init__(name: str, age: int, stamina: int)
Upon initialization, all the needed attributes must be set.

__str__()
Override the method so that its return the player's data in the format:
"Player: {player_name}, {age}, {stamina}, {need_sustenance}"
5.	Class Controller
In the controller.py file, the class Controller should be implemented. It will contain all the functionality of the project.
Structure
This class will have the following attributes:
•	players: list
o	An empty list that will contain all the players (objects)
•	supplies: list
o	An empty list that will contain all the supplies (objects)
Methods
__init__()
Upon initialization, all the needed attributes must be set.
add_player(player1: Player, player2: Player, … playerN: Player)
•	Add the players to the players' list. You should not add a player who has already been added.
•	In the end, return a message with the successfully added players' names, separated with a comma and a space (", ") in the format: "Successfully added: {name1}, {name2}, … {nameN}"
add_supply(supply1: Supply, supply2: Supply, … supplyN: Supply)
•	Add all supplies to the supplies list
•	A supply could be added multiple times
sustain(player_name: str, sustenance_type: str)
•	Use the last supply added from the given type to sustain the player (increase his stamina with the supply's energy value and remove the supply from the list) and return the message "{player_name} sustained successfully with {supply_name}."
•	A player always uses the whole amount (units) of the given supply, but his stamina cannot enhance above 100 (it should be set to 100).
•	If the player doesn't need sustenance, it won't be appropriate to waste a supply. Just return the message "{player_name} have enough stamina."
•	If the given type is food, but there is no food left, raise an Exception with the message "There are no food supplies left!"
•	If the given type is drink, but there are no drinks left, raise an Exception with the message "There are no drink supplies left!"
•	The valid sustenance types are "Food" and "Drink". In any other case, ignore the command.
•	If the player is not in the players list, ignore the command. 
duel(first_player_name: str, second_player_name: str)
•	The two players participate in a duel, each of them could only attack once.
•	If a player's stamina is 0, he could not participate in a duel. In that case, return a message "Player {player_name} does not have enough stamina." and discontinue the duel. If both players' stamina is 0, return the message for both players on separate lines, starting from the first one given.
•	If both players have a positive value of stamina, the duel begins:
o	The player with a lower value of stamina attacks first. He reduces the other player's stamina by a value equal to one-half of his own (the attacker's) stamina. 
o	Next, the other player attacks the same way (reduces the first player's stamina by a value equal to one-half of his own (the second attacker's) stamina).
o	If, during the duel, a player's stamina becomes equal to or less than 0, it should be set to 0. The player immediately loses the duel, and the other player becomes a winner. 
o	Otherwise, the winner is the player who has left with more stamina. 
o	Return the winner's name in the format: "Winner: {winner_name}"
•	Note: there will be no case where both players will have equal stamina values at the beginning or in the end.
•	Note: the players will always exist in the players list.
next_day()
•	First, the stamina of each added player gets reduced by the result of multiplying their age by 2
•	If a player's stamina becomes less than 0, it should be set to 0
•	Then, you need to sustain each player by giving them one food (first) and one drink (second)
__str__()
Override the method so that its return the players' data and the supplies' data in the format:
"Player: {player_name_1}, {age}, {stamina}, {need_sustenance}
Player: {player_name_2}, {age}, {stamina}, {need_sustenance}
...
Player: {player_name_N}, {age}, {stamina}, {need_sustenance}
{supply_type}: {name_1}, {energy}
{supply_type}: {name_2}, {energy}
...
{supply_type}: {name_N}, {energy}"



_______________________________________________
Example

from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)



_______________________________________________
Output

None
Successfully added: Peter, Lilly
Winner: Lilly
Successfully added: 
Lilly sustained successfully with water.
Player Peter does not have enough stamina.
Player: Peter, 15, 0, True
Player: Lilly, 12, 82.5, True
Player: Peter, 15, 37, True
Player: Lilly, 12, 98.5, True
Food: cheese, 25
Food: apple, 22


_______________________________________________


Task 3: Unit Tests
You will be provided with another skeleton for this problem. Open the new skeleton as a new project and write tests for the ToyStore class. The class will have some methods, fields, and one constructor, all of them working properly. You are NOT ALLOWED to change any class. Cover the whole class with unit tests to make sure that the class is working as intended. Submit only the test folder.

_______________________________________________