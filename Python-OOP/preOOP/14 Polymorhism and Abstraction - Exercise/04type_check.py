def type_check(main_type):
    def decorator(function):
        def wrapper(data):
            if main_type == type(data):
                return function(data)

            return "Bad Type"
        return wrapper
    return decorator


# Part below is part from automatic judge system from SoftUni
@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


#################################### TASK CONDITION ############################
'''
                4.	Type Check
Create a decorator called type_check. It should receive a type (int/float/str/…), 
and it should check if the parameter passed to the decorated function is of the type 
given to the decorator. If it is, execute the function and return the result, 
otherwise return "Bad Type".

_______________________________________________
Example_01

Test Code	(no input data in this task)

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

Output
4
Bad Type

_______________________________________________
Example_02

Test Code	(no input data in this task)

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

Output
H
Bad Type


'''