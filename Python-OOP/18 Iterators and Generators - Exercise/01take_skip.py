class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iterations += 1
        if self.count <= self.iterations:
            raise StopIteration

        return self.step * self.iterations


# Part below is part from automatic judge system from SoftUni
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
