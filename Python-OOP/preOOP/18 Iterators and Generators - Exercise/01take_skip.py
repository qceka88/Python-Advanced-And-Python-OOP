class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number
        self.number += self.step
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return num


# Part below is part from automatic judge system from SoftUni

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)



#################################### TASK CONDITION ############################
'''
                           1.	Take Skip
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). 
Implement the __iter__ and __next__ functions. The iterator should return the count 
numbers (starting from 0) with the given step. For more clarification, see the examples:


_______________________________________________
Example_01

Test Code	(no input data in this task)


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

Output

    
0
2
4
6
8
10


_______________________________________________
Example_02

Test Code	(no input data in this task)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
    

Output
0
10
20
30
40

'''
