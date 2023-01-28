class Rhombus:

    def __init__(self, n):
        self.n = n
        self.result = []

    def main_method(self):
        self.create_rhombus()
        return '\n'.join(self.result)

    def create_rhombus(self):
        self.upper_part_of_rhombus()
        self.lower_part_of_rhombus()

    def upper_part_of_rhombus(self):
        for row in range(1, self.n + 1):
            self.result.append(self.generating_image(row))

    def lower_part_of_rhombus(self):
        for row in range(self.n - 1, 0, -1):
            self.result.append(self.generating_image(row))

    def generating_image(self, row):
        row_image = ''
        for space in range(self.n - row):
            row_image += ' '
        for star in range(row - 1):
            row_image += '* '
        row_image += '*'
        return row_image


if __name__ == '__main__':
    number = int(input())
    output = Rhombus(number).main_method()
    print(output)


#################################### TASK CONDITION ############################
'''
                   1.	Rhombus of Stars
Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

____________________________________________________________________________________________
Example_01

Input
1	

Output
*

____________________________________________________________________________________________
Example_02

Input
2

Output	 
 *
* *
 *
 
____________________________________________________________________________________________
Example_03

Input
3	  
  *
 * *
* * *
 * *
  *
  
____________________________________________________________________________________________
Example_04

Input
4	

Output   
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

'''
