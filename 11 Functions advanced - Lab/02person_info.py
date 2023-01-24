class GetInfo:

    def __init__(self, name, town, age):
        self.name = name
        self.town = town
        self.age = age

    def result_info_for_person(self):
        return f'This is {self.name} from {self.town} and he is {self.age} years old'


def get_info(**kwargs):
    output = GetInfo(**kwargs).result_info_for_person()
    return output

##################################### variant 01 #####################################
def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

# This part below is part from automatic test code from Judge system in SoftUni
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


##################################### variant 02 #####################################
class PersonalInfo:

    def __init__(self, name, town, age):
        self.name = name
        self.town = town
        self.age = age

    def create_sequence(self):
        return f"This is {self.name} from {self.town} and he is {self.age} years old"


def get_info(name, town, age):
    output = PersonalInfo(name, town, age).create_sequence()
    return output

# This part below is part from automatic test code from Judge system in SoftUni
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


#################################### TASK CONDITION ############################
'''
                        2.	Person Info
Write a function called get_info that receives a name, an age, and a town 
and returns a string in the format:

"This is {name} from {town} and he is {age} years old".

Use dictionary unpacking when testing your function. 
Submit only the function in the judge system.

_______________________________________________
Example

Test Code	(no input data in this task)
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))	

Output
This is George from Sofia and he is 20 years old

'''