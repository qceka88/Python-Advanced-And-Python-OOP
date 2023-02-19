class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, data):
        if not isinstance(data, float):
            return "value is not a float"
        return cls(int(data))

    @classmethod
    def from_roman(cls, data):
        def convert_to_decimal(num):
            roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            result = 0
            for i, c in enumerate(num):
                if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                    result += roman_numerals[c]
                else:
                    result -= roman_numerals[c]
            return result

        output = convert_to_decimal(data)
        return cls(int(output))

    @classmethod
    def from_string(cls, data):
        if not isinstance(data, str):
            return "wrong type"
        else:
            return cls(int(data))


# Part below is part from automatic judge system from SoftUni
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))


#################################### TASK CONDITION ############################
'''
                         3.	Integer
Create a class called Integer. Upon initialization, it should receive a single parameter value (int). 
It should have 3 additional methods:
•	from_float(float_value) - creates a new instance by flooring the provided floating number. 
If the value is not a float, return a message "value is not a float"
•	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer
•	from_string(value) - creates a new instance by converting the string to an integer
 (if the value cannot be converted, return a message "wrong type")

_______________________________________________
Example

Test Code    (no input data in this task)

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))


Output
10
4
value is not a float
wrong type


'''
