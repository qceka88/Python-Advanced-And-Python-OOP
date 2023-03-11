def get_primes(data):
    for number in data:
        if number > 1:
            for num in range(2, number):
                if number % num == 0:
                    break
            else:
                yield number

# Part below is part from automatic judge system from SoftUni
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

#################################### TASK CONDITION ############################
'''
                         8.	Prime Numbers
Create a generator function called get_primes() which should receive a list of integer 
numbers and return a list containing only the prime numbers from the initial list. 
You can learn more about prime numbers from here:

Note: Submit only the function in the judge system


_______________________________________________
Example_01

Test Code	(no input data in this task)


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

Output
[2, 3, 5]


_______________________________________________
Example_02

Test Code	(no input data in this task)


print(list(get_primes([-2, 0, 0, 1, 1, 0])))

Output

[]

'''
