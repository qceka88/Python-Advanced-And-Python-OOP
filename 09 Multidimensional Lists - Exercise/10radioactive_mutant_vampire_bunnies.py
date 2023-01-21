from collections import deque


class RadioactiveBunnies:

    def __init__(self):
        self.output_message = ''
        self.rows = 0
        self.cols = 0
        self.lair = []
        self.player_pos = []
        self.bunnies_locations = deque()
        self.actions = deque()
        self.dead = False
        self.exit = False
        self.moves = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_for_lair()
        self.fill_lair_with_elements()
        self.define_commands_for_player()
        self.start_to_play_the_game()
        self.prepare_output_message()

    def define_rows_cols_for_lair(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def fill_lair_with_elements(self):
        for row in range(self.rows):
            line = list(input())
            self.lair.append(line)
            if 'P' in line:
                self.player_pos = [row, line.index('P')]

    def define_commands_for_player(self):
        self.actions = deque(input())

    def start_to_play_the_game(self):
        while self.actions and not self.dead and not self.exit:
            self.move_player_in_lair_field(self.actions.popleft())
            self.spread_bunnies_in_lair_field()

    def move_player_in_lair_field(self, way):
        self.lair[self.player_pos[0]][self.player_pos[1]] = '.'
        row = self.player_pos[0] + self.moves[way][0]
        col = self.player_pos[1] + self.moves[way][1]
        if 0 <= row < self.rows and 0 <= col < self.cols:
            symbol = self.lair[row][col]
            if symbol == 'B':
                self.dead = True
            else:
                self.lair[row][col] = 'P'
            self.player_pos = [row, col]
        else:
            self.exit = True

    def spread_bunnies_in_lair_field(self):
        self.find_existing_bunnies()
        while self.bunnies_locations:
            bunny = self.bunnies_locations.popleft()
            self.move_bunny_on_field(bunny)

    def find_existing_bunnies(self):
        for row in range(self.rows):
            for col in range(self.cols):
                symbol = self.lair[row][col]
                if symbol == 'B':
                    self.bunnies_locations.append([row, col])

    def move_bunny_on_field(self, bunny):
        for move in self.moves:
            row_bunny = bunny[0] + self.moves[move][0]
            col_bunny = bunny[1] + self.moves[move][1]
            if 0 <= row_bunny < self.rows and 0 <= col_bunny < self.cols:
                symbol = self.lair[row_bunny][col_bunny]
                if symbol in ['.', 'P']:
                    if symbol == 'P':
                        self.dead = True
                    self.lair[row_bunny][col_bunny] = 'B'

    def prepare_output_message(self):
        self.output_message = '\n'.join(''.join(r) for r in self.lair)
        self.output_message += f'\n{"dead:" if self.dead else "won:"} {" ".join(map(str, self.player_pos))}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(RadioactiveBunnies())


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
