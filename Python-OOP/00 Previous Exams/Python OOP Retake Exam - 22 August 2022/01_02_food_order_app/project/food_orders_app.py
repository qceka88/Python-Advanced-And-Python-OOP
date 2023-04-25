from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.client import Client


class FoodOrdersApp:

    def __init__(self):
        self.menu: [Meal] = []
        self.clients_list: [Client] = []
        self.receipt_id = 1

    @property
    def approved_meals(self):
        return {"Starter": Starter,
                "Dessert": Dessert,
                "MainDish": MainDish}

    @staticmethod
    def find_object(value, attribute, list_of_objects):
        for obj in list_of_objects:
            if getattr(obj, attribute) == value:
                return obj

    def register_client(self, client_phone_number: str):
        client = self.find_object(client_phone_number, "phone_number", self.clients_list)
        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: [Meal]):
        for meal in meals:
            if meal.__class__.__name__ in self.approved_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        details = [m.details() for m in self.menu]
        return "\n".join(details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.find_object(client_phone_number, "phone_number", self.clients_list)
        if not client:
            self.register_client(client_phone_number)

        client = self.find_object(client_phone_number, "phone_number", self.clients_list)

        for meal, quantity in meal_names_and_quantities.items():
            meal_obj = self.find_object(meal, "name", self.menu)

            if not meal_obj:
                client.shopping_cart = []
                client.bill = 0
                raise Exception(f"{meal} is not on the menu!")

            if meal_obj.quantity < quantity:
                client.shopping_cart = []
                client.bill = 0
                raise Exception(f"Not enough quantity of {meal_obj.type_of_meal}: {meal}!")

            meal_obj.quantity -= quantity

            client_meal = self.approved_meals[meal_obj.__class__.__name__](meal_obj.name, meal_obj.price, quantity)
            client.shopping_cart.append(client_meal)
            client.bill += client_meal.price * client_meal.quantity

        client_meals = ", ".join(n.name for n in client.shopping_cart)

        return f"Client {client_phone_number} successfully ordered {client_meals} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client = self.find_object(client_phone_number, "phone_number", self.clients_list)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            menu_meal = self.find_object(meal.name, "name", self.menu)

            menu_meal.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = self.find_object(client_phone_number, "phone_number", self.clients_list)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        message = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."

        self.receipt_id += 1
        client.shopping_cart = []
        client.bill = 0

        return message

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
