##################################### variant 01 #####################################

from collections import deque

input_line = deque(input())
opening_brackets = deque()
balanced = True

pairs = {"(": ")", "[": "]", "{": "}"}

while input_line:
    bracket = input_line.popleft()

    if bracket in '{([':
        opening_brackets.append(bracket)
    elif not opening_brackets:
        balanced = False
    elif pairs[opening_brackets.pop()] != bracket:
        balanced = False

    if not balanced:
        break

print('YES' if balanced and not opening_brackets else 'NO')

##################################### variant 02 #####################################

from collections import deque


class Balancing:

    def __init__(self, some_text):
        self.some_text = some_text
        self.opening_brackets = deque()
        self.balanced = True
        self.pairs = {"(": ")", "[": "]", "{": "}"}

    def check_balance(self):
        while self.some_text:
            bracket = self.some_text.popleft()

            if bracket in '{([':
                self.opening_brackets.append(bracket)
            elif not self.opening_brackets:
                self.balanced = False
            elif self.pairs[self.opening_brackets.pop()] != bracket:
                self.balanced = False

            if not self.balanced:
                break

    def __repr__(self):
        return 'YES' if self.balanced and not self.opening_brackets else 'NO'


input_line = deque(input())
output = Balancing(input_line)
output.check_balance()
print(output)



input_line = deque(input())
output = Balancing(input_line)
output.check_balance()
print(output)

#################################### TASK CONDITION ############################
"""
                         6. Balanced Parentheses
You will be given a sequence consisting of parentheses. 
Your job is to determine whether the expression is balanced. 
A sequence of parentheses is balanced if every opening 
parenthesis has a corresponding closing parenthesis that occurs 
after the former. There will be no interval symbols between 
the parentheses. You will be given three types of parentheses: (), {}, and [].

{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output 
•	For each test case, print on a new line "YES" if the parentheses are balanced. 
•	Otherwise, print "NO"
Constraints
•	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
•	Each character of the sequence will be one of {, }, (, ), [, ]

____________________________________________________________________________________________
Example_01

Input
{[()]}	

Output
YES

____________________________________________________________________________________________
Example_02

Input
{[(])}	

Output
NO

____________________________________________________________________________________________
Example_02

Input
{{[[(())]]}}

Output
YES

"""
