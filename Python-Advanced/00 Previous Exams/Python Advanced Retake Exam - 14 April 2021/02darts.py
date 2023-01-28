##################################### variant 01 #####################################
from collections import deque

size = 7
player_names = deque(input().split(', '))
players_result = {player_names[0]: [501, 0],
                  player_names[1]: [501, 0]}
board = [input().split() for row in range(size)]

while True:
    coordinates = input()
    if not coordinates:
        break
    row, col = tuple(map(int, coordinates[1:-1].split(', ')))
    current_player = player_names.popleft()
    players_result[current_player][1] += 1
    if 0 <= row < size and 0 <= col < size:
        symbol = board[row][col]
        hit = 0
        if symbol == 'D':
            hit = 2 * (int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1]))
        elif symbol == 'T':
            hit = 3 * (int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1]))
        elif symbol == 'B':
            players_result[current_player][0] = 0
            break
        else:
            hit = int(symbol)
        players_result[current_player][0] -= hit
        if players_result[current_player][0] <=0:
            break
    player_names.append(current_player)

game_result = dict(sorted(players_result.items(), key=lambda x: (x[1][0])))
winner = list(game_result.keys())[0]
turns = game_result[winner][1]
print(f'{winner} won the game with {turns} throws!')
##################################### variant 02 #####################################
from collections import deque

size = 7
player_names = deque(input().split(', '))
players_result = {player_names[0]: [501, 0],
                  player_names[1]: [501, 0]}
board = [input().split() for row in range(size)]

options = {'D': 2,
           'T': 3,
           'B': 501}

while True:
    coordinates = input()
    if not coordinates:
        break
    row, col = tuple(map(int, coordinates[1:-1].split(', ')))
    current_player = player_names.popleft()
    players_result[current_player][1] += 1
    if 0 <= row < size and 0 <= col < size:
        symbol = board[row][col]
        hit = 0

        try:
            hit = options[symbol] * (
                    int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1]))
        except KeyError:
            hit = int(symbol)
        players_result[current_player][0] -= hit
        if players_result[current_player][0] <= 0:
            break
    player_names.append(current_player)

game_result = dict(sorted(players_result.items(), key=lambda x: (x[1][0])))
winner = list(game_result.keys())[0]
turns = game_result[winner][1]
print(f'{winner} won the game with {turns} throws!')
##################################### variant 03 #####################################
from collections import deque


class Darts:

    def __init__(self, size):
        self.size = size
        self.player_names = deque()
        self.players_statistics = {}
        self.board = []

    def define_players(self):
        self.player_names = deque(input().split(', '))
        self.players_statistics = {self.player_names[0]: [501, 0],
                                   self.player_names[1]: [501, 0]}

    def create_board_field(self):
        for row in range(self.size):
            self.board.append(input().split())

    def the_darts_game(self):
        while True:
            input_line = input()
            if not input_line:
                break
            row, col = tuple(map(int, input_line[1:-1].split(', ')))
            current_player = self.player_names.popleft()
            self.players_statistics[current_player][1] += 1
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.board[row][col]
                hit = 0
                if symbol == 'D':
                    hit = 2 * (int(self.board[0][col]) + int(self.board[self.size - 1][col]) + int(
                        self.board[row][0]) + int(
                        self.board[row][self.size - 1]))
                elif symbol == 'T':
                    hit = 3 * (int(self.board[0][col]) + int(self.board[self.size - 1][col]) + int(
                        self.board[row][0]) + int(
                        self.board[row][self.size - 1]))
                elif symbol == 'B':
                    self.players_statistics[current_player][0] = 0
                    break
                else:
                    hit = int(symbol)
                self.players_statistics[current_player][0] -= hit
                if self.players_statistics[current_player][0] <= 0:
                    break
            self.player_names.append(current_player)

    def __repr__(self):
        self.players_statistics = dict(sorted(self.players_statistics.items(), key=lambda x: (x[1][0])))
        winner = list(self.players_statistics.keys())[0]
        turns = self.players_statistics[winner][1]
        return f'{winner} won the game with {turns} throws!'


size_of_board = 7
output = Darts(size_of_board)
output.define_players()
output.create_board_field()
output.the_darts_game()
print(output)


#################################### TASK CONDITION ############################
'''

                   Problem 2
Two players bare-handedly throw small sharp-pointed missiles known as darts at a 
round target known as a dartboard. Who is going to win this game?
You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
                        1	2	3	4	5	6	7
                        24	D	D	D	D	D	8
                        23	D	T	T	T	D	9
                        22	D	T	B	T	D	10
                        21	D	T	T	T	D	11
                        20	D	D	D	D	D	12
                        19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw 
for each player. The score for each turn is deducted from the player’s total score. The first player 
who reduces their score to zero or less wins the game. You are going to receive the information for 
every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
•	If a player hits outside the dartboard, he does not score any points.
•	If a player hits a number, it is deducted from his total.
•	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is 
doubled and then deducted from his total.
•	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is 
tripled and then deducted from his total.
•	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points
 and they are deducted from his total.
Your job is to find who won the game and with how many turns.
Input
•	The name of the first player and the name of the second player, separated by ", "
•	7 lines – the dartboard (separated by single space)
•	On the next lines - the coordinates in the format: "({row}, {column})"
Output
•	You should print only one line containing the winner and his count of throws: 
"{name} won the game with {count_turns} throws!"
Constrains
•	There will always be exactly 7 lines
•	There will always be a winner
•	The points will be in range [1, 24]
•	The coordinates will be in range [0, 100]

_______________________________________________
Example_01

Input
Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)

Output
Ivan won the game with 1 throws!

Explanation
Ivan hits the Bullseye and wins the game. The program ends.

_______________________________________________
Example_02

Input
George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)

Output
Hristo won the game with 4 throws!

Explanation
George 1st throw: 501 – 16 = 485
Hristo 1st throw: 501 – 144 = 357
George 2nd throw: 485 – 17 = 468
Hristo 2nd throw: 357 – 168 = 189
George 3rd throw: 468 – 110 = 358
Hristo 3rd throw: 189 – 102 = 87
George 4th throw: 358 – 17 = 341
Hristo 4th throw: 87 – 144 = -57 
Hristo wins the game. The program ends.



'''
