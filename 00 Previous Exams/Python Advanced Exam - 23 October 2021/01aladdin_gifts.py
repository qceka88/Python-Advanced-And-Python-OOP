##################################### variant 01 #####################################

from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(int(n) for n in input().split())

catalogue = {
    'Gemstone': [100, 199], 'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399], 'Diamond Jewellery': [400, 499]}

created_presents = {
    'Gemstone': 0, 'Porcelain Sculpture': 0,
    'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    product = current_material + current_magic

    if product < 100:
        if product % 2 == 0:
            product = current_material * 2 + current_magic * 3
        else:
            product *= 2
    elif product > 499:
        product /= 2

    if 100 <= product <= 499:
        for gift, cost in catalogue.items():
            if cost[0] <= product <= cost[1]:
                created_presents[gift] += 1
                break

success = created_presents['Gemstone'] > 0 and created_presents['Porcelain Sculpture'] > 0 or \
          created_presents['Gold'] > 0 and created_presents['Diamond Jewellery'] > 0
if success:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic_levels:
    print(f'Magic left: {", ".join(map(str, magic_levels))}')
print('\n'.join(f'{key}: {value}' for key, value in sorted(created_presents.items()) if value > 0))

##################################### variant 02 #####################################

from collections import deque


class AladdinGifts:

    def __init__(self, materials, magic_levels):
        self.materials = materials
        self.magic_levels = magic_levels
        self.catalogue = {
            'Gemstone': [100, 199], 'Porcelain Sculpture': [200, 299],
            'Gold': [300, 399], 'Diamond Jewellery': [400, 499]}
        self.created_presents = {
            'Gemstone': 0, 'Porcelain Sculpture': 0,
            'Gold': 0, 'Diamond Jewellery': 0}
        self.output_message = ''

    def build_the_gifts(self):
        while self.materials and self.magic_levels:
            current_material = self.materials.pop()
            current_magic = self.magic_levels.popleft()
            product = current_material + current_magic

            if product < 100:
                if product % 2 == 0:
                    product = current_material * 2 + current_magic * 3
                else:
                    product *= 2
            elif product > 499:
                product /= 2

            if 100 <= product <= 499:
                for gift, cost in self.catalogue.items():
                    if cost[0] <= product <= cost[1]:
                        self.created_presents[gift] += 1
                        break

    def check_for_success(self):
        success = self.created_presents['Gemstone'] > 0 and self.created_presents['Porcelain Sculpture'] > 0 or \
                  self.created_presents['Gold'] > 0 and self.created_presents['Diamond Jewellery'] > 0
        return success

    def prepare_result(self):
        if self.check_for_success():
            self.output_message = 'The wedding presents are made!'
        else:
            self.output_message = 'Aladdin does not have enough wedding presents.'
        if self.materials:
            self.output_message += f'\nMaterials left: {", ".join(map(str, self.materials))}'
        if self.magic_levels:
            self.output_message += f'\nMagic left: {", ".join(map(str, self.magic_levels))}'
        self.output_message += '\n' + '\n'.join(
            f'{key}: {value}' for key, value in sorted(self.created_presents.items()) if value > 0)

    def __repr__(self):
        return f'{self.output_message}'


material_values = list(map(int, input().split()))
magic_level_values = deque(int(n) for n in input().split())

output = AladdinGifts(material_values, magic_level_values)
output.build_the_gifts()
output.prepare_result()
print(output)

#################################### TASK CONDITION ############################
'''
                        Problem 1 - Aladdin's Gifts

Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess 
Jasmine. He asks Genie for help to prepare the wedding presents. First, you will receive a sequence 
of integers representing the materials for every wedding present. After that, you will be given another 
sequence of integers – Genie magic level for every aim to make a gift. Your task is to mix materials 
with magic levels so you can make presents, listed in the table below.

Gift	                ->      Magic needed
Gemstone	            ->         100 to 199
Porcelain Sculpture     ->         200 to 299
Gold	                ->         300 to 399
Diamond Jewellery       ->         400 to 499

To make a present, you should take the last integer of materials and sum it with the first magic level value. 
If the result is between or equal to the numbers described in the table above, you make the corresponding 
gift and remove both materials and magic value. Otherwise:
•	If the product of the operation is under 100:
o	And if it is an even number, double the materials, and triple the magic, then sum it again. 
o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if 
it is between or equal to any of the numbers in the table above.
•	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. 
Then, check again if it is between or equal to any of the numbers in the table above.
•	If, however, the result is not between or equal to any of the numbers in the table above after performing 
the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and 
a sculpture or gold and jewellery.
Input
•	The first line of input will represent the values of materials - integers, separated by a single space
•	On the second line, you will be given the magic levels - integers, separated by a single space
Output
•	On the first line - print whether you have succeeded in crafting the presents:
o	"The wedding presents are made!"
o	"Aladdin does not have enough wedding presents."
•	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
o	"Materials left: {material1}, {material2}, …"
o	"Magic left: {magicValue1}, {magicValue2}, …
•	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"
Constraints
•	All the materials values will be integers in the range [1, 1000]
•	Magic level values will be integers in the range [1, 1000]

_______________________________________________
Example_01

Input
105 20 30 25
120 60 11 400 10 1

Output
The wedding presents are made!
Magic left: 10, 1
Gemstone: 1
Porcelain Sculpture: 2	First, we have 25 + 120 = 145, which is the needed product 
for a gemstone. Remove both.  30 + 60 = 90 (under 100 and even) => 30 * 2 + 60 * 3 = 240 
which is the needed product for a porcelain sculpture. Remove both. 
20 + 11 = 31 (under 100 and odd) => 31 * 2 = 62 which is under 100 again so we remove both.
105 + 400 = 505 (more than 450) => 505 / 2 = 252.5 which is the needed product for a 
diamond porcelain sculpture. Remove both.
We do not have any material left. The program ends. Print the desired text.

_______________________________________________
Example_02

Input
30 5 21 6 0 91
15 9 5 15 8

Output
Aladdin does not have enough wedding presents.
Materials left: 30
Gemstone: 1	

_______________________________________________
Example_03

Input
200
5 15 32 20 10 5

Output
Aladdin does not have enough wedding presents.
Magic left: 15, 32, 20, 10, 5
Porcelain Sculpture: 1	

'''
