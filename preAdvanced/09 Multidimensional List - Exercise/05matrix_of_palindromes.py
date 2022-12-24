##################################### variant 01 #####################################
rows, cols = list(map(int, input().split()))

matrix = []

letter = 97

for row in range(rows):
    current_row = []
    for col in range(cols):
        element = chr(letter + row) + chr(letter + row + col) + chr(letter + row)
        current_row.append(element)
    matrix.append(current_row)

for row in matrix:
    print(*row)


##################################### variant 02 #####################################
class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.letter = 97

    def palindrome_matrix(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                element = chr(self.letter + row) + chr(self.letter + row + col) + chr(self.letter + row)
                current_row.append(element)
            self.matrix.append(current_row)

    def printing(self):
        for row in self.matrix:
            print(*row)


rows_number, cols_number = list(map(int, input().split()))
output = Main(rows_number, cols_number)
output.palindrome_matrix()
output.printing()

#################################### TASK CONDITION ############################
"""
                5.	Matrix of Palindromes
Write a program to generate the following matrix of palindromes of 
3 letters with r rows and c columns like the one in the examples below.
•	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
•	Columns + rows define the middle letter: 
o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
•	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"

____________________________________________________________________________________________
Example_01

Input
4 6	

Output
aaa aba aca ada aea afa
bbb bcb bdb beb bfb bgb
ccc cdc cec cfc cgc chc
ddd ded dfd dgd dhd did

____________________________________________________________________________________________
Example_02

Input
3 2	

Output
aaa aba
bbb bcb
ccc cdc
	

"""
