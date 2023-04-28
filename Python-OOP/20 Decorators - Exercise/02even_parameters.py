def even_parameters(func):
    def wrapper(*args):
        for el in args:
            if not isinstance(el, int) or not el % 2 == 0:
                return "Please use only even numbers!"
        else:
            return func(*args)

    return wrapper


# Part below is part from automatic judge system from SoftUni
@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


#################################### TASK CONDITION ############################
'''
                          2.	Even Parameters
Create a decorator function called even_parameters. It should check if all 
parameters passed to a function are even numbers and only then execute the 
function and return the result. Otherwise, don't execute the function and 
return "Please use only even numbers!"


_______________________________________________
Example_01

Test Code	(no input data in this task)

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

Output
6
Please use only even numbers!


_______________________________________________
Example_02

Test Code	(no input data in this task)


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


Output
384
Please use only even numbers!


'''
