##################################### variant 01 #####################################
size = 5
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
total_targets = 0
targets = []
trainee_location = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        trainee_location = [row, line.index('A')]
        matrix[row][trainee_location[1]] = '.'
    total_targets += line.count('x')

moves = int(input())

for _ in range(moves):
    data = input().split()
    act, direction = data[0], data[1]
    if act == 'shoot':
        row = trainee_location[0] + directions[direction][0]
        col = trainee_location[1] + directions[direction][1]
        while True:
            if 0 <= row < size and 0 <= col < size:
                if matrix[row][col] == 'x':
                    targets.append([row, col])
                    matrix[row][col] = '.'
                    break
            else:
                break
            row += directions[direction][0]
            col += directions[direction][1]

    elif act == 'move':
        value = int(data[2])
        row = trainee_location[0] + (directions[direction][0] * value)
        col = trainee_location[1] + (directions[direction][1] * value)
        if 0 <= row < size and 0 <= col < size and matrix[row][col] == '.':
            trainee_location = [row, col]
    if len(targets) == total_targets:
        break

diff = total_targets - len(targets)
if diff == 0:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {diff} targets left.')

print(*targets, sep='\n')


##################################### variant 02 #####################################

class RangeDay:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.total_targets = 0
        self.targets_location = []
        self.trainee_location = []
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

    def training_field(self):
        for row in range(self.size):
            line = input().split()
            self.matrix.append(line)
            if 'A' in line:
                self.trainee_location = [row, line.index('A')]
                self.matrix[self.trainee_location[0]][self.trainee_location[1]] = '.'
            self.total_targets += line.count('x')

    def shooting_action(self, way):
        row = self.trainee_location[0] + self.directions[way][0]
        col = self.trainee_location[1] + self.directions[way][1]
        while True:
            if not (0 <= row < self.size and 0 <= col < self.size):
                break
            if self.matrix[row][col] == 'x':
                self.targets_location.append([row, col])
                self.matrix[row][col] = '.'
                break
            row += self.directions[way][0]
            col += self.directions[way][1]

    def moving_action(self, way, steps):
        row = self.trainee_location[0] + (self.directions[way][0] * steps)
        col = self.trainee_location[1] + (self.directions[way][1] * steps)
        if 0 <= row < self.size and 0 <= col < self.size and self.matrix[row][col] == '.':
            self.trainee_location = [row, col]

    def actions(self, moves):
        for _ in range(moves):
            data = input().split()
            act, direction = data[0], data[1]
            if act == 'shoot':
                self.shooting_action(direction)
            elif act == 'move':
                self.moving_action(direction, int(data[2]))
            if len(self.targets_location) == self.total_targets:
                break

    def printing(self):
        diff = self.total_targets - len(self.targets_location)
        if diff == 0:
            print(f'Training completed! All {self.total_targets} targets hit.')
        else:
            print(f'Training not completed! {diff} targets left.')

        print(*self.targets_location, sep='\n')


size_of_matrix = 5

output = RangeDay(size_of_matrix)
output.training_field()
output.actions(int(input()))
output.printing()

#################################### TASK CONDITION ############################
"""
                              06. Range Day
You are participating in a Firearm course. It is a training day at 
the shooting range. You will be given a matrix with 5 rows and 5 columns. 
It is a shotgun range represented as some symbols separated by a single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number 
of commands you will receive. The possible commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given 
direction with the given steps. You can only move if the field you want 
to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction 
(from your current position without moving). Beware that there might be 
targets that stand in the way of other targets, and you cannot reach
them - you can shoot only the nearest target. When you have shot a target, 
the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: 
"Training completed! All {count_targets} targets hit.". 
•	If, after you perform all the commands, there are some targets left print: 
"Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
"Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, 
as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one target

____________________________________________________________________________________________
Example_01

Input
. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 

Output
1	Training not completed! 3 targets left.
[4, 1]

____________________________________________________________________________________________
Example_02

Input
. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right	

Output
Training completed! All 2 targets hit.
[4, 1]
[2, 2]

____________________________________________________________________________________________
Example_03

Input
. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left	

Output
Training not completed! 1 targets left.
[4, 1]

"""