class RangeDay:

    def __init__(self):
        self.output_message = ''
        self.size = 5
        self.field = []
        self.player_pos = []
        self.total_targets = 0
        self.hits = []
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.actions = {
            'move': self.moving_action,
            'shoot': self.shooting_action
        }
        self.main_meth()

    def main_meth(self):
        self.create_field_find_player_position_count_targets()
        self.start_shooting_training()
        self.prepare_output_message()

    def create_field_find_player_position_count_targets(self):
        for row in range(self.size):
            line = input().split()
            if 'A' in line:
                self.player_pos = [row, line.index('A')]
            if 'x' in line:
                self.total_targets += line.count('x')
            self.field.append(line)

    def start_shooting_training(self):
        number_of_actions = int(input())
        for _ in range(number_of_actions):
            act, *data = input().split()
            self.actions[act](data)

            if len(self.hits) == self.total_targets:
                break

    def moving_action(self, data):
        way, steps = data[0], int(data[1])
        player_row = self.player_pos[0] + (self.directions[way][0] * steps)
        player_col = self.player_pos[1] + (self.directions[way][1] * steps)
        if 0 <= player_row < self.size and 0 <= player_col < self.size:
            if self.field[player_row][player_col] != 'x':
                self.player_pos = [player_row, player_col]

    def shooting_action(self, data):
        way = data[0]
        row = self.player_pos[0]
        col = self.player_pos[1]
        while True:
            row += self.directions[way][0]
            col += self.directions[way][1]
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.field[row][col]
                if symbol == 'x':
                    self.hits.append([row, col])
                    self.field[row][col] = '.'
                    break
            else:
                break

    def prepare_output_message(self):
        if len(self.hits) == self.total_targets:
            self.output_message = f'Training completed! All {self.total_targets} targets hit.'
        else:
            left_targets = self.total_targets - len(self.hits)
            self.output_message = f'Training not completed! {left_targets} targets left.'
        self.output_message += '\n' + '\n'.join(f'[{x}, {y}]' for x, y in self.hits)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(RangeDay())


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