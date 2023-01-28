from collections import deque


class PresentFactory:

    def __init__(self):
        self.result_message = ''
        self.boxes = []
        self.magic_values = deque()
        self.factory = {
            150: 'Doll',
            250: 'Wooden train',
            300: 'Teddy bear',
            400: 'Bicycle'}
        self.toys = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
        self.main_meth()

    def main_meth(self):
        self.fill_boxes_with_materials_stack()
        self.fill_magic_values_deque()
        self.start_creating_toys()
        self.prepare_result_message()

    def fill_boxes_with_materials_stack(self):
        self.boxes = [int(x) for x in input().split()]

    def fill_magic_values_deque(self):
        self.magic_values = deque(int(x) for x in input().split())

    def start_creating_toys(self):
        while self.boxes and self.magic_values:
            box = self.boxes.pop()
            magic = self.magic_values.popleft()

            if box == 0 or magic == 0:
                if box != 0:
                    self.boxes.append(box)
                if magic != 0:
                    self.magic_values.appendleft(magic)
                continue
            self.check_crafting_result(box, magic)

    def check_crafting_result(self, box, magic):
        product = box * magic
        if product < 0:
            self.boxes.append(box + magic)
        elif product in self.factory:
            name = self.factory[product]
            self.toys[name] += 1
        elif product > 0:
            self.boxes.append(box + 15)

    def prepare_result_message(self):
        if self.check_success():
            self.result_message = "The presents are crafted! Merry Christmas!"
        else:
            self.result_message = "No presents this Christmas!"
        if self.boxes:
            self.result_message += f"\nMaterials left: {', '.join(str(x) for x in reversed(self.boxes))}"
        if self.magic_values:
            self.result_message += f"\nMagic left: {', '.join(str(x) for x in self.magic_values)}"
        for toy, amount in sorted(self.toys.items()):
            if amount > 0:
                self.result_message += f"\n{toy}: {amount}"

    def check_success(self):
        return self.toys['Doll'] >= 1 and self.toys['Wooden train'] >= 1 \
            or self.toys['Bicycle'] >= 1 and self.toys['Teddy bear'] >= 1

    def __repr__(self):
        return self.result_message


if __name__ == '__main__':
    print(PresentFactory())

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


