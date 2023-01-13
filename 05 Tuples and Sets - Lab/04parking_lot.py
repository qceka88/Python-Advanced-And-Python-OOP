class ParkingLot:

    def __init__(self):
        self.number = int(input())
        self.parking_lot = set()
        self.actions = {'IN': self.add_cars_to_parking,
                        'OUT': self.remove_cars_form_parking}
        self.message = ''
        self.main()

    def add_cars_to_parking(self, plate):
        self.parking_lot.add(plate)

    def remove_cars_form_parking(self, plate):
        self.parking_lot.remove(plate)

    def process_the_data(self):
        for _ in range(self.number):
            act, car_plate = input().split(', ')
            self.actions[act](car_plate)

    def return_data(self):
        if self.parking_lot:
            return '\n'.join(self.parking_lot)
        else:
            return 'Parking Lot is Empty'

    def main(self):
        self.process_the_data()
        self.message = self.return_data()

    def __repr__(self):
        return self.message


if __name__ == '__main__':
    print(ParkingLot())

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