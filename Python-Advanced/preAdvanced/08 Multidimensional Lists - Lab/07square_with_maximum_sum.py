##################################### variant 01 #####################################

rows, cols = list(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]
max_sum = 0
max_mini_matrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        mini_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
        current_sum = sum(int(x) for row in mini_matrix for x in row)
        if current_sum > max_sum:
            max_mini_matrix = mini_matrix
            max_sum = current_sum

for row in max_mini_matrix:
    print(*row, sep=' ')
print(max_sum)

##################################### variant 02 #####################################
class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.result = [[], 0]

    def the_matrix(self):
        self.matrix = [[int(x) for x in input().split(', ')] for i in range(self.rows)]

    def research(self):
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                mini_matrix = [[self.matrix[row][col], self.matrix[row][col + 1]],
                               [self.matrix[row + 1][col], self.matrix[row + 1][col + 1]]]
                current_sum = sum(int(x) for row in mini_matrix for x in row)
                if current_sum > self.result[1]:
                    self.result = [mini_matrix, current_sum]

    def printing(self):
        for row in self.result[0]:
            print(*row, sep=' ')
        print(self.result[1])


rows_number, cols_number = list(map(int, input().split(', ')))
output = Main(rows_number, cols_number)
output.the_matrix()
output.research()
output.printing()


#################################### TASK CONDITION ############################
"""
                    7.	Square with Maximum Sum
Write a program that reads a matrix from the console and finds the 2x2 top-left 
submatrix with biggest sum of its values. On first line you will get matrix 
sizes in format "{rows}, {columns}".  On the next rows, you will get elements 
for each column, separated with a comma and a space ", ".  You should print 
the found submatrix and the sum of its elements, as shown in the examples. 

____________________________________________________________________________________________
Example_01

Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0	

Output
9 8
7 9
33

____________________________________________________________________________________________
Example_02

Input
2, 4
10, 11, 12, 13
14, 15, 16, 17

Output
12 13 
16 17 
58

Hints
•	Be aware of IndexError
•	If you find more than one max square, print the top-left one

"""
