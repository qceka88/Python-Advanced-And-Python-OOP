x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"
        print(x)

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()

#################################### TASK CONDITION ############################
'''
2.	Scope Mess
Fix the code below, so it returns the expected output. Submit the fixed code in the judge system.
 '''

# Code to fix
x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

'''
Examples
Current Output	
global
outer: local
inner: nonlocal
outer: local
global

Expected Output

global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!


'''
