class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, *args):
        self.hours, self.minutes, self.seconds = args

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def next_second(self):
        h, m, s = self.hours, self.minutes, self.seconds
        if s + 1 > Time.max_seconds:
            s = 0
            if m + 1 > Time.max_minutes:
                m = 0
                if h + 1 > Time.max_hours:
                    h = 0
                else:
                    h += 1
            else:
                m += 1
        else:
            s += 1
        self.set_time(h, m, s)
        return self.get_time()

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


# Part below is part from automatic judge system from SoftUni
time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())


#################################### TASK CONDITION ############################
'''
                      2.	Time
Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). 
The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, 
and max_seconds equal to 59. You should also create 3 additional instance methods:
-	set_time(hours, minutes, seconds) - updates the time with the new values
-	get_time() - returns "{hh}:{mm}:{ss}"
-	next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)
Examples
Test Code	Output
time = Time(9, 30, 59)
print(time.next_second())	09:31:00
time = Time(10, 59, 59)
print(time.next_second())	11:00:00
time = Time(23, 59, 59)
print(time.next_second())	00:00:00

'''
