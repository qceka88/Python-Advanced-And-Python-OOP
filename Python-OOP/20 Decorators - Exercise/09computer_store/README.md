Problem description

                                  *09.Computer Store
For this task, you will be provided with a skeleton that includes all the folders and files you need.

![img.png](img.png)

Note: You cannot change the folder and file structure and their names!
Judge Upload
Create a zip file with the project folder and upload it to the judge system.
You do not need to include in the zip file your venv, .idea, pycache, and __MACOSX (for Mac users), so you do not exceed the maximum allowed size of 16.00 KB.
Description
Your friend is the owner of one of the best computer stores in the world. Recently he started building computers, and he asked you as a programmer to create a program for his store so that he can track the computer's building process and the sale process. Your app should have the following structure and functionality.
1. Class Computer
In the computer.py file, the class Computer should be implemented. It is a base class for any type of computer, and it should not be able to be instantiated.
Structure
The class should have the following attribute:
•	manufacturer: str
o	A string that represents the manufacturer's name.
o	If the string is empty or contains only whitespaces, raise ValueError with the message: "Manufacturer name cannot be empty."
•	model: str
o	A string that represents the computer's model name.
o	If the string is empty or contains only whitespaces, raise ValueError with the message: "Model name cannot be empty."
•	processor: str
o	A string that represents the computer's processor.
o	Should be set to None upon initialization
•	ram: int
o	An integer that represents the computer's RAM memory.
o	Should be set to None upon initialization
•	price: int
o	An integer that represents the computer's price.
o	Should be set to 0 upon initialization
Methods
__init__(manufacturer: str, model: str)
•	In the __init__ method, all the needed attributes must be set.
 configure_computer(processor: str, ram,: int)
•	Every type of computer should be configurable
•	Valid types: "Laptop", "Desktop Computer"
__repr__()
•	Representsts the class as: "{ manufacturer } { model } with { processor } and { ram }GB RAM"
2. Class DesktopComputer
In the desktop_computer.py file, the class DesktopComputer should be implemented.
Methods
__init__(manufacturer: str, model: str)
•	In the __init__ method, all the needed attributes must be set.
 configure_computer(processor: str, ram,: int)
•	Desktop computers can be built only with the available processors for desktop computers, which are:
o	AMD Ryzen 7 5700G: 500$
o	Intel Core i5-12600K: 600$
o	Apple M1 Max: 1800$
•	Desktop computers can have a max RAM of 128GB
o	Valid RAM sizes are 2, 4, 8…128. In other words, all the powers of the number 2 to the max size.
o	RAM price is defined by the power of the number 2, which gives the RAM size, multiplied by 100. 
For example: 2GB RAM will cost 100$ because 2 = 21  and 1 * 100 = 100. 4GB will be 200$.
•	If a processor is not in the available processors, raise ValueError with the message: "{ processor } is not compatible with desktop computer { manufacturer name } { model name }!"
•	If RAM is not a valid size or is above the max size, raise ValueError with the message: "{ RAM }GB RAM is not compatible with desktop computer { manufacturer name } { model name }!"
•	If everything is valid, attach the processor to the computer, attach the RAM, and update the price. Return the following message: "Created { manufacturer name } { model name } with { processor } and { ram }GB RAM for { computer price }$."
3. Class Laptop
In the laptop.py file, the class Laptop should be implemented.
Methods
__init__(manufacturer: str, model: str)
•	In the __init__ method, all the needed attributes must be set.
 configure_computer(processor: str, ram: int)
•	Laptops can be built only with the available processors for laptops, which are:
o	AMD Ryzen 9 5950X: 900$
o	Intel Core i9-11900H: 1050$
o	Apple M1 Pro: 1200$
•	Laptops can have a max RAM of 64GB
o	Valid RAM sizes are 2, 4, 8…64. In other words, all the powers of the number 2 to the max size.
o	RAM price is defined by the power of the number 2, which gives the RAM size, multiplied by 100. 
For example: 2GB RAM will cost 100$ because 2 = 21  and 1 * 100 = 100. 4GB will be 200$.
•	If a processor is not in the available processors, raise ValueError with the message: "{ processor } is not compatible with laptop { manufacturer name } { model name }!"
•	If RAM is not a valid size or is above the max size, raise ValueError with the message: "{ RAM }GB RAM is not compatible with laptop { manufacturer name } { model name }!"
•	If everything is valid, attach the processor to the computer, attach the RAM, and update the price. Return the following message: "Created { manufacturer name } { model name } with { processor } and { ram }GB RAM for { computer price }$."
4. Class ComputerStoreApp
In the computer_store_app.py file, the class ComputerStoreApp should be implemented. It will contain all the functionality of the project.
Structure
The class should have the following attribute:
•	warehouse: list
o	A list that will store the built computers.
o	Should be empty upon initialization
•	profits: int
o	An integer that represents the store profits.
o	Should be set to 0 on initialization
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
build_computer(type_computer: str, manufacturer: str, model: str, processor: str, ram: int)
•	Valid types of computers are: "Desktop Computer", "Laptop"
•	If a computer type isn't valid, raise ValueError with the message: "{ type computer } is not a valid type computer!"
•	Otherwise, configure the computer, add it to the warehouse, and return the result from the configuration.
sell_computer(client_budget: int, wanted_processor: str, wanted_ram: int)
•	Search for a computer in the warehouse. To sell a computer, it has to meet the following criteria:
o	Computer's price is less than or equal to the client's budget.
o	The computer has the same processors as the one requested by the client.
o	The computer's RAM is more or equal to the one requested by the client.
•	If you can't find a computer to sell, raise an Exception with the message: "Sorry, we don't have a computer for you."
•	If you find a computer that meets the criteria, sell it at the client's budget price, add the difference between the sale price and the build price to the store profits, and return the following message: "{ computer } sold for { client budget }$."


_______________________________________________
Example

Test Code	(no input data in this task)


from project.computer_store_app import ComputerStoreApp

computer_store = ComputerStoreApp()

print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))

print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))




_______________________________________________
Output


Created Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.

Apple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.

_______________________________________________
