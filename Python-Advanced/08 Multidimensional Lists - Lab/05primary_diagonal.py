##################################### variant 01 #####################################

print(sum([int(input().split()[row]) for row in range(int(input()))]))


##################################### variant 02 #####################################
class PrimaryDiagonal:

    def __init__(self):
        self.rows = int(input())
        self.matrix = []
        self.sum_of_diagonal = 0
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.find_sum_of_diagonal()

    def create_matrix(self):
        for row in range(self.rows):
            line = [int(x) for x in input().split()]
            self.matrix.append(line)

    def find_sum_of_diagonal(self):
        for index in range(len(self.matrix)):
            self.sum_of_diagonal += self.matrix[index][index]

    def __repr__(self):
        return str(self.sum_of_diagonal)


if __name__ == '__main__':
    print(PrimaryDiagonal())



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
