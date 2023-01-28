##################################### variant 01 #####################################
def naughty_or_nice_list(*args, **kwargs):
    list_of_santa = args[0]
    argument_commands = args[1:]
    keyword_commands = kwargs
    kids_result = {'Nice': [], 'Naughty': [], 'Not found': []}
    if argument_commands:
        for data in argument_commands:
            data = data.split('-')
            number, command = int(data[0]), data[1]
            matched_number = [(data[0], data[1]) for data in list_of_santa if data[0] == number]
            if len(matched_number) == 1:
                kids_result[command].append(matched_number[0][1])
                list_of_santa.remove(*matched_number)
    if keyword_commands:
        for name, command in keyword_commands.items():
            matched_names = [(data[0], data[1]) for data in list_of_santa if data[1] == name]
            if len(matched_names) == 1:
                kids_result[command].append(matched_names[0][1])
                list_of_santa.remove(*matched_names)
    if len(list_of_santa) > 0:
        for data in list_of_santa:
            kids_result['Not found'].append(data[1])
    result = '\n'.join(f'{key}: {", ".join(value)}' for key, value in kids_result.items() if len(value) > 0)
    return result


# Part below is part from automatic judge system from SoftUni
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


##################################### variant 02 #####################################

class NaughtyNice:

    def __init__(self, *args, **kwargs):
        self.santa_list = args[0]
        self.argument_commands = args[1:]
        self.keyword_commands = kwargs
        self.kids_result = {'Nice': [], 'Naughty': [], 'Not found': []}
        self.message = ''

    def argument(self):
        if self.argument_commands:
            for data in self.argument_commands:
                data = data.split('-')
                number, command = int(data[0]), data[1]
                matched_number = [(data[0], data[1]) for data in self.santa_list if data[0] == number]
                if len(matched_number) == 1:
                    self.kids_result[command].append(matched_number[0][1])
                    self.santa_list.remove(*matched_number)

    def keyword(self):
        if self.keyword_commands:
            for name, command in self.keyword_commands.items():
                matched_names = [(data[0], data[1]) for data in self.santa_list if data[1] == name]
                if len(matched_names) == 1:
                    self.kids_result[command].append(matched_names[0][1])
                    self.santa_list.remove(*matched_names)

    def left_kids(self):
        if len(self.santa_list) > 0:
            for data in self.santa_list:
                self.kids_result['Not found'].append(data[1])

    def prepare_result(self):
        self.message = '\n'.join(
            f'{key}: {", ".join(value)}' for key, value in self.kids_result.items() if len(value) > 0)

    def __repr__(self):
        return f'{self.message}'


def naughty_or_nice_list(*args, **kwargs):
    output = NaughtyNice(*args, **kwargs)
    output.argument()
    output.keyword()
    output.left_kids()
    output.prepare_result()
    return f'{output}'


# Part below is part from automatic judge system from SoftUni
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

#################################### TASK CONDITION ############################
'''
                          03. Naughty or Nice
 
Santa Claus is always watching and seeing if children are good or bad. Only the nice children 
get Christmas presents, so Santa Claus is preparing his list this year to check which child has been good or bad.
Write a function called naughty_or_nice_list which will receive
•	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
•	A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number
(integer) at the first position and a name (string) at the second position. 
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords. 
Each argument is a command. The commands could be the following:
•	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, 
MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
•	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, 
MOVE the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"): 
•	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list 
with NICE kids depending on the value in the keyword. Then, remove it from the Santa list.
•	Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
•	The function should return strings with the names on each list on separate lines, 
if there are any, otherwise skip the line:
o	"Nice: {name1}, {name2} … {nameN}"
o	"Naughty: {name1}, {name2} … {nameN}"
o	"Not found: {name1}, {name2} … {nameN}"

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

Output
Nice: Amy
Naughty: Tom, Katy
Not found: George

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

Output    
Nice: Simon, Peter, Lilly
Not found: Peter, Peter

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


Output
Nice: Karen, Tim, Frank
Naughty: Merry, John



'''
