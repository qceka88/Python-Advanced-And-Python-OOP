from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def find_data(id_number, data_list):
        for data in data_list:
            if id_number == data.id:
                return data

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        info = (self.subscriptions, self.customers, self.trainers, self.equipment, self.plans)

        return '\n'.join(str(self.find_data(subscription_id, lst)) for lst in info)

    # this is second variant of method  "subscription info"
    def subscription_info2(self, subscription_id: int):
        subscription = self.find_data(subscription_id, self.subscriptions)
        customer = self.find_data(subscription.id, self.customers)
        trainer = self.find_data(subscription.id, self.trainers)
        plan = self.find_data(subscription_id, self.plans)
        equipment = self.find_data(plan.id, self.equipment)

        info = [subscription, customer, trainer, equipment, plan]

        return '\n'.join(str(i) for i in info)
