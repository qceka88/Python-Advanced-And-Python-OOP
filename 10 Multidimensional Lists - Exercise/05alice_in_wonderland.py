from collections import deque


class AliceInWonderland:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.wonderland = []
        self.alice_pos = []
        self.collected_teabags = 0
        self.finish = False
        self.moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.main_meth()

    def main_meth(self):
        self.create_wonderland_find_alice()
        self.alice_journey_in_wonderland()
        self.prepare_output_message()

    def create_wonderland_find_alice(self):
        for row in range(self.size):
            line = input().split()
            self.wonderland.append(line)
            if 'A' in line:
                self.alice_pos = [row, line.index('A')]
                self.wonderland[row][self.alice_pos[1]] = '*'

    def check_move_of_alice(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            symbol = self.wonderland[row][col]
            if symbol == 'R':
                self.finish = True
            elif symbol.isdigit():
                self.collected_teabags += int(symbol)
            self.wonderland[row][col] = '*'
            self.alice_pos = [row, col]
        else:
            self.finish = True

    def alice_journey_in_wonderland(self):
        while True:
            direction = input()
            if not direction:
                break
            alice_row = self.alice_pos[0] + self.moves[direction][0]
            alice_col = self.alice_pos[1] + self.moves[direction][1]
            self.check_move_of_alice(alice_row, alice_col)

            if self.collected_teabags >= 10 or self.finish:
                break

    def prepare_output_message(self):
        if self.collected_teabags >= 10:
            self.output_message = 'She did it! She went to the party.'
        elif self.finish:
            self.output_message = "Alice didn't make it to the tea party."
        self.output_message += '\n' + '\n'.join(' '.join(row) for row in self.wonderland)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(AliceInWonderland())


#################################### TASK CONDITION ############################
"""
                       5.	Alice in Wonderland
Alice is going to the mad tea party, to see her friends. On the way to 
the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory 
with a square shape. On the following n lines, you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A". 
•	On the territory, there will be bags of tea, represented as numbers. 
If Alice steps on a number position, she collects the tea bags and increases 
the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. 
Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea 
party, and she does not need to continue collecting. Otherwise, if she steps
on the rabbit hole or goes out of the territory, she can't return, and the program ends. 
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
•	On the first line, you will be given the integer n – the size of the square matrix
•	On the following n lines - matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will be given a move command
Output
•	On the first line: 
o	If Alice steps on the rabbit hole or she go out of the territory, print: 
"Alice didn't make it to the tea party."
o	If she collected at least 10 bags of tea, print: 
"She did it! She went to the party."
•	On the following lines, print the matrix.
Constraints
•	Alice will always either go outside the Wonderland or collect 10 bags of tea
•	All the commands will be valid
•	All of the given numbers will be valid integers in the range [0, 10]

____________________________________________________________________________________________
Example_01

Input
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left	

Output
Alice didn't make it to the tea party.
. * . . 1
* * * . .
4 * . 1 .
. . . 2 .
. 3 . . .

____________________________________________________________________________________________
Example_02

Input
7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right	

Output
She did it! She went to the party.
* * . 1 1 . .
* . . . 6 . 5
* * . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2


"""
