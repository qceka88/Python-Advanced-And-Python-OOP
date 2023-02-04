class Text:

    def __init__(self, text):
        self.text = text


class Number:

    def __init__(self, number):
        self.number = number

    def check_number(self):
        try:
            return int(self.number)
        except ValueError:
            return 'Variable times must be an integer'


class RepeatText:

    def __init__(self, number: Number, text: Text):
        self.number = number
        self.text = text

    def __repr__(self):
        if type(number.check_number()) != int:
            return number.check_number()
        else:
            return f'{self.text.text * number.check_number()}'


if __name__ == '__main__':
    text = Text(input())
    number = Number(input())
    repeat = RepeatText(number, text)
    print(repeat)

#################################### TASK CONDITION ############################
'''
     2.	Repeat Text
Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
 If the user passes a non-integer type for the times variable, handle the exception and print a message 
"Variable times must be an integer".

____________________________________________________________________________________________
Example_01

Input
Hello
Bye

Output
Variable times must be an integer

____________________________________________________________________________________________
Example_02

Input
Hello
2

Output
HelloHello

'''
