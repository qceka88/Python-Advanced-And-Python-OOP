class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, data):
        if not (5 <= len(data) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = data

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, data):
        def valid_length():
            return len(data) >= 8

        def valid_upper_case():
            return [char for char in data if char.isupper()]

        def valid_digit():
            return [let for let in data if let.isdigit()]

        if not all([valid_length(), valid_upper_case(), valid_digit()]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = data

    def __str__(self):
        hidden_password = "*" * len(self.password)
        message = f'You have a profile with username: "{self.username}" and password: {hidden_password}'
        return message


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
(inclusive). If it is not, raise a ValueError with the message 
"The username must be between 5 and 15 characters."
•	password: str - the password must be at least 8 characters long;
 it must contain at least one upper case letter and at least one digit.
  If it does not, raise a ValueError with the message 
  "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
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
