##################################### variant 01 #####################################
text = list(input())

result = []
while len(text) > 0:
    print(text.pop(), end='')


##################################### variant 02 #####################################

class ReversedString:

    def __init__(self):
        self.input_string = list(input())

    def printing(self):
        while self.input_string:
            print(self.input_string.pop(), end='')


output = ReversedString().printing()
