##################################### variant 01 #####################################
rows = int(input())
even_matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    even_matrix.append(current_row)
print(even_matrix)


##################################### variant 02 #####################################
class Main:

    def __init__(self, rows):
        self.rows = rows
        self.even_matrix = []

    def the_even_matrix(self):
        self.even_matrix = [[int(i) for i in input().split(', ') if int(i) % 2 == 0] for j in range(self.rows)]

    def printing(self):
        print(self.even_matrix)


number_of_rows = int(input())
output = Main(number_of_rows)
output.the_even_matrix()
output.printing()

#################################### TASK CONDITION ############################
"""

                    2.	Even Matrix
Write a program that receives a matrix of numbers and prints a new one 
only with the numbers that are even. Use nested comprehension for that problem. 
On the first line, you will receive the rows of the matrix. On the 
next rows, you will get elements for each column separated with a 
comma and a space ", ".  

____________________________________________________________________________________________
Example_01

Input
2
1, 2, 3
4, 5, 6	

Output
[[2], [4, 6]]

____________________________________________________________________________________________
Example_02

Input
4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67	

Output
[[10, 24], [34, 110], [4, 12], []]


"""
