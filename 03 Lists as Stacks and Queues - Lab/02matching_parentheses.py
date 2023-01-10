class MatchingParentheses:

    def __init__(self, sequence):
        self.sequence = sequence
        self.opening_bracket_indexes = []
        self.result = []

    def matching_parentheses(self):
        for index in range(len(self.sequence)):
            character = self.sequence[index]

            if character == '(':
                self.opening_bracket_indexes.append(index)
            elif character == ')':
                last_opening_index = self.opening_bracket_indexes.pop()
                self.result.append(self.sequence[last_opening_index:index + 1])

    def __repr__(self):
        return '\n'.join(self.result)


output = MatchingParentheses(input())
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
