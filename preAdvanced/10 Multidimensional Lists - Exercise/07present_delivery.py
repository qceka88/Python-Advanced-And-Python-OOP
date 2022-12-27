##################################### variant 01 #####################################

presents = int(input())
size = int(input())
neighborhood = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

santa_pos = []
total_nice_kids = 0
nice_kid_present = 0

for row in range(size):
    line = input().split()
    neighborhood.append(line)
    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][santa_pos[1]] = '-'
    total_nice_kids += line.count('V')

while True:
    command = input()
    if command == 'Christmas morning':
        break
    row = santa_pos[0] + directions[command][0]
    col = santa_pos[1] + directions[command][1]

    house = neighborhood[row][col]
    santa_pos = [row, col]
    neighborhood[row][col] = '-'
    if house == 'V':
        presents -= 1
        nice_kid_present += 1
    elif house == 'C':
        for way in directions.values():
            r = santa_pos[0] + way[0]
            c = santa_pos[1] + way[1]
            box = neighborhood[r][c]
            neighborhood[r][c] = '-'
            if box == 'X':
                presents -= 1
            if box == 'V':
                presents -= 1
                nice_kid_present += 1
            if presents <= 0:
                break
    if presents <= 0 or nice_kid_present == total_nice_kids:
        break
neighborhood[santa_pos[0]][santa_pos[1]] = 'S'
if presents <= 0 and nice_kid_present < total_nice_kids:
    print('Santa ran out of presents!')
print(*[' '.join(row) for row in neighborhood], sep='\n')

diff = total_nice_kids - nice_kid_present
if diff == 0:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {diff} nice kid/s.')

##################################### variant 02 #####################################

class SantaTour:

    def __init__(self, size, presents):
        self.size = size
        self.presents = presents
        self.neighborhood = []
        self.santa_pos = []
        self.total_nice_kids = 0
        self.nice_kid_present = 0
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

    def draw_santa_map(self):
        for row in range(self.size):
            line = input().split()
            self.neighborhood.append(line)
            if 'S' in line:
                self.santa_pos = [row, line.index('S')]
                self.neighborhood[row][self.santa_pos[1]] = '-'
            self.total_nice_kids += line.count('V')

    def cookie_monster(self):
        for way in self.directions.values():
            r = self.santa_pos[0] + way[0]
            c = self.santa_pos[1] + way[1]
            house = self.neighborhood[r][c]
            self.neighborhood[r][c] = '-'
            if house != '-':
                self.presents -= 1
                if house == 'V':
                    self.nice_kid_present += 1
            if not self.presents:
                break

    def santa_in_action(self):
        while True:
            command = input()
            if command == 'Christmas morning':
                break
            row = self.santa_pos[0] + self.directions[command][0]
            col = self.santa_pos[1] + self.directions[command][1]

            house = self.neighborhood[row][col]
            self.santa_pos = [row, col]
            self.neighborhood[row][col] = '-'
            if house == 'V':
                self.presents -= 1
                self.nice_kid_present += 1
            elif house == 'C':
                self.cookie_monster()
            if not self.presents or self.nice_kid_present == self.total_nice_kids:
                break
        self.neighborhood[self.santa_pos[0]][self.santa_pos[1]] = 'S'

    def printing(self):
        if not self.presents and self.nice_kid_present < self.total_nice_kids:
            print('Santa ran out of presents!')
        print(*[' '.join(row) for row in self.neighborhood], sep='\n')

        diff = self.total_nice_kids - self.nice_kid_present
        if diff == 0:
            print(f'Good job, Santa! {self.total_nice_kids} happy nice kid/s.')
        else:
            print(f'No presents for {diff} nice kid/s.')


presents_number = int(input())
size_of_matrix = int(input())

output = SantaTour(size_of_matrix, presents_number)
output.draw_santa_map()
output.santa_in_action()
output.printing()


#################################### TASK CONDITION ############################
"""
                        7.	Present Delivery
The presents are ready, and Santa has to deliver them to the kids. 
You will receive an integer m for the number of presents Santa has and an 
integer n for the size of the neighborhood with a square shape. On the following 
lines, you will receive the matrix, which represents the neighborhood. Santa 
will be in a random cell, marked with the letter "S". Each cell stands for a 
house where children may live. If the cell has "X" on it, that means there 
lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked 
by "V". There can also be cells marked with "C" for cookies. All of the empty 
positions will be marked with "-". Santa can move "up", "down", "left", "right" 
with one position each time. These will be the commands that you receive. If he 
moves to a house with a nice kid, the kid receives a present, but if Santa reaches 
a house with a naughty kid, he doesn't drop a present. If the command sends Santa 
to a cell marked with "C", Santa eats cookies and becomes happy and extra generous 
to all the kids around him* (meaning all of them will receive presents - it doesn't 
matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In 
this case, Santa doesn't move to these cells, or if he does, he returns to the cell 
where the cookie was. If Santa runs out of presents or receives the command 
"Christmas morning", you should end the program.  Keep in mind that you should 
check whether all the nice kids received presents.
Input
•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
Output
•	On the first line:
o	If Santa runs out of presents, but there are still some nice kids 
left print: "Santa ran out of presents!"
•	Next, print the matrix.
•	In the end, print one of these messages:
o	If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o	Otherwise, print: 
"No presents for {count nice kids} nice kid/s."
Constraints
•	The size of the square matrix will be between [2…10].
•	Santa's position will be marked with 'S'.
•	There will always be at least 1 nice kid.
•	There won't be a case where the cookie is on the border of the matrix.

____________________________________________________________________________________________
Example_01

Input
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning	

Output
- - - - 
- - - S 
- - - - 
X - - - 
Good job, Santa! 2 happy nice kid/s.	

Explanation
Santa has 5 presents. The size of the matrix is 4. After we receive the matrix, 
we start reading commands. The first one is "up". The "X" means there is a naughty 
kid, so Santa moves on without dropping any presents. Next, he reaches a nice kid 
and drops a present. The "down" command moves Santa to an empty cell. The last 
command before the "Christmas morning" message is "right". Again we have a nice kid. 
The count of nice kids reached 2, and we don't have any nice kids without presents left. 
So we print the appropriate message.

____________________________________________________________________________________________
Example_02

Input
3
4
- - - -
V - X -
- V C V
- - - S
left
up	

Output
Santa ran out of presents!
- - - - 
V - - - 
- - S - 
- - - - 
No presents for 1 nice kid/s.	

Explanation
The commands send Santa to a cell with a cookie, so all of the kids around him 
receive presents. He runs out of presents because we have 3 kids there and only 
3 presents. The program ends, and we have 1 nice kid that hasn't received a present. 

"""
