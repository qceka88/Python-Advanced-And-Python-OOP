import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MustContainSingleAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class DomainForbiddenCharacterError(Exception):
    pass


class NameForbiddenCharacterError(Exception):
    pass


class EmailValidation:
    __min_size = 4
    __allowed_domains = ["com", "bg", "org", "net"]
    __domain_pattern = r'(?<=@)[\.a-z]+(\.[a-z]+)$'
    __name_pattern = r'^[\.\w+]+(?=@)'

    def __init__(self, data):
        self.data = data

    def check_input_data_is_valid_email(self):

        if '@' not in self.data:
            raise MustContainAtSymbolError('Input data must contain @!')
        if self.data.count('@') > 1:
            raise MustContainSingleAtSymbolError('Input email must contain only one "@" symbol!')
        if len(self.data.split('@')[0]) <= self.__min_size:
            raise NameTooShortError('Name must be longer thant 4 characters!')
        if not re.findall(self.__domain_pattern, self.data):
            raise DomainForbiddenCharacterError('Domain must contains only non-capitol letters and points')
        if re.findall(self.__domain_pattern, self.data)[0].split('.')[-1] not in self.__allowed_domains:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(self.__allowed_domains)}')
        if not re.findall(self.__name_pattern, self.data):
            raise NameForbiddenCharacterError('Email must contains only, letters,numbers, dots, underscores')


data = input()
while data != 'End':
    check_valid = EmailValidation(data)
    check_valid.check_input_data_is_valid_email()
    print('Email is valid')
    data = input()


#################################### TASK CONDITION ############################
'''
                       2.	Email Validator
You will be given some emails until you receive the command "End". Create the following 
custom exceptions to validate the emails:
•	NameTooShortError - raise it when the name in the email is less 
than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
•	MustContainAtSymbolError - raise it when there is no "@" in the email
•	InvalidDomainError - raise it when the domain of the email
 is invalid (valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
•	NameTooShortError - "Name must be more than 4 characters"
•	MustContainAtSymbolError - "Email must contain @"
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one


____________________________________________________________________________________________
Example_01

Input
abc@abv.bg

Output
Traceback (most recent call last):
  File ".\email_validator.py", line 20, in <module>
    raise NameTooShort("Name must be more than 4 characters")
__main__.NameTooShort: Name must be more than 4 characters

____________________________________________________________________________________________
Example_02

Input
peter@gmail.com
petergmail.com

Output
Email is valid
Traceback (most recent call last):
  File ".\email_validator.py", line 18, in <module>
    raise MustContainAtSymbolError("Email must contain @")
__main__.MustContainAtSymbolError: Email must contain @

____________________________________________________________________________________________
Example_03

Input
peter@gmail.hotmail

Output
Traceback (most recent call last):
  File ".\email_validator.py", line 22, in <module>
    raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
__main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net


'''