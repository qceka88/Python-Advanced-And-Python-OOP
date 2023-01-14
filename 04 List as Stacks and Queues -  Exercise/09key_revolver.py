from collections import deque


class KeyRevolver:

    def __init__(self):
        self.price_bullet = int(input())
        self.size_barrel = int(input())
        self.bullets = input()
        self.locks = input()
        self.intelligence_value = int(input())
        self.shoots = 0
        self.message = ''
        self.main_meth()

    def create_bullets_stack(self):
        self.bullets = [int(n) for n in self.bullets.split()]

    def create_locks_deque(self):
        self.locks = deque(int(n) for n in self.locks.split())

    def start_shooting(self):
        while self.bullets and self.locks:
            lock = self.locks.popleft()
            while self.bullets:
                bullet = self.bullets.pop()
                self.shoots += 1
                if lock >= bullet:
                    self.message += 'Bang!\n'
                    break
                else:
                    self.locks.appendleft(lock)
                    self.message += 'Ping!\n'
                    break
            if self.shoots % self.size_barrel == 0 and self.bullets:
                self.message += 'Reloading!\n'

    def money_calculator(self):
        earned_money = self.intelligence_value - (self.shoots * self.price_bullet)
        return earned_money

    def prepare_result(self):
        if not self.locks:
            money = self.money_calculator()
            left_bullets = len(self.bullets)
            self.message += f'{left_bullets} bullets left. Earned ${money}'
        else:
            locks_left = len(self.locks)
            self.message += f"Couldn't get through. Locks left: {locks_left}"

    def main_meth(self):
        self.create_bullets_stack()
        self.create_locks_deque()
        self.start_shooting()
        self.prepare_result()

    def __repr__(self):
        return self.message


if __name__ == '__main__':
    print(KeyRevolver())


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