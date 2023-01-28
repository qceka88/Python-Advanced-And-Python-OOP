##################################### variant 01 #####################################
size = 6
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)}
matrix = [input().split() for row in range(size)]
my_location = list(map(int, input()[1:-1].split(', ')))

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break
    act, move = command[0], command[1]
    try:
        value = command[2]
    except IndexError:
        pass

    my_row = my_location[0] + directions[move][0]
    my_col = my_location[1] + directions[move][1]
    symbol = matrix[my_row][my_col]

    if act == 'Create':
        if symbol == '.':
            matrix[my_row][my_col] = value
    elif act == 'Update':
        if symbol != '.':
            matrix[my_row][my_col] = value
    elif act == 'Delete':
        if symbol != '.':
            matrix[my_row][my_col] = '.'
    elif act == 'Read':
        if symbol != '.':
            print(symbol)
    my_location = [my_row, my_col]

print('\n'.join(' '.join(row) for row in matrix))

##################################### variant 02 #####################################

class CRUD:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.my_loc = []
        self.moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        self.log = []

    def create_matrix(self):
        for row in range(self.size):
            line = input().split()
            self.matrix.append(line)

    def my_initial_location(self):
        self.my_loc = list(map(int, input()[1:-1].split(', ')))

    def crud_actions(self):
        while True:
            command = input().split(', ')
            if command[0] == 'Stop':
                break
            act, way = command[0], command[1]
            try:
                value = command[2]
            except IndexError:
                pass

            my_row = self.my_loc[0] + self.moves[way][0]
            my_col = self.my_loc[1] + self.moves[way][1]
            symbol = self.matrix[my_row][my_col]
            if act == 'Create':
                if symbol == '.':
                    self.matrix[my_row][my_col] = value
            elif act == 'Update':
                if symbol != '.':
                    self.matrix[my_row][my_col] = value
            elif act == 'Delete':
                if symbol != '.':
                    self.matrix[my_row][my_col] = '.'
            elif act == 'Read':
                if symbol != '.':
                    self.log.append(symbol)
            self.my_loc = [my_row, my_col]

    def __repr__(self):
        for row in self.matrix:
            self.log.append(' '.join(row))
        return '\n'.join(self.log)


output = CRUD(6)
output.create_matrix()
output.my_initial_location()
output.crud_actions()
print(output)


#################################### TASK CONDITION ############################
'''

                              02. CRUD
The abbreviation CRUD expands to Create, Read, Update and Delete.
These are the four fundamental operations in a database.

In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information. 
It consists of:
•	Letters - on one or many positions in the table
•	Numbers - on one or many positions in the table
•	Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
•	"Create, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step in an empty position, create the given value on that position. E.g., 
if the given value is "A", and the position is empty (".") - change it to "A"
o	If the position is NOT empty, do NOT create a value on that position
•	"Update, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, update the position with the given value. E.g.,
 if the given value is "h", and the position's value is "12" - change it to "h"
o	If the position is empty, do NOT update the value on that position
•	"Delete, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, delete it, and empty the position. E.g., 
if the given position's value is "h" - change it to "."
o	If the position is already empty, do NOT delete it
•	"Read, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, print it on the console
o	If the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.
Input
•	On the first 6 lines - a matrix with positions separated by a single space
o	Letters are in the range [a-zA-Z]
o	Numbers are in the range [-100, 100]
•	On the next line - your first position in the format: "({row}, {column})"
•	On the following lines until you receive the command "Stop" - commands in the format shown above
Output
•	In the end, print the final matrix, each row on a new line, each position separated by a single space.
Constraints
•	You will always receive valid coordinates
•	You will always receive directions in the range of the table
•	You will always receive letters or numbers

_______________________________________________
Example_01

Input
. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop	

Output
t
. . . . . .
. 6 . . . .
G r e a t .
. . 10 . . .
. 95 . . 8 .
. . P . . .	

Explanation
Start from the position (1, 1).
1) The first command is "Create", the direction is "down" and the value is "r".
Create the value "r" on the empty position (2, 1). 
2) The next command is "Update", the direction is "right" and the value is "e".
We change the old value "S" on position (2, 2) with the value "e".
3) The next command is "Create", the direction is "right" and the value is "a".
Create the value "a" on the empty position (2, 3). 
4) The next command is "Read", the direction is "right". Print the value "t" on position (2, 4).
5) The next command is "Delete", the direction is "right". Delete the value "S" on position (2, 5).
6) Receive the command "Stop", print the final matrix, and end the program.

_______________________________________________
Example_02

Input
. . . . . .  
. 6 . . . .  
. T . D . O  
. . 10 A . .  
. 95 . 80 5 .  
. . P . t .   
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop

Output
. . . . . .
. 6 . . . .
. T . D . O
. . 10 A . .
. 95 . 80 5 .
. . P . t .	

_______________________________________________
Example_03

Input
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop

Output
8
i
70
H 8 . . . .
70 i . . . .
. 10 . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .	

'''
