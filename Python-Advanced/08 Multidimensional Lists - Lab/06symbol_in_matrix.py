class SymbolLocation:

    def __init__(self):
        self.result_message = ''
        self.rows = int(input())
        self.matrix = []
        self.searched_symbol = ''
        self.location_of_symbol = ()
        self.is_found = False
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.define_searched_symbol()
        self.check_matrix_for_symbol()
        self.prepare_result()

    def create_matrix(self):
        for _ in range(self.rows):
            line = list(input())
            self.matrix.append(line)

    def define_searched_symbol(self):
        self.searched_symbol = input()

    def check_matrix_for_symbol(self):
        for row in range(len(self.matrix)):
            if self.searched_symbol in self.matrix[row]:
                col = self.matrix[row].index(self.searched_symbol)
                self.is_found = True
                self.result_message = row, col
                break

    def prepare_result(self):
        if self.is_found:
            self.result_message = f"{self.result_message}"
        else:
            self.result_message = f'{self.searched_symbol} does not occur in the matrix'

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(SymbolLocation())


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

