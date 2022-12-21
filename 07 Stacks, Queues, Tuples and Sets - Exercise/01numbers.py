##################################### variant 01 #####################################

first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
lines = int(input())

for i in range(lines):
    input_line = input().split()
    command = input_line[0] + ' ' + input_line[1]
    numbers = input_line[2:]

    if command == 'Add First':
        first_sequence = first_sequence.union(map(int, numbers))
    elif command == 'Add Second':
        second_sequence = second_sequence.union(map(int, numbers))
    elif command == 'Remove First':
        for num in map(int, numbers):
            first_sequence.discard(num)
    elif command == 'Remove Second':
        for num in map(int, numbers):
            second_sequence.discard(num)
    elif command == 'Check Subset':
        print(
            'True' if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence) else 'False')

print(', '.join(str(num) for num in sorted(first_sequence)))
print(', '.join(str(num) for num in sorted(second_sequence)))


##################################### variant 02 #####################################
class Main:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.log = []

    def actions(self):
        lines = int(input())
        for i in range(lines):
            input_line = input().split()
            command = input_line[0] + ' ' + input_line[1]
            numbers = input_line[2:]

            if command == 'Add First':
                self.first = self.first.union(map(int, numbers))
            elif command == 'Add Second':
                self.second = self.second.union(map(int, numbers))
            elif command == 'Remove First':
                for num in map(int, numbers):
                    self.first.discard(num)
            elif command == 'Remove Second':
                for num in map(int, numbers):
                    self.second.discard(num)
            elif command == 'Check Subset':
                self.log.append(
                    'True' if self.first.issubset(self.second) or self.second.issubset(self.first) else 'False')

    def result(self):
        self.log.append(', '.join(str(num) for num in sorted(self.first)))
        self.log.append(', '.join(str(num) for num in sorted(self.second)))

    def __repr__(self):
        return '\n'.join(self.log)


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
output = Main(first_sequence, second_sequence)
output.actions()
output.result()
print(output)


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
