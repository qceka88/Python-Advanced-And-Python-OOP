def make_bold(func):
    def wrapper(*data):
        return f"<b>{func(*data)}</b>"

    return wrapper


def make_italic(func):
    def wrapper(*data):
        return f"<i>{func(*data)}</i>"

    return wrapper


def make_underline(func):
    def wrapper(*data):
        return f"<u>{func(*data)}</u>"

    return wrapper


# Part below is part from automatic judge system from SoftUni
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))


#################################### TASK CONDITION ############################
'''
3.	Bold, Italic, Underline
Create three decorators: make_bold, make_italic, make_underline, 
which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.

_______________________________________________
Example_01

Test Code	(no input data in this task)

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

Output
<b><i><u>Hello, Peter</u></i></b>

_______________________________________________
Example_02

Test Code	(no input data in this task)

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))


Output
<b><i><u>Hello, Peter, George</u></i></b>


'''