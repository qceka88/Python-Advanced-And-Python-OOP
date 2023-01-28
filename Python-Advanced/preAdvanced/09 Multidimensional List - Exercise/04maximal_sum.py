##################################### variant 01 #####################################

import sys

rows, cols = list(map(int, input().split()))

matrix = [[int(x) for x in input().split()] for row in range(rows)]
max_mini_matrix = []
max_sum_mini = -sys.maxsize

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):
        mini_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                       [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                       [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]],
                       ]
        mini_sum = sum([sum(x) for x in mini_matrix])
        if mini_sum > max_sum_mini:
            max_mini_matrix, max_sum_mini = mini_matrix, mini_sum

print(f'Sum = {max_sum_mini}')
for row in max_mini_matrix:
    print(*row)

##################################### variant 02 #####################################

import sys


class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.max_mini_matrix = []
        self.max_sum_mini = -sys.maxsize

    def create_matrix(self):
        self.matrix = [[int(num) for num in input().split()] for row in range(self.rows)]

    def find_sum(self):
        for row in range(len(self.matrix) - 2):
            for col in range(len(self.matrix[row]) - 2):
                mini_matrix = [[self.matrix[row][col], self.matrix[row][col + 1], self.matrix[row][col + 2]],
                               [self.matrix[row + 1][col], self.matrix[row + 1][col + 1],
                                self.matrix[row + 1][col + 2]],
                               [self.matrix[row + 2][col], self.matrix[row + 2][col + 1],
                                self.matrix[row + 2][col + 2]],
                               ]
                mini_sum = sum([sum(x) for x in mini_matrix])
                if mini_sum > self.max_sum_mini:
                    self.max_mini_matrix, self.max_sum_mini = mini_matrix, mini_sum

    def printing(self):
        print(f'Sum = {self.max_sum_mini}')
        for row in self.max_mini_matrix:
            print(*row)


rows_number, cols_number = list(map(int, input().split()))
output = Main(rows_number, cols_number)
output.create_matrix()
output.find_sum()
output.printing()

#################################### TASK CONDITION ############################
"""
                      4.	Maximal Sum
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 
square with a maximum sum of its elements. There will be no case with two 
or more 3x3 squares with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in 
the format "{rows} {columns}" – integers in the range [1, 20]
•	On the following lines, you will receive each row with its 
columns - integers, separated by a single space in the range [-20, 20]
Output
•	On the first line, print the maximum sum of the elements 
in the 3x3 square in the format "Sum = {sum}"
•	On the following 3 lines, print each element of the found 
submatrix, separated by a single space

____________________________________________________________________________________________
Example_01

Input
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4	 	

Output
Sum = 75
1 4 14
7 11 2
8 12 16

____________________________________________________________________________________________
Example_02

Input
5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5		

Output
Sum = 34
2 5 6 
5 4 1 
6 0 5

"""
