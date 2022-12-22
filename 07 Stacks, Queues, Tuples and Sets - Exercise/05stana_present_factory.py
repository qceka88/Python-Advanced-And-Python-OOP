##################################### variant 01 #####################################
from collections import deque

box_stack = list(map(int, input().split()))
magic_deque = deque(map(int, input().split()))

toys = {150: ['Doll', 0], 250: ['Wooden train', 0], 300: ['Teddy bear', 0], 400: ['Bicycle', 0]}

while box_stack and magic_deque:
    box = box_stack.pop()
    magic = magic_deque.popleft()
    if box == 0 or magic == 0:
        if box != 0:
            box_stack.append(box)
        if magic != 0:
            magic_deque.appendleft(magic)
        continue

    total_magic = box * magic
    if total_magic in toys:
        toys[total_magic][1] += 1
    elif total_magic < 0:
        total_magic = box + magic
        box_stack.append(total_magic)
    else:
        box_stack.append(box + 15)

if toys[150][1] > 0 and toys[250][1] > 0 or toys[300][1] > 0 and toys[400][1] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if box_stack:
    print(f"Materials left: {', '.join(str(i) for i in reversed(box_stack))}")
if magic_deque:
    print(f"Magic left: {', '.join(map(str, magic_deque))}")

for magic_level, data in sorted(toys.items(), key=lambda x: x[1][0]):
    toy_name = data[0]
    amount = data[1]
    if amount > 0:
        print(f'{toy_name}: {amount}')

##################################### variant 02 #####################################
from collections import deque


class Main:
    def __init__(self, materials, magic):
        self.materials = materials
        self.magic = magic
        self.toys = {150: ['Doll', 0], 250: ['Wooden train', 0], 300: ['Teddy bear', 0], 400: ['Bicycle', 0]}
        self.message = []

    def factory(self):
        while self.materials and self.magic:
            box = self.materials.pop()
            magic = self.magic.popleft()
            if box == 0 or magic == 0:
                if box != 0:
                    self.materials.append(box)
                if magic != 0:
                    self.magic.appendleft(magic)
                continue

            total_magic = box * magic
            if total_magic in self.toys:
                self.toys[total_magic][1] += 1
            elif total_magic < 0:
                total_magic = box + magic
                self.materials.append(total_magic)
            else:
                self.materials.append(box + 15)

    def result(self):
        if self.toys[150][1] > 0 and self.toys[250][1] > 0 or self.toys[300][1] > 0 and self.toys[400][1] > 0:
            self.message.append("The presents are crafted! Merry Christmas!")
        else:
            self.message.append("No presents this Christmas!")
        if self.materials:
            self.message.append(f"Materials left: {', '.join(str(i) for i in reversed(self.materials))}")
        if self.magic:
            self.message.append(f"Magic left: {', '.join(map(str, self.magic))}")

        for magic_level, data in sorted(self.toys.items(), key=lambda x: x[1][0]):
            toy_name, amount = data[0], data[1]
            if amount > 0:
                self.message.append(f'{toy_name}: {amount}')

    def __repr__(self):
        return '\n'.join(self.message)


box_materials_stack = list(map(int, input().split()))
magic_deque = deque(map(int, input().split()))

output = Main(box_materials_stack, magic_deque)
output.factory()
output.result()
print(output)


#################################### TASK CONDITION ############################
"""

  5.	Santa's Present Factory
This year Santa has decided to share his secret with you. Get ready to learn 
how his elves craft all the presents. First, you will receive a sequence of 
integers representing the number of materials for crafting toys in one box. 
After that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in 
the table below with the exact magic level:


Present	Magic needed
Doll	        150
Wooden train	250
Teddy bear	    300
Bicycle 	    400

You should take the last box with materials and the first magic level value to 
craft a toy. Their multiplication calculates the total magic level. If the result 
equals one of the levels described in the table above, you craft the present and 
remove both materials and magic value. Otherwise:
•	If the product of the operation is a negative number, you should sum the
 values together, remove them both from their positions, and add the result to the materials.
•	If the product doesn't equal one of the magic levels in the table and
 is a positive number, remove only the magic value and increase the material value by 15.
•	If the magic or material (or both) equals 0, remove it (or both) and
 continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
•	a doll and a train
•	a teddy bear and a bicycle
Input
•	The first line of input will represent the values of boxes with
 materials - integers, separated by a single space
•	On the second line, you will be given the magic values - integers
 again, separated by a single space
Output
•	On the first line - print whether you've succeeded in crafting the presents:
o	"The presents are crafted! Merry Christmas!"
o	"No presents this Christmas!"
•	On the next two lines print the materials and magic that are left,
 if there are any (otherwise skip the line)
o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
•	On the next lines print the presents you have crafted, ordered alphabetically in the format:
o	"{toy_name1}: {amount}
{toy_name2}: {amount}
...
{toy_nameN}: {amount}"
Constraints
•	All the materials' values will be integers in the range [1, 100]
•	Magic level values will be integers in the range [-10, 100]
•	In all cases, at least one present will be crafted

____________________________________________________________________________________________
Example_01

Input
10 -5 20 15 -30 10
40 60 10 4 0 0	

Output
The presents are crafted! Merry Christmas!
Materials left: 20, -5, 10
Bicycle: 1
Teddy bear: 2	

Explanation
First, we have 40*10=400, which is the needed magic for a bicycle. Remove both.
60*(-30) = -1800 (negative). 60+(-30) = 30. Remove 60 and -30. Add 30 to materials.
30*10=300 (bear). Remove both.
4*15=60, so remove 4, and the material is increased by 15 (15+15=30).
10*30=300 (bear).
Print desired text.

____________________________________________________________________________________________
Example_02

Input
30 5 15 60 0 30
-15 10 5 -15 25	

Output
No presents this Christmas!
Materials left: 20, 30
Doll: 1
Teddy bear: 1


____________________________________________________________________________________________
Example_03

Input
30 10
15 10 5 0 10	

Output
No presents this Christmas!
Magic left: 5, 0, 10
Doll: 1
Teddy bear: 1	


"""


