##################################### variant 01 #####################################
from collections import defaultdict

text = input()
symbols = defaultdict(int)

for character in text:
    symbols[character] += 1

for symbol, count in sorted(symbols.items()):
    print(f'{symbol}: {count} time/s')

##################################### variant 02 #####################################

from collections import defaultdict


class Main:

    def __init__(self, some_text):
        self.some_text = some_text
        self.symbols = defaultdict(int)

    def check_symbol(self):
        for character in self.some_text:
            self.symbols[character] += 1

    def __repr__(self):
        return '\n'.join(f'{symbol}: {count} time/s' for symbol, count in sorted(self.symbols.items()))


text = input()
output = Main(text)
output.check_symbol()

print(output)


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
