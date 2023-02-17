class SantaList:

    def __init__(self, *data):
        self.santa_list = data[0]
        self.kids_dict = {"Nice": [], "Naughty": [], "Not found": []}


class SantaInAction:

    def __init__(self, data: SantaList):
        self.data = data

    def kids_matches(self, check):
        return [t for t in self.data.santa_list if check in t]

    def santa_check_kids(self, *commands):
        for info in commands:
            number, command = info.split("-")

            kids = self.kids_matches(int(number))

            if len(kids) == 1:
                self.data.kids_dict[command].append(kids[0][1])
                self.data.santa_list.remove(*kids)

    def check_keywords(self, **kwargs):
        for name, command in kwargs.items():

            kids = self.kids_matches(name)

            if len(kids) == 1:
                self.data.kids_dict[command].append(kids[0][1])
                self.data.santa_list.remove(*kids)

    def check_for_not_found_kids(self):
        not_found_kids = [x[1] for x in self.data.santa_list]
        self.data.kids_dict["Not found"].extend(not_found_kids)


class Result:

    def __init__(self):
        self.result = []

    def prepare_result(self, data: SantaList):
        for type_of_kid, kids in data.kids_dict.items():
            if kids:
                self.result.append(f"{type_of_kid}: {', '.join(kids)}")


def naughty_or_nice_list(*args, **kwargs):
    santa_list = SantaList(*args)
    santa_in_action = SantaInAction(santa_list)
    santa_in_action.santa_check_kids(*args[1:])
    santa_in_action.check_keywords(**kwargs)
    santa_in_action.check_for_not_found_kids()
    result = Result()
    result.prepare_result(santa_list)
    return '\n'.join(result.result)





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
