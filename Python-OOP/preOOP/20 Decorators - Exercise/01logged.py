def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}({', '.join(str(n) for n in args)})\nit returned {function(*args)}"

    return wrapper


# Part below is part from automatic judge system from SoftUni
@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))



#################################### TASK CONDITION ############################
'''
              1.	Logged
Create a decorator called logged. It should return the name of the function that is 
being called and its parameters. It should also return the result of the execution 
of the function being called. See the examples for more clarification.

_______________________________________________
Example_01

Test Code	(no input data in this task)

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


Output
you called func(4, 4, 4)
it returned 6


_______________________________________________
Example_02

Test Code	(no input data in this task)

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))	you called sum_func(1, 4)
it returned 5


'''