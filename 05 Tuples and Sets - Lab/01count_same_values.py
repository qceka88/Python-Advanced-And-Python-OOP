##################################### variant 01 #####################################

from collections import defaultdict

numbers = tuple(map(float, input().split()))

unique = defaultdict(int)
for number in numbers:
    unique[number] += 1

for number, count in unique.items():
    print(f"{number} - {count} times")

##################################### variant 02 #####################################

from collections import defaultdict


class Main:

    def __init__(self, string):
        self.string = string
        self.unique = defaultdict(int)
        self.log = ''

    def string_to_dict(self):
        numbers = tuple(map(float, self.string.split()))
        for number in numbers:
            self.unique[number] += 1

    def message(self):
        for number, count in self.unique.items():
            self.log += f"{number} - {count} times\n"

    def __repr__(self):
        return self.log

input_line = input()
output = Main(input_line)
output.string_to_dict()
output.message()
print(output)