##################################### variant 01 #####################################

from collections import defaultdict

numbers = tuple(map(float, input().split()))

unique = defaultdict(int)
for number in numbers:
    unique[number] += 1

for number, count in unique.items():
    print(f"{number} - {count} times")

##################################### variant 02 #####################################

from collections import defaultdict


class Main:

    def __init__(self, string):
        self.string = string
        self.unique = defaultdict(int)
        self.log = ''

    def string_to_dict(self):
        numbers = tuple(map(float, self.string.split()))
        for number in numbers:
            self.unique[number] += 1

    def message(self):
        for number, count in self.unique.items():
            self.log += f"{number} - {count} times\n"

    def __repr__(self):
        return self.log

input_line = input()
output = Main(input_line)
output.string_to_dict()
output.message()
print(output)


#################################### TASK CONDITION ############################
"""

                  1.	Count Same Values
You will be given numbers separated by a space. Write a program that 
prints the number of occurrences of each number in the format 
"{number} - {count} times". The number must be formatted to the 
first decimal point.

____________________________________________________________________________________________
Example_01

Input
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

Output
-2.5 - 3 times
4.0 - 2 times
3.0 - 4 times
-5.5 - 1 times

____________________________________________________________________________________________
Example_02

Input
2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3

Output
2.0 - 3 times
4.0 - 6 times
5.0 - 4 times
3.0 - 7 times


"""