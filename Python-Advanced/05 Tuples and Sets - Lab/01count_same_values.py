from collections import defaultdict


class CountSameValue:

    def __init__(self, row_of_numbers):
        self.row_of_numbers = row_of_numbers
        self.dict = defaultdict(int)

    def count_values(self):
        for number in self.row_of_numbers:
            self.dict.setdefault(number, self.row_of_numbers.count(number))

    def __repr__(self):
        return '\n'.join(f"{num} - {count} times" for num, count in self.dict.items())


sequence_of_numbers = tuple(float(x) for x in input().split())
output = CountSameValue(sequence_of_numbers)
output.count_values()
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