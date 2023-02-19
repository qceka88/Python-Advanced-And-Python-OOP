from collections import deque


def initial_data():
    textiles_materials = deque(int(i) for i in input().split())
    medicaments_materials = deque(int(i) for i in input().split())
    return textiles_materials, medicaments_materials


def add_product(data):
    if name not in provisions:
        provisions[data] = 0
    provisions[data] += 1


def print_result():
    def add_product_to_result():
        for prod_name, prod_qty in sorted(provisions.items(), key=lambda x: (-x[1], x[0])):
            if prod_qty:
                log_file.append(f"{prod_name} - {prod_qty}")

    log_file = []
    if not textiles and not medicaments:
        log_file.append("Textiles and medicaments are both empty.")
        add_product_to_result()
    elif medicaments and not textiles:
        log_file.append("Textiles are empty.")
        add_product_to_result()
    elif textiles and not medicaments:
        log_file.append("Medicaments are empty.")
        add_product_to_result()

    if medicaments:
        left_medicaments = [str(x) for x in medicaments][::-1]
        log_file.append(f"Medicaments left: {', '.join(left_medicaments)}")
    if textiles:
        left_textiles = [str(x) for x in textiles]
        log_file.append(f"Textiles left: {', '.join(left_textiles)}")

    return '\n'.join(log_file)


MAX_COST = 100
inventory = {30: 'Patch', 40: 'Bandage', 100: 'MedKit'}
textiles, medicaments = initial_data()

provisions = {}

while textiles:
    current_textile = textiles.popleft()
    while medicaments:
        current_medicament = medicaments.pop()

        product = current_textile + current_medicament

        if product > MAX_COST:
            medicaments[-1] += product - MAX_COST
            product = MAX_COST

        if product in inventory:
            name = inventory[product]
            add_product(name)
            break
        else:
            medicaments.append(current_medicament + 10)
            break
    if not medicaments:
        break

print(print_result())



#################################### TASK CONDITION ############################
"""
                          01 Apocalypse Preparation
 
You are in the middle of a zombie apocalypse and you want to go out for exploration. But before you do that, 
you need to prepare some healing items. On the first line, you will be given a sequence representing textiles.
On the second line, you will be given another sequence, which represents medicaments. While both collections 
contain any elements, you will have to combine elements from the collections in order to create healing items. 
You should start by getting the first value of textile and the last value of medicaments:
•	If their sum is equal to any of the items in the table below create that item and remove both values. 
•	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values, 
and add the remaining resources(of the sum) to the next value in the medicament collection (Take the element 
from the collection, add the remaining sum to it, and put the element back to its place).
•	If you can’t create anything, remove the textile value, add 10 to the medicament value, and return the 
medicament back to its place, into its collection. 
You need to stop creating healing items when either the textile or the medicaments are exhausted.

                         Healing item	    Resources needed
                            Patch	              30
                            Bandage	          40
                            MedKit	              100

In the end, you should print on the console message for the sequence that has ended, 
hen the created items, and in the end the remaining items (if any).
Input
•	On the first line, you will receive a sequence of integers representing the textiles, 
separated by a single space (" ").
•	On the second line, you will receive a sequence of integers representing the medicaments, 
separated by a single space (" ").
Output
•	On the first line print which one of the collections is over:
o	If the textile is over print: "Textiles are empty."
o	If the medicaments are over print: "Medicaments are empty."
o	If both are empty print: "Textiles and medicaments are both empty."
•	On the next n lines print only the created items (if any) ordered by the amount 
created descending, then by name alphabetically:
"{item name} - {amount created}
  {item name} - {amount created}
…
"
Hint: Do not print items, which are not created.
•	On the last line print the remaining items(if any):
o	If there are any medicaments left: 
 "Medicaments left: …{medicament2}, {medicament1}"
o	If there are any textiles left:  
"Textiles left: {textile1}, {textile2}…"
Constraints
•	All the numbers will be in the range [0…1000].
•	All the inputs will be valid.

____________________________________________________________________________________________
Example_01

Input
20 10 40 70 20
10 50 10 30 20 80


Output
Textiles are empty.
MedKit - 2
Bandage - 1
Patch - 1
Medicaments left: 50, 10


____________________________________________________________________________________________
Example_02

Input
30 30 10 80 60
40 20 30 10 70

Output
Textiles and medicaments are both empty.
MedKit - 3
Bandage - 2


____________________________________________________________________________________________
Example_03

Input
30 30 10 80 60 20
40 20 30 10 70

Output
Medicaments are empty.
MedKit - 3
Bandage - 2
Textiles left: 20
60 15 20 30 20
20 15 40

Output
Medicaments are empty.
Bandage - 1
MedKit - 1
Patch - 1
Textiles left: 30, 20



"""


