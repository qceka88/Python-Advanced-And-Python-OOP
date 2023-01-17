class Numbers:

    def __init__(self):
        self.output_message = ''
        self.commands = {'Add': self.add_numbers,
                         'Remove': self.remove_numbers,
                         'Check': self.check_subset}
        self.rows = {'First': set(),
                     'Second': set()}
        self.main_meth()

    def main_meth(self):
        self.fill_rows_with_numbers()
        self.receive_commands()
        self.prepare_result()

    def fill_rows_with_numbers(self):
        for row in self.rows:
            self.rows[row] = set(int(n) for n in input().split())

    def receive_commands(self):
        number_of_commands = int(input())
        for _ in range(number_of_commands):
            act, *data = input().split()
            self.commands[act](*data)

    def add_numbers(self, *args):
        side = args[0]
        for number in args[1:]:
            self.rows[side].add(int(number))

    def remove_numbers(self, *args):
        side = args[0]
        for number in args[1:]:
            self.rows[side].discard(int(number))

    def check_subset(self, *args):
        if self.rows['First'].issubset(self.rows['Second']) or self.rows['Second'].issubset(self.rows['First']):
            self.output_message += 'True\n'
        else:
            self.output_message += 'False\n'

    def prepare_result(self):
        for row in self.rows:
            self.output_message += f'{", ".join(str(n) for n in sorted(self.rows[row]))} \n'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(Numbers())

#################################### TASK CONDITION ############################
"""

                             1.	Numbers
First, you will be given two sequences of integers values on different lines. 
The values of the sequences are separated by a single space between them. Keep 
in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive 
one of the following commands:
•	"Add First {numbers, separated by a space}" - add the given numbers at 
the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at 
the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers 
contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers 
contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the 
other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". 
The values in each sequence should be sorted in ascending order.

____________________________________________________________________________________________
Example_01

Input
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset	

Output
True
1, 2, 3, 4, 5, 6
1, 2, 3


____________________________________________________________________________________________
Example_02

Input
5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5	

Output
False
2, 3, 4, 5, 6, 9
6

"""
