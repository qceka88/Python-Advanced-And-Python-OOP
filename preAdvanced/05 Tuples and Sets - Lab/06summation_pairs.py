##################################### variant 01 #####################################
from collections import deque

row = deque(map(int, input().split()))
target = int(input())

for i in range(len(row)):
    num_01 = row.popleft()
    for j in range(len(row)):
        num_02 = row.popleft()
        if num_01 + num_02 == target:
            print(f"{num_01} + {num_02} = {target}")
            break
        else:
            row.append(num_02)
    else:
        row.append(num_01)

##################################### variant 02 #####################################

from collections import deque


class Main:

    def __init__(self, row, number):
        self.row = row
        self.number = number
        self.result = []

    def compare(self):
        for i in range(len(self.row)):
            num_01 = self.row.popleft()
            for j in range(len(self.row)):
                num_02 = self.row.popleft()
                if num_01 + num_02 == self.number:
                    print(f"{num_01} + {num_02} = {self.number}")
                    break
                else:
                    self.row.append(num_02)
            else:
                self.row.append(num_01)

    def __repr__(self):
        return '\n'.join(code for code in self.result)


row_numbers = deque(map(int, input().split()))
target = int(input())
output = Main(row_numbers, target)
output.compare()
print(output)




#################################### TASK CONDITION ############################
"""
                    6.	Summation Pairs
The task is not included in the Judge system. On the first line, 
you will receive a sequence of numbers separated by space. On the 
second line, you'll receive a target number. Your task is to find 
the pairs of numbers whose sum equals the target number. For each 
found pair print "{number} + {number} = {target_number}". You may 
NOT use the same element twice to fulfill the condition above.
Can you come up with an algorithm that has less time complexity?

____________________________________________________________________________________________
Example_01

Input
1 5 4 2 2 3 1 3 2
4	

Output
1 + 3 = 4
1 + 3 = 4
2 + 2 = 4

____________________________________________________________________________________________
Example_02

Input
11 8 5 6 9 2 9 7 3 4
11 	

Output
8 + 3 = 11
5 + 6 = 11
9 + 2 = 11
7 + 4 = 11

"""