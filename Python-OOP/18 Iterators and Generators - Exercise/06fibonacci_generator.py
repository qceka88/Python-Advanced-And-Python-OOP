def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1

        n1, n2 = n2, n1 + n2


# Part below is part from automatic judge system from SoftUni
generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))

#################################### TASK CONDITION ############################
'''
           6.	Fibonacci Generator
Create a generator function called fibonacci() that generates the Fibonacci 
numbers infinitely. The first two numbers in the sequence are always 0 and 1. 
Each following Fibonacci number is created by the sum of the current number with the previous one.
Note: Submit only the function in the judge system


_______________________________________________
Example_01

Test Code	(no input data in this task)


generator = fibonacci()
for i in range(5):
    print(next(generator))


Output

0
1
1
2
3


_______________________________________________
Example_02

Test Code	(no input data in this task)


generator = fibonacci()
for i in range(1):
    print(next(generator))

Output

0

'''
