class UniqueNames:

    def __init__(self):
        self.output_message = ''
        self.number_of_names = int(input())
        self.unique_names_set = set()
        self.main_meth()

    def add_names_to_set_with_unique_names(self):
        for _ in range(self.number_of_names):
            current_name = input()
            self.unique_names_set.add(current_name)

    def main_meth(self):
        self.add_names_to_set_with_unique_names()
        self.prepare_result()

    def prepare_result(self):
        self.output_message = '\n'.join(self.unique_names_set)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(UniqueNames())

############################ TASK CONDITION ############################
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
