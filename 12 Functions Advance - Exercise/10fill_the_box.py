from functools import reduce
from collections import deque


class BoxFill:

    def __init__(self, *args):
        self.result = ''
        self.data = deque(args)
        self.box = 0

    def main_meth(self):
        self.define_capacity_of_box()
        self.define_data_for_processing()
        self.start_to_fill_the_box_with_cubes()
        self.prepare_output_message()
        return self.result

    def define_capacity_of_box(self):
        dimensions_of_box = [self.data[n] for n in range(3)]
        self.box = reduce(lambda a, b: a * b, dimensions_of_box)

    def define_data_for_processing(self):
        self.data = deque(self.data[n] for n in range(3, len(self.data) - 1))

    def start_to_fill_the_box_with_cubes(self):
        def put_cubes_in_box(some_data):
            cubes = some_data
            if self.box - cubes >= 0:
                self.box -= cubes
            else:
                cubes -= self.box
                self.box = 0
                self.data.append(cubes)

        while self.data:
            data = self.data.popleft()
            if data == 'Finish':
                break
            put_cubes_in_box(data)
            if not self.box:
                break

    def prepare_output_message(self):
        if not self.box:
            self.result = f'No more free space! You have {sum(self.data)} more cubes.'
        else:
            self.result = f'There is free space in the box. You could put {self.box} more cubes.'


def fill_the_box(*args):
    output = BoxFill(*args).main_meth()
    return output


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