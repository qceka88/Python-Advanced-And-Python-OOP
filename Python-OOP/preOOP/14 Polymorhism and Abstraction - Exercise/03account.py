class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)

        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")

        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_name = f"{self.owner}&{other.owner}"
        new_amount = sum([self.amount, other.amount])
        new_account = Account(new_name, new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

# Part below is part from automatic judge system from SoftUni
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

#################################### TASK CONDITION ############################
'''
                          3.	Account
Create a single class called Account. Upon initialization, it should receive an owner (str) and a 
starting amount (int, optional, 0 by default). It should also have an attribute called _transactions (empty list).
Create the following methods:
•	handle_transaction(transaction_amount)
o	If the balance becomes less than zero, raise ValueError with the
 message "sorry cannot go in debt!" and break the transaction. 
o	Otherwise, complete it, save it and return a message "New balance: {account_balance}"
•	add_transaction(amount) 
o	if the amount is not an integer, raise ValueError with the message "please use int for amount". 
o	Otherwise, check what the balance will be with the new transaction
	If the balance becomes less than zero, raise ValueError with the
 message "sorry cannot go in debt!" and break the transaction. 
	Otherwise, complete it and return a message "New balance: {account_balance}"
•	balance() - a property that returns the sum between the amount and all the transactions
Implement the correct magic methods so the code in the example below works properly:
•	When you print an account instance, the output should be in
the format "Account of {owner} with starting amount: {amount}".
•	When you print a representational string of an account instance, 
the output should be in the format "Account({owner}, {amount})".
•	When you access the length of an account instance, 
you should receive the total number of transactions made.
•	You should iterate over an account instance and receive each transaction as a result.
•	You should be able to reverse the order of transactions by 
reversing an account instance.
•	You should be able to compare (>, <, >=, <=, ==, !=) two account 
instances by their balance amount.
•	When you concatenate two accounts, you should return a new account 
with a name - string in the format "{first_owner}&{second_owner}" and 
starting amount - the sum between their two. Both their transactions should be added to the new account.

_______________________________________________
Example

Test Code	(no input data in this task)

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

Output
Account of bob with starting amount: 10
Account(bob, 10)
40
3
20
-20
30
-20
[30, -20, 20]
False
False
True
True
False
True
Account of bob&john with starting amount: 10
[20, -20, 30, 10, 60]

'''