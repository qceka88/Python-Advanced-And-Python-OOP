from collections import deque


class WaterDispenser:

    def __init__(self):
        self.water = int(input())
        self.people = deque()
        self.message = []

    def fill_people_deque(self):
        command = input()
        while command != 'Start':
            self.people.append(command)
            command = input()

    def return_message(self):
        print('\n'.join(self.message))

    def drink_water(self):
        self.fill_people_deque()
        while True:
            command = input()
            if 'End' in command:
                self.message.append(f'{self.water} liters left')
                break

            if 'refill' in command:
                current_liters = int(command.split()[1])
                self.water += current_liters
            else:
                thirst = int(command)
                person_name = self.people.popleft()
                if thirst <= self.water:
                    self.water -= thirst
                    self.message.append(f'{person_name} got water')
                else:
                    self.message.append(f'{person_name} must wait')

        self.return_message()


if __name__ == '__main__':
    WaterDispenser().drink_water()

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