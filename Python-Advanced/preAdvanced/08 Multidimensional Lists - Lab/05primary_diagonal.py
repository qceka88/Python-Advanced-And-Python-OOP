##################################### variant 01 #####################################
size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

summed = sum(matrix[i][i] for i in range(len(matrix)))
print(summed)


##################################### variant 02 #####################################
class Main:

    def __init__(self, size):
        self.size = size
        self.matrix = []

    def the_matrix(self):
        for _ in range(self.size):
            self.matrix.append([int(x) for x in input().split()])

    def __repr__(self):
        sum_diagonal = sum(self.matrix[i][i] for i in range(len(self.matrix)))
        return f'{sum_diagonal}'


number = int(input())
output = Main(number)
output.the_matrix()
print(output)


#################################### TASK CONDITION ############################
"""
                    5.	Primary Diagonal
Write a program that finds the sum of all numbers in a matrix's primary 
diagonal (runs from top left to bottom right). On the first line, 
you will receive an integer N – the size of a square matrix. The next N 
lines holds the values for each column - N numbers, separated by a single space. 

____________________________________________________________________________________________
Example_01

Input
3
11 2 4
4 5 6
10 8 -12	

Output
4	

____________________________________________________________________________________________
Example_02

Input
3
1 2 3
4 5 6
7 8 9	

Output
15

"""
