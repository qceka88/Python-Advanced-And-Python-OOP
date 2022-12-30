##################################### variant 01 #####################################
def concatenate(*args, **kwargs):
    sequence = ''.join(args)
    for key, value in kwargs.items():
        sequence = sequence.replace(key, value)
    return sequence

#Part below is part from automatic judge system from SoftUni
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


##################################### variant 02 #####################################
class Concatenator:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.sequence = ''

    def create_sequence(self):
        self.sequence = ''.join(self.args)
        for key, value in self.kwargs.items():
            self.sequence = self.sequence.replace(key, value)
        return self.sequence


def concatenate(*args, **kwargs):
    result = Concatenator(*args, **kwargs).create_sequence()
    return result

#Part below is part from automatic judge system from SoftUni
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

#################################### TASK CONDITION ############################
'''
                   5.	Concatenate
Write a concatenate() function that receives some strings as arguments 
and some named arguments (the key will be a string, and the value will 
be another string). First, you should concatenate all arguments successively. 
Next, take each key successively, and if it is present in the resulted 
string, change all matching parts with the key's value. In the end, 
return the final string.
See the examples for more clarification.
Submit only your function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))	

Output
SoftUniIsGreat!

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))	

Output
I Love Python


'''
