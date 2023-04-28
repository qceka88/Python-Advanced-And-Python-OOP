import timeit


def exec_time(func):
    def wrapper(*args):
        start, _, end = timeit.default_timer(), func(*args), timeit.default_timer()

        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))

@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())



#################################### TASK CONDITION ############################
'''

                           8.	Execution Time
Import the time module. Create a decorator called exec_time. It should calculate 
how much time a function needs to be executed. See the examples for more clarification.
Note: You might have different results from the given ones. The 
solutions to this problem cannot be submitted in the judge system.

_______________________________________________
Example_01

Test Code

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))

Output (It depend on calculating power of current machine)

0.8342537879943848

_______________________________________________
Example_02

Test Code

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

Output (It depend on calculating power of current machine)

0.14537858963012695

_______________________________________________
Example_03

Test Code

@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())

Output (It depend on calculating power of current machine)

0.4199554920196533

'''
