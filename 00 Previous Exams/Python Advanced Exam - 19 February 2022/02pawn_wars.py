##################################### variant 01 #####################################
size = 8
player_location = {'w': [], 'b': []}
figure_color = {'w': 'White', 'b': 'Black'}

first_letter_ascii = 97
chess_board = []
directions_dict = {'l': (0, -1), 'r': (0, 1)}
for row in range(size):
    line = input().split()
    if 'w' in line:
        player_location['w'] = [row, line.index('w')]
    if 'b' in line:
        player_location['b'] = [row, line.index('b')]
    chess_board.append(line)

winner = False
square = ''
while not winner:

    for pawn in player_location:
        operator = '-' if pawn == 'w' else '+'
        for way in directions_dict.values():
            try_row, try_col = eval(str(player_location[pawn][0]) + operator + '1'), way[1] + player_location[pawn][1]
            if 0 <= try_row < size and 0 <= try_col < size:
                if chess_board[try_row][try_col] != '-':
                    square = chr(first_letter_ascii + try_col) + str(size - try_row)
                    winner = True
                    break
        if winner:
            print(f"Game over! {figure_color[pawn]} win, capture on {square}.")
            break
        chess_board[player_location[pawn][0]][player_location[pawn][1]] = '-'

        pawn_row = eval(str(player_location[pawn][0]) + operator + '1')
        pawn_col = player_location[pawn][1]
        player_location[pawn] = [pawn_row, pawn_col]
        chess_board[pawn_row][pawn_col] = pawn
        if pawn_row == 0 or pawn_row == size - 1:
            square = chr(first_letter_ascii + pawn_col) + str(size - pawn_row)
            print(f"Game over! {figure_color[pawn]} pawn is promoted to a queen at {square}.")
            winner = True
            break

##################################### variant 01 #####################################


class PawnWars:

    def __init__(self, size):
        self.size = size
        self.player_location = {'w': [], 'b': []}
        self.figure_color = {'w': 'White', 'b': 'Black'}
        self.first_letter_ascii = 97
        self.chess_board = []
        self.directions = {'l': (0, -1), 'r': (0, 1)}
        self.winner = False
        self.message = ''

    def create_chess_board(self):
        for row in range(self.size):
            line = input().split()
            if 'w' in line:
                self.player_location['w'] = [row, line.index('w')]
            if 'b' in line:
                self.player_location['b'] = [row, line.index('b')]
            self.chess_board.append(line)

    def check_for_capture(self, color,operator):
        for way in self.directions.values():
            try_row, try_col = eval(str(self.player_location[color][0]) + operator + '1'), way[1] + self.player_location[color][1]
            if 0 <= try_row < self.size and 0 <= try_col < self.size:
                if self.chess_board[try_row][try_col] != '-':
                    coordinates = chr(self.first_letter_ascii + try_col) + str(self.size - try_row)
                    return coordinates
        return False

    def time_to_play_the_game(self):
        while not self.winner:

            for pawn in self.player_location:
                operator = '-' if pawn == 'w' else '+'
                self.winner = self.check_for_capture(pawn, operator)
                if self.winner is not False:
                    square = self.winner
                    self.message = f"Game over! {self.figure_color[pawn]} win, capture on {square}."
                    break
                self.chess_board[self.player_location[pawn][0]][self.player_location[pawn][1]] = '-'

                pawn_row = eval(str(self.player_location[pawn][0]) + operator + '1')
                pawn_col = self.player_location[pawn][1]
                self.player_location[pawn] = [pawn_row, pawn_col]
                self.chess_board[pawn_row][pawn_col] = pawn

                if pawn_row == 0 or pawn_row == self.size - 1:
                    square = chr(self.first_letter_ascii + pawn_col) + str(self.size - pawn_row)
                    self.message = f"Game over! {self.figure_color[pawn]} pawn is promoted to a queen at {square}."
                    self.winner = True
                    break

    def __repr__(self):
        return self.message


size_of_matrix = 8

output = PawnWars(size_of_matrix)
output.create_chess_board()
output.time_to_play_the_game()
print(output)


#################################### TASK CONDITION ############################
'''
                     02. Pawn Wars
 
A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from 
number 1 to 8, and columns are marked from A to H. We have a total of 64 squares. 
Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). 
In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
	White (w) moves from the 1st rank to the 8th rank direction.
	Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:
 
When a pawn reaches the last rank (for the white one - this is the 8th rank, 
and for the black one - this is the 1st rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the bord. 
The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on. 


Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
o	Empty positions are marked with "-".
o	White pawn is marked with "w"
o	Black pawn is marked with "b"
Output
Print either one of the following:
•	If a pawn captures the other, print:
o	"Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
Constraints
•	The input will always be valid.
•	The matrix will always be 8x8.
•	There will be no case where two pawns are placed on the same square.
•	There will be no case where two pawns are placed on the same column.
•	There will be no case where black/white will be placed on the last rank.

_______________________________________________
Example_01

Input
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -	

Output
Game over! White pawn is promoted to a queen at b8.

Explanation
We start by pushing the white pawn to b4, next, we push the black pawn to g7:
- - - - - - - -
- - - - - - b -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
Then white play b5, black play g6:
- - - - - - - -
- - - - - - - -
- - - - - - b -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
…
Capturing is not possible here, so after a few more moves, the white pawn is promoted to a queen on b8.

_______________________________________________
Example_02

Input
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -	

Output
Game over! White win, capture on a3.	

Explanation
A white pawn always start first, so it must capture the black one on a3 in the first move:
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - -
- - - - - - - -
- - - - - - - -

'''