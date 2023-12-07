import copy
from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    receipt_id = 1

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def get_receipt_id(self):
        current = self.receipt_id
        self.receipt_id += 1
        return current

    def register_client(self, client_phone_number: str):
        same_number = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if same_number:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        # TODO: check if it works
        for meal in meals:
            # if isinstance(meal, Meal):
            if meal.__class__.__name__ in self.VALID_MEALS.keys():
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [m.details() for m in self.menu]

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if client is None:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        orders_list = []
        bill = 0.0

        for name, quantity in meal_names_and_quantities.items():
            meal = next((m for m in self.menu if m.name == name), None)

            if meal is None:
                raise Exception(f"{name} is not on the menu!")

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {name}!")

            # TODO: check if errors
            # meal.quantity -= quantity
            # current_meal = self.VALID_MEALS[meal.__class__.__name__](meal.name, meal.price, quantity)
            current_meal = copy.copy(meal)
            current_meal.quantity = quantity
            orders_list.append(current_meal)
            bill += current_meal.price * quantity

        client.shopping_cart.extend(orders_list)
        client.bill += bill

        # for meal in orders_list:
        for meal in client.shopping_cart:
            menu_meal = next((m for m in self.menu if m.name == meal.name), None)

            if menu_meal is None:
                continue

            menu_meal.quantity -= meal.quantity

        meal_names = ", ".join([m.name for m in client.shopping_cart])
        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            menu_meal = next((m for m in self.menu if m.name == meal.name), None)

            if menu_meal is None:
                continue

            menu_meal.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        result = (f"Receipt #{self.get_receipt_id()} with total amount of {client.bill:.2f} "
                  f"was successfully paid for {client_phone_number}.")

        # for meal in client.shopping_cart:
        #     menu_meal = next((m for m in self.menu if m.name == meal.name), None)
        #
        #     if menu_meal is None:
        #         continue
        #
        #     if meal.quantity == menu_meal.quantity:
        #         self.menu.remove(menu_meal)
        #     else:
        #         menu_meal.quantity -= meal.quantity

        client.shopping_cart.clear()
        client.bill = 0.0

        return result

    def __str__(self):
        result = f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
        return result
