def solution():
    def integers():
        num = 1
        while True:
            yield num

            num += 1

    def halves():
        for n in integers():
            yield n / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


# Part below is part from automatic judge system from SoftUni

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

#################################### TASK CONDITION ############################
'''
                5.	Take Halves
You are given a skeleton with the following code:

'''


def solution():
    def integers():
        # TODO: Implement
        pass

    def halves():
        for i in integers():
            # TODO: Implement
            pass
        pass

    def take(n, seq):
        # TODO: Implement
        pass

    return (take, halves, integers)


'''
 
Implement the three generator functions:
•	integers() - generates an infinite amount of integers (starting from 1)
•	halves() - generates the halves of those integers (each integer / 2)
•	take(n, seq) - takes the first n halves of those integers
Note: Complete the functionality in the skeleton and submit it to the judge system

_______________________________________________
Example_01

Test Code	(no input data in this task)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))


Output
[0.5, 1.0, 1.5, 2.0, 2.5]


_______________________________________________
Example_02

Test Code	(no input data in this task)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))


Output
[]


'''
