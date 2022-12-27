##################################### variant 01 #####################################

input_data = [[num for num in row.split()] for row in input().split("|")]
print(*[n for num in reversed(input_data) for n in num])

##################################### variant 02 #####################################

print(*[n for row in reversed(input().split("|")) for n in row.split()])

##################################### variant 03 #####################################

class Main:

    def __init__(self, text):
        self.text = text
        self.flat = []

    def reading(self):
        for row in reversed(self.text.split('|')):
            for num in row.split():
                self.flat.append(num)

    def __repr__(self):
        return ' '.join(self.flat)


line = input()
output = Main(line)
output.reading()
print(output)

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
