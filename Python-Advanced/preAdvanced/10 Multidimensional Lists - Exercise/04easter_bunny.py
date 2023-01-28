##################################### variant 01 #####################################
size = int(input())

bunny_location = []
bunny_path = []
eggs = 0
way = ''
matrix = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for n in range(size):
    row = input().split()
    matrix.append(row)
    if 'B' in row:
        bunny_location = [n, row.index('B')]

for direction, location in directions.items():
    bunny_row = bunny_location[0] + location[0]
    bunny_col = bunny_location[1] + location[1]
    current_eggs = 0
    current_path = []
    while 0 <= bunny_row < size and 0 <= bunny_col < size:
        if matrix[bunny_row][bunny_col] == 'X':
            break
        else:
            current_eggs += int(matrix[bunny_row][bunny_col])
            current_path.append([bunny_row, bunny_col])
            bunny_row += location[0]
            bunny_col += location[1]
    if current_eggs >= eggs:
        eggs = current_eggs
        bunny_path = current_path
        way = direction

print(way)
print(*bunny_path, sep='\n')
print(eggs)


##################################### variant 02 #####################################
class EasterBunny:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.bunny_location = []
        self.best_path = []
        self.max_eggs = 0
        self.best_way = ''
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

    def create_rabbit_matrix(self):
        for row in range(self.size):
            line = input().split()
            self.matrix.append(line)
            if 'B' in line:
                self.bunny_location = [row, line.index('B')]

    def rabbit_run(self, location):
        bunny_row = self.bunny_location[0] + location[0]
        bunny_col = self.bunny_location[1] + location[1]
        current_eggs = 0
        current_path = []
        while 0 <= bunny_row < self.size and 0 <= bunny_col < self.size:
            if self.matrix[bunny_row][bunny_col] == 'X':
                break
            else:
                current_eggs += int(self.matrix[bunny_row][bunny_col])
                current_path.append([bunny_row, bunny_col])
                bunny_row += location[0]
                bunny_col += location[1]
        return current_eggs, current_path

    def rabbit_check(self):
        for direction, location in self.directions.items():
            result = self.rabbit_run(location)
            eggs = result[0]
            if eggs >= self.max_eggs:
                self.max_eggs = eggs
                self.best_path = result[1]
                self.best_way = direction

    def printing(self):
        print(self.best_way)
        print(*self.best_path, sep='\n')
        print(self.max_eggs)


size_of_matrix = int(input())

output = EasterBunny(size_of_matrix)
output.create_rabbit_matrix()
output.rabbit_check()
output.printing()

#################################### TASK CONDITION ############################
"""
                   4.	Easter Bunny
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size 
of the field. On the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should 
go to collect the maximum number of eggs. The directions that should 
be considered as possible are up, down, left, and right. If you reach 
a trap while checking some of the directions, you should not consider 
the fields after the trap in this direction. For more clarifications, 
see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
Constraints
•	There will NOT be two or more paths consisting of the same total amount of eggs.

____________________________________________________________________________________________
Example_01

Input
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0	

Output
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87	

Explanation
The number of eggs if the bunny goes up is equal to 7. 
If he goes down = 9, there are no eggs on the left and 87 on 
the right. That's why the bunny should follow this direction 
(right) and collect the eggs provided there.

____________________________________________________________________________________________
Example_02

Input
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22	

Output
down
[6, 2]
[7, 2]
113	

"""
