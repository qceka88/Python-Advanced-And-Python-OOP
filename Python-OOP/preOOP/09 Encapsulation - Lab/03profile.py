class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name):
        if not (5 <= len(name) <= 15):
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        def len_password():
            if len(password) < 8:
                return True

        def upper_case():
            if len([let for let in password if let.isupper()]) < 1:
                return True

        def digit_contain():
            if len([let for let in password if let.isdigit()]) < 1:
                return True

        if any([len_password(), upper_case(), digit_contain()]):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# Part below is part from automatic judge system from SoftUni
profile_with_invalid_password = Profile('My_username', 'My-password')
print(profile_with_invalid_password)
profile_with_invalid_username = Profile('Too_long_username', 'Any')
print(profile_with_invalid_username)
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
#################################### TASK CONDITION ############################
'''
        3.	Profile
Create a class called Profile. Upon initialization, it should receive:
•	username: str - the username should be between 5 and 15 characters 
(inclusive). If it is not, raise a ValueError with the message "The username must be between 5 and 15 characters."
•	password: str - the password must be at least 8 characters long;
 it must contain at least one upper case letter and at least one digit.
  If it does not, raise a ValueError with the message "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
Hint: Use Getters and Setters to name-mangle them. 
Override the __str__() method of the base class, so it returns:
 "You have a profile with username: "{username}" and password: {"*" with the length of password}".

_______________________________________________
Example_01

Test Code	(no input data in this task)
profile_with_invalid_password = Profile('My_username', 'My-password')
Output
ValueError: The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.

_______________________________________________
Example_02

Test Code	(no input data in this task)

profile_with_invalid_username = Profile('Too_long_username', 'Any')


Output
ValueError: The username must be between 5 and 15 characters.

_______________________________________________
Example_03

Test Code	(no input data in this task)

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)


Output
You have a profile with username: "Username" and password: ********


'''
