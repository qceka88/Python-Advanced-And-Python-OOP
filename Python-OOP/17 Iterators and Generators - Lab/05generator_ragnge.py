##################################### variant 01 #####################################
def genrange(*args):
    # s = start, e = end
    s, e = args

    while s <= e:
        yield s
        s += 1

##################################### variant 02 #####################################
# s = start, e = end
def genrange(s, e):
    for i in range(s, e + 1):
        yield i


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

