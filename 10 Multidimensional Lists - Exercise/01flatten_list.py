class FattenList:

    def __init__(self):
        self.output_message = ''
        self.first_matrix = []
        self.flatten_matrix = []
        self.main_meth()

    def main_meth(self):
        self.fill_first_matrix_with_elements()
        self.fill_flatten_matrix()
        self.prepare_output_message()

    def fill_first_matrix_with_elements(self):
        self.first_matrix = [row.split() for row in input().split('|')]

    def fill_flatten_matrix(self):
        for row in self.first_matrix[::-1]:
            self.flatten_matrix.extend(row)

    def prepare_output_message(self):
        self.output_message = ' '.join(self.flatten_matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(FattenList())


#################################### TASK CONDITION ############################
"""
                    1.	Flatten Lists
Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix
sub-lists and their values from left to right as shown below

____________________________________________________________________________________________
Example_01

Input
1 2 3 |4 5 6 |  7  88

Output
7 88 4 5 6 1 2 3
____________________________________________________________________________________________
Example_02

Input
7 | 4  5|1 0| 2 5 |3

Output
3 2 5 1 0 4 5 7
____________________________________________________________________________________________
Example_03

Input
1| 4 5 6 7  |  8 9	

Output
8 9 4 5 6 7 1

"""
