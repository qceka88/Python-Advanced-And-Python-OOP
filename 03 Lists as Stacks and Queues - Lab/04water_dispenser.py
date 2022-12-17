##################################### variant 01 #####################################
from collections import deque

initial_water = int(input())
people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)

while True:
    data = input().split()
    if data[0] == 'End':
        print(f"{initial_water} liters left")
        break
    if data[0] == 'refill':
        new_water = int(data[1])
        initial_water += new_water
    else:
        water = int(data[0])
        person = people.popleft()
        if initial_water - water >= 0:
            initial_water -= water
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
##################################### variant 02 #####################################
from collections import deque


class Main:

    def __init__(self):
        self.people_names = deque()

    def fill_deque(self):
        while True:
            command = input()
            if command == 'Start':
                break
            self.people_names.append(command)
        return self.people_names


class DrinkWater:

    def __init__(self, people, dispenser):
        self.people = people
        self.dispenser = dispenser
        self.log = ''

    def drinking(self):
        while True:
            data = input().split()
            if data[0] == 'End':
                self.log += f"{self.dispenser} liters left"
                break
            if data[0] == 'refill':
                new_water = int(data[1])
                self.dispenser += new_water
            else:
                water = int(data[0])
                person = self.people.popleft()
                if self.dispenser - water >= 0:
                    self.dispenser -= water
                    self.log += f"{person} got water\n"
                else:
                    self.log += f"{person} must wait\n"

    def __repr__(self):
        return self.log


initial_water = int(input())
collect_names = Main().fill_deque()
output = DrinkWater(collect_names, initial_water)
output.drinking()
print(output)

#################################### TASK CONDITION ############################
"""
                     4.	Water Dispenser
Write a program that keeps track of people getting water from a 
dispenser and the amount of water left at the end. On the first 
line, you will receive the starting quantity of water (integer) 
in a dispenser. Then, on the following lines, you will be given 
the names of some people who want to get water (each on a separate line) 
until you receive the command "Start". Add those people in a queue. 
Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the 
queue wants to get. Check if there is enough water in the dispenser for that person.

o	If there is enough water, print "{person_name} got water" 
and remove him/her from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person 
from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left 
in the format: "{left_liters} liters left".

____________________________________________________________________________________________
Example_01

Input
2
Peter
Amy
Start
2
refill 1
1
End	

Output
Peter got water
Amy got water
0 liters left	

Explanation
We create a queue with Peter and Amy. 
After the start command, we see that 
Peter wants 2 liters of water (and he gets them). 
The water dispenser is left with 0 liters. 
After refilling, there is 1 liter in the dispenser.
So when Amy wants 1 liter, she gets it, and there are 
0 liters left in the dispenser.


____________________________________________________________________________________________
Example_02

Input
10
Peter
George
Amy
Alice
Start
2
3
3
3
End	

Output
Peter got water
George got water
Amy got water
Alice must wait
2 liters left	

"""