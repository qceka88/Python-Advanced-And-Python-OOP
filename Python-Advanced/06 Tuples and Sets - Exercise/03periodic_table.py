class PeriodicTable:

    def __init__(self):
        self.output_message = ""
        self.rows = int(input())
        self.unique_elements = set()
        self.main_meth()

    def main_meth(self):
        self.receive_input_data_on_rows()
        self.prepare_output_message()

    def receive_input_data_on_rows(self):
        for _ in range(self.rows):
            new_elements = set(input().split())
            self.unique_elements.update(new_elements)

    def prepare_output_message(self):
        self.output_message = '\n'.join(self.unique_elements)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(PeriodicTable())


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
