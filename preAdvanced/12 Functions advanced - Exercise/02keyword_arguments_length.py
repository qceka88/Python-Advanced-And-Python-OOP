##################################### variant 01 #####################################
def kwargs_length(**kwargs):
    return len(kwargs)

#Part below is part from automatic judge system from SoftUni
dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))


##################################### variant 02 #####################################

class Main:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def return_to_main(self):
        return len(self.kwargs)


def kwargs_length(**kwargs):
    result = Main(**kwargs).return_to_main()
    return result

#Part below is part from automatic judge system from SoftUni
dictionary = {'name': 'Peter', 'age': 25}
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