##################################### variant 01 #####################################
def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        first_letter = name[0]
        people[name] = kwargs[first_letter]
    return '\n'.join(f"{name} is {age} years old." for name, age in sorted(people.items()))

#Part below is part from automatic judge system from SoftUni
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
##################################### variant 02 #####################################
class Humans:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.people = {}

    def assignment(self):
        for name in self.args:
            first_letter = name[0]
            self.people[name] = self.kwargs[first_letter]
        return '\n'.join(f"{name} is {age} years old." for name, age in sorted(self.people.items()))


def age_assignment(*args, **kwargs):
    output = Humans(*args, **kwargs).assignment()
    return output


#Part below is part from automatic judge system from SoftUni
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


#################################### TASK CONDITION ############################
'''
                            8.	Age Assignment
Create a function called age_assignment() that receives a different number 
of names and a different number of key-value pairs. The key will be a single 
letter (the first letter of each name) and the value - a number (age). 
Find its first letter in the key-value pairs for each name and assign the 
age to the person's name. Then, sort the names in ascending order (alphabetically) 
and return the information for each person on a new line in the format:
"{name} is {age} years old."
Submit only the function in the judge system.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(age_assignment("Peter", "George", G=26, P=19))

Output
George is 26 years old.
Peter is 19 years old.

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	

Output
Amy is 22 years old.
Bill is 61 years old.
Willy is 36 years old.

'''