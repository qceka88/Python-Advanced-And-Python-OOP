class PalindromesMatrix:

    def __init__(self):
        self.output_message = ''
        self.rows, self.cols = 0, 0
        self.first_letter = 97
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_of_matrix()
        self.fill_the_matrix_with_palindromes()
        self.prepare_output_message()

    def define_rows_cols_of_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def fill_the_matrix_with_palindromes(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                current_row.append(self.palindrome(row, col))
            self.matrix.append(current_row)

    def palindrome(self, row, col):
        combination = chr(row + self.first_letter) + chr(self.first_letter + col + row) + chr(
            row + self.first_letter)
        return combination

    def prepare_output_message(self):
        self.output_message = '\n'.join(' '.join(row) for row in self.matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(PalindromesMatrix())

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
