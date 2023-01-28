class AgeAssignment:

    def __init__(self, *args, **kwargs):
        self.output_message = ''
        self.citizens = args
        self.data = kwargs
        self.result = {}

    def main_meth(self):
        self.compare_names_with_data()
        self.sort_result_alphabetically_and_prepare_result_message()
        return self.output_message

    def compare_names_with_data(self):
        for name in self.citizens:
            self.update_result(name)

    def update_result(self, name):
        letter = name[0]
        if letter in self.data:
            self.result[name] = self.data[letter]

    def sort_result_alphabetically_and_prepare_result_message(self):
        sorted_result = [f'{name} is {age} years old.' for name, age in sorted(self.result.items())]
        self.output_message = '\n'.join(sorted_result)


def age_assignment(*args, **kwargs):
    output = AgeAssignment(*args, **kwargs).main_meth()
    return output


# Part below is part from automatic judge system from SoftUni
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