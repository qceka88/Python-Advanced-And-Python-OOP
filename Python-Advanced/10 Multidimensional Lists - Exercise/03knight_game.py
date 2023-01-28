class KnightGame:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.chess_board = []
        self.removed_knights = 0
        self.moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (2, -1),
            (2, 1),
            (1, -2),
            (1, 2)
        ]
        self.main_meth()

    def main_meth(self):
        self.fill_chess_board_with_elements()
        self.start_attacks()

    def fill_chess_board_with_elements(self):
        self.chess_board = [list(input()) for _ in range(self.size)]

    def start_attacks(self):
        while True:
            location = self.check_for_best_attacker_knight()

            if location:
                self.chess_board[location[0]][location[1]] = '0'
                self.removed_knights += 1
            else:
                break

    def check_for_best_attacker_knight(self):
        greatest_attacker = 0
        greatest_attacker_location = []
        for row in range(self.size):
            for col in range(len(self.chess_board[row])):
                symbol = self.chess_board[row][col]
                if symbol == 'K':
                    knight_attacks = self.check_knight_attacks(row, col)
                    if knight_attacks > greatest_attacker:
                        greatest_attacker = knight_attacks
                        greatest_attacker_location = [row, col]
        return greatest_attacker_location

    def check_knight_attacks(self, row, col):
        attacks = 0
        for way in self.moves:
            knight_row = row + way[0]
            knight_col = col + way[1]
            if 0 <= knight_row < self.size and 0 <= knight_col < self.size:
                if self.chess_board[knight_row][knight_col] == 'K':
                    attacks += 1
        return attacks

    def __repr__(self):
        return str(self.removed_knights)


if __name__ == '__main__':
    print(KnightGame())


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