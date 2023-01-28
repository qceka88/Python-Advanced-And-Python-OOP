class DictionaryLength:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def returning_length_of_dictionary(self):
        return len(self.kwargs)


def kwargs_length(**kwargs):
    output = DictionaryLength(**kwargs).returning_length_of_dictionary()
    return output


# Part below is part from automatic judge system from SoftUni
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
dictionary = {}

print(kwargs_length(**dictionary))

#################################### TASK CONDITION ############################
'''
                  2.	Keyword Arguments Length
Create a function called kwargs_length() that can receive some 
keyword arguments and return their length.
Submit only your function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))	

Output
2

_______________________________________________
Example_02

Test Code	(no input data in this task)
dictionary = {}

print(kwargs_length(**dictionary))	

Output
0


'''
