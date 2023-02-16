class Resources:

    def __init__(self):
        self.resources = []
        self.names = {"W": "Water", "M": "Metal", "C": "Concrete"}


class Rover:

    def __init__(self):
        self.position = []
        self.damaged = False
        self.status = ''


class Mars:

    def __init__(self):
        self.SIZE = 6
        self.field = []

    def create_mars_field(self, rover_obj: Rover):
        for row in range(self.SIZE):
            line = input().split()
            if "E" in line:
                rover_obj.position = [row, line.index("E")]
                line[line.index("E")] = "-"
            self.field.append(line)


class CommandActions:

    def __init__(self):
        self.commands = []

    def define_commands(self):
        self.commands = input().split(", ")


class MissionMars:

    def __init__(self, resources: Resources, rover: Rover, mars: Mars):
        self.resources = resources
        self.rover = rover
        self.mars = mars
        self.moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

    def start_of_mission(self, command_ojb: CommandActions):
        def check_boundaries(position):
            for idx in range(len(position)):
                if position[idx] < 0:
                    self.rover.position[idx] = self.mars.SIZE - 1
                elif position[idx] == self.mars.SIZE:
                    self.rover.position[idx] = 0
            return self.rover.position

        def check_square():
            symbol = self.mars.field[r][c]
            if symbol in self.resources.names:
                resource = self.resources.names[symbol]
                self.resources.resources.append([resource, [r, c]])
                self.mars.field[r][c] = '-'
            elif symbol == 'R':
                self.rover.damaged = True
                self.rover.status = f"Rover got broken at ({r}, {c})"

        for act in command_ojb.commands:
            self.rover.position = [
                self.rover.position[0] + self.moves[act][0],
                self.rover.position[1] + self.moves[act][1]
            ]
            r, c = check_boundaries(self.rover.position)
            check_square()

            if self.rover.damaged:
                break


class ResultClass:

    def __init__(self, resources: Resources, rover: Rover):
        self.resources = resources
        self.rover = rover
        self.result = []

    def prepare_result(self):
        suitable = set()
        for data in self.resources.resources:
            resource, [row, col] = data
            suitable.add(resource)
            self.result.append(f"{resource} deposit found at ({row}, {col})")
        if self.rover.damaged:
            r, c = self.rover.position
            self.result.append(f"Rover got broken at ({r}, {c})")

        if len(suitable) == 3:
            self.result.append("Area suitable to start the colony.")
        else:
            self.result.append("Area not suitable to start the colony.")

    def __str__(self):
        return '\n'.join(self.result)


deposits = Resources()
vehicle = Rover()

field = Mars()
field.create_mars_field(vehicle)

commands = CommandActions()
commands.define_commands()

mission = MissionMars(deposits, vehicle, field)
mission.start_of_mission(commands)

result = ResultClass(deposits, vehicle)
result.prepare_result()
print(result)

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
