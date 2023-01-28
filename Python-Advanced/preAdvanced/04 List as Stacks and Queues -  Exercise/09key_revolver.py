##################################### variant 01 #####################################
from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())
shoot_count = 0

while locks and bullets:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()
    shoot_count += 1
    if current_lock < current_bullet:
        print('Ping!')
        locks.appendleft(current_lock)
    else:
        print('Bang!')
    if shoot_count % barrel_size == 0 and len(bullets) > 0:
        print('Reloading!')

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence - (bullet_price * shoot_count)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")


##################################### variant 02 #####################################

from collections import deque


class Mission:

    def __init__(self, price, size, quantity_bullets, targets, sponsorship):
        self.price = price
        self.size = size
        self.quantity_bullets = quantity_bullets
        self.targets = targets
        self.sponsorship = sponsorship
        self.shoot_count = 0
        self.log = []

    def key_revolver(self):
        while self.targets and self.quantity_bullets:
            current_lock = self.targets.popleft()
            current_bullet = self.quantity_bullets.pop()
            self.shoot_count += 1
            if current_lock < current_bullet:
                self.log.append('Ping!')
                self.targets.appendleft(current_lock)
            else:
                self.log.append('Bang!')
            if self.shoot_count % self.size == 0 and len(self.quantity_bullets) > 0:
                self.log.append('Reloading!')

    def resulting(self):
        if len(self.targets) > 0:
            self.log.append(f"Couldn't get through. Locks left: {len(self.targets)}")
        else:
            money_earned = self.sponsorship - (self.price * self.shoot_count)
            self.log.append(f"{len(self.quantity_bullets)} bullets left. Earned ${money_earned}")

    def __repr__(self):
        return '\n'.join(msg for msg in self.log)


bullets_price = int(input())
barrel_size = int(input())
bullets_quantity = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())

output = Mission(bullets_price, barrel_size, bullets_quantity, locks, intelligence)
output.key_revolver()
output.resulting()
print(output)


#################################### TASK CONDITION ############################
"""

                            9. *Key Revolver
Our favorite super-spy action hero Sam is back from his vacation, and it 
is time to go on a mission. He needs to unlock a safe locked by several 
locks in a row, which all have varying sizes. The hero possesses a special 
weapon called the Key Revolver, with special bullets. Each bullet can unlock 
a lock with a size equal to or larger than the size of the bullet. The bullet 
goes into the keyhole, then explodes, completely destroying it. Sam doesn't 
know the size of the locks, so he needs to just shoot at all of them until 
the safe runs out of locks. What's behind the safe, you ask? Well, intelligence! 
It is told that Sam's sworn enemy – Nikoladze, keeps his top-secret Georgian 
Chacha Brandy recipe inside. It's valued differently across different times 
of the year, so Sam's boss will tell him what it's worth over the radio. 
One last thing, every bullet Sam fires will also cost him money, which will 
be deducted from his pay from the price of the intelligence. 
Good luck, operative.
Input
•	On the first line of input, you will receive the price of 
each bullet – an integer in the range [0-100]
•	On the second line, you will receive the size of the gun 
barrel – an integer in the range [1-5000]
•	On the third line, you will receive the bullets – a 
space-separated integer sequence with [1-100] integers
•	On the fourth line, you will receive the locks – a space-separated 
integer sequence with [1-100] integers
•	On the fifth line, you will receive the value of the 
intelligence – an integer in the range [1-100000]
After Sam receives all of his information and gear (input), 
he starts to shoot the locks front-to-back while going through 
the bullets back-to-front. If he successfully destroyed a lock, 
print "Bang!", then remove the lock. If not, print "Ping!", 
leaving the lock intact. The bullet is removed in both cases.
If Sam runs out of bullets in his barrel, print "Reloading!" on 
the console, then continue shooting. If there aren't any bullets 
left, don't print it. The program ends when Sam runs out of bullets 
or the safe runs out of locks.
Output
•	If Sam manages to open the safe, print:
"{bullets_left} bullets left. Earned ${money_earned}" 
•	Otherwise, print:
"Couldn't get through. Locks left: {locks_left}"
Make sure to include the price of the bullets when calculating the money earned.
Constraints
•	The input will be within the constraints specified above and will 
always be valid. There is no need to check it explicitly.
•	There will never be a case where Sam breaks the lock and ends up with а negative balance.

____________________________________________________________________________________________
Example_01

Input
50
2
11 10 5 11 10 20
15 13 16
1500	

Output
Ping!
Bang!
Reloading!
Bang!
Bang!
Reloading!
2 bullets left. Earned $1300	

Explanation
20 shoots lock 15 (ping)
10 shoots lock 15 (bang)
11 shoots lock 13 (bang)
5 shoots lock 16 (bang)
Bullets' cost: 4 * 50 = $200
Earned: 1500 – 200 = $1300

____________________________________________________________________________________________
Example_02

Input
20
6
14 13 12 11 10 5
13 3 11 10
800	

Output
Bang!
Ping!
Ping!
Ping!
Ping!
Ping!
Couldn't get through. Locks left: 3	 5 shoots lock 13 (bang)

Explanation
10 shoots lock  3 (ping)
11 shoots lock  3 (ping)
12 shoots lock  3 (ping)
13 shoots lock  3 (ping)
14 shoots lock  3 (ping) 

____________________________________________________________________________________________
Example_03

Input
33
1
12 11 10
10 20 30
100	

Output
Bang!
Reloading!
Bang!
Reloading!
Bang!
0 bullets left. Earned $1	

Explanation
10 shoots lock 10 (bang)
11 shoots lock 20 (bang)
12 shoots lock 30 (bang)
Bullets' cost: 3 * 33 = $99
Earned: 100 – 99 = $1

"""