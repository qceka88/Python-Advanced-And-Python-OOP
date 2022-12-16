#################################### variant 01 #####################################
from collections import deque

visitors = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(visitors)} people remaining.')
        break
    elif command == 'Paid':
        print('\n'.join(visitors))
        visitors.clear()
    else:
        visitors.append(command)

#################################### variant 02 #####################################

from collections import deque


class Main:

    def __init__(self):
        self.visitors = deque()
        self.log = ''

    def supermarket(self):

        while True:
            command = input()
            if command == 'End':
                self.log += f'{len(self.visitors)} people remaining.'
                break
            if command == 'Paid':
                self.log += '\n'.join(self.visitors) + '\n'
                self.visitors.clear()
                continue
            self.visitors.append(command)

    def __repr__(self):
        return self.log


output = Main()
output.supermarket()
print(output)

#################################### TASK CONDITION ############################
"""

                              3.	Supermarket
Tom is working at the supermarket, and he needs your help to keep track 
of his clients. Write a program that reads lines of input consisting of a 
customer's name and adds it to the end of a queue until "End" is received.
If, in the meantime, you receive the command "Paid", you should print each 
customer in the order they are served (from the first to the last one) and 
empty the queue. When you receive "End", you should print the count of the
remaining people in the queue in the format: "{count} people remaining.".

____________________________________________________________________________________________
Example_01

Input
George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End	

Output
George
Peter
William
4 people remaining.

____________________________________________________________________________________________
Example_02

Input
Anna
Emma
Alexander
End	

Output
3 people remaining.


"""
