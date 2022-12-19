##################################### variant 01 #####################################
lines = int(input())

car_plates = set()

for i in range(lines):
    direction, plate = input().split(', ')
    if direction == 'IN':
        car_plates.add(plate)
    if direction == 'OUT':
        car_plates.remove(plate)

if len(car_plates) > 0:
    for plate in car_plates:
        print(plate)
else:
    print('Parking Lot is Empty')

##################################### variant 02 #####################################

class Main:

    def __init__(self, number):
        self.number = number
        self.parking = set()

    def entrance(self):
        for i in range(self.number):
            action, plate = input().split(', ')
            if action == 'IN':
                self.parking.add(plate)
            elif action == 'OUT':
                self.parking.remove(plate)

    def __repr__(self):
        if len(self.parking) > 0:
            return '\n'.join(car for car in self.parking)
        else:
            return 'Parking Lot is Empty'


number_of_cars = int(input())
output = Main(number_of_cars)
output.entrance()
print(output)


#################################### TASK CONDITION ############################
"""

                        4.	Parking Lot
Write a program that:
•	Records a car number for every car that enters the parking lot
•	Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. 
On the following N lines, you will receive the direction and car's 
number in the format: "{direction}, {car_number}". The direction 
could only be "IN" or "OUT". Print the car numbers which are still 
in the parking lot. Keep in mind that all car numbers must be unique. 
If the parking lot is empty, print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.

____________________________________________________________________________________________
Example_01

Input
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU	

Output
CA2844AA
CA9999TT
CA2822UU
CA9876HH

____________________________________________________________________________________________
Example_01

Input
4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA	

Output
Parking Lot is Empty


"""