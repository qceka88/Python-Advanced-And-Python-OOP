class vowels:

    def __init__(self, some_string):
        self.string = some_string
        self.index = 0

    @property
    def vowels(self):
        return 'aeiyou'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration

        letter = self.string[self.index]
        self.index += 1
        
        if letter.lower() in self.vowels:
            return letter

        return self.__next__()


# Part below is part from automatic judge system from SoftUni
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


#################################### TASK CONDITION ############################
'''
                             3.	Vowels
Create a class called vowels, which should receive a string. 
Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.

Note: Submit only the class in the judge system

_______________________________________________
Example

Test Code	(no input data in this task)

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)




Output

A
e
i
u
y
o



'''
