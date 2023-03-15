def tags(tag):
    def decorator(function):
        def wrapper(*data):
            return f"<{tag}>{function(*data)}</{tag}>"

        return wrapper

    return decorator

# Part below is part from automatic judge system from SoftUni
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))



#################################### TASK CONDITION ############################
'''

                6.	HTML Tags
Create a decorator called tags. It should receive an HTML tag as a parameter, 
wrap the result of a function with the given tag and return the new result. 
For more clarification, see the examples below

_______________________________________________
Example_01

Test Code	(no input data in this task)

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

Output
<p>Hello you!</p>

_______________________________________________
Example_02

Test Code	(no input data in this task)

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

Output
<h1>HELLO</h1>

'''