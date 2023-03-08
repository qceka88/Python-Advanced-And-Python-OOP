def reverse_text(string):
    
    index = len(string)

    while index > 0:
        yield string[index - 1]

        index -= 1


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
