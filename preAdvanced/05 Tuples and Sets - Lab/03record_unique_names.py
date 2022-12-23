##################################### variant 01 #####################################
number_of_names = int(input())

names_book = set()

for name in range(number_of_names):
    names_book.add(input())

print(*names_book, sep='\n')

##################################### variant 02 #####################################
class Main:

    def __init__(self, number):
        self.number = number
        self.names_book = set()

    def fill_the_set(self):
        for name in range(self.number):
            self.names_book.add(input())

    def __repr__(self):
        return '\n'.join(name for name in self.names_book)


number_of_names = int(input())
output = Main(number_of_names)
output.fill_the_set()
print(output)

#################################### TASK CONDITION ############################
"""
                   3.	Record Unique Names
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.

____________________________________________________________________________________________
Example_01

Input	
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey	

Output
Alan
Joey
Lee
Joe
Peter

____________________________________________________________________________________________
Example_02

Input
7
Lyle
Bruce
Alice
Easton
Shawn
Alice
Shawn	

Output
Easton
Lyle
Alice
Bruce
Shawn	

____________________________________________________________________________________________
Example_03

Input
6
Adam
Adam
Adam
Adam
Adam
Adam	

Output
Adam


"""