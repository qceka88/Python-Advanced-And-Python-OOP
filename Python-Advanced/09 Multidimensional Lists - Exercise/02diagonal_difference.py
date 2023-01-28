class DiagonalDifference:

    def __init__(self):
        self.size = int(input())
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = []
        self.difference_of_diagonals = 0
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.find_diagonals_of_matrix()
        self.find_difference_of_sum_of_diagonals()

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split()] for row in range(self.size)]

    def find_diagonals_of_matrix(self):
        for i in range(self.size):
            self.primary_diagonal.append(self.matrix[i][i])
            self.secondary_diagonal.append(self.matrix[self.size - 1 - i][i])

    def find_difference_of_sum_of_diagonals(self):
        sum_of_primary_diagonal = sum(self.primary_diagonal)
        sum_of_secondary_diagonal = sum(self.secondary_diagonal)
        self.difference_of_diagonals = abs(sum_of_primary_diagonal - sum_of_secondary_diagonal)

    def __repr__(self):
        return str(self.difference_of_diagonals)


if __name__ == '__main__':
    print(DiagonalDifference())

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
