class ConcatenateClass:

    def __init__(self, *args, **kwargs):
        self.substrings = args
        self.keywords = kwargs
        self.result = ''

    def main_meth(self):
        self.concatenate_substrings_in_single_string()
        self.change_matching_parts()
        return self.result

    def concatenate_substrings_in_single_string(self):
        self.result = ''.join(self.substrings)

    def change_matching_parts(self):
        for key, value in self.keywords.items():
            self.result = self.result.replace(key, value)


def concatenate(*args, **kwargs):
    output = ConcatenateClass(*args, **kwargs).main_meth()
    return output


# Part below is part from automatic judge system from SoftUni
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
