##################################### variant 01 #####################################

def flights(*args):
    flights_result = {}
    for index in range(0, len(args) - 1, 2):
        city = args[index]
        if city == 'Finish':
            break

        passengers = int(args[index + 1])

        if city not in flights_result:
            flights_result[city] = 0

        flights_result[city] += passengers
    return flights_result


# Part below is part from automatic judge system from SoftUni
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))


##################################### variant 02 #####################################

class Flights:

    def __init__(self, *args):
        self.input_data = args
        self.flights_result = {}

    def check_flights_data(self):
        for index in range(0, len(self.input_data) - 1, 2):
            city = self.input_data[index]
            if city == 'Finish':
                break
            passengers = int(self.input_data[index + 1])
            if city not in self.flights_result:
                self.flights_result[city] = 0
            self.flights_result[city] += passengers
        return self.flights_result


def flights(*args):
    output = Flights(*args).check_flights_data()
    return output


# Part below is part from automatic judge system from SoftUni
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

#################################### TASK CONDITION ############################
'''
                             Problem 3
Create a function named flights that receives a different number of arguments representing 
the information about the flights for a day:
•	the destination of each flight
•	the count of passengers that are boarding the plane
•	a string "Finish"
You need to take each argument and make a dictionary with the plane’s destination as a key and 
the passengers as a value of the corresponding key. 
If there are more than one flight to the same destination, you should count all the passengers 
that flew to the destination. 
You should modify the dictionary until the current argument is equal to "Finish".
Note: Submit only the function in the judge system
Input
•	There will be no input, just parameters passed to your function
Output
•	The function should return the final dictionary
Constrains
•	All numbers will be valid integers in the range [0, 300]
•	There will be no flight without given number of passengers

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))	

Output
{'Vienna': 282, 'Morocco': 98, 'Paris': 115}

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

Output
{'London': 0, 'New York': 309, 'Aberdeen': 215, 'Sydney': 2, 'Nice': 0}

_______________________________________________
Example_03

Test Code	(no input data in this task)
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))	{}

'''
