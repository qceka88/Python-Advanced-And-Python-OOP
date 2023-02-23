class Employee:

    def __init__(self, *data):
        [self.id,
         self.first_name,
         self.last_name,
         self.salary
         ] = data

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


# Part below is part from automatic judge system from SoftUni
employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())


#################################### TASK CONDITION ############################
'''
3.	Employee
Create class Employee. Upon initialization, it should 
receive: id (number), first_name (string), last_name (string) and salary (number). Create 3 instance methods:
-	get_full_name() - returns "{first_name} {last_name}"
-	get_annual_salary() - returns the total salary for 12 months
-	raise_salary(amount) - increases the salary by the given amount and returns the new salary

_______________________________________________
Example

Test Code	(no input data in this task)

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

Output
John Smith
1500
18000

'''
