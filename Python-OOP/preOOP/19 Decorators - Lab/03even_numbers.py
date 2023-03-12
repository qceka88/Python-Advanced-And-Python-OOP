def even_numbers(function):
    def wrapper(numbers):
        return [x for x in numbers if x % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

#################################### TASK CONDITION ############################
'''
3.	Even Numbers
Having the following code:

'''


def even_numbers(function):
    def wrapper(numbers):
        # TODO: Implement
        ...

    return wrapper


'''
Complete the code, so it works as expected.

_______________________________________________
Example

Test Code	(no input data in this task)

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))


Output
[2, 4]

'''
