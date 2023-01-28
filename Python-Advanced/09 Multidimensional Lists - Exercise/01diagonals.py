class Diagonals:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.matrix = []
        self.primary_diagonal = []
        self.secondary_diagonal = []
        self.main_meth()

    def main_meth(self):
        self.create_matrix()
        self.find_diagonals_of_matrix()
        self.prepare_output_message()

    def create_matrix(self):
        self.matrix = [[int(x) for x in input().split(', ')] for row in range(self.size)]

    def find_diagonals_of_matrix(self):
        for i in range(self.size):
            self.primary_diagonal.append(self.matrix[i][i])
            self.secondary_diagonal.append(self.matrix[len(self.matrix) - 1 - i][i])

    def prepare_output_message(self):
        primary_diagonal = ', '.join(str(x) for x in self.primary_diagonal)
        secondary_diagonal = ', '.join(str(x) for x in reversed(self.secondary_diagonal))
        self.output_message = f'Primary diagonal: {primary_diagonal}. Sum: {sum(self.primary_diagonal)}'
        self.output_message += f'\nSecondary diagonal: {secondary_diagonal}. Sum: {sum(self.secondary_diagonal)}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Diagonals())



#################################### TASK CONDITION ############################
"""
                          1.	Diagonals
Using a nested list comprehension, write a program that reads rows of a square 
matrix and its elements, separated by a comma and a space ", ". You should find 
the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}

____________________________________________________________________________________________
Example

Input
3
1, 2, 3
4, 5, 6
7, 8, 9

Output
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

"""
