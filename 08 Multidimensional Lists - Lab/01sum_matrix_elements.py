##################################### variant 01 #####################################

rows, column = list(map(int, input().split(', ')))
matrix = [list(map(int, input().split(', '))) for j in range(rows)]
print(sum([sum(i) for i in matrix]))
print(matrix)

##################################### variant 02 #####################################
def matrix_fill(some_matrix, some_input):
    row = []
    for num in some_input.split(', '):
        row.append(int(num))
    some_matrix.append(row)
    return some_matrix


rows, cols = list(map(int, input().split(', ')))

matrix = []

for _ in range(rows):
    matrix = matrix_fill(matrix, input())

sum = sum(i for row in matrix for i in row)
print(sum)
print(matrix)


#################################### TASK CONDITION ############################
"""

                  1.	Sum Matrix Elements
Write a program that reads a matrix from the console and prints:
•	The sum of all numbers in the matrix
•	The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
On the next rows, you will get elements for each column separated by a comma and a space ", ". 

____________________________________________________________________________________________
Example

Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0	

Output
76
[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]


"""
