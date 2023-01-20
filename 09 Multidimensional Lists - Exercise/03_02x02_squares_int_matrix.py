class SquaresInMatrix:

    def __init__(self):
        self.rows, self.cols = 0, 0
        self.matrix = []
        self.counted_squares = 0
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols()
        self.create_matrix()
        self.find_squares_in_matrix()


    def define_rows_cols(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def create_matrix(self):
        self.matrix = [input().split() for row in range(self.rows)]

    def find_squares_in_matrix(self):
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                self.square_for_matched_symbols(row, col)

    def square_for_matched_symbols(self, row, col):
        if self.matrix[row][col] == self.matrix[row][col + 1] \
                == self.matrix[row + 1][col] == self.matrix[row + 1][col + 1]:
            self.counted_squares += 1

    def __repr__(self):
        return str(self.counted_squares)


if __name__ == '__main__':
    print(SquaresInMatrix())


#################################### TASK CONDITION ############################
"""
                     3.	2x2 Squares in Matrix
Find the number of all 2x2 squares containing identical chars in a matrix. 
On the first line, you will receive the matrix's dimensions in the 
format "{rows} {columns}". On the following rows, you will receive characters 
separated by a single space. Print the number of all square matrices you have found.

____________________________________________________________________________________________
Example_01

Input
3 4
A B B D
E B B B
I J B B	

Output
2	

Example
Two 2x2 squares of equal cells:
A B B D	A B B D
E B B B	E B B B
I J B B	I J B B

____________________________________________________________________________________________
Example_02

Input
2 2
a b
c d	

Output
0	

Example
No 2x2 squares of equal cells exist.

____________________________________________________________________________________________
Example_03

Input
5 4
A A B D
A A B B
I J B B
C C C G
C C K P

Output
3

Example
Three 2x2 squares of equal cells:
A A B D  A A B D  A A B D 
A A B B  A A B B  A A B B 
I J B B  I J B B  I J B B
C C C G  C C C G  C C C G
C C K P  C C K P  C C K P

"""
