from itertools import permutations


def possible_permutations(data):
    for part in permutations(data):
        yield list(part)


# Part below is part from automatic judge system from SoftUni
[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]



#################################### TASK CONDITION ############################
'''
                9.	Possible permutations
Create a generator function called possible_permutations() which should receive a 
list and return lists with all possible permutations between its elements.
Note: Submit only the function in the judge system

_______________________________________________
Example_01

Test Code	(no input data in this task)


[print(n) for n in possible_permutations([1, 2, 3])]


Output

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

_______________________________________________
Example_02

Test Code	(no input data in this task)


[print(n) for n in possible_permutations([1])]

Output

[1]

'''
