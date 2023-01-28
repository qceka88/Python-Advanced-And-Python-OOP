##################################### variant 01 #####################################

names_quantity = int(input())

usernames_set = set()

for current in range(names_quantity):
    usernames_set.add(input())

for username in usernames_set:
    print(username)

##################################### variant 02 #####################################


print(*(set(input() for _ in range(int(input())))), sep='\n')


##################################### variant 03 #####################################

class Main:

    def __init__(self, names):
        self.names = names
        self.set_names = set()

    def fill_set(self):
        for current in range(self.names):
            name = input()
            self.set_names.add(name)

    def __repr__(self):
        return '\n'.join(str(name) for name in self.set_names)


output = Main(int(input()))
output.fill_set()
print(output)

#################################### TASK CONDITION ############################
"""

                            1.	Unique Usernames
Write a program that reads from the console a sequence of N usernames and 
keeps a collection only of the unique ones. On the first line, you will 
receive an integer N. On the next N lines, you will receive a username. 
Print the collection on the console (the order does not matter):

____________________________________________________________________________________________
Example_01

Input
6
George
George
George
Peter
George
NiceGuy1234	

Output
George
Peter
NiceGuy1234

____________________________________________________________________________________________
Example_02

Input
10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George	

Output
Peter
Maria
George
Steve
Alex

"""
