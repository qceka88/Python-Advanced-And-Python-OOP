##################################### variant 01 #####################################

size_of_matrix = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

ocean = []
submarine_loc = []
submarine_health = 3
battle_cruisers = 3

for row in range(size_of_matrix):
    line = list(input())
    ocean.append(line)
    if 'S' in line:
        submarine_loc = [row, line.index('S')]
        ocean[row][submarine_loc[1]] = '-'

move = input()
while move:
    submarine_row = submarine_loc[0] + directions[move][0]
    submarine_col = submarine_loc[1] + directions[move][1]

    cell = ocean[submarine_row][submarine_col]
    submarine_loc = [submarine_row, submarine_col]
    ocean[submarine_row][submarine_col] = '-'
    if cell == 'C':
        battle_cruisers -= 1
    elif cell == '*':
        submarine_health -= 1
    if battle_cruisers == 0 or submarine_health == 0:
        break

    move = input()

ocean[submarine_loc[0]][submarine_loc[1]] = 'S'
if not battle_cruisers:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
if not submarine_health:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_loc[0]}, {submarine_loc[1]}]!")
print('\n'.join(''.join(row) for row in ocean))


##################################### variant 02 #####################################
class BattleField:

    def __init__(self, size):
        self.size = size
        self.ocean = []
        self.submarine_loc = []
        self.submarine_health = 3
        self.battle_cruisers = 3
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.log = ''

    def create_ocean_matrix(self):
        for row in range(self.size):
            line = list(input())
            self.ocean.append(line)
            if 'S' in line:
                self.submarine_loc = [row, line.index('S')]
                self.ocean[row][self.submarine_loc[1]] = '-'

    def battle(self):
        move = input()
        while move:
            submarine_row = self.submarine_loc[0] + self.directions[move][0]
            submarine_col = self.submarine_loc[1] + self.directions[move][1]

            cell = self.ocean[submarine_row][submarine_col]
            self.submarine_loc = [submarine_row, submarine_col]
            self.ocean[submarine_row][submarine_col] = '-'
            if cell == 'C':
                self.battle_cruisers -= 1
            elif cell == '*':
                self.submarine_health -= 1
            if self.battle_cruisers == 0 or self.submarine_health == 0:
                break

            move = input()
        self.ocean[self.submarine_loc[0]][self.submarine_loc[1]] = 'S'

    def __repr__(self):
        if not self.battle_cruisers:
            self.log += 'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!'
        if not self.submarine_health:
            row, col = self.submarine_loc[0], self.submarine_loc[1]
            self.log += f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
        self.log += '\n' + '\n'.join(''.join(row) for row in self.ocean)
        return self.log

size_of_matrix = int(input())
output = BattleField(size_of_matrix)
output.create_ocean_matrix()
output.battle()
print(output)

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