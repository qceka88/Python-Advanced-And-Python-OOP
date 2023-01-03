##################################### variant 01 #####################################
from collections import deque

size = 6

players = deque(input().split(', '))
matrix = [[col for col in input().split()] for row in range(size)]

resting_players = {}

while True:
    input_data = input()
    if not input_data:
        break
    coordinates = list(map(int, input_data[1:-1].split(', ')))
    current_name = players.popleft()
    player_row, player_col = coordinates[0], coordinates[1]
    symbol = matrix[player_row][player_col]

    if current_name in resting_players:
        if resting_players[current_name] == 0:
            resting_players[current_name] += 1
            players.append(current_name)
            continue
        else:
            del resting_players[current_name]

    if symbol == 'E':
        print(f"{current_name} found the Exit and wins the game!")
        break
    elif symbol == 'T':
        print(f"{current_name} is out of the game! The winner is {players[0]}.")
        break
    elif symbol == 'W':
        print(f"{current_name} hits a wall and needs to rest.")
        resting_players[current_name] = 0

    players.append(current_name)
##################################### variant 02 #####################################
from collections import deque


class ExitFounder:

    def __init__(self, size):
        self.size = size
        self.players = deque()
        self.matrix = []
        self.resting_players = {}
        self.log = []

    def take_players(self):
        self.players = deque(input().split(', '))

    def create_field(self):
        for row in range(self.size):
            self.matrix.append(input().split())

    def try_to_find_exit(self):
        while True:
            input_data = input()
            if not input_data:
                break
            coordinates = list(map(int, input_data[1:-1].split(', ')))
            current_name = self.players.popleft()
            player_row, player_col = coordinates[0], coordinates[1]
            symbol = self.matrix[player_row][player_col]

            if current_name in self.resting_players:
                if self.resting_players[current_name] == 0:
                    self.resting_players[current_name] += 1
                    self.players.append(current_name)
                    continue
                else:
                    del self.resting_players[current_name]

            if symbol == 'E':
                self.log.append(f"{current_name} found the Exit and wins the game!")
                break
            elif symbol == 'T':
                self.log.append(f"{current_name} is out of the game! The winner is {self.players[0]}.")
                break
            elif symbol == 'W':
                self.log.append(f"{current_name} hits a wall and needs to rest.")
                self.resting_players[current_name] = 0

            self.players.append(current_name)

    def __repr__(self):
        return '\n'.join(self.log)


size_of_matrix = 6

output = ExitFounder(size_of_matrix)
output.take_players()
output.create_field()
output.try_to_find_exit()
print(output)

#################################### TASK CONDITION ############################
'''
                                    2. Exit Founder
 
Tom and Jerry decided to play a game together. The game is a maze of which they need 
to find a way out. Monitor their moves closely and find out who the winner will be!
First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". 
The order in which they are received determines the order in which they will take turns. 
The first player starts first. Next, you will be given a matrix with 6 rows and 6 columns 
representing the maze board. It consists of:
•	Only one Exit - marked with the "E" letter
•	Trap (one, many, or none) - marked with the "T" letter
•	Wall (one, many, or none) - marked with the "W" letter
•	Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, 
you will be receiving coordinates for each of the players. They will be taking turns and stepping 
on different positions on the board until one of them find the Exit or falls into a Trap. 
Here are the rules:
•	If a player hits the letter "E", he escapes the maze and wins the game.
o	Print "{player} found the Exit and wins the game!" and end the program.
•	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
o	Print "{player} is out of the game! The winner is {winner}." and end the program.
•	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
o	Print "{player} hits a wall and needs to rest."
•	If a player steps on an empty position ".", nothing happens. 
•	Both players can step in the same position at the same time.
Input
•	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
•	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
•	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
Output
•	You should print the output as described above.
•	The input coordinates will always be valid.

_______________________________________________
Example_01

Input
Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)	

Output
Tom hits a wall and needs to rest.
Jerry is out of the game! The winner is Tom.

Explanation
First is Tom. He moves to position (3, 2). He hits a wall and needs to rest.
Next is Jerry. He moves to position (1, 3). It is an empty position.
Tom's next move (5, 1) is ignored because he is resting.
Jerry moves to (5, 1). There is a trap, so he is out of the game. The program ends.

_______________________________________________
Example_02

Input
Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)

Output
Jerry found the Exit and wins the game!

_______________________________________________
Example_03

Input
Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)


Output
Jerry hits a wall and needs to rest.
Tom hits a wall and needs to rest.
Tom hits a wall and needs to rest.
Jerry hits a wall and needs to rest.
Tom found the Exit and wins the game!	

'''
