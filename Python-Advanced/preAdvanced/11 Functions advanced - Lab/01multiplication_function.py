##################################### variant 01 #####################################
from functools import reduce


def multiply(*args):
    args = reduce(lambda x, y: x * y, args)
    return args


# This part below is part from automatic test code from Judge system in SoftUni
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
##################################### variant 02 #####################################
from functools import reduce


class Multiply:

    def __init__(self, some_tuple):
        self.some_tuple = some_tuple

    def multiplying(self):
        result = reduce(lambda x, y: x * y, self.some_tuple)
        return result


def multiply(*args):
    output = Multiply(args).multiplying()
    return output


# This part below is part from automatic test code from Judge system in SoftUni
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))

#################################### TASK CONDITION ############################
'''
                1.	Multiplication Function
Write a function called multiply that can receive any quantity of numbers 
(integers) as different parameters and returns the result of the 
multiplication of all of them. Submit only your function in the Judge system.

_______________________________________________
Examples

Test Code	(no input data in this task)
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))	

Output
20
360
0

'''
