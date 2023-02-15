class Submarine:

    def __init__(self):
        self.submarine_health = 3
        self.submarine_pos = []


class Cruisers:

    def __init__(self):
        self.enemy_ships = 3


class Ocean:

    def __init__(self):
        self.size = int(input())
        self.water_field = []

    def create_battle_field_in_ocean(self, submarine_obj: Submarine):
        for row in range(self.size):
            line = list(input())
            if 'S' in line:
                submarine_obj.submarine_pos = [row, line.index('S')]
            self.water_field.append(line)


class Battle:

    def __init__(self, submarine: Submarine, enemy: Cruisers, ocean: Ocean):
        self.submarine = submarine
        self.enemy = enemy
        self.ocean = ocean
        self.moves = {"up": (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    def start_battle(self, move):
        def move_submarine_in_the_ocean():
            symbol = self.ocean.water_field[self.submarine.submarine_pos[0]][self.submarine.submarine_pos[1]]

            if symbol == 'C':
                self.enemy.enemy_ships -= 1
            elif symbol == '*':
                self.submarine.submarine_health -= 1

        self.ocean.water_field[self.submarine.submarine_pos[0]][self.submarine.submarine_pos[1]] = '-'
        self.submarine.submarine_pos = [
            self.submarine.submarine_pos[0] + self.moves[move][0],
            self.submarine.submarine_pos[1] + self.moves[move][1]
        ]
        move_submarine_in_the_ocean()


class CommandActions:

    def __init__(self, data):
        self.data = data
        self.commands = []

    def define_commands(self):

        def end_game():
            if self.data.enemy.enemy_ships == 0:
                return True
            if self.data.submarine.submarine_health == 0:
                return True

        while True:
            input_line = input()
            self.data.start_battle(input_line)

            if end_game():
                r, c = [self.data.submarine.submarine_pos[0], self.data.submarine.submarine_pos[1]]
                self.data.ocean.water_field[r][c] = 'S'
                break


class BattleResult:

    def __init__(self, data):
        self.data = data
        self.result = []
        self.__define_result()

    def __define_result(self):
        r, c = self.data.submarine.submarine_pos
        if self.data.submarine.submarine_health == 0:
            self.result.append(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")

        if self.data.enemy.enemy_ships == 0:
            self.result.append("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

        [self.result.append(''.join(row)) for row in self.data.ocean.water_field]

    def __str__(self):
        return '\n'.join(self.result)


if __name__ == '__main__':
    submarine = Submarine()
    enemy = Cruisers()
    field = Ocean()
    field.create_battle_field_in_ocean(submarine)
    battle = Battle(submarine, enemy, field)
    commands = CommandActions(battle)
    commands.define_commands()
    result_of_battle = BattleResult(battle)
    print(result_of_battle)

#################################### TASK CONDITION ############################
'''

                             02. Navy Battle
1914, September 22 – German submarine U-9 sinks three unescorted British armored cruisers 
HMS Aboukir, HMS Hogue, and HMS Cressy in approximately one hour. Imagine that they had the 
technology to make themselves a navigational program for the submarine and you are chosen to 
implement the logic. Navigate U-9 through the battlefield, find and sink the British cruisers 
in the dark night, avoiding the floating mines all over the North Sea. You will be given an 
integer n for the size of the battlefield (square shape). On the next n lines, you will receive 
the rows of the battlefield. The submarine will start at a random position, marked with the letter 'S'. 
The submarine surveys the surrounding area through its periscope, so it has to climb up to periscope 
depth, where it might run across naval mines. When the submarine receives direction, it goes deep and 
moves one position toward the given direction. On each turn, you will be guiding the submarine and 
giving it the direction, in which it should move. The commands will be "up", "down", "left" and "right".
When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
•	If a position with '-' (dash) is reached, it means that the field is empty and the
 submarine awaits its next direction.
•	If it runs across a naval mine ('*'), the submarine takes serious damage. 
When a mine is blown, the position of the mine will be marked with '-' (dash). U-9 can withstand 
two hits from naval mines.  The third time the submarine is hit by a mine, it disappears
and the mission is failed. The battle is over and the following message should be printed 
on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
•	If a battle cruiser is reached ('C'), the submarine destroys it and the position of 
the destroyed cruiser will be marked with '-' (dash).
•	If this is the last (third) battle cruiser on the battlefield, the battle is over and 
the following message should be printed on the Console: "Mission accomplished, U-9 has 
destroyed all battle cruisers of the enemy!" The program will end when the battle is over 
(All battle cruisers are destroyed or the submarine hits mines three times).
Input
•	On the first line, you are given the integer n – the size of the matrix (wall).
•	The next n lines hold the values for every row (NOT separated by anything).
•	On each of the next lines you will get a direction command.
Output
•	If all battle cruisers are destroyed, print: "Mission accomplished, 
U-9 has destroyed all battle cruisers of the enemy!"
•	If U-9 is hit by a mine three times, print: "Mission failed, 
U-9 disappeared! Last known coordinates [{row}, {col}]!".
•	At the end, print the final state of the matrix (battlefield)
 with the last known U-9’s position on it.
Constraints
•	The size of the square matrix (battlefield) will be between [4…10].
•	U-9’s starting position will always be marked with 'S'.
•	There will be always three battle cruisers - fields marked with 'C'.
•	There will be always enough mines on the battlefield to destroy the submarine.
•	The commands given will direct the submarine only in the limits of the battlefield.

_______________________________________________
Example_01

Input
5
*--*-
-S-*C
-*---
-----
-C-*C
right
down
left
up
right
right
right
down
down
down
up
left
left
left
down	

Output
Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!
*--*-
-----
-----
-----
-S-*-

_______________________________________________
Example_02

Input
5
*--*-
-S-*C
-*---
-----
*C-*C
right
right
up
left
left
left	

Output
Mission failed, U-9 disappeared! Last known coordinates [0, 0]!
S----
----C
-*---
-----
*C-*C


'''
