from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def get_item(collection, searched_id):
        item = next((el for el in collection if el.id == searched_id), None)
        return item

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
        subscription = self.get_item(self.subscriptions, subscription_id)
        customer = self.get_item(self.customers, subscription.customer_id)
        trainer = self.get_item(self.trainers, subscription.trainer_id)
        plan = next((p for p in self.plans if p.trainer_id == trainer.id), None)
        equipment = self.get_item(self.equipment, plan.equipment_id)

        result = [repr(subscription), repr(customer), repr(trainer), repr(equipment), repr(plan)]

        return '\n'.join(result)
