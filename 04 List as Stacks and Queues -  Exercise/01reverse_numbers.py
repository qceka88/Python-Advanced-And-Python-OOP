##################################### variant 01 #####################################
string_stack = input().split()

while string_stack:
    print(string_stack.pop(), end=' ')


##################################### variant 02 #####################################

class Reverse:

    def __init__(self, some_string: str):
        self.some_string = some_string.split()
        self.stack = []

    def reversing(self):
        for iteration in range(len(self.some_string)):
            self.stack.append(self.some_string.pop())

    def __repr__(self):
        return f"{' '.join(self.stack)}"


input_string = input()

output = Reverse(input_string)
output.reversing()
print(output)

#################################### TASK CONDITION ############################
"""

                       1.	Reverse Numbers
Write a program that reads a string with N integers from the console, 
separated by a single space, and reverses them using a stack. 
Print the reversed integers on one line, separated by a single space.

____________________________________________________________________________________________
Example_02

Input
1 2 3 4 5	

Output
5 4 3 2 1

____________________________________________________________________________________________
Example_02

Input
1

Output
1

"""