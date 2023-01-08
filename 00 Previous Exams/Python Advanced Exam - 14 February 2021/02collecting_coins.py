##################################### variant 01 #####################################
from math import floor

size = int(input())

moves = {"up": (-1, 0), "down": (1, 0),
         "left": (0, -1), "right": (0, 1)}

game_field = []
player_pos = []
path = []

collected_coins = 0
for row in range(size):
    input_line = input().split()
    if 'P' in input_line:
        player_pos.append([row, input_line.index('P')])
        input_line[player_pos[-1][1]] = 'v'
    game_field.append(input_line)

while True:
    command = input()
    if not command:
        break

    row, col = player_pos[-1][0] + moves[command][0], player_pos[-1][1] + moves[command][1]

    if row >= size:
        row = 0
    elif row < 0:
        row = size - 1
    elif col >= size:
        col = 0
    elif col < 0:
        col = size - 1
    player_pos.append([row, col])

    symbol = game_field[row][col]
    if symbol == 'X':
        collected_coins = floor(collected_coins / 2)
        break
    elif symbol.isdigit():
        collected_coins += int(symbol)
        game_field[row][col] = 'v'

    if collected_coins >= 100:
        break

if collected_coins >= 100:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")
print('Your path:')
print(*player_pos, sep='\n')

##################################### variant 02 #####################################
from math import floor


class CollectingCoins:

    def __init__(self, size):
        self.size = size
        self.moves = {"up": (-1, 0), "down": (1, 0),
                      "left": (0, -1), "right": (0, 1)}
        self.game_field = []
        self.player_pos = []
        self.collected_coins = 0
        self.log = ''

    def create_game_field(self):
        for row in range(self.size):
            input_line = input().split()
            if 'P' in input_line:
                self.player_pos.append([row, input_line.index('P')])
                input_line[self.player_pos[-1][1]] = 'v'
            self.game_field.append(input_line)

    def check_row_col(self, row, col):
        if row >= self.size:
            row = 0
        elif row < 0:
            row = self.size - 1
        elif col >= self.size:
            col = 0
        elif col < 0:
            col = self.size - 1
        return row, col

    def collect_the_coins(self):
        while True:
            command = input()
            if not command:
                break

            row = self.player_pos[-1][0] + self.moves[command][0]
            col = self.player_pos[-1][1] + self.moves[command][1]
            row, col = self.check_row_col(row, col)
            self.player_pos.append([row, col])

            symbol = self.game_field[row][col]
            if symbol == 'X':
                self.collected_coins = floor(self.collected_coins / 2)
                break
            elif symbol.isdigit():
                self.collected_coins += int(symbol)
                self.game_field[row][col] = 'v'

            if self.collected_coins >= 100:
                break

    def prepare_result(self):
        if self.collected_coins >= 100:
            self.log = f"You won! You've collected {self.collected_coins} coins."
        else:
            self.log = f"Game over! You've collected {self.collected_coins} coins."
        self.log += '\nYour path:'
        self.log += '\n' + '\n'.join(str(row) for row in self.player_pos)

    def __repr__(self):
        return f'{self.log}'


size_of_field = int(input())

output = CollectingCoins(size_of_field)
output.create_game_field()
output.collect_the_coins()
output.prepare_result()
print(output)



#################################### TASK CONDITION ############################
'''
                           02. Collecting Coins
You are playing a game, and your goal is to collect 100 coins.
On the first line, you will be given a number representing the size of the field with a square shape. 
On the following few lines, you will be given the field with: 
•	One player - randomly placed in it and marked with the symbol "P"
•	Numbers for coins placed at different positions of the field
•	Walls marked with "X"
After the field state, you will be given commands for the player's movement. Commands can be:
 "up", "down", "left", "right". If the command is invalid, you should ignore it. 
The player moves in the given direction with one step for each command and collects all the coins
 that come across. If he goes out of the field, he should continue to traverse the field from the 
 opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins just once (the first time).
There are only two possible outcomes of the game:
•	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded
 down to the next-lowest number.
•	The player collects at least 100 coins and wins the game.
For more clarifications, see the examples below.
Input
•	A number representing the size of the field (matrix NxN)
•	A matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will get a move command.
Output
•	If the player won the game, print: "You won! You've collected {total_coins} coins."
•	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
•	Collected coins have to be rounded down to the next-lowest number.
•	The player's path as cooridnates in lists on separate lines: 
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"
Constrains
•	There will be no case in which less than 100 coins will be in the field
•	All given numbers will be valid integers in the range [0, 100]

_______________________________________________
Example_01

Input
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

Output
You won! You've collected 125 coins.
Your path:
[3, 0]
[3, 4]
[3, 0]
[3, 1]
[2, 1]
[1, 1]
[1, 2]

_______________________________________________
Example_02

Input
8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left

Output
Game over! You've collected 0 coins.
Your path:
[5, 2]
[4, 2]
[5, 2]
[4, 2]
[4, 1]


'''