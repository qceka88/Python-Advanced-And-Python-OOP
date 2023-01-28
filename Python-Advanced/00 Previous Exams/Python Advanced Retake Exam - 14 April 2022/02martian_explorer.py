##################################### variant 01 #####################################
size = 6
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
deposits = {'M': 'Metal', 'W': 'Water', 'C': 'Concrete'}

mars = []
rover_location = []
founded_deposits = set()
for row in range(size):
    line = input().split()
    if 'E' in line:
        rover_location = [row, line.index('E')]
        line[rover_location[1]] = '-'
    mars.append(line)

command_line = input().split(', ')

for direction in command_line:
    rover_row = rover_location[0] + moves[direction][0]
    rover_col = rover_location[1] + moves[direction][1]

    if rover_row < 0:
        rover_row = size - 1
    elif rover_row == size:
        rover_row = 0
    elif rover_col < 0:
        rover_col = size - 1
    elif rover_col == size:
        rover_col = 0

    symbol = mars[rover_row][rover_col]
    if symbol in deposits:
        material = deposits[symbol]
        founded_deposits.add(material)
        print(f"{material} deposit found at ({rover_row}, {rover_col})")
    elif symbol == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    rover_location = [rover_row, rover_col]

if len(founded_deposits) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")

##################################### variant 02 #####################################

class MartianExplorer:

    def __init__(self, size):
        self.size = size
        self.moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        self.deposits = {'M': 'Metal', 'W': 'Water', 'C': 'Concrete'}
        self.mars_map = []
        self.rover_loc = []
        self.command_line = []
        self.founded_deposits = set()
        self.log = []

    def create_map_of_mars(self):
        for row in range(self.size):
            input_line = input().split()
            if 'E' in input_line:
                self.rover_loc = [row, input_line.index('E')]
                input_line[self.rover_loc[1]] = '-'
            self.mars_map.append(input_line)

    def create_command_line(self):
        for command in input().split(', '):
            self.command_line.append(command)

    def searching_resources(self):
        def check_rover_location(row, col):
            if row < 0:
                row = self.size - 1
            elif row == self.size:
                row = 0
            elif col < 0:
                col = self.size - 1
            elif col == self.size:
                col = 0
            return row, col

        for direction in self.command_line:
            rover_row = self.rover_loc[0] + self.moves[direction][0]
            rover_col = self.rover_loc[1] + self.moves[direction][1]
            rover_row, rover_col = check_rover_location(rover_row, rover_col)
            symbol = self.mars_map[rover_row][rover_col]
            if symbol in self.deposits:
                material = self.deposits[symbol]
                self.founded_deposits.add(material)
                self.log.append(f"{material} deposit found at ({rover_row}, {rover_col})")
            elif symbol == 'R':
                self.log.append(f"Rover got broken at ({rover_row}, {rover_col})")
                break
            self.rover_loc = [rover_row, rover_col]

    def __repr__(self):
        if len(self.founded_deposits) < 3:
            self.log.append("Area not suitable to start the colony.")
        else:
            self.log.append("Area suitable to start the colony.")

        return '\n'.join(self.log)


size_of_matrix = 6
output = MartianExplorer(size_of_matrix)
output.create_map_of_mars()
output.create_command_line()
output.searching_resources()
print(output)


#################################### TASK CONDITION ############################
'''

                            02. Martian Explorer
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by
a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land 
on one of the given types of deposit or a rock:
•	When it lands on a deposit, you must print the coordinates of that deposit in the 
format shown below and increase its value by 1.
•	If the rover lands on a rock, it gets broken. Print the coordinates where it got 
broken in the format shown below, and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in 
the same direction. Example: If the rover is at position (3, 0) and it needs to move 
left (outside the matrix), it should be placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to
 start our colony. 
Stop the program if you run out of commands or the rover gets broken.
Input
•	On the first 6 lines, you will receive the matrix.
•	On the following line, you will receive the commands for the rover separated by a comma and a space.
Output
•	For each deposit found while you go through the commands, print out on the console: 
"{Water, Metal or Concrete} deposit found at ({row}, {col})"
•	If the rover hits a rock, print the coordinates where it got broken in the format:
 "Rover got broken at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
•	If the rover has found at least one of each deposit, print on the console:
 "Area suitable to start the colony."
•	Otherwise, print on the console: "Area not suitable to start the colony."
See examples for more clarification.

_______________________________________________
Example_01

Input
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left

Output
Water deposit found at (3, 1)
Concrete deposit found at (4, 3)
Metal deposit found at (5, 0)
Area suitable to start the colony.

_______________________________________________
Example_02

Input
R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right

Output
Water deposit found at (3, 2)
Water deposit found at (4, 3)
Rover got broken at (4, 5)
Area not suitable to start the colony.
_______________________________________________
Example_03

Input
R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left

Output
Water deposit found at (4, 3)
Metal deposit found at (3, 2)
Concrete deposit found at (3, 0)
Metal deposit found at (3, 5)
Rover got broken at (3, 4)
Area suitable to start the colony.

'''
