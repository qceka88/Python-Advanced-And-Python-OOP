from collections import deque


class vowels:
    VOWEL_LETTERS = ['a', 'e', 'i', 'u', 'y', 'o']

    def __init__(self, string):
        self.string = string
        self.vowel_in_text = deque(vow for vow in self.string if vow.lower() in self.VOWEL_LETTERS)

    def __iter__(self):
        return self

    def __next__(self):
        if self.vowel_in_text:
            return self.vowel_in_text.popleft()

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# [print(i) for i in range(1, 100) if len([x for x in range(1, 100) if i % x == 0]) <= 2]


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
