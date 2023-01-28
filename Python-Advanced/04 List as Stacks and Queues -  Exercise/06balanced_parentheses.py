from collections import deque


class BalancedParentheses:

    def __init__(self):
        self.sequence = deque(input())
        self.is_balanced = True
        self.opening_brackets = []
        self.balancing = {"(": ")", "[": "]", "{": "}"}
        self.message = ''
        self.main()

    def check_brackets(self, some_bracket):
        opening_bracket = self.opening_brackets.pop()
        if self.balancing[opening_bracket] != some_bracket:
            self.is_balanced = False

    def check_for_balancing(self):
        while self.sequence and self.is_balanced:
            bracket = self.sequence.popleft()
            if bracket in "{[(":
                self.opening_brackets.append(bracket)
            elif self.opening_brackets:
                self.check_brackets(bracket)
            else:
                self.is_balanced = False


    def prepare_result(self):
        self.message = 'YES' if self.is_balanced else 'NO'

    def main(self):
        self.check_for_balancing()
        self.prepare_result()

    def __repr__(self):
        return self.message


if __name__ == "__main__":
    print(BalancedParentheses())



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
