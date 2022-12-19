##################################### variant 01 #####################################
guest_number = int(input())

set_guest = set()
for i in range(guest_number):
    set_guest.add(input())

came_to_party = set()

while True:
    command = input()
    if command == "END":
        break
    came_to_party.add(command)

result = set_guest.difference(came_to_party)

print(f'{len(result)}' + '\n' + '\n'.join(code for code in sorted(result)))

##################################### variant 01 #####################################

class Main:

    def __init__(self, number):
        self.number = number
        self.invite_guest = set()
        self.came_to_party = set()
        self.result = set()

    def invitations(self):
        for i in range(self.number):
            self.invite_guest.add(input())

    def arrived(self):
        while True:
            command = input()
            if command == "END":
                break
            self.came_to_party.add(command)

    def compare(self):
        self.result = self.invite_guest.difference(self.came_to_party)

    def __repr__(self):
        return f'{len(self.result)}' + '\n' + '\n'.join(code for code in sorted(self.result))


guest_number = int(input())
output = Main(guest_number)
output.invitations()
output.arrived()
output.compare()
print(output)



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