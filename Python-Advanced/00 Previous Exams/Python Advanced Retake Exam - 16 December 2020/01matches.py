##################################### variant 01 #####################################
from collections import deque

male_row = list(map(int, input().split()))
female_row = deque(map(int, input().split()))
match_counter = 0

while male_row and female_row:
    male = male_row.pop()
    female = female_row.popleft()

    if male <= 0:
        female_row.appendleft(female)
        continue
    if female <= 0:
        male_row.append(male)
        continue
    if male % 25 == 0:
        male_row.pop()
        female_row.appendleft(female)
        continue
    if female % 25 == 0:
        female_row.pop()
        male_row.append(male)
        continue

    if male == female:
        match_counter += 1
    else:
        male_row.append(male - 2)

print(f"Matches: {match_counter}")

males = ', '.join(map(str, male_row[::-1])) if male_row else 'none'
print(f"Males left: {males}")
females = ', '.join(map(str, female_row)) if female_row else 'none'
print(f"Females left: {females}")

##################################### variant 02 #####################################

from collections import deque


class DatingApp:

    def __init__(self, row_male, row_female):
        self.row_male = row_male
        self.row_female = row_female
        self.match_counter = 0

    def match_couples(self):
        while self.row_male and self.row_female:
            male = self.row_male.pop()
            female = self.row_female.popleft()

            if male <= 0:
                self.row_female.appendleft(female)
                continue
            if female <= 0:
                self.row_male.append(male)
                continue
            if male % 25 == 0:
                self.row_male.pop()
                self.row_female.appendleft(female)
                continue
            if female % 25 == 0:
                self.row_female.pop()
                self.row_male.append(male)
                continue

            if male == female:
                self.match_counter += 1
            else:
                self.row_male.append(male - 2)

    def __repr__(self):
        message = f"Matches: {self.match_counter}"
        males = ', '.join(map(str, self.row_male[::-1])) if self.row_male else 'none'
        females = ', '.join(map(str, self.row_female)) if self.row_female else 'none'
        message += f"\nMales left: {males}"
        message += f"\nFemales left: {females}"

        return message


male_row = list(map(int, input().split()))
female_row = deque(map(int, input().split()))

output = DatingApp(male_row, female_row)
output.match_couples()
print(output)

#################################### TASK CONDITION ############################
'''

                                Problem 1
 
First you will be given a sequence of integers representing males. Afterwards you will be given 
another sequence of integers representing females. You have to start from the first female and 
try to match it with the last male.
•	If their values are equal, you have to match them and remove both of them. Otherwise you
 should remove only the female and decrease the value of the male by 2.
•	If someone’s value is equal to or below 0, you should remove him/her from the records 
before trying to match him/her with anybody.
•	Special case - if someone’s value divisible by 25 without remainder, you should remove 
him/her and the next person of the same gender before trying to match them with anybody.
You need to stop matching people when you have no more females or males.
Input
•	On the first line of input you will receive the integers, representing the males, separated by a single space. 
•	On the second line of input you will receive the integers, representing the females, separated by a single space.
Output
•	On the first line of output - print the number of successful matches:
o	"Matches: {matchesCount}"
•	On the second line - print all males left:
o	If there are no males: "Males left: none"
o	If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
•	On the third line - print all females left:
o	If there are no females: "Females left: none"
o	If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
Constraints
•	All of the given numbers will be valid integers in the range [-100, 100]. 

_______________________________________________
Example_01

Input
4 5 7 3 6 9 12
12 9 6 1

Output
Matches: 3
Males left: 1, 7, 5, 4

Explanation
Females left: none	The first pair is the first female with value of 12 and the last male of value 12,
their values are equal, so we match them, therefore - remove them from the records. 
Then we have two more matches (9 == 9 and 6 == 6). But the value of the next male is 3 and the value 
of the next female is 1, it's not a match and we remove the female and reduce the male’s value by 2.
Then, we print the desired output.

_______________________________________________
Example_02

Input
3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4

Output
Matches: 4
Males left: none
Females left: 15, 13, 4	


'''
