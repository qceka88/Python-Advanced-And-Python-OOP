##################################### variant 01 #####################################d
def get_magic_triangle(rows):
    pascal_triangle = []
    for row in range(rows):
        current_row = [1]
        if len(pascal_triangle) > 0:
            last_row = pascal_triangle[-1]
            for i in range(len(last_row) - 1):
                num = last_row[i] + last_row[i + 1]
                current_row.append(num)
            current_row.append(1)
        pascal_triangle.append(current_row)

    return pascal_triangle


# Part below is part from automatic judge system from SoftUni
get_magic_triangle(5)


##################################### variant 02 #####################################

class PascalTriangle:

    def __init__(self, rows):
        self.rows = rows
        self.pascal_triangle = []

    def create_pascal_triangle(self):
        for row in range(self.rows):
            current_row = [1]
            if len(self.pascal_triangle) > 0:
                last_row = self.pascal_triangle[-1]
                for i in range(len(last_row) - 1):
                    num = last_row[i] + last_row[i + 1]
                    current_row.append(num)
                current_row.append(1)
            self.pascal_triangle.append(current_row)

        return self.pascal_triangle


def get_magic_triangle(number):
    output = PascalTriangle(number).create_pascal_triangle()
    return output


# Part below is part from automatic judge system from SoftUni
get_magic_triangle(5)

#################################### TASK CONDITION ############################
'''
                       Problem 3

Create a function called get_magic_triangle which will receive a single parameter 
(integer n) and it should create a magic triangle which follows those rules:
•	We start with this simple triangle [[1], [1, 1]]
•	We generate the next rows until we reach n amount of rows
•	Each number in each row is equal to the sum of the two numbers right above it in the triangle
•	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
 
Note: Submit only the function in the judge system
Input
•	There will be no inputs
•	The function will be tested by passing different values of n
•	You can test your function with the test code below
Constraints
•	N will be in range [2, 100]

_______________________________________________
Example

Test Code	(no input data in this task)
get_magic_triangle(5)	


Output (code returns matrix)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


'''
