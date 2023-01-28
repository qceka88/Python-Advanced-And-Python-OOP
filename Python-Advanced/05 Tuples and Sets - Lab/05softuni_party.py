class SoftUniParty:

    def __init__(self):
        self.number = int(input())
        self.reservations = set()
        self.arrived = set()
        self.unused_reservations = set()
        self.message = ''
        self.main_meth()

    def register_reservations(self):
        for _ in range(self.number):
            number_of_reservation = input()
            self.reservations.add(number_of_reservation)

    def register_arrived_guests(self):
        reservation_number = input()

        while reservation_number != 'END':
            self.arrived.add(reservation_number)
            reservation_number = input()

    def check_unused_reservations(self):
        self.unused_reservations = self.reservations - self.arrived

    def prepare_result(self):
        self.message = str(len(self.unused_reservations)) + '\n' + '\n'.join(sorted(self.unused_reservations))

    def main_meth(self):
        self.register_reservations()
        self.register_arrived_guests()
        self.check_unused_reservations()
        self.prepare_result()

    def __repr__(self):
        return self.message


if __name__ == '__main__':
    print(SoftUniParty())


#################################### TASK CONDITION ############################
"""
                    5.	SoftUni Party
There is a party at SoftUni. Many guests are invited, and there are 
two types of them: Regular and VIP. When a guest comes, check if 
they exist on any of the two reservation lists.On the first line, 
you will receive the number of guests – N. On the following N lines, 
you will be receiving their reservation codes. All reservation 
codes are 8 characters long, and all VIP numbers will start with 
a digit. Keep in mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party 
until you read the "END" command. In the end, print the number of 
guests who did not come to the party and their reservation numbers:
•	The VIP guests must be first.
•	Both the VIP and the Regular guests must be sorted in ascending order.

____________________________________________________________________________________________
Example_01

Input
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END	

Output
2
7IK9Yo0h
tSzE5t0p

____________________________________________________________________________________________
Example_02

Input
6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END	

Output
3
7ugX7bm0
UgffRkOn
m8rfQBvl


"""