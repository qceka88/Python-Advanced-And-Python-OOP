##################################### variant 01 #####################################
text = list(input())

while len(text) > 0:
    print(text.pop(), end='')
##################################### variant 02 #####################################
text = list(input())

while text:
    print(text.pop(), end='')

##################################### variant 03 #####################################

class ReversedString:

    def __init__(self,input_string):
        self.input_string = list(input_string)

    def printing(self):
        while self.input_string:
            print(self.input_string.pop(), end='')

input_text = input()
output = ReversedString(input_text).printing()

##################################### variant 04 #####################################

class ReversedString:

    def __init__(self):
        self.input_string = list(input())

    def printing(self):
        while self.input_string:
            print(self.input_string.pop(), end='')


output = ReversedString().printing()
# ##################################### variant 05 #####################################
class ReversedString:

    def __init__(self, input_string):
        self.input_string = list(input_string)

    def __repr__(self):
        output_string = ''
        while self.input_string:
            output_string += f'{self.input_string.pop()}'
        return output_string

input_text = input()
output = ReversedString(input_text)
print(output)


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
