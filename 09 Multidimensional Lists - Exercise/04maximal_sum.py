import sys


class MaximalSum:

    def __init__(self):
        self.output_message = ''
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.mini_matrix = []
        self.sum_of_mini_matrix = -sys.maxsize
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_for_matrix()
        self.create_matrix()
        self.find_maximal_sum_of_square_3x3()
        self.prepare_output_message()

    def define_rows_cols_for_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def create_matrix(self):
        self.matrix = [[int(n) for n in input().split()] for _ in range(self.rows)]

    def find_maximal_sum_of_square_3x3(self):
        for row in range(self.rows - 2):
            for col in range(self.cols - 2):
                mini_matrix = self.define_square_3x3(row, col)
                sum_mini = self.sum_elements_of_mini(mini_matrix)
                self.check_current_sum_of_mini_is_bigger(sum_mini, mini_matrix)

    def define_square_3x3(self, row, col):
        mini_matrix = [self.matrix[row][col:col + 3],
                       self.matrix[row + 1][col:col + 3],
                       self.matrix[row + 2][col:col + 3]]
        return mini_matrix

    def sum_elements_of_mini(self, some_matrix):
        sum_of_mini_matrix = sum(sum(r) for r in some_matrix)
        return sum_of_mini_matrix

    def check_current_sum_of_mini_is_bigger(self, some_sum, some_mini_matrix):
        if some_sum > self.sum_of_mini_matrix:
            self.sum_of_mini_matrix = some_sum
            self.mini_matrix = some_mini_matrix

    def prepare_output_message(self):
        self.output_message = f'Sum = {self.sum_of_mini_matrix}\n'
        self.output_message += '\n'.join(' '.join(str(x) for x in row) for row in self.mini_matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(MaximalSum())

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
