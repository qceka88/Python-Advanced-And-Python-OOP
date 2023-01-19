class MatrixColumnsSum:

    def __init__(self):
        self.result_message = ''
        self.rows, self.cols = [int(n) for n in input().split(', ')]
        self.matrix = []
        self.columns_sum = []
        self.main_meth()

    def main_meth(self):
        self.fill_matrix_with_elements()
        self.sum_columns_of_matrix()
        self.prepare_result()

    def fill_matrix_with_elements(self):
        self.matrix = [[int(x) for x in input().split()] for _ in range(self.rows)]

    def sum_columns_of_matrix(self):
        for col in range(self.cols):
            col_sum = 0
            for row in range(self.rows):
                col_sum += self.matrix[row][col]
            self.columns_sum.append(col_sum)

    def prepare_result(self):
        self.result_message = '\n'.join(str(n) for n in self.columns_sum)

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(MatrixColumnsSum())


#################################### TASK CONDITION ############################
"""

                    4.	Sum Matrix Columns
Write a program that reads a matrix from the console and prints 
the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". 
On the next rows, you will get elements for each column separated with a single space. 

____________________________________________________________________________________________
Example_01

Input
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0	

Output
12
10
19
20
8
7

____________________________________________________________________________________________
Example_02

Input
3, 3
1 2 3
4 5 6
7 8 9	

Output
12
15
18


"""
