##################################### variant 01 #####################################
size = int(input())

matrix = [[int(x) for x in input().split()] for row in range(int(size))]

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[(len(matrix) - 1) - i][i])

total = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(total)
##################################### variant 02 #####################################
class Main:

    def __init__(self, some_size):
        self.some_size = some_size
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = []

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split()] for row in range(int(self.some_size))]

    def find_diagonals(self):
        for i in range(len(self.matrix)):
            self.primary_diagonal.append(self.matrix[i][i])
            self.secondary_diagonal.append(self.matrix[(len(self.matrix) - 1) - i][i])

    def __repr__(self):
        total = abs(sum(self.primary_diagonal) - sum(self.secondary_diagonal))
        return str(total)


size = int(input())
output = Main(size)
output.create_matrix()
output.find_diagonals()
print(output)


#################################### TASK CONDITION ############################
"""
               2.	Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
 
On the first line, you will receive an integer N - the size of a square matrix. 
The following N lines hold the values for each column - N numbers separated by 
a single space. Print the absolute difference between the primary and the secondary diagonal sums.

____________________________________________________________________________________________
Example_01

Input
3
11 2 4
4 5 6
10 8 -12	

Output
15	

Explanation
Primary diagonal: sum = 11 + 5 + (-12) = 4
Secondary diagonal: sum = 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

____________________________________________________________________________________________
Example_02

Input
4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14	

Output
34	

"""
