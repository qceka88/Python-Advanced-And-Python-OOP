class Reversing:

    def __init__(self):
        self.initial_string = input().split()
        self.reversed_string = []
        self.reversing_string()

    def reversing_string(self):
        while self.initial_string:
            self.reversed_string.append(self.initial_string.pop())

    def __repr__(self):
        return f'{" ".join(self.reversed_string)}'


if __name__ == "__main__":
    print(Reversing())


#################################### TASK CONDITION ############################
"""

                       1.	Reverse Numbers
Write a program that reads a string with N integers from the console, 
separated by a single space, and reverses them using a stack. 
Print the reversed integers on one line, separated by a single space.

____________________________________________________________________________________________
Example_01

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