class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, current_email):
        name, data = current_email.split('@')
        mail, domain = data.split('.')

        if all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)]):
            return True
        return False

# Part below is part from automatic judge system from SoftUni
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

#################################### TASK CONDITION ############################
'''
                         4.	Email Validator
Create a class called EmailValidator. Upon initialization it should receive:
•	min_length (of the username; example: in "peter@gmail.com" "peter" is the username) 
•	mails (list of the valid mails; example: "gmail", "abv") 
•	domains (list of valid domains; example: "com", "net")
Create three methods that should not be accessed outside the class:
•	is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
•	is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
•	is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)
Create one public method:
•	validate(email) - using the three methods returns whether the email is valid (True/False)
_______________________________________________
Example

Test Code	(no input data in this task)

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

Output

True
False
False
False


'''
