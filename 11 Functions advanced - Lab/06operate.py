from functools import reduce


class Operate:

    def __init__(self, operator, *args):
        self.operator = operator
        self.numbers = args
        self.actions = {
            '+': self.sum_numbers,
            '-': self.subtract_numbers,
            '*': self.multiply_numbers,
            '/': self.divide_numbers,
        }

    def main_meth(self):
        result = self.actions[self.operator]()
        return result

    def subtract_numbers(self):
        return reduce(lambda a, b: a - b, self.numbers)

    def sum_numbers(self):
        return reduce(lambda a, b: a + b, self.numbers)

    def multiply_numbers(self):
        return reduce(lambda a, b: a * b, self.numbers)

    def divide_numbers(self):
        return reduce(lambda a, b: a / b, self.numbers)


def operate(*args):
    output = Operate(*args).main_meth()
    return output


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


#################################### TASK CONDITION ############################
'''
                      6.	Operate
Write a function called operate that receives an operator 
("+", "-", "*" or "/") as first argument and multiple numbers (integers) 
as additional arguments (*args). The function should return the result of
the operator applied to all the numbers. For more clarification, see the examples below. 
Submit only your function in the Judge system.
Note: Be careful when you have multiplication and division

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(operate("+", 1, 2, 3))	

Output
6	

Explanation
1 + 2 + 3 = 6

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(operate("*", 3, 4))	

Output
12	

Explanation
3 * 4 = 12


'''
