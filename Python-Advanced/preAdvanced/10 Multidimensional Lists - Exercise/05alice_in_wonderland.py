##################################### variant 01 #####################################
size = int(input())

matrix = []
alice_location = []
tea_bags = 0
path = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        alice_location = [row, line.index('A')]
        matrix[alice_location[0]][alice_location[1]] = '*'

while tea_bags < 10:
    direction = input()
    row = alice_location[0] + path[direction][0]
    col = alice_location[1] + path[direction][1]

    if 0 <= row < size and 0 <= col < size:
        symbol = matrix[row][col]
        alice_location = [row, col]
        matrix[row][col] = '*'
        if symbol == 'R':
            break
        elif symbol.isdigit():
            tea_bags += int(symbol)
    else:
        break
print("Alice didn't make it to the tea party." if tea_bags < 10 else "She did it! She went to the party.")
print(*[" ".join(row) for row in matrix], sep='\n')


##################################### variant 02 #####################################
class Alice:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.alice_location = []
        self.tea_bags = 0
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

    def create_alice_matrix(self):
        for row in range(self.size):
            line = input().split()
            self.matrix.append(line)
            if 'A' in line:
                self.alice_location = [row, line.index('A')]
                self.matrix[self.alice_location[0]][self.alice_location[1]] = '*'

    def alice_walk(self):
        while self.tea_bags < 10:
            direction = input()
            row = self.alice_location[0] + self.directions[direction][0]
            col = self.alice_location[1] + self.directions[direction][1]

            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.matrix[row][col]
                self.alice_location = [row, col]
                self.matrix[row][col] = '*'
                if symbol == 'R':
                    break
                elif symbol.isdigit():
                    self.tea_bags += int(symbol)
            else:
                break

    def printing(self):
        print("Alice didn't make it to the tea party." if self.tea_bags < 10 else "She did it! She went to the party.")
        print(*[" ".join(row) for row in self.matrix], sep='\n')


size_of_matrix = int(input())

output = Alice(size_of_matrix)
output.create_alice_matrix()
output.alice_walk()
output.printing()

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
