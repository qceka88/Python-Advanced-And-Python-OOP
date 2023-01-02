##################################### variant 01 #####################################

def forecast(*args):
    initial_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for data in args:
        weather = data[1]
        location_name = data[0]
        initial_dict[weather].append(location_name)
    sorted_result = {}
    for key, value in initial_dict.items():
        if value:
            sorted_result[key] = sorted(value)

    return '\n'.join(
        f'{location_name} - {weather}' for weather in sorted_result for location_name in sorted_result[weather])

#Part below is part from automatic judge system from SoftUni
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

##################################### variant 02 #####################################

class Forecast:

    def __init__(self, *args):
        self.some_data = args
        self.sorted_result = []

    def sort_data(self):
        initial_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
        for data in self.some_data:
            weather = data[1]
            location_name = data[0]
            initial_dict[weather].append(location_name)

        for weather, cities in initial_dict.items():
            if cities:
                for city in sorted(cities):
                    self.sorted_result.append(f'{city} - {weather}')

    def return_data(self):
        return '\n'.join(self.sorted_result)


def forecast(*args):
    output = Forecast(*args)
    output.sort_data()
    return output.return_data()

#Part below is part from automatic judge system from SoftUni
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


#################################### TASK CONDITION ############################
'''
                             3. Hourly Forecast
Patricia wants to go on vacation for the weekend and wants to know where the weather 
will be the best, so she can see the most sights. Patricia is busy at work and doesn't 
have time to think about the perfect place for her vacation, so she wants your help.
Write a function called forecast that stores information about the weather, and returns 
sorted information for all locations. The function will receive a different number of arguments. 
The arguments will be passed as tuples with two elements - the first one is the location, 
and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, 
next are the locations with cloudy weather, and last are the locations with rainy weather. 
For each sequence of locations (e.g. all sunny locations), sort them by their name in 
ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"
Constraints
•	Each tuple given will always contain the location with its weather.
•	You will never receive the same location twice or more times.

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))	New York - Sunny
Sofia - Sunny
London - Cloudy
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))	Beijing - Sunny
Bourgas - Sunny
Peru - Sunny
Tokyo - Sunny
Florence - Cloudy
Sofia - Cloudy
Hong Kong - Rainy

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))	Sofia - Rainy
Tokyo - Rainy

'''