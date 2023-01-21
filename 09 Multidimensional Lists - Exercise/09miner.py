from collections import deque


class Miner:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.commands = deque()
        self.matrix = []
        self.miner_pos = []
        self.total_coal = 0
        self.collected_coal = 0
        self.exit = False
        self.moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        self.main_meth()

    def main_meth(self):
        self.define_commands_for_moving()
        self.fill_matrix_with_elements()
        self.start_mining_operation()
        self.prepare_output_message()

    def define_commands_for_moving(self):
        self.commands = deque(input().split())

    def fill_matrix_with_elements(self):
        for row in range(self.size):
            line = input().split()
            if 's' in line:
                self.miner_pos = [row, line.index('s')]
                line[self.miner_pos[1]] = '*'
            if 'c' in line:
                self.total_coal += line.count('c')
            self.matrix.append(line)

    def start_mining_operation(self):
        while self.commands and not self.exit:
            act = self.commands.popleft()

            row = self.miner_pos[0] + self.moves[act][0]
            col = self.miner_pos[1] + self.moves[act][1]

            if 0 <= row < self.size and 0 <= col < self.size:
                self.check_cell_for_coal_or_exit(row, col)

            if self.collected_coal == self.total_coal:
                break

    def check_cell_for_coal_or_exit(self, row, col):
        symbol = self.matrix[row][col]
        self.miner_pos = [row, col]
        if symbol == 'c':
            self.collected_coal += 1
            self.matrix[row][col] = '*'
        elif symbol == 'e':
            self.exit = True

    def prepare_output_message(self):
        if self.exit:
            self.output_message = f'Game over! ({self.miner_pos[0]}, {self.miner_pos[1]})'
        elif self.collected_coal == self.total_coal:
            self.output_message = f'You collected all coal! ({self.miner_pos[0]}, {self.miner_pos[1]})'
        else:
            left_coal = self.total_coal - self.collected_coal
            self.output_message = f'{left_coal} pieces of coal left. ({self.miner_pos[0]}, {self.miner_pos[1]})'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Miner())


#################################### TASK CONDITION ############################
"""
                                   9.	*Miner
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move. 
On the second line, you will receive the commands for the miner's movement, 
separated by a single space. The possible commands are "left", "right", "up" and "down". 
In the end, you will receive each row of the field on a separate line. 
The possible characters that may appear on the screen are:
•	* - a regular position on the field
•	e - the end of the route
•	c - coal
•	s - miner
The miner starts moving from the position "s". He should perform the given commands 
successively, moving with only one position in the given direction. If the miner has 
reached the edge of the field and the following command indicates that he has to get 
out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the 
collected coal. In the end, you should print whether the miner has succeeded in 
collecting the coal or not and his final position:
•	If the miner has collected all coal in the field, the program stops, 
and you should print the message: "You collected all coal! ({row_index}, {col_index})".
•	If the miner steps at "e", the game is over (the program stops), and you 
should print the message: "Game over! ({row_index}, {col_index})".
•	If there are no more commands and none of the above cases had happened, 
you should print the message: 
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
•	Field size - an integer number
•	Commands to move the miner - a sequence of directions, 
separated by single whitespace (" ")
•	The field: some of the following characters ("*", "e", "c ", "s"), 
separated by a single whitespace (" ")
Output
•	There are three types of output as mentioned above.
Constraints
•	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
•	The field will always have only one "s"

____________________________________________________________________________________________
Example_01

Input
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *	

Output
Game over! (1, 3)

____________________________________________________________________________________________
Example_02

Input
4
up right right right down
* * * e
* * c *
* s * c
* * * *	

Output
You collected all coal! (2, 3)

____________________________________________________________________________________________
Example_03

Input
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *	

Output
3 pieces of coal left. (5, 0)


"""
