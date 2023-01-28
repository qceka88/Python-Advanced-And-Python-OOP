##################################### variant 01 #####################################

lines = int(input())

set_of_elements = set()

for row in range(lines):
    current_input = set(input().split())
    set_of_elements.update(current_input)

print(*set_of_elements, sep='\n')


##################################### variant 02 #####################################

class Main:

    def __init__(self, number):
        self.number = number
        self.set_of_elements = set()

    def fill_set_of_elements(self):
        for current in range(self.number):
            current_elements = set(input().split())
            self.set_of_elements.update(current_elements)

    def __repr__(self):
        return '\n'.join(str(element) for element in self.set_of_elements)


rows = int(input())
output = Main(rows)
output.fill_set_of_elements()

print(output)


#################################### TASK CONDITION ############################
"""

                           3.	Periodic Table
Write a program that keeps all the unique chemical elements. On the first 
line, you will be given a number n - the count of input lines that you will 
receive. On the following n lines, you will be receiving chemical compounds 
separated by a single space. Your task is to print all the unique ones on 
separate lines (the order does not matter):

____________________________________________________________________________________________
Example_01

Input
4
Ce O
Mo O Ce
Ee
Mo	

Output
Ce
Ee
Mo
O
3
Ge Ch O Ne
Nb Mo Tc
O Ne

Output
Ch
Ge
Mo
Nb
Ne
O
Tc

"""
