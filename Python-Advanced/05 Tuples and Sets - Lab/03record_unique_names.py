class UniqueNames:

    def __init__(self):
        self.number = int(input())
        self.some_set = set()
        self.main()

    def process_the_names(self):
        for _ in range(self.number):
            name = input()
            self.some_set.add(name)

    def main(self):
        self.process_the_names()

    def __repr__(self):
        return '\n'.join(self.some_set)


if __name__ == '__main__':
    print(UniqueNames())

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