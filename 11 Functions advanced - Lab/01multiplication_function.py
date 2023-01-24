from functools import reduce


class Multiply:

    def __init__(self, *args):
        self.numbers = args
        self.result = 0

    def multiply_numbers(self):
        self.result = reduce(lambda a, b: a * b, self.numbers)
        return self.result


def multiply(*args):
    output = Multiply(*args).multiply_numbers()
    return output


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
