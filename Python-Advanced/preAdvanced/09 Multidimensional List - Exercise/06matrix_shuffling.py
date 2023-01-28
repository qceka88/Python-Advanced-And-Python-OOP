##################################### variant 01 #####################################

rows, cols = list(map(int, input().split()))
matrix = [[x for x in input().split()] for i in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
    else:
        row01, col01, row02, col02 = list(map(int, command[1:]))
        if (row01 or row02 or col01 or col02) < 0 or (row01 or row02) >= rows or (col01 or col02) >= cols:
            print('Invalid input!')
        else:
            matrix[row01][col01], matrix[row02][col02] = matrix[row02][col02], matrix[row01][col01]
            for row in matrix:
                print(*row)

##################################### variant 02 #####################################

class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.result = []

    def create_matrix(self):
        self.matrix = [[x for x in input().split()] for i in range(self.rows)]

    def shuffle(self):
        while True:
            command = input().split()
            if command[0] == 'END':
                break
            if command[0] != 'swap' or len(command) != 5:
                self.result.append('Invalid input!')
            else:
                row01, col01, row02, col02 = list(map(int, command[1:]))
                if (row01 or row02 or col01 or col02) < 0 or \
                        (row01 or row02) >= self.rows or (col01 or col02) >= self.cols:
                    self.result.append('Invalid input!')
                else:
                    self.matrix[row01][col01], self.matrix[row02][col02] = \
                        self.matrix[row02][col02], self.matrix[row01][col01]
                    for row in self.matrix:
                        self.result.append(' '.join(row))

    def __repr__(self):
        return '\n'.join(self.result)


rows_number, cols_number = list(map(int, input().split()))
output = Main(rows_number, cols_number)
output.create_matrix()
output.shuffle()
print(output)

#################################### TASK CONDITION ############################
"""
                           6.	Matrix Shuffling
Write a program that reads a matrix from the console and performs certain 
operations with its elements. User input is provided similarly to the 
problems above - first, you read the dimensions and then the data.  Your 
program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
 where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in 
 the matrix. A valid command starts with the "swap" keyword along with four 
 valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes 
and print the matrix at each step (thus, you will be able to check if the 
operation was performed correctly). 
•	If the command is not valid (does not contain the keyword "swap", has fewer 
or more coordinates entered, or the given coordinates are not valid), 
print "Invalid input!" and move on to the following command. 
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

____________________________________________________________________________________________
Example_01

Input
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END	

Output
5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6

____________________________________________________________________________________________
Example_02

Input
1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END	

Output
Invalid input!
World Hello
Hello World


"""
