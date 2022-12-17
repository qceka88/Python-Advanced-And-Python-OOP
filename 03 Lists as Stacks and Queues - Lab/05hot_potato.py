#################################### variant 01 #####################################

from collections import deque

kids = deque(input().split())
step = int(input())

while kids:
    kids.rotate(-step)
    kid_name = kids.pop()
    if len(kids) == 0:
        print(f'Last is {kid_name}')
        break
    print(f'Removed {kid_name}')

#################################### variant 02 #####################################

from collections import deque


class Potato:

    def __init__(self, some_kids, some_number):
        self.some_kids = some_kids
        self.some_number = some_number
        self.log = ''

    def pass_potato(self):
        while self.some_kids:
            self.some_kids.rotate(-self.some_number)
            kid_name = self.some_kids.pop()
            if len(kids) == 0:
                self.log += f'Last is {kid_name}'
                break
            self.log += f'Removed {kid_name}\n'

    def __repr__(self):
        return self.log


kids = deque(input().split())
step = int(input())

output = Potato(kids, step)
output.pass_potato()
print(output)

#################################### TASK CONDITION ############################
"""
                   5.	Hot Potato
Hot Potato is a game in which children form a circle and toss a hot potato. 
The counting starts with the first kid. Every nth toss, the child holding the 
potato leaves the game. When a kid leaves the game, it passes the potato to the 
next kid. It continues until there is only one kid left. Create a program that 
simulates the game of Hot Potato. On the first line, you will receive kids' names, 
separated by a single space. On the second line, you will receive the nth toss 
(integer) in which a child leaves the game.Print every kid who is removed from 
the circle in the format "Removed {kid}". In the end, print the only kid left 
in the format "Last is {kid}".

____________________________________________________________________________________________
Example_01

Input
Tracy Emily Daniel
2

Output
Removed Emily
Removed Tracy
Last is Daniel

____________________________________________________________________________________________
Example_02

Input
George Peter Michael William Thomas
10	

Output
Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William

____________________________________________________________________________________________
Example_03

Input
George Peter Michael William Thomas
1

Output
Removed George
Removed Peter
Removed Michael
Removed William
Last is Thomas

"""