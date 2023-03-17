##################################### variant 01 #####################################
def reverse_text(some_text):
    idx = len(some_text)

    while idx > 0:
        idx -= 1

        yield some_text[idx]

##################################### variant 02 #####################################
def reverse_text(some_text):
    for let in reversed(some_text):
        yield let


# Part below is part from automatic judge system from SoftUni
for char in reverse_text("step"):
    print(char, end='')


#################################### TASK CONDITION ############################
'''
                            6.	Reverse string
Create a generator function called reverse_text that receives a string and 
yields all string characters on one line in reversed order.

Note: Submit only the function in the judge system


_______________________________________________
Example

Test Code	(no input data in this task)

for char in reverse_text("step"):
    print(char, end='')



Output

pets


'''
