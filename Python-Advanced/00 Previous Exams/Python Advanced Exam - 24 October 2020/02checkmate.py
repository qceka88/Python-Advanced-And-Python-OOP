##################################### variant 01 #####################################

size = 8
directions = {
    'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
    'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
    'l': (0, -1), 'r': (0, 1)}

board = []
queens_positions = []
king = []

for row in range(size):
    line = input().split()
    board.append(line)

    if 'K' in line:
        king = [row, line.index('K')]

for way in directions.values():
    king_row, king_col = king
    while True:
        row = king_row + way[0]
        col = king_col + way[1]

        if 0 <= row < size and 0 <= col < size:
            symbol = board[row][col]
            if symbol == 'Q':
                queens_positions.append([row, col])
                break
        else:
            break
        king_row, king_col = row, col
if queens_positions:
    print(*queens_positions, sep='\n')
else:
    print('The king is safe!')

##################################### variant 02 #####################################
class ChessGame:

    def __init__(self, size):
        self.size = size
        self.directions = {
            'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
            'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
            'l': (0, -1), 'r': (0, 1)}
        self.board = []
        self.queens_positions = []
        self.king = []

    def create_chess_board(self):
        for row in range(self.size):
            line = input().split()
            self.board.append(line)

            if 'K' in line:
                self.king = [row, line.index('K')]

    def check_attack_queens(self):
        for way in self.directions.values():
            king_row, king_col = self.king
            while True:
                row = king_row + way[0]
                col = king_col + way[1]

                if 0 <= row < self.size and 0 <= col < self.size:
                    symbol = self.board[row][col]
                    if symbol == 'Q':
                        self.queens_positions.append([row, col])
                        break
                else:
                    break
                king_row, king_col = row, col

    def __repr__(self):
        if self.queens_positions:
            return '\n'.join(str(row) for row in self.queens_positions)
        else:
            return 'The king is safe!'


board_size = 8
output = ChessGame(board_size)
output.create_chess_board()
output.check_attack_queens()
print(output)

#################################### TASK CONDITION ############################
'''
                            02 Checkmate
 
You will be given a chess board (8x8). On the board there will be 3 types of symbols:
•	"." – empty square
•	"Q" – a queen
•	"K" – the king
Your job is to find which queens can capture the king and print them. The moves that the queen can do 
is to move diagonally, horizontally and vertically (basically all the moves that all the other figures 
can do except from the knight). Beware that there might be queens that stand in the way of other queens 
and can stop them from capturing the king. For more clarification see the examples.
Input
•	8 lines – the state of the board (each square separated by single space)
Output
•	The positions of the queens that can capture the king as lists
•	If the king cannot be captured, print: "The king is safe!"
•	The order of output does not matter
Constrains
•	There will always be exactly 8 lines
•	There will always be exactly one King
•	Only the 3 symbols described above will be present in the input

_______________________________________________
Example_01

Input
. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .	

Output
[2, 5]
[5, 1]
[1, 0]	

Explanation
The queens marked with green can capture the king. The queen marked with blue cannot
capture the king, since the queen at [5, 1] stands in the way

_______________________________________________
Example_02

Input
. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .	

Output
The king is safe!	


'''
