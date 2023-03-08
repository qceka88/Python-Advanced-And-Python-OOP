def genrange(start, end):
    number = start
    while number <= end:
        yield number
        number += 1

# Part below is part from automatic judge system from SoftUni
print(list(genrange(1, 10)))


#################################### TASK CONDITION ############################
'''
                        5.	Generator Range
Create a generator function called genrange that receives a start (int) and an
end (int) upon initialization. It should generate all the 
numbers from the start to the end (inclusive).



_______________________________________________
Example

Test Code	(no input data in this task)

print(list(genrange(1, 10)))


Output

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'''
