def vowel_filter(function):
    def wrapper():
        return [a for a in function() if a in 'aeiuyo']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


#################################### TASK CONDITION ############################
'''
2.	Vowel Filter
Having the following code:

'''

def vowel_filter(function):

    def wrapper():
        # TODO: Implement
        ...
    return wrapper


'''
Complete the code, so it works as expected.

_______________________________________________
Example

Test Code	(no input data in this task)

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())


Output
["a", "e"]

'''
