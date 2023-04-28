def cache(func):
    def wrapper(n):
        if n not in wrapper.log:
            wrapper.log[n] = func(n)
        return func(n)

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)


#################################### TASK CONDITION ############################
'''
                             5.	Cache
Create a decorator called cache. It should store all the returned values 
of the recursive function fibonacci. You are provided with this code:

 '''

# Code to refactor
# x = "global"


# def cache(func):
#
#
# # TODO: Implement
#
#
# @cache
# def fibonacci(n):
#
#
# if n < 2:
#
#     return n
#
# else:
#
#     return fibonacci(n - 1) + fibonacci(n - 2)

'''
You need to create a dictionary called log that will store all the n's (keys) and the returned 
results (values) and attach that dictionary to the fibonacci function as a variable called log, 
so when you call it, it returns that dictionary. For more clarification, see the examples

_______________________________________________
Example_01

Test Code	(no input data in this task)

fibonacci(3)
print(fibonacci.log)

Output
{1: 1, 0: 0, 2: 1, 3: 2}

_______________________________________________
Example_02

Test Code	(no input data in this task)

fibonacci(4)
print(fibonacci.log)

Output
{1: 1, 0: 0, 2: 1, 3: 2, 4: 3}

'''
