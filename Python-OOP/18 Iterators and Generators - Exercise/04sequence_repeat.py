class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number - 1:
            raise StopIteration

        self.iterations += 1
        return self.sequence[self.iterations % len(self.sequence)]


# Part below is part from automatic judge system from SoftUni
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')

#################################### TASK CONDITION ############################
'''
                           4.	Sequence Repeat

Create a class called sequence_repeat which should receive a sequence and a number 
upon initialization. Implement an iterator to return the given elements, so they form a 
string with a length - the given number. If the number is greater than the number of 
elements, then the sequence repeats as necessary. For more clarification, see the examples:



_______________________________________________
Example_01

Test Code	(no input data in this task)


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


Output

abcab



_______________________________________________
Example_02

Test Code	(no input data in this task)


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')




Output

I L

'''
