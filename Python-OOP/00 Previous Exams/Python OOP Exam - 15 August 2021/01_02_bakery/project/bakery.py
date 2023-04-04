from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    DRINK_TYPES = {"Tea": Tea, "Water": Water}
    TABLE_TYPE = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: [BakedFood] = []
        self.drinks_menu: [Drink] = []
        self.tables_repository: [Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in Bakery.FOOD_TYPES:
            if self.find_data(name, "name", self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")

            new_food = Bakery.FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)

            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in Bakery.DRINK_TYPES:
            if self.find_data(name, "name", self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")

            new_drink = Bakery.DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)

            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in Bakery.TABLE_TYPE:
            if self.find_data(table_number, "table_number", self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")

            new_table = Bakery.TABLE_TYPE[table_type](table_number, capacity)
            self.tables_repository.append(new_table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self.find_data(table_number, "table_number", self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        ordered_food = []
        not_in_the_menu_food = []

        for name in food_names:
            food = self.find_data(name, "name", self.food_menu)
            if food:
                table.order_food(food)
                ordered_food.append(food)
            else:
                not_in_the_menu_food.append(name)

        message = [f"Table {table_number} ordered:"]
        for food in ordered_food:
            message.append(str(food))
        message.append(f"{self.name} does not have in the menu:")
        for food in not_in_the_menu_food:
            message.append(food)

        return "\n".join(message)

    def order_drink(self, table_number: int, *drinks_names: str):
        table = self.find_data(table_number, "table_number", self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drink = []
        not_in_the_menu_drink = []

        for name in drinks_names:
            drink = self.find_data(name, "name", self.drinks_menu)
            if drink:
                table.order_drink(drink)
                ordered_drink.append(str(drink))
            else:
                not_in_the_menu_drink.append(name)

        message = [f"Table {table_number} ordered:"]
        for drink in ordered_drink:
            message.append(drink)
        message.append(f"{self.name} does not have in the menu:")
        for drink in not_in_the_menu_drink:
            message.append(drink)

        return "\n".join(message)

    def leave_table(self, table_number: int):
        table = self.find_data(table_number, "table_number", self.tables_repository)
        if table:
            self.total_income += table.get_bill()
            message = f"Table: {table.table_number}\nBill: {table.get_bill():.2f}"
            table.clear()

            return message

    def get_free_tables_info(self):
        info = [t.free_table_info() for t in self.tables_repository if t.free_table_info()]

        return "\n".join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
