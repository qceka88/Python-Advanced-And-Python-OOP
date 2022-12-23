##################################### variant 01 #####################################
rows, cols = list(map(int, input().split()))
matrix = [[x for x in input().split()] for i in range(rows)]

squares = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)
##################################### variant 02 #####################################
class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = []
        self.squares = 0

    def create_matrix(self):
        self.matrix = [[x for x in input().split()] for i in range(self.rows)]

    def find_diagonals(self):
        for row in range(self.rows - 1):
            for col in range(self.cols - 1):
                if self.matrix[row][col] == self.matrix[row][col + 1] == self.matrix[row + 1][col] == \
                        self.matrix[row + 1][col + 1]:
                    self.squares += 1

    def __repr__(self):
        return str(self.squares)


rows_number, cols_number = list(map(int, input().split()))
output = Main(rows_number, cols_number)
output.create_matrix()
output.find_diagonals()
print(output)

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
