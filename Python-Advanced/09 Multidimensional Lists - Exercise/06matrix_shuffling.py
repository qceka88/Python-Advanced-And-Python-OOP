class ShuffleMatrix:

    def __init__(self):
        self.output_message = ''
        self.rows, self.cols = 0, 0
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_for_matrix()
        self.fill_matrix_with_elements()
        self.start_to_shuffle_matrix()

    def define_rows_cols_for_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def fill_matrix_with_elements(self):
        self.matrix = [[x for x in input().split()] for _ in range(self.rows)]

    def start_to_shuffle_matrix(self):
        while True:
            line = input().split()
            if line[0] == 'END':
                break

            valid = self.validate_data(line)
            if valid:
                self.swap_elements(valid)
                self.output_message += '\n'.join(' '.join(map(str, row)) for row in self.matrix) + '\n'
            else:
                self.output_message += 'Invalid input!\n'

    def validate_data(self, data):
        command = data[0]
        indexes = [int(n) for n in data if n.isdigit()]
        if command == 'swap' and len(indexes) == 4:
            row1, col1, row2, col2 = indexes
            if 0 <= (row1 and row2) < self.rows and 0 <= (col1 and col2) < self.cols:
                return indexes

    def swap_elements(self, some_indexes):
        row1, col1, row2, col2 = [int(n) for n in some_indexes]
        self.matrix[row1][col1], self.matrix[row2][col2] = self.matrix[row2][col2], self.matrix[row1][col1]

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(ShuffleMatrix())


#################################### TASK CONDITION ############################
"""
                           6.	Matrix Shuffling
Write a program that reads a matrix from the console and performs certain 
operations with its elements. User input is provided similarly to the 
problems above - first, you read the dimensions and then the data.  Your 
program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
 where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in 
 the matrix. A valid command starts with the "swap" keyword along with four 
 valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes 
and print the matrix at each step (thus, you will be able to check if the 
operation was performed correctly). 
•	If the command is not valid (does not contain the keyword "swap", has fewer 
or more coordinates entered, or the given coordinates are not valid), 
print "Invalid input!" and move on to the following command. 
A negative value makes the coordinates not valid.
Your program should finish when the command "END" is entered.

____________________________________________________________________________________________
Example_01

Input
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END	

Output
5 2 3
4 1 6
Invalid input!
5 4 3
2 1 6

____________________________________________________________________________________________
Example_02

Input
1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END	

Output
Invalid input!
World Hello
Hello World


"""
