numbers_list = input().split(", ")  # removed int()
result = 1

for i in range(len(numbers_list)):  # added len() for the list
    number = int(numbers_list[i])  # added  int() for number. Removed  +1 for index
    if number <= 5:  # added :
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)  # changed to result



#################################### TASK CONDITION ############################
'''
1.	So Many Exceptions
You are provided with the following code. This code raises many exceptions.
Fix it, so it works correctly. It is given a sequence of numbers, separated by a ", ".
Iterate through each number by its index, and if the number is smaller or equal to 5,
make a multiplication. If the number is larger than 5 and smaller or equal to 10, 
divide the result by the number. In the end, print the final result.

 '''

# Code to fix  (Is commented because python alarming for problems)
# x = "global"
#
# numbers_list = int(input()).split(", ")
# result = 1
#
# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number <= 5
#         result *= number
#     elif 5 < number <= 10:
#         result /= number

#print(total)


'''

____________________________________________________________________________________________
Example_01

Input
2, 5, 10

Output
1.0

____________________________________________________________________________________________
Example_02

Input
4, 5, 6, 1, 3

Output
10.0

____________________________________________________________________________________________
Example_03

Input
1, 4, 5

Output
20.0

____________________________________________________________________________________________
Example_04

Input
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

Output
0.003968253968253968


'''
