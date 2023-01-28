##################################### variant 01 #####################################
from collections import deque

elves = deque(map(int, input().split()))
boxes = list(map(int, input().split()))
created_toys = 0
total_elves_energy = 0
elf_counter = 0

while boxes and elves:
    current_box = boxes.pop()
    while elves:
        current_elf = elves.popleft()
        if current_elf < 5:
            if not elves:
                boxes.append(current_box)
            continue
        elf_counter += 1
        current_toys = 1
        cookie = 1
        needed_energy = current_box
        if elf_counter % 3 == 0:
            current_toys = 2
            needed_energy *= 2
        if needed_energy > current_elf:
            current_elf *= 2
            elves.append(current_elf)
            continue
        else:
            if elf_counter % 5 == 0:
                cookie = 0
                current_toys = 0
            current_elf -= needed_energy
            total_elves_energy += needed_energy
            elves.append(current_elf + cookie)
            created_toys += current_toys
            break

print(f'Toys: {created_toys}')
print(f'Energy: {total_elves_energy}')
if elves:
    print(f'Elves left: {", ".join(str(e) for e in elves)}')
if boxes:
    print(f'Boxes left: {", ".join(map(str, boxes))}')

##################################### variant 02 #####################################
from collections import deque


class ChristmasElves:

    def __init__(self, elves, boxes):
        self.elves = elves
        self.boxes = boxes
        self.created_toys = 0
        self.total_elves_energy = 0
        self.output_message = ''

    def create_the_toys(self):
        elf_counter = 0
        while self.boxes and self.elves:
            current_box = self.boxes.pop()

            while self.elves:
                current_elf = self.elves.popleft()

                if current_elf < 5:
                    if not self.elves:
                        self.boxes.append(current_box)
                    continue

                elf_counter += 1
                current_toys, cookie, needed_energy = 1, 1, current_box

                if elf_counter % 3 == 0:
                    current_toys, needed_energy = 2, needed_energy * 2

                if needed_energy > current_elf:
                    current_elf *= 2
                    self.elves.append(current_elf)
                    continue
                else:
                    if elf_counter % 5 == 0:
                        cookie, current_toys = 0, 0

                    current_elf -= needed_energy
                    self.total_elves_energy += needed_energy
                    self.elves.append(current_elf + cookie)
                    self.created_toys += current_toys
                    break

    def return_result(self):
        self.output_message = f'Toys: {self.created_toys}\nEnergy: {self.total_elves_energy}'
        if self.elves:
            self.output_message += f'\nElves left: {", ".join(str(e) for e in self.elves)}'
        if self.boxes:
            self.output_message += f'\nBoxes left: {", ".join(map(str, self.boxes))}'

    def __repr__(self):
        return f'{self.output_message}'


elves_energy_que = deque(map(int, input().split()))
boxes_stack = [int(box) for box in input().split()]
output = ChristmasElves(elves_energy_que, boxes_stack)
output.create_the_toys()
output.return_result()
print(output)

#################################### TASK CONDITION ############################
'''

                 01.	 Christmas Elves
         
Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, 
a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't be able 
to meet their December deadline. It could be a disaster, and some children around the 
world may not get their Christmas toys. Luckily, you've come up with an idea, and you 
just need to write a program that manages your plan. The Christmas elves have special 
toy-making skills - еach elf can make a toy from a given number of materials. First, 
you will receive a sequence of integers representing each elf's energy. On the following 
line, you will be given another sequence of integers, each representing a number of 
materials in a box.Your task is to calculate the total elves' energy used for making 
toys and the total  number of successfully made toys.You are very clever and have immediately 
recognized  the pros and cons of the work process - the first elf takes the last box of materials 
and tries to create the toy:
•	Usually, the elf needs energy equal to the number of materials. If he has enough energy, 
he makes the toy. His energy decreases by the used energy, and the toy goes straight 
to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1,
 and goes to the end of the line, preparing for the upcoming boxes.
•	Every third time one of the elves takes a box, he tries his best to be creative, 
and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys. 
Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
•	Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages 
to break the toy when he just made it (if he made it). The toy is thrown away, and the elf 
doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
o	If an elf creates 2 toys, but he is clumsy, he breaks them.
•	If an elf does not have enough energy, he leaves the box of materials to the next elf. 
Instead of making the toy, the elf drinks a hot chocolate which doubles his energy, 
and goes to the end of the line, preparing for the upcoming boxes.
Note: North Pole's social policy is very tolerant of the elves. If the current elf's 
energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. 
Remove the elf from the collection.
Stop crafting toys when you are out of materials or elves.
Input
•	The first line of input will represent each elf's energy - integers, separated by a single space
•	On the second line, you will be given the number of materials in each box - integers, 
separated by a single space
Output
•	On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
•	On the second line, print the total used energy: "Energy: {total_used_energy}"
•	On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
o	"Elves left: {elf1}, {elf2}, … {elfN}"
o	"Boxes left: {box1}, {box2}, … {boxN}"
Constraints
•	All the elves' values will be integers in the range [1, 100]
•	All the boxes' values will be integers in the range [1, 100]

_______________________________________________
Example_01

Input
10 16 13 25
12 11 8

Output
Toys: 3
Energy: 31
Elves left: 3, 6, 26, 14

Example
1) The elf with energy 10 takes the box with 8 materials. He creates 1 gift and uses 8 units 
of energy. He eats a cookie and goes to the end of the line, which now looks like this: 16 13 25 3.
2) The elf with energy 16 takes the box with 11 materials. He creates 1 gift and uses 11 units 
of energy. Then, he eats a cookie and goes to the end of the line, which now looks like this: 13 25 3 6.
3) The elf with energy 13 takes the box with 12 materials. It is the third time an elf takes a box. 
The elf does not have the needed energy: 12 * 2, so he drinks a hot chocolate and goes 
to the end of the line: 25 3 6 26.
4) The elf with energy 25 takes the box with 12 materials. It is the fourth time an elf takes a box.
He creates 1 gift and uses 12 units of energy. He eats a cookie and goes to the end of the line,
which now looks like this: 3 6 26 14.
No boxes are left, so the program ends. Print the desired text.

_______________________________________________
Example_02

Input
10 14 22 4 5
11 16 17 11 1 8

Output 
Toys: 7
Energy: 75
Elves left: 10, 14

_______________________________________________
Example_03

Input
5 6 7
2 1 5 7 5 3

Output
Toys: 3
Energy: 20
Boxes left: 2, 1	

'''
