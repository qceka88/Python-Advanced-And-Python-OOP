class Size:

    def __init__(self):
        self.size = int(input())


class Rhombus:

    def __init__(self):
        self.storage = []

    def generate_figure(self, size):
        for num in range(1, size * 2):
            row = self.spaces(num, size) + self.stars(num, size)
            self.storage.append(row)

    @staticmethod
    def spaces(number, size):
        return ' ' * abs(number - size)

    @staticmethod
    def stars(number, size):
        return '* ' * (size - (abs(number - size)))


class Draw:

    def __init__(self, data):
        self.data = data

    def draw_image(self):
        for row in self.data.storage:
            print(row)


if __name__ == '__main__':
    size = Size()
    rhombus = Rhombus()
    rhombus.generate_figure(size.size)
    result = Draw(rhombus)
    result.draw_image()




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
