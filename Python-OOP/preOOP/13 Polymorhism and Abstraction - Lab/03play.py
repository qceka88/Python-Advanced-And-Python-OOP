class Guitar:
    # Class a is part from automatic judge system from SoftUni
    def play(self):
        return "Playing the guitar"


class Children:
    # Class a is part from automatic judge system from SoftUni
    def play(self):
        return "Children are playing"


def start_playing(some_object):
    return some_object.play()


# Part below is part from automatic judge system from SoftUni
children = Children()
print(start_playing(children))
guitar = Guitar()
print(start_playing(guitar))

#################################### TASK CONDITION ############################
'''
                         3.	Playing
Create a function called start_playing which will receive an instance and will return its play() method.
Submit only the start_playing function in the judge system

_______________________________________________
Example_01

Test Code	(no input data in this task)

class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))

Output
Playing the guitar

_______________________________________________
Example_02

Test Code	(no input data in this task)

class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))

Output
Children are playing

'''
