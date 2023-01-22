class EasterBunny:

    def __init__(self):
        self.output_message = ''
        self.result = ['', [], 0]
        self.size = int(input())
        self.matrix = []
        self.bunny_pos = []
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.main_meth()

    def main_meth(self):
        self.fill_matrix_with_elements()
        self.bunny_start_to_collect_eggs()
        self.prepare_output_message()

    def fill_matrix_with_elements(self):
        for row in range(self.size):
            line = input().split()
            if 'B' in line:
                self.bunny_pos = [row, line.index('B')]

            self.matrix.append(line)

    def bunny_start_to_collect_eggs(self):
        for way in self.directions:
            eggs, locations = self.check_for_collected_eggs_in_current_direction(way)
            self.check_is_best_direction(eggs, locations, way)

    def check_for_collected_eggs_in_current_direction(self, way):
        eggs = 0
        eggs_locations = []
        bunny_row, bunny_col = self.bunny_pos
        while True:
            bunny_row += self.directions[way][0]
            bunny_col += self.directions[way][1]
            if 0 <= bunny_row < self.size and 0 <= bunny_col < self.size:
                symbol = self.matrix[bunny_row][bunny_col]
                if symbol != 'X':
                    eggs_locations.append([bunny_row, bunny_col])
                    eggs += int(symbol)
                else:
                    break
            else:
                break

        return eggs, eggs_locations

    def check_is_best_direction(self, eggs, locations, direction):
        if eggs >= self.result[2]:
            self.result = [direction, locations, eggs]

    def prepare_output_message(self):
        self.output_message = self.result[0] + '\n'
        self.output_message += '\n'.join(f"[{r}, {c}]" for r, c in self.result[1])
        self.output_message += f'\n{self.result[2]}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(EasterBunny())


#################################### TASK CONDITION ############################
"""
                   4.	Easter Bunny
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size 
of the field. On the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should 
go to collect the maximum number of eggs. The directions that should 
be considered as possible are up, down, left, and right. If you reach 
a trap while checking some of the directions, you should not consider 
the fields after the trap in this direction. For more clarifications, 
see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
Constraints
•	There will NOT be two or more paths consisting of the same total amount of eggs.

____________________________________________________________________________________________
Example_01

Input
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0	

Output
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87	

Explanation
The number of eggs if the bunny goes up is equal to 7. 
If he goes down = 9, there are no eggs on the left and 87 on 
the right. That's why the bunny should follow this direction 
(right) and collect the eggs provided there.

____________________________________________________________________________________________
Example_02

Input
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22	

Output
down
[6, 2]
[7, 2]
113	

"""
