class countdown_iterator:

    def __init__(self, iterations: int):
        self.iterations = iterations
        self.counter = iterations + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration

        self.counter -= 1
        return self.counter


# Part below is part from automatic judge system from SoftUni
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

#################################### TASK CONDITION ############################
'''
                           3.	Countdown Iterator

Create a class called countdown_iterator. Upon initialization, it should receive a count. 
Implement the iterator to return each countdown number (from count to 0 inclusive), 
separated by a single space.
Note: Submit only the class in the judge system


_______________________________________________
Example_01

Test Code	(no input data in this task)


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")



Output

10 9 8 7 6 5 4 3 2 1 0



_______________________________________________
Example_01

Test Code	(no input data in this task)


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")



Output

0


'''
