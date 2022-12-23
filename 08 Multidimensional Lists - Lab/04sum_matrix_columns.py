##################################### variant 01 #####################################

rows, cols = list(map(int, input().split(', ')))

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(cols):
    sum_of_numbers = 0
    for row in range(rows):
        sum_of_numbers += matrix[row][col]
    print(sum_of_numbers)


##################################### variant 02 #####################################
class Main:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.result = []

    def the_matrix(self):
        for _ in range(self.rows):
            self.matrix.append([int(x) for x in input().split()])

    def sum_of_columns(self):
        for col in range(self.cols):
            sum_of_numbers = 0
            for row in range(self.rows):
                sum_of_numbers += self.matrix[row][col]
            self.result.append(sum_of_numbers)

    def __repr__(self):
        return "\n".join(map(str, self.result))


rows_number, cols_number = list(map(int, input().split(', ')))
output = Main(rows_number, cols_number)
output.the_matrix()
output.sum_of_columns()
print(output)

#################################### TASK CONDITION ############################
"""

                    4.	Sum Matrix Columns
Write a program that reads a matrix from the console and prints 
the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". 
On the next rows, you will get elements for each column separated with a single space. 

____________________________________________________________________________________________
Example_01

Input
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0	

Output
12
10
19
20
8
7

____________________________________________________________________________________________
Example_02

Input
3, 3
1 2 3
4 5 6
7 8 9	

Output
12
15
18


"""
