##################################### variant 01 #####################################
from collections import deque

size = int(input())
command_line = deque(act for act in input().split())
mine = []
total_coal = 0
collected_coal = 0
miner_location = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    mine.append(line)
    if 's' in line:
        miner_location = [row, line.index('s')]
        mine[row][miner_location[1]] = '*'
    total_coal += line.count('c')

found_exit = False
while command_line:
    act = command_line.popleft()

    miner_row = miner_location[0] + directions[act][0]
    miner_col = miner_location[1] + directions[act][1]
    if not (0 <= miner_row < size and 0 <= miner_col < size):
        continue
    miner_location = [miner_row, miner_col]
    symbol = mine[miner_row][miner_col]
    mine[miner_row][miner_col] = '*'
    if 'e' == symbol:
        found_exit = True
        break
    elif 'c' == symbol:
        collected_coal += 1

if collected_coal == total_coal:
    print(f'You collected all coal! ({miner_location[0]}, {miner_location[1]})')
elif found_exit:
    print(f'Game over! ({miner_location[0]}, {miner_location[1]})')
else:
    print(f'{total_coal-collected_coal} pieces of coal left. ({miner_location[0]}, {miner_location[1]})')
##################################### variant 02 #####################################
from collections import deque


class MinerTask:

    def __init__(self, size):
        self.size = size
        self.command_line = deque()
        self.mine = []
        self.total_coal = 0
        self.miner_location = []
        self.collected_coal = 0
        self.found_exit = False
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.message = ''

    def create_command_line(self):
        for act in input().split():
            self.command_line.append(act)

    def create_mine_matrix(self):
        for row in range(self.size):
            line = input().split()
            self.mine.append(line)
            if 's' in line:
                self.miner_location = [row, line.index('s')]
                self.mine[row][self.miner_location[1]] = '*'
            self.total_coal += line.count('c')

    def miner_in_action(self):
        while self.command_line:
            act = self.command_line.popleft()

            miner_row = self.miner_location[0] + self.directions[act][0]
            miner_col = self.miner_location[1] + self.directions[act][1]
            if not (0 <= miner_row < self.size and 0 <= miner_col < self.size):
                continue
            self.miner_location = [miner_row, miner_col]
            symbol = self.mine[miner_row][miner_col]
            self.mine[miner_row][miner_col] = '*'
            if 'e' == symbol:
                self.found_exit = True
                break
            elif 'c' == symbol:
                self.collected_coal += 1

    def result_of_mining(self):

        if self.collected_coal == self.total_coal:
            print(f'You collected all coal! ({self.miner_location[0]}, {self.miner_location[1]})')
        elif self.found_exit:
            print(f'Game over! ({self.miner_location[0]}, {self.miner_location[1]})')
        else:
            left_pieces = self.total_coal - self.collected_coal
            print(f'{left_pieces} pieces of coal left. ({self.miner_location[0]}, {self.miner_location[1]})')

    def __repr__(self):
        return f'{self.message}'


size_of_mine = int(input())
output = MinerTask(size_of_mine)
output.create_command_line()
output.create_mine_matrix()
output.miner_in_action()
output.result_of_mining()
print(output)

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
