class MaxSumSquare:

    def __init__(self):
        self.result_message = ''
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.square = []
        self.square_sum = 0
        self.main_meth()

    def main_meth(self):
        self.define_rows_and_cols_for_matrix()
        self.create_matrix()
        self.search_in_matrix_biggest_square_sum()
        self.prepare_result()

    def define_rows_and_cols_for_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split(', ')]

    def create_matrix(self):
        for _ in range(self.rows):
            row = [int(num) for num in input().split(', ')]
            self.matrix.append(row)

    def search_in_matrix_biggest_square_sum(self):
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                sum_of_square = self.sum_numbers_in_square(row, col)
                self.check_square_sum(sum_of_square, row, col)

    def sum_numbers_in_square(self, row, col):
        sum_of_numbers = self.matrix[row][col] + self.matrix[row][col + 1] + \
                         self.matrix[row + 1][col] + self.matrix[row + 1][col + 1]
        return sum_of_numbers

    def check_square_sum(self, some_sum, row, col):
        if some_sum > self.square_sum:
            self.square_sum = some_sum
            self.square = [[self.matrix[row][col], self.matrix[row][col + 1]],
                           [self.matrix[row + 1][col], self.matrix[row + 1][col + 1]]]

    def prepare_result(self):
        self.result_message = "\n".join(' '.join(str(x) for x in row) for row in self.square)
        self.result_message += f"\n{self.square_sum}"

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(MaxSumSquare())


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
