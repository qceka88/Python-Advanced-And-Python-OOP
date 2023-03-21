def multiply(times):
    def decorator(function):
        def wrapper(numer):
            return function(numer) * times

        return wrapper

    return decorator

# Part below is part from automatic judge system from SoftUni
@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))


#################################### TASK CONDITION ############################
'''
4.	Multiply
Having the following code:


'''


def multiply(times):
    def decorator(function):
        # TODO: Implement
        ...

    return decorator


'''
Complete the code, so it works as expected.

_______________________________________________
Example_01

Test Code	(no input data in this task)

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


Output

39

_______________________________________________
Example_02

Test Code	(no input data in this task)

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

Output 


80


'''
