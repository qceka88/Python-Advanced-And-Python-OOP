##################################### variant 01 #####################################
size = int(input())
matrix = [[int(n) for n in input().split()] for row in range(size)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    order = command[0]
    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif order == 'Add':
        matrix[row][col] += value
    elif order == 'Subtract':
        matrix[row][col] -= value

print(*[' '.join(map(str, row)) for row in matrix], sep='\n')
##################################### variant 02 #####################################
class Main:

    def __init__(self, number, some_matrix):
        self.number = number
        self.some_matrix = some_matrix
        self.log = []

    def modification(self):
        while True:
            command = input().split()
            if command[0] == 'END':
                break
            order = command[0]
            row, col, value = int(command[1]), int(command[2]), int(command[3])

            if not (0 <= row < self.number and 0 <= col < self.number):
                self.log.append(["Invalid coordinates"])
            elif order == 'Add':
                self.some_matrix[row][col] += value
            elif order == 'Subtract':
                self.some_matrix[row][col] -= value
        for row in self.some_matrix:
            self.log.append(row)

    def __repr__(self):
        return '\n'.join(' '.join(str(n) for n in data) for data in self.log)


size = int(input())
matrix = [[int(n) for n in input().split()] for row in range(size)]

output = Main(size, matrix)
output.modification()
print(output)


#################################### TASK CONDITION ############################
"""
                     2.	Matrix Modification
Write a program that reads a matrix from the console and changes its 
values. On the first line, you will get the matrix's rows - N. You will 
get elements for each column on the following N lines, separated with 
a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given 
coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the 
given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". 
A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

____________________________________________________________________________________________
Example_01

Input
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END	

Output
6 2 3
4 3 6
7 8 9

____________________________________________________________________________________________
Example_02

Input
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END	

Output
Invalid coordinates
Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101

"""
