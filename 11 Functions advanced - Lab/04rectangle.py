class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def main_meth(self):
        try:
            return self.result_message(self.perimeter(), self.area())
        except TypeError:
            return self.error_message()

    def result_message(self, perimeter, area):
        return f'Rectangle area: {area}\nRectangle perimeter: {perimeter}'

    def error_message(self):
        return 'Enter valid values!'

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


def rectangle(*args):
    output = Rectangle(*args).main_meth()
    return output


print(rectangle(2, 10))
print(rectangle('2', 10))
