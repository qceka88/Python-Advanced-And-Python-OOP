##################################### variant 01 #####################################
from functools import reduce



def operate(operator, *args):
    result = reduce(lambda x, y: eval(str(x) + operator + str(y)), args)
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))




##################################### variant 02 #####################################
from functools import reduce
class Operator:

    def __init__(self, symbol, numbers):
        self.operator, self.numbers = symbol, numbers

    def action(self):
        result = reduce(lambda x, y: eval(str(x) + self.operator + str(y)), self.numbers)
        return result


def operate(operator, *args):
    output = Operator(operator, args).action()
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
