##################################### variant 01 #####################################
from collections import defaultdict


def check_row_col(row, col):
    if row < 0:
        row = rows_size - 1
    elif row >= rows_size:
        row = 0
    elif col < 0:
        col = cols_size - 1
    elif col >= cols_size:
        col = 0
    return row, col


rows_size, cols_size = list(map(int, input().split(', ')))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

names = {'D': 'Christmas decorations', 'G': 'Gifts', 'C': 'Cookies'}
items_to_collect = defaultdict(int)
matrix = []
my_loc = []
collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
for row in range(rows_size):
    line = input().split()
    matrix.append(line)
    for col in range(cols_size):
        symbol = line[col]
        if symbol == 'Y':
            my_loc = [row, col]
        elif symbol in names:
            items_to_collect[names[symbol]] += 1

collected = False
while not collected:
    command = input().split('-')
    if command[0] == 'End':
        break

    way, steps = command[0], int(command[1])

    for step in range(1, steps + 1):
        matrix[my_loc[0]][my_loc[1]] = 'x'
        my_row = my_loc[0] + directions[way][0]
        my_col = my_loc[1] + directions[way][1]
        my_row, my_col = check_row_col(my_row, my_col)
        my_loc = [my_row, my_col]
        symbol = matrix[my_row][my_col]
        if symbol in names:
            collected_items[names[symbol]] += 1
        matrix[my_loc[0]][my_loc[1]] = 'Y'
        if sum(items_to_collect.values()) == sum(collected_items.values()):
            collected = True
            break
if collected:
    print('Merry Christmas!')
print("You've collected:")
print('\n'.join(f'- {value} {key}' for key, value in collected_items.items()))
print('\n'.join(' '.join(row) for row in matrix))


##################################### variant 02 #####################################
from collections import defaultdict


class NorthPole:

    def __init__(self, size_rows, size_cols):
        self.size_rows = size_rows
        self.size_cols = size_cols
        self.nort_pole = []
        self.my_loc = []
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        self.names = {'D': 'Christmas decorations', 'G': 'Gifts', 'C': 'Cookies'}
        self.items_to_collect = defaultdict(int)
        self.collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
        self.collected = False
        self.output_message = ''

    def create_nort_pole_map(self):
        for row in range(self.size_rows):
            line = input().split()
            for col in range(self.size_cols):
                symbol = line[col]
                if symbol == 'Y':
                    self.my_loc = [row, col]
                elif symbol in self.names:
                    self.items_to_collect[self.names[symbol]] += 1
            self.nort_pole.append(line)

    def check_row_col(self, row, col):
        if row < 0:
            row = self.size_rows - 1
        elif row >= self.size_rows:
            row = 0
        elif col < 0:
            col = self.size_cols - 1
        elif col >= self.size_cols:
            col = 0
        return row, col

    def santa_search_for_gifts(self):
        while not self.collected:
            command = input().split('-')
            if command[0] == 'End':
                break

            way, steps = command[0], int(command[1])

            for step in range(1, steps + 1):
                self.nort_pole[self.my_loc[0]][self.my_loc[1]] = 'x'
                my_row = self.my_loc[0] + self.directions[way][0]
                my_col = self.my_loc[1] + self.directions[way][1]
                my_row, my_col = self.check_row_col(my_row, my_col)
                self.my_loc = [my_row, my_col]
                symbol = self.nort_pole[my_row][my_col]
                if symbol in self.names:
                    self.collected_items[self.names[symbol]] += 1
                self.nort_pole[self.my_loc[0]][self.my_loc[1]] = 'Y'
                if sum(self.items_to_collect.values()) == sum(self.collected_items.values()):
                    self.collected = True
                    break

    def process_result(self):
        if self.collected:
            self.output_message = 'Merry Christmas!\n'
        self.output_message += "You've collected:\n"
        self.output_message += '\n'.join(f'- {value} {key}' for key, value in self.collected_items.items())
        self.output_message += '\n' + '\n'.join(' '.join(row) for row in self.nort_pole)

    def __repr__(self):
        return f'{self.output_message}'


rows_size, cols_size = list(map(int, input().split(', ')))

output = NorthPole(rows_size, cols_size)
output.create_nort_pole_map()
output.santa_search_for_gifts()
output.process_result()
print(output)

#################################### TASK CONDITION ############################
'''

                        02. North Pole Challenge
 
You are visiting Santa Claus' workshop, and it is complete chaos. You will need to 
help Santa find all items scattered around the workshop. You will be given the size of
the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented as some 
symbols separated by a single space:
•	Your position is marked with the symbol "Y"
•	Christmas decorations are marked with the symbol "D"
•	Gifts are marked with the symbol "G"
•	Cookies are marked with the symbol "C"
•	All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". 
The commands will be in the format "right/left/up/down-{steps}". You should move in the 
given direction with the given steps and collect all the items that come across. If you go out of 
the field, you should continue to traverse the field from the opposite side in the same direction. 
You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program 
and print: "Merry Christmas!".
Input
•	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
•	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
•	On the following lines, you will receive commands in the format described above until
 you receive the command "End" or until you collect all items.
Output
•	On the first line, if you have collected all items, print:
o	"Merry Christmas!"
o	Otherwise, skip the line
•	Next, print the number of collected items in the format:
o	"You've collected:
o	- {number_of_decoration} Christmas decorations
o	- {number_of_gifts} Gifts
o	- {number_of_cookies} Cookies"
•	Finally, print the field, as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one item
•	The dimensions of the matrix will be integers in the range [1, 20]
•	The field will always have only one "Y"
•	On the field, there will always be only the symbols shown above.

_______________________________________________
Example_01

Input
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End

Output
You've collected:
- 2 Christmas decorations
- 1 Gifts
- 0 Cookies
. . . . .
C . . G .
. C . . .
G . Y C .
x x x x x
x . x x x

_______________________________________________
Example_02

Input
5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3

Output
Merry Christmas!
You've collected:
- 2 Christmas decorations
- 0 Gifts
- 3 Cookies
. . . . . .
. . . . . .
x x x x . .
. . . x . .
. . . Y . .

_______________________________________________
Example_03

Input
5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End

Output
You've collected:
- 0 Christmas decorations
- 0 Gifts
- 0 Cookies
x .
Y x
x x
x .
x G

'''
