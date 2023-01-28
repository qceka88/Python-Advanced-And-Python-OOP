##################################### variant 01 #####################################
from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    rotations = args[-1]
    best_pureness = [0, 0]
    for rotation in range(rotations + 1):
        summed = sum([idx * value for idx, value in enumerate(numbers)])
        if summed > best_pureness[0]:
            best_pureness = [summed, rotation]
        numbers.rotate()
    return f'Best pureness {best_pureness[0]} after {best_pureness[1]} rotations'


# Part below is part from automatic judge system from SoftUni
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

##################################### variant 02 #####################################

from collections import deque


class Pureness:

    def __init__(self, *args):
        self.numbers = deque(args[0])
        self.rotations = args[-1]
        self.best_pureness = [0, 0]

    def find_pure_combination(self):
        for rotation in range(self.rotations + 1):
            summed = sum([idx * value for idx, value in enumerate(self.numbers)])
            if summed > self.best_pureness[0]:
                self.best_pureness = [summed, rotation]
            self.numbers.rotate()

    def __repr__(self):
        return f'Best pureness {self.best_pureness[0]} after {self.best_pureness[1]} rotations'


def best_list_pureness(*args):
    output = Pureness(*args)
    output.find_pure_combination()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


#################################### TASK CONDITION ############################
'''
                 03 List Pureness
 
Write function called best_list_pureness which will receive a list of numbers and a number K. You have 
to rotate the list K times (last becomes first) to find the variation of the list with the best pureness 
(pureness is calculated by summing all the elements in the list multiplied by their indices). For example, 
in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end 
the function should return a string containing the highest pureness and the amount of rotations that were 
made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} 
rotations". If there is more than one highest pureness, take the first one.
Note: Submit only the function in the judge system
Input
•	There will be no input, just parameters passed to your function
Output
•	There is no expected output
•	The function should return a string in the following format: 
"Best pureness {pureness_value} after {count_rotations} rotations"

_______________________________________________
Example_01

Test Code	(no input data in this task)
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 26 after 3 rotations

Explanation
Rotation 0 -> Pureness 25
Rotation 1 -> Pureness 16
Rotation 2 -> Pureness 23
Rotation 3 -> Pureness 26
Rotation 4 -> Pureness 25

_______________________________________________
Example_02

Test Code	(no input data in this task)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 78 after 2 rotations

Explanation
Rotation 0 -> Pureness 60
Rotation 1 -> Pureness 66
Rotation 2 -> Pureness 78
Rotation 3 -> Pureness 78

_______________________________________________
Example_03

Test Code	(no input data in this task)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 40 after 0 rotations	


'''

