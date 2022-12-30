##################################### variant 01 #####################################
def func_executor(*args):
    output = []
    for data in args:
        func_name, func_data = data
        result = func_name(*func_data)
        output.append(f'{func_name.__name__} - {result}')
    return '\n'.join(output)

#Part below is part from automatic judge system from SoftUni
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

##################################### variant 02 #####################################

class Executor:

    def __init__(self, *args):
        self.args = args
        self.output = []

    def func_executor(self):
        for data in self.args:
            func_name, func_data = data
            result = func_name(*func_data)
            self.output.append(f'{func_name.__name__} - {result}')
        return '\n'.join(self.output)


def func_executor(*args):
    output = Executor(*args).func_executor()
    return output

#Part below is part from automatic judge system from SoftUni
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))


#################################### TASK CONDITION ############################
'''
                6.	Function Executor
Create a function called func_executor() that can receive a different 
number of tuples, each of which will have exactly 2 elements: the first 
will be a function, and the second will be a tuple of the arguments that 
need to be passed to that function. You should execute each function and 
return its result in the format:
"{function name} - {function result}"
For more clarification, see the examples below.
Submit only your function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)), 
    (multiply_numbers, (2, 4))
))	

Output
sum_numbers - 3
multiply_numbers - 8

_______________________________________________
Example_02

Test Code	(no input data in this task)
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

Output
make_upper - ('PYTHON', 'SOFTUNI')
make_lower - ('python', )


'''