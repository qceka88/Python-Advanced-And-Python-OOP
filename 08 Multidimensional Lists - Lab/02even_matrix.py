class EvenMatrix:
    def __init__(self):
        self.rows = int(input())
        self.initial_matrix = []
        self.even_matrix = []
        self.main_meth()

    def main_meth(self):
        self.fill_initial_matrix()
        self.filter_even_numbers_in_even_matrix()

    def fill_initial_matrix(self):
        for _ in range(self.rows):
            current_row = [int(x) for x in input().split(', ')]
            self.initial_matrix.append(current_row)

    def filter_even_numbers_in_even_matrix(self):
        for row in range(len(self.initial_matrix)):
            even_row = []
            for col in range(len(self.initial_matrix[row])):
                number = self.initial_matrix[row][col]
                if number % 2 == 0:
                    even_row.append(number)
            self.even_matrix.append(even_row)

    def __repr__(self):
        return f'{self.even_matrix}'


if __name__ == '__main__':
    print(EvenMatrix())


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
