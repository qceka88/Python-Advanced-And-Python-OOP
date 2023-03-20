def read_next(*args):
    for data in args:
        for element in data:
            yield element


# Part below is part from automatic judge system from SoftUni
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

#################################### TASK CONDITION ############################
'''
                 7.	Reader
Create a generator function called read_next() which should receive a different number of 
arguments (all iterable). On each iteration, the function should return each element from each sequence.
Note: Submit only the function in the judge system


_______________________________________________
Example_01

Test Code	(no input data in this task)


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')


Output

string2dict


_______________________________________________
Example_02

Test Code	(no input data in this task)


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)


Output

N
e
e
d
2
3
words
.

'''
