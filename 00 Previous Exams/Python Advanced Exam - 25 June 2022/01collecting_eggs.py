##################################### variant 01 #####################################
from collections import deque

eggs_sizes = deque(map(int, input().split(', ')))
paper_sizes = list(map(int, input().split(', ')))

boxes = 0

while eggs_sizes and paper_sizes:
    current_egg = eggs_sizes.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue
    current_paper = paper_sizes.pop()
    if current_egg + current_paper <= 50:
        boxes += 1

if boxes == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {boxes} boxes.")
if eggs_sizes:
    print(f'Eggs left: {", ".join(map(str, eggs_sizes))}')
if paper_sizes:
    print(f'Pieces of paper left: {", ".join(map(str, paper_sizes))}')
##################################### variant 02 #####################################
from collections import deque


class Eggs:

    def __init__(self, eggs, papers):
        self.eggs = eggs
        self.papers = papers
        self.boxes = 0
        self.log = []

    def packing_the_eggs(self):
        while self.eggs and self.papers:
            current_egg = self.eggs.popleft()
            if current_egg <= 0:
                continue
            if current_egg == 13:
                self.papers[0], self.papers[-1] = self.papers[-1], self.papers[0]
                continue
            current_paper = self.papers.pop()
            if current_egg + current_paper <= 50:
                self.boxes += 1

    def process_output(self):
        if self.boxes == 0:
            self.log.append("Sorry! You couldn't fill any boxes!")
        else:
            self.log.append(f"Great! You filled {self.boxes} boxes.")
        if self.eggs:
            self.log.append(f'Eggs left: {", ".join(map(str, self.eggs))}')
        if self.papers:
            self.log.append(f'Pieces of paper left: {", ".join(map(str, self.papers))}')

    def __repr__(self):
        return '\n'.join(self.log)


eggs_sizes = deque(map(int, input().split(', ')))
paper_sizes = list(map(int, input().split(', ')))

output = Eggs(eggs_sizes, paper_sizes)
output.packing_the_eggs()
output.process_output()
print(output)

#################################### TASK CONDITION ############################
'''

                                   1.	Collecting Eggs
Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.
On the first line, you will receive a sequence of numbers, each representing an egg with its size. 
On the second line, you will receive another sequence of numbers, each representing a piece of paper with its size. 
You should take the first egg and wrap it with the last piece of paper. Then, try to put it in 
a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits in it. Your task 
is to check whether you have filled at least one box. You should comply with the following conditions:
•	If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it 
from the sequence before it is wrapped with a piece of paper.
•	If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), 
put the wrapped egg in the box and remove both from the sequences.
o	Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without 
putting them in a box.
•	During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 
it brings bad luck to him. You should remove this egg from the sequence before it is wrapped with a piece of paper. 
o	Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and 
last pieces of paper positions to bring the good luck back to Old MacDonald.
	Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.
Input
•	In the first line, you will be given a sequence of eggs with their sizes - integers separated
 by comma and space ", " in the range [-100, 100]
•	In the second line, you will be given a sequence of pieces of paper with their sizes - 
integers separated by comma and space ", " in the range [1, 100]
Output
•	On the first line:
o	If you have at least one box filled, print: 
	"Great! You filled {total count} boxes."
o	If you couldn't fill any boxes, print:
	"Sorry! You couldn't fill any boxes!"
•	On the following lines, print the eggs left or pieces of paper left if there are any:
o	Eggs left: {left eggs joined by ", "}
o	Pieces of paper left: {left pieces of paper joined by ", "}
Constraints
•	You will always have at least one egg and at least one piece of paper.

_______________________________________________
Example_01

Input
20, 13, -7, 7
10, 5, 20, 15, 7, 9	

Output
Great! You filled 2 boxes.
Pieces of paper left: 7, 5, 20, 15

Explanation
1) The first egg (20) is wrapped with the last piece of paper (9).
 We put them in a box and remove them from the sequences.
2) The second egg (13) brings back luck so it's removed. Then the 
first piece of paper (10) is switched with the last piece of paper (7).
3) The third egg (-7) is not fresh, so we remove it.
4) The fourth egg (7) is wrapped with the last piece of paper (10). 
We put them in a box and remove them from the sequences. Remove them both.
5) We successfully filled 2 boxes.

_______________________________________________
Example_02

Input
2, 4, 7, 8, 0
5, 6, 2	

Output
Great! You filled 3 boxes.
Eggs left: 8, 0

_______________________________________________
Example_03

Input
12, 23
28, 40	

Output
Sorry! You couldn't fill any boxes!

'''
