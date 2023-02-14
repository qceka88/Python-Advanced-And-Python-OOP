class ChessBoard:

    def __init__(self):
        self.SIZE = 8
        self.players = {'w': [], 'b': []}
        self.game_board = []
        self.create_chess_broad()

    def create_chess_broad(self):
        for row in range(self.SIZE):
            line = input().split()
            if 'w' in line:
                self.players['w'] = [row, line.index('w')]
            elif 'b' in line:
                self.players['b'] = [row, line.index('b')]
            self.game_board.append(line)


class CapturePawn:

    def __init__(self, pawn, board):
        self.pawn = pawn
        self.board = board
        self.diagonals = ((0, 1), (0, -1))

    def check_for_capture(self):

        for move in self.diagonals:
            pawn_col = self.board.players[self.pawn][1] + move[1]
            if 0 <= pawn_col < self.board.SIZE:
                if self.board.game_board[self.board.players[self.pawn][0]][pawn_col] != '-':
                    self.board.players[self.pawn][1] = pawn_col
                    return True
        return False


class ChessGame:

    def __init__(self, board: ChessBoard):
        self.names = {'w': 'White', 'b': 'Black'}
        self.board = board
        self.finish, self.capture = False, False
        self.start_moving_pawns()

    def start_moving_pawns(self):
        while not self.capture and not self.finish:

            for pawn in self.board.players:
                self.board.game_board[self.board.players[pawn][0]][self.board.players[pawn][1]] = '-'
                one_move = '1'
                move_direction = '-' if pawn == 'w' else '+'
                self.board.players[pawn][0] = eval(str(self.board.players[pawn][0]) + move_direction + one_move)
                self.capture = CapturePawn(pawn, self.board).check_for_capture()
                if self.capture:
                    self.board.players = {pawn: self.board.players[pawn]}
                    break
                self.board.game_board[self.board.players[pawn][0]][self.board.players[pawn][1]] = pawn
                if self.board.players[pawn][0] in [0, self.board.SIZE - 1]:
                    self.board.players = {pawn: self.board.players[pawn]}
                    self.finish = True
                    break


class Result:

    def __init__(self, game, chess):
        self.names = {'w': 'White', 'b': 'Black'}
        self.result = ''
        self.game = game
        self.chess = chess

    def prepare_result(self):
        pawn = list(self.chess.players)[0]
        letter = chr(97 + self.chess.players[pawn][1])
        number = self.chess.SIZE - self.chess.players[pawn][0]
        sector = f"{letter}{number}"
        if self.game.finish:
            self.result = f"Game over! {self.names[pawn]} pawn is promoted to a queen at {sector}."
        else:
            self.result = f"Game over! {self.names[pawn]} win, capture on {sector}."

    def __str__(self):
        return self.result


chess_board = ChessBoard()
play_chess = ChessGame(chess_board)
result_of_game = Result(play_chess, chess_board)
result_of_game.prepare_result()
print(result_of_game)

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