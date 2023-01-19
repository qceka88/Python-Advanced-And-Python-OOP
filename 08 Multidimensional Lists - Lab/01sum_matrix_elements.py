class SumMatrixElements:

    def __init__(self):
        self.result_message = ''
        self.rows, self.cols = [int(n) for n in input().split(', ')]
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.fill_matrix_with_elements()
        self.find_sum_of_elements()
        self.prepare_return_message()

    def fill_matrix_with_elements(self):
        for _ in range(self.rows):
            line = [int(x) for x in input().split(', ')]
            self.matrix.append(line)

    def find_sum_of_elements(self):
        self.result_message = str(sum(sum(row) for row in self.matrix))

    def prepare_return_message(self):
        self.result_message += f'\n{self.matrix}'

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(SumMatrixElements())

#################################### TASK CONDITION ############################
"""

                  1.	Sum Matrix Elements
Write a program that reads a matrix from the console and prints:
•	The sum of all numbers in the matrix
•	The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
On the next rows, you will get elements for each column separated by a comma and a space ", ". 

____________________________________________________________________________________________
Example

Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0	

Output
76
[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]


"""
