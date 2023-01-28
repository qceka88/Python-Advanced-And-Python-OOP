##################################### variant 01 #####################################
def fill_the_box(height, length, width, *args):
    capacity = height * length * width
    left_boxes = 0
    for box in args:
        if box == 'Finish':
            break
        if capacity >= box:
            capacity -= box
        else:
            box -= capacity
            capacity = 0
            left_boxes += box
    if capacity > left_boxes:
        return f'There is free space in the box. You could put {capacity} more cubes.'
    else:
        return f'No more free space! You have {left_boxes} more cubes.'


# Part below is part from automatic judge system from SoftUni
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
##################################### variant 02 #####################################
from collections import deque


class Boxes:
    def __init__(self, height, length, width, *args):
        self.capacity = height * length * width
        self.boxes = deque(args)
        self.left_boxes = 0

    def fill_the_box(self):
        while self.boxes:
            command = self.boxes.popleft()
            if command == 'Finish':
                break
            box = command
            if self.capacity >= box:
                self.capacity -= box
            else:
                box -= self.capacity
                self.boxes.remove('Finish')
                self.boxes.append(box)
                self.left_boxes += sum(self.boxes)
                break

    def return_result(self):
        if self.capacity > self.left_boxes:
            return f'There is free space in the box. You could put {self.capacity} more cubes.'
        else:
            return f'No more free space! You have {self.left_boxes} more cubes.'


def fill_the_box(*args):
    output = Boxes(*args)
    output.fill_the_box()
    return output.return_result()


# Part below is part from automatic judge system from SoftUni
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

#################################### TASK CONDITION ############################
'''
                10.	*Fill the Box
Write a function called fill_the_box that receives a different number of arguments representing:
•	the height of a box
•	the length of a box
•	the width of a box
•	n-times a different number of cubes with exact size 1 x 1 x 1
•	a string "Finish"
Your task is to fill the box with the given cubes 
until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
•	If, at the end, there is free space left 
in the box, print:
o	"There is free space in the box. You could put {free space in cubes} more cubes."
•	If there is no free space in the box, print:
o	"No more free space! You have {cubes left} more cubes."

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))	

Output
There is free space in the box. You could put 13 more cubes.	

Explanation
The size of the box: 2 * 8 * 2 = 32
We put the cubes consistently.
At the end there is more free space left. 

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

Output
No more free space! You have 17 more cubes.	

Explanation
The size of the box: 5 * 5 * 2 = 50
We put the cubes consistently. 
First, we put 40 cubes and there is free space left. 
Then we try to put 11 cubes, but there is only space for 10.
Cubes left: 1 + 7 + 3 + 1 + 5 = 17

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))	

Output
There is free space in the box. You could put 960 more cubes.	

'''