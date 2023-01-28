class CountSymbols:

    def __init__(self):
        self.output_message = ''
        self.input_data = list(input())
        self.result = {}
        self.main_meth()

    def main_meth(self):
        self.cont_unique_elements_in_input_data()
        self.prepare_result()

    def cont_unique_elements_in_input_data(self):
        for symbol in set(self.input_data):
            self.result[symbol] = self.input_data.count(symbol)

    def prepare_result(self):
        for letter, count in sorted(self.result.items()):
            self.output_message += f'{letter}: {count} time/s\n'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(CountSymbols())

#################################### TASK CONDITION ############################
"""

                          4.	Count Symbols
Write a program that reads a text from the console and counts the occurrences 
of each character in it. Print the results in alphabetical (lexicographical) order.  

____________________________________________________________________________________________
Example_01

Input
SoftUni rocks	

Output
 : 1 time/s
S: 1 time/s
U: 1 time/s
c: 1 time/s
f: 1 time/s
i: 1 time/s
k: 1 time/s
n: 1 time/s
o: 2 time/s
r: 1 time/s
s: 1 time/s
t: 1 time/s	


____________________________________________________________________________________________
Example_02

Input
Why do you like Python?	:

Output 
 4 time/s
?: 1 time/s
P: 1 time/s
W: 1 time/s
d: 1 time/s
e: 1 time/s
h: 2 time/s
i: 1 time/s
k: 1 time/s
l: 1 time/s
n: 1 time/s
o: 3 time/s
t: 1 time/s
u: 1 time/s
y: 3 time/s

"""
