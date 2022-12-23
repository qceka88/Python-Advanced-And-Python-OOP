##################################### variant 01 #####################################

rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flat = [num for row in matrix for num in row]
print(flat)


##################################### variant 02 #####################################

class Main:

    def __init__(self, rows):
        self.rows = rows
        self.matrix = []

    def the_matrix(self):
        for _ in range(self.rows):
            self.matrix.append([int(x) for x in input().split(', ')])

    def the_flat_matrix(self):
        return [num for row in self.matrix for num in row]


number_of_rows = int(input())
output = Main(number_of_rows)
output.the_matrix()
print(output.the_flat_matrix())


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
