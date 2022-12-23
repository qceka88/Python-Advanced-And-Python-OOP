##################################### variant 01 #####################################

size = int(input())

matrix = [list(input()) for ch in range(size)]
searched_symbol = input()

found = False
location = {}
for row_i in range(len(matrix)):
    for col_i in range(len(matrix[row_i])):
        if searched_symbol == matrix[row_i][col_i]:
            location = (row_i, col_i)
            found = True
            break
    if found:
        break

print(location if found else f'{searched_symbol} does not occur in the matrix')


##################################### variant 02 #####################################

class Main:

    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.found = False
        self.message = ''

    def the_matrix(self):
        self.matrix = [list(input()) for ch in range(self.size)]

    def the_search(self, searched_symbol):
        for row_i in range(len(self.matrix)):
            for col_i in range(len(self.matrix[row_i])):
                if searched_symbol == self.matrix[row_i][col_i]:
                    location = (row_i, col_i)
                    self.found = True
                    break
            if self.found:
                break
        self.message = f'{location}' if self.found else f'{searched_symbol} does not occur in the matrix'

    def __repr__(self):
        return self.message


number = int(input())
output = Main(number)
output.the_matrix()
symbol = input()
output.the_search(symbol)
print(output)

#################################### TASK CONDITION ############################
"""

                6.	Symbol in Matrix
Write a program that reads a number - N, representing the rows and columns 
of a square matrix. On the next N lines, you will receive rows of the matrix. 
Each row consists of ASCII characters. After that, you will receive a symbol. 
Find the first occurrence of that symbol in the matrix and print its position 
in the format: "({row}, {col})". You should start searching from the top left. 
If there is no such symbol, print the message "{symbol} does not occur in the matrix".

____________________________________________________________________________________________
Example_01

Input
3
ABC
DEF
X!@
!	

Output
(2, 1)

____________________________________________________________________________________________
Example_02

Input
4
asdd
xczc
qwee
qefw
4	

Output
4 does not occur in the matrix

"""

