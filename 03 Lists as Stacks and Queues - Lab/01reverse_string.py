##################################### variant 01 #####################################
text = list(input())

while len(text) > 0:
    print(text.pop(), end='')


##################################### variant 02 #####################################

class ReversedString:

    def __init__(self):
        self.input_string = list(input())

    def printing(self):
        while self.input_string:
            print(self.input_string.pop(), end='')


output = ReversedString().printing()


#################################### TASK CONDITION ############################
"""

1.	Reverse Strings
Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console

____________________________________________________________________________________________
Example_01

Input
I Love Python

Output
nohtyP evoL I

____________________________________________________________________________________________
Example_02

Input
Stacks and Queues

Output
seueuQ dna skcatS

"""
