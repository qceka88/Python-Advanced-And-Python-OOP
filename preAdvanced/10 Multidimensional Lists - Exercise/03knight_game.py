##################################### variant 01 #####################################
size = int(input())
matrix = [list(input()) for row in range(size)]

directions = (
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)
removed_horses = 0
while True:
    max_hits = 0
    horse_to_remove = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'K':
                hits = 0
                current_horse_position = [row, col]
                for dir in directions:
                    horse_row = row + dir[0]
                    horse_col = col + dir[1]
                    if 0 <= horse_row < size and 0 <= horse_col < size:
                        if matrix[horse_row][horse_col] == 'K':
                            hits += 1
                if hits > max_hits:
                    max_hits = hits
                    horse_to_remove = current_horse_position
    if max_hits > 0:
        matrix[horse_to_remove[0]][horse_to_remove[1]] = '0'
        removed_horses += 1
    else:
        break
print(removed_horses)


##################################### variant 02 #####################################
class Game:
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix
        self.path = (
            (-2, 1),
            (-2, -1),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (1, 2),
            (1, -2),
        )

    def hits_check(self):
        hits = 0
        for direction in self.path:
            horse_row = self.row + direction[0]
            horse_col = self.col + direction[1]
            if 0 <= horse_row < len(self.matrix) and 0 <= horse_col < len(self.matrix[self.row]):
                if self.matrix[horse_row][horse_col] == 'K':
                    hits += 1

        return hits


class FindHorses:

    def __init__(self, matrix):
        self.matrix = matrix
        self.max_hits = 0
        self.horse_location = []

    def check_field(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col] == 'K':
                    target = Game(row, col, self.matrix).hits_check()

                    if target > self.max_hits:
                        self.max_hits = target
                        self.horse_location = [row, col]

    def return_to_main(self):
        return self.max_hits, self.horse_location


class Main:

    def __init__(self, size, matrix):
        self.size = size
        self.matrix = matrix
        self.removed_horses = 0

    def chess_game(self):
        while True:
            horse_object = FindHorses(self.matrix)
            horse_object.check_field()
            hits = horse_object.return_to_main()[0]
            if hits > 0:
                horse_row = horse_object.return_to_main()[1][0]
                horse_col = horse_object.return_to_main()[1][1]
                self.matrix[horse_row][horse_col] = '0'
                self.removed_horses += 1
            else:
                break

    def __repr__(self):
        return str(self.removed_horses)


size_of_matrix = int(input())
chess_table = [list(input()) for row in range(size_of_matrix)]

output = Main(size_of_matrix, chess_table)
output.chess_game()
print(output)


#################################### TASK CONDITION ############################
"""
                             3.	Knight Game
Chess is the oldest game, but it is still popular these days. 
It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated. 
It can move to the nearest square but not on the same row, column, 
or diagonal. (e.g., it can move two squares horizontally, then one 
square vertically, or it can move one square horizontally then two 
squares vertically - i.e., in an "L" pattern.) 
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. 
Your task is to remove knights until no knights that can attack one 
another with one move are left.  Always remove the knight who can attack 
the greatest number of knights. If there are two or more knights with the 
same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.
Constraints
•	The size of the board will be 0 < N < 30
•	Time limit: 0.3 sec. Memory limit: 16 MB

____________________________________________________________________________________________
Example_01

Input				
5 
0K0K0
K000K
00K00
K000K
0K0K0	

Output
1

____________________________________________________________________________________________
Example_02

Input
2
KK
KK	

Output
0	

____________________________________________________________________________________________
Example_03

Input
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK	

Output
12

"""