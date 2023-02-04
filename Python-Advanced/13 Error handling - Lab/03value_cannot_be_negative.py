class ValueCannotBeNegative(Exception):
    pass


class Numbers:

    def __init__(self):
        self.input_values = []
        self.take_values()

    def take_values(self):
        for _ in range(5):
            self.input_values.append(int(input()))


class NumbersChecker:

    def __init__(self, some_value):
        self.some_value = some_value
        self.values_check()

    def values_check(self):
        if self.some_value < 0:
            raise ValueCannotBeNegative(f'Value of input number "{self.some_value}", must  be positive!')


numbers_list = Numbers()
for num in numbers_list.input_values:
    NumbersChecker(num)


#################################### TASK CONDITION ############################
'''
                    3.	Value Cannot Be Negative
Create your own exception called ValueCannotBeNegative. Write a program that reads five numbers from
 the console (on separate lines). If a negative number occurs, raise the exception.

____________________________________________________________________________________________
Example

Input
1
4
-5
3
10

Output
Traceback (most recent call last):
  File ".\value_cannot_be_negative.py", line 8, in <module>
    raise ValueCannotBeNegative
__main__.ValueCannotBeNegative


'''
