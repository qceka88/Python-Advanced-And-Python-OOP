class MatrixModification:

    def __init__(self):
        self.output_message = []
        self.size = int(input())
        self.matrix = []
        self.actions = {
            'Add': self.add_number,
            'Subtract': self.subtract_number,
        }
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.start_modifications()
        self.prepare_output_message()

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split()] for _ in range(self.size)]

    def valid_coordinates(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        else:
            return False

    def add_number(self, r, c, value):
        self.matrix[r][c] += value

    def subtract_number(self, r, c, value):
        self.matrix[r][c] -= value

    def start_modifications(self):
        while True:
            data = input().split()
            if data[0] == 'END':
                break
            act, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])

            if self.valid_coordinates(row, col):
                self.actions[act](row, col, value)
            else:
                self.output_message.append('Invalid coordinates')

    def prepare_output_message(self):
        for row in self.matrix:
            line = ' '.join(str(x) for x in row)
            self.output_message.append(line)

    def __repr__(self):
        return '\n'.join(self.output_message)


if __name__ == '__main__':
    print(MatrixModification())


#################################### TASK CONDITION ############################
"""
                     2.	Matrix Modification
Write a program that reads a matrix from the console and changes its 
values. On the first line, you will get the matrix's rows - N. You will 
get elements for each column on the following N lines, separated with 
a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given 
coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the 
given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". 
A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

____________________________________________________________________________________________
Example_01

Input
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END	

Output
6 2 3
4 3 6
7 8 9

____________________________________________________________________________________________
Example_02

Input
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END	

Output
Invalid coordinates
Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101

"""
