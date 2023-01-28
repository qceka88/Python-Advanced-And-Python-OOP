##################################### variant 01 #####################################
import sys

size = 6

matrix = [input().split() for _ in range(size)]
prize = {'Football': [100, 199],
         'Teddy Bear': [200, 299],
         'Lego Construction Set': [300, sys.maxsize]}

total_points = 0

for throw in range(3):
    row, col = list(map(int, input()[1:-1].split(', ')))
    if 0 <= row < size and 0 <= col < size:
        symbol = matrix[row][col]
        if symbol == 'B':
            matrix[row][col] = '0'
            total_points += sum(int(x[col]) for x in matrix)

if total_points < 100:
    needed_points = 100 - total_points
    print(f'Sorry! You need {needed_points} points more to win a prize.')
else:
    for prize_name, points in prize.items():
        if points[0] <= total_points <= points[1]:
            print(f"Good job! You scored {total_points} points, and you've won {prize_name}.")
            break
##################################### variant 02 #####################################

import sys


class BallInBucket:

    def __init__(self, size):
        self.size = size
        self.field = []
        self.prizes_catalogue = {'Football': [100, 199],
                                 'Teddy Bear': [200, 299],
                                 'Lego Construction Set': [300, sys.maxsize]}
        self.total_points = 0
        self.message = ''

    def create_game_field(self):
        for row in range(self.size):
            self.field.append(input().split())

    def throw_the_ball(self):
        throws = 3
        for throw in range(throws):
            row, col = list(map(int, input()[1:-1].split(', ')))
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.field[row][col]
                if symbol == 'B':
                    self.field[row][col] = '0'
                    self.total_points += sum(int(x[col]) for x in self.field)

    def check_win_prize(self):
        if self.total_points < 100:
            needed_points = 100 - self.total_points
            self.message = f'Sorry! You need {needed_points} points more to win a prize.'
        else:
            for prize_name, points in self.prizes_catalogue.items():
                if points[0] <= self.total_points <= points[1]:
                    self.message = f"Good job! You scored {self.total_points} points, and you've won {prize_name}."
                    break

    def __repr__(self):
        return f'{self.message}'


size_of_matrix = 6
output = BallInBucket(size_of_matrix)
output.create_game_field()
output.throw_the_ball()
output.check_win_prize()
print(output)

#################################### TASK CONDITION ############################
'''
                                     Problem 2 - Ball in the Bucket

You are at the funfair to play different games and test your skills. Now you are playing ball in 
the bucket game. You will be given a matrix with 6 rows and 6 columns representing the board. 
On the board, there will be points (integers) and buckets marked with the letter "B". Rules of the game:
•	You can throw a ball only 3 times.
•	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
•	You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
•	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 
After the board state, you are going to receive the information for every throw on a separate line. 
The coordinates’ information of a hit will be in the format: "({row}, {column})".
Depending on how many points you have collected, you win one of the following:

Football	             ->       100 to 199 points
Teddy Bear	             ->       200 to 299 points
Lego Construction Set	 ->       300 and more points

Your job is to keep track of the scored points and to check if you won a prize. 
For more clarifications, see the examples below.
Input
•	6 lines – matrix representing the board (each position separated by a single space)
•	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

Output
•	On the first line:
o	If you won a prize, print: 
"Good job! You scored {points} points, and you've won {prize}."
o	If you did not win any prize, print the points you need to get at least the first prize: 
"Sorry! You need {points} points more to win a prize."
Constraints
•	All of the given points will be integers in the range [1, 30]
•	All the given indexes will be integers in the range [0, 30]
•	There always will be exactly 6 buckets - 1 on each column

_______________________________________________
Example_01

Input
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)	


Output
Sorry! You need 33 points more to win a prize.

_______________________________________________
Example_02

Input
B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)

Output
Good job! You scored 299 points, and you've won Teddy Bear.


'''