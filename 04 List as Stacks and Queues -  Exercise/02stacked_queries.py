##################################### variant 01 #####################################
number_of_lines = int(input())

stack = []

for iteration in range(number_of_lines):
    data = input().split()

    if data[0] == '1':
        number = int(data[1])
        stack.append(number)
    if stack:
        if data[0] == '2':
            stack.pop()
        elif data[0] == '3':
            print(max(stack))
        elif data[0] == '4':
            print(min(stack))

print(*stack[::-1], sep=', ')


##################################### variant 01 #####################################
class Queries:

    def __init__(self, number):
        self.number = number
        self.stack = []
        self.log = ''

    def actions(self):
        for iteration in range(self.number):
            data = input().split()

            if data[0] == '1':
                number = int(data[1])
                self.stack.append(number)
            if self.stack:
                if data[0] == '2':
                    self.stack.pop()
                elif data[0] == '3':
                    self.log += f'{max(self.stack)}\n'
                elif data[0] == '4':
                    self.log += f'{min(self.stack)}\n'

        self.log += f'{", ".join(str(ch) for ch in self.stack[::-1])}'

    def __repr__(self):
        return self.log


number_of_lines = int(input())
output = Queries(number_of_lines)
output.actions()
print(output)
#################################### TASK CONDITION ############################
"""
                        2. Stacked Queries
You have an empty stack. You will receive an integer – N. 
On the next N lines, you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"

____________________________________________________________________________________________
Example_01

Input
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

Output
26
20
91, 20, 26

____________________________________________________________________________________________
Example_02

Input
10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4

Output
32
66
8
8, 16, 25, 32, 66, 47


"""