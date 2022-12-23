#################################### variant 01 #####################################
text = list(input())

stack = []
for chr_i in range(len(text)):
    symbol = text[chr_i]

    if symbol == '(':
        stack.append(chr_i)
    elif symbol == ')':
        open_bracket_index = stack.pop()
        string = text[open_bracket_index:chr_i + 1]
        print(''.join(string))
#################################### variant 01 #####################################
class Matching:

    def __init__(self, some_text):
        self.some_text = some_text
        self.indices_stack = []
        self.log = ''

    def matching_parentheses(self):
        for chr_idx in range(len(self.some_text)):
            symbol = self.some_text[chr_idx]

            if symbol == '(':
                self.indices_stack.append(chr_idx)
            elif symbol == ')':
                open_bracket_index = self.indices_stack.pop()
                string = self.some_text[open_bracket_index:chr_idx + 1]
                self.log += f'{"".join(string)}\n'

    def __repr__(self):
        return self.log


expression = input()
output = Matching(expression)
output.matching_parentheses()
print(output)


#################################### TASK CONDITION ############################
"""

                     2.	Matching Parentheses
You are given an algebraic expression with parentheses. 
Scan through the string and extract each set of parentheses.
Print the result back on the console.

____________________________________________________________________________________________
Example_01

Input
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

Output
(2 + 3)
(3 + 1)
(2 - (2 + 3) * 4 / (3 + 1))

____________________________________________________________________________________________
Example_02

Input
(2 + 3) - (2 + 3)

Output
(2 + 3)
(2 + 3)


"""
