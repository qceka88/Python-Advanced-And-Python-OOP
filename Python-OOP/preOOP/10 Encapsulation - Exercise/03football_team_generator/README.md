Problem description

                3.	Football Team Generator


Create a separate file for each class as shown below and submit a zip file containing 
all files (zip the whole project folder/module) - it is important to include all files 
in the project module to make proper imports.
Create a class called Player. Upon initialization, it should receive:
•	Private attribute name: string
•	Private attribute sprint: int
•	Private attribute dribble: int
•	Private attribute passing: int
•	Private attribute shooting: int
You should create property only for the name of the player. The class should also have one additional method:
Override the __str__() method of the class so it returns:
"Player: {name}
Sprint: {sprint}
Dribble: {dribble}
Passing: {passing}
Shooting: {shooting}"
Create a class called Team. Upon initialization, it should receive:
•	Private attribute name: string
•	Private attribute rating: int
The class should also have a private instance attribute - players: list - empty list upon 
initialization that will contain all the players (objects)
The Team class have the following methods:
•	add_player(player: Player)
o	If the player is already in the team, return "Player {name} has already joined"
o	Otherwise, add the player to the team and return "Player {name} joined team {team_name}"
•	remove_player(player_name: str)
o	Remove the player and return him
o	If the player is not in the team, return "Player {player_name} not found"
Examples


_______________________________________________
Example

p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)


print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)

print("Points passing:", p._Player__passing)

print("Points shooting:", p._Player__shooting)


print("\ncalling the __str__ method")

print(p)

print("\nAbout the team")

t = Team("Best", 10)

print("Team name:", t._Team__name)

print("Teams points:", t._Team__rating)


print("Teams players:", len(t._Team__players))

print(t.add_player(p))

print(t.add_player(p))

print("Teams players:", len(t._Team__players))

print(t.remove_player("Pall"))

print(t.remove_player("Pall"))




Output

Player name: Pall

Points sprint: 1

Points dribble: 3

Points passing: 5

Points shooting: 7

calling the __str__ method

Player: Pall

Sprint: 1

Dribble: 3

Passing: 5

Shooting: 7


About the team

Team name: Best

Teams points: 10

Teams players: 0

Player Pall joined team Best

Player Pall has already joined

Teams players: 1

Player: Pall

Sprint: 1


Dribble: 3

Passing: 5

Shooting: 7

Player Pall not found



