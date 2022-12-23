##################################### variant 01 #####################################

rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flat = [num for row in matrix for num in row]
print(flat)


##################################### variant 02 #####################################

class Main:

    def __init__(self, rows):
        self.rows = rows
        self.matrix = []

    def the_matrix(self):
        for _ in range(self.rows):
            self.matrix.append([int(x) for x in input().split(', ')])

    def the_flat_matrix(self):
        return [num for row in self.matrix for num in row]


number_of_rows = int(input())
output = Main(number_of_rows)
output.the_matrix()
print(output.the_flat_matrix())
