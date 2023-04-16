Problem description 

                  Hotel Everland

It is summertime, and you are hired to calculate the expenses and profit of the most popular hotel in town: Everland.
You will be provided with a skeleton that includes all the folders and files that you will need. 
Note: You are not allowed to change the folder and file structure and change their names!


![img.png](img.png)


Judge Upload
For the first 2 problems, create a zip file with the name project and upload it to the judge system
For the last problem, create a zip file with the name tests and upload it to the judge system
Structure (Problem 1) and Functionality (Problem 2)
Our first task is to implement the structure and functionality of all the classes (properties, methods, inheritance, etc.)
1.	Class Appliance
In the file appliance.py, the class Appliance should be implemented:
Structure
The class should have the following attributes:
•	cost: float - passed upon initialization. The cost is for a single day
Methods
__init__(cost: float)
The __init__ method should receive a cost: float
get_monthly_expense()
The method should return the cost for a month (30 days)
2.	Class Fridge
In the fridge.py file, the class Fridge should be implemented
Structure
The class should inherit from the Appliance class
Methods
__init__()
An instance of the Fridge class will have a cost of 1.2
3.	Class Laptop
In the laptop.py file, the class Laptop should be implemented
Structure
The class should inherit from the Appliance class
Methods
__init__()
An instance of the Laptop class will have a cost of 1
4.	Class Stove
In the stove.py file, the class Stove should be implemented
Structure
The class should inherit from the Appliance class
Methods
__init__()
An instance of the Stove class will have a cost of 0.7
5.	Class TV
In the tv.py file, the class TV should be implemented
Structure
The class should inherit from the Appliance class
Methods
__init__()
An instance of the TV class will have a cost of 1.5
6.	Class Child
In the child.py file, the class Child should be implemented
Structure
The class should have the following attributes:
•	cost: float – the money that the kid requires for a day
Methods
__init__(food_cost: int, *toys_cost)
Sum the food_cost with the cost of each toy and set the cost attribute to the result
7.	Class Room
In the room.py file, the class Room should be implemented
Structure
The class should have the following attributes:
•	family_name: str – passed upon initialization
•	budget: float – passed upon initialization
•	members_count: int – passed upon initialization
•	children: list – an empty list that will contain all kids in that room (objects)
•	expenses – 0 by default. If it is set to a negative number, raise ValueError with the message "Expenses cannot be negative"
Methods
__init__(name: str, budget: float, members_count: int)
Set the attributes to the given values
calculate_expenses(*args)
Each element of args will be a list (with children or appliances). Calculate the total cost for a month (30 days) of all elements in the lists and set the expenses attribute to the result.
8.	Class AloneOld
In the alone_old.py file, the AloneOld class should be implemented
Structure
The AloneOld class should inherit from the Room class.
Attributes
Apart from the attributes of the Room class, it should have a room_cost attribute equal to 10
Methods
__init__(family_name: str, pension: float)
This room has only one member, and the budget equals the pension of the person.
9.	Class AloneYoung
In the alone_young.py file, the AloneYoung class should be implemented
Structure
The AloneYoung class should inherit from the Room class.
Attributes
Apart from the attributes of the Room class, it should have a room_cost attribute equal to 10 and a list of appliances (a tv)
Methods
__init__(family_name: str, salary: float)
This room has only one member, and the budget equals the salary of the person.
Calculate the expenses of each appliance.
10.	Class OldCouple
In the old_couple.py file, the OldCouple class should be implemented
Structure
The OldCouple class should inherit from the Room class.
Attributes
Apart from the attributes of the Room class, the OldCouple class should have a room_cost attribute equal to 15 and a list of appliances (a tv, a fridge, and a stove for each person)
Methods
__init__(family_name: str, pension_one: float, pension_two: float)
This room has two members, and the budget equals the two pensions of the people.
Calculate the expenses of each appliance.
11.	Class YoungCouple
In the young_couple.py file, the YoungCouple class should be implemented
Structure
The YoungCouple class should inherit from the Room class.
Attributes
Apart from the attributes of the Room class, the YoungCouple class should have a room_cost attribute equal to 20 and a list of appliances (a tv, a fridge, and a laptop for each person)
Methods
__init__(family_name: str, salary_one: float, salary_two: float)
This room has two members, and the budget equals the two salaries of the people.
Calculate the expenses of each appliance.
12.	Class YoungCoupleWithChildren
In the young_couple_with_children.py file, the YoungCoupleWithChildren class should be implemented
Structure
The YoungCoupleWithChildren class should inherit from the Room class.
Attributes
Apart from the attributes of the Room class, the YoungCoupleWithChildren class should have a room_cost attribute equal to 30, a list of children, and a list of appliances (a tv, a fridge, and a laptop for each person, including the children)
Methods
__init__(family_name: str, salary_one: float, salary_two: float, *children)
Add the children to the children attribute. Each child will be an instance of the Child class. This room can have a different number of members (parents + children), the budget equals to the two salaries of the people.
Calculate the expenses (appliances and children expenses).
13.	Class Everland
Attributes
•	rooms: list – an empty list that will contain all rooms (objects)
Methods
__init__()
Set the rooms attribute to an empty list
add_room(room: Room)
Add the room in the rooms list
get_monthly_consumptions()
Calculate the expenses of each room + the room_cost and return the result in the following format: "Monthly consumption: {total_consumption}$."
pay()
Each room represents one of the following strings:
•	If the budget of the family is enough to pay for the month – "{family_name} paid {expenses+room_cost}$ and have {new_budget}$ left." and reduce the budget of the family
•	If the budget is NOT enough to pay for the month – "{family_name} does not have enough budget and must leave the hotel." and remove the room from the rooms list
Return all the information by joining the strings by a new line
status()
Return information about the hotel. If there are children in the room, print them first, and then the appliances monthly cost. The result should be in the following format:
Total population: {all_people_in_the_hotel}
{room_name} with {members} members. Budget: {current_budget}$, Expenses: {expenses}$
--- Child {n} monthly cost: {cost_for_one_month}$
… {rest of the children if any}
--- Appliances monthly cost: {cost_of_all_appliances_for_one_month}$
… {rest of the rooms if any}
Note: All the numbers must be formatted to the second digit



_______________________________________________
Example

from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()

_______________________________________________
Output

Monthly consumtions: 1136.00$.
Johnsons paid 242.00$ and have 113.00$ left.
Peterson paid 894.00$ and have 226.00$ left.
Total population: 6
Johnsons with 2 members. Budget: 113.00$, Expenses: 222.00$
--- Appliances monthly cost: 222.00$
Peterson with 4 members. Budget: 226.00$, Expenses: 864.00$
--- Child 1 monthly cost: 270.00$
--- Child 2 monthly cost: 150.00$
--- Appliances monthly cost: 444.00$



_______________________________________________


Problem 3. Unit Tests
You will be provided with another skeleton for this problem. You should write tests for the SchoolReportCard class. It will have some properties, methods, and a constructor, all of them working properly. You are NOT ALLOWED to change the class. Cover the whole class with unit tests to make sure that the class is working as intended. Submit only the test folder.

_______________________________________________