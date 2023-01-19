class FlatteningMatrix:

    def __init__(self):
        self.rows = int(input())
        self.initial_matrix = []
        self.flat_matrix = []
        self.main_meth()

    def main_meth(self):
        self.fill_initial_matrix_with_elements()
        self.create_the_flat_matrix()

    def fill_initial_matrix_with_elements(self):
        for _ in range(self.rows):
            row = [int(n) for n in input().split(', ')]
            self.initial_matrix.append(row)

    def create_the_flat_matrix(self):
        self.flat_matrix = [n for row in self.initial_matrix for n in row]

    def __repr__(self):
        return f'{self.flat_matrix}'


if __name__ == '__main__':
    print(FlatteningMatrix())


#################################### TASK CONDITION ############################
"""

                  3.	Flattening Matrix
Write a program that receives a matrix and prints the flattened 
version of it (a list with all the values). For example, the flattened 
list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. 
On the next rows, you will get the elements for each column separated 
with a comma and a space ", ".

____________________________________________________________________________________________
Example_01

Input
2
1, 2, 3
4, 5, 6	

Output
[1, 2, 3, 4, 5, 6]

____________________________________________________________________________________________
Example_02

Input
3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99	

Output
[10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]


"""
