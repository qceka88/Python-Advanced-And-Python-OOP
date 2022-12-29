##################################### variant 01 #####################################
def spread_bunnies(is_dead, matrix, bunnies):
    for bunny in bunnies:
        for move in moves.values():
            bunny_row = bunny[0] + move[0]
            bunny_col = bunny[1] + move[1]
            if 0 <= bunny_row < rows and 0 <= bunny_col < cols:
                if matrix[bunny_row][bunny_col] == '.' or matrix[bunny_row][bunny_col] == 'P':
                    if matrix[bunny_row][bunny_col] == 'P':
                        is_dead = True
                    matrix[bunny_row][bunny_col] = 'B'
    bunnies.clear()
    return is_dead, matrix, bunnies


rows, cols = tuple(map(int, input().split()))

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

lair = []
player_pos = []
bunnies_locs = []

for row in range(rows):
    line = list(input())
    lair.append(line)
    if 'P' in line:
        player_pos = [row, line.index('P')]

command_line = list(input())

escape = False
dead = False
for act in command_line:
    lair[player_pos[0]][player_pos[1]] = '.'
    player_row = player_pos[0] + moves[act][0]
    player_col = player_pos[1] + moves[act][1]

    if 0 <= player_row < rows and 0 <= player_col < cols:
        if lair[player_row][player_col] == 'B':
            dead = True
        else:
            lair[player_row][player_col] = 'P'
        player_pos = [player_row, player_col]
    else:
        escape = True
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'B':
                bunnies_locs.append([row, col])
    dead, lair, bunnies_locs = spread_bunnies(dead, lair, bunnies_locs)
    if escape or dead:
        break

print(*[''.join(row) for row in lair], sep='\n')
if dead:
    print(f'dead: {" ".join(map(str, player_pos))}')
elif escape:
    print(f'won: {" ".join(map(str, player_pos))}')
##################################### variant 02 #####################################

from collections import deque


class VampireBunnies:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lair = []
        self.player_pos = []
        self.command_line = deque()
        self.escape = False
        self.dead = False
        self.moves = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        self.message = ''

    def create_lair_matrix(self):
        for row in range(self.rows):
            line = list(input())
            self.lair.append(line)
            if 'P' in line:
                self.player_pos = [row, line.index('P')]

    def create_commands(self):
        self.command_line = deque(input())

    def spread_bunnies(self):
        bunnies_locs = deque()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.lair[row][col] == 'B':
                    bunnies_locs.append([row, col])
        while bunnies_locs:
            current_bunny = bunnies_locs.popleft()
            for move in self.moves.values():
                bunny_row = current_bunny[0] + move[0]
                bunny_col = current_bunny[1] + move[1]
                if 0 <= bunny_row < self.rows and 0 <= bunny_col < self.cols:
                    if self.lair[bunny_row][bunny_col] in ('.', 'P'):
                        if self.lair[bunny_row][bunny_col] == 'P':
                            self.dead = True
                        self.lair[bunny_row][bunny_col] = 'B'

    def player_move(self, move):
        self.lair[self.player_pos[0]][self.player_pos[1]] = '.'
        player_row = self.player_pos[0] + self.moves[move][0]
        player_col = self.player_pos[1] + self.moves[move][1]

        if 0 <= player_row < self.rows and 0 <= player_col < self.cols:
            if self.lair[player_row][player_col] == 'B':
                self.dead = True
            else:
                self.lair[player_row][player_col] = 'P'
            self.player_pos = [player_row, player_col]
        else:
            self.escape = True

    def action(self):
        while self.command_line:
            self.player_move(self.command_line.popleft())
            self.spread_bunnies()
            if self.escape or self.dead:
                break

    def result_of_game(self):
        self.message += '\n'.join([''.join(row) for row in self.lair])
        if self.dead:
            self.message += f'\ndead: {" ".join(map(str, self.player_pos))}'
        elif self.escape:
            self.message += f'\nwon: {" ".join(map(str, self.player_pos))}'

    def __repr__(self):
        return f'{self.message}'


rows_of_lair, cols_of_lair = tuple(map(int, input().split()))
output = VampireBunnies(rows_of_lair, cols_of_lair)
output.create_lair_matrix()
output.create_commands()
output.action()
output.result_of_game()
print(output)

#################################### TASK CONDITION ############################
"""
                10.	*Radioactive Mutant Vampire Bunnies
You come across an old JS Basics teamwork game. It is about bunnies that 
multiply extremely fast. There's also a player that should escape from their 
lair. You like the game, so you decide to port it to Python because that's 
your language of choice. The last thing left is the algorithm that determines 
if the player will escape the lair or not. First, you will receive a line 
holding integers N and M, representing the  lair's rows and columns. 
Next, you receive N strings that can consist only of ".", "B", "P". They 
represent the initial state of the lair. There will be only one player. 
The bunnies are marked with "B", the player is marked with "P", and 
everything else is free space, marked with a dot ".".  Then you will receive 
a string with commands (e.g., LRRULUD) - each letter represents the next move
of the player:
•	L - the player should move one position to the left
•	R - the player should move one position to the right
•	U - the player should move one position up
•	D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. 
If the player moves to a bunny cell or a bunny reaches the player, the player dies. 
If the player goes out of the lair without encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn 
continue (e.g., all the bunnies spread normally), but there are no more turns. 
There will be no cases where the moves of the player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. 
On the last line, print either "dead: {row} {col}" or "won: {row} {col}". 
"Row" and "col" are the cell coordinates where the player has died or the last 
cell he has been in before escaping the lair.
Input
•	On the first line of input, the numbers N and M are 
received - the number of rows and columns in the lair
•	On the following N lines, each row is received in the form of a
string. The string will contain only ".", "B", "P". All strings will 
be the same length. There will be only one "P" for all the input
•	On the last line, the directions are received in the form of a string, 
containing "R", "L", "U", "D"
Output
•	On the first N lines, print the final state of the bunny lair
•	On the last line, print:
o	If the player won - "won: {row} {col}"
o	If the player dies - "dead: {row} {col}"
Constraints
•	The dimensions of the lair are in the range [3…20]
•	The directions string length is in the range [1…20]

____________________________________________________________________________________________
Example_01

Input
5 6
.....P
......
...B..
......
......
ULDDDR

Output
......
...B..
..BBB.
...B..
......
won: 0 5	

____________________________________________________________________________________________
Example_02

Input
4 5
.....
.....
.B...
...P.
LLLLLLLL

Output
.B...
BBB..
BBBB.
BBB..
dead: 3 1

____________________________________________________________________________________________
Example_01

Input
5 8
.......B
...B....
....B..B
........
..P.....
ULLL

Output
BBBBBBBB
BBBBBBBB
BBBBBBBB
.BBBBBBB
..BBBBBB
won: 3 0



"""
