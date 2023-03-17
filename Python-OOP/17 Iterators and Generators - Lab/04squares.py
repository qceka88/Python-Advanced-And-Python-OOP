##################################### variant 01 #####################################
def squares(n):
    num = 0

    while num < n:
        num += 1

        yield num ** 2


##################################### variant 02 #####################################
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2


# Part below is part from automatic judge system from SoftUni
print(list(squares(5)))


#################################### TASK CONDITION ############################
'''
                              4.	Squares
Create a generator function called squares that should receive a number n. 
It should generate the squares of all numbers from 1 to n (inclusive).
Note: Submit only the function in the judge system


_______________________________________________
Example

Test Code	(no input data in this task)

print(list(squares(5)))



Output

[1, 4, 9, 16, 25]



'''
