from project.meals.meal import Meal


class Dessert(Meal):
    TYPE = "Dessert"

    def __init__(self, name: str, price: float, quantity=30):
        super().__init__(name, price, quantity)

    def details(self):
        return f"{self.TYPE} {self.name}: {self.price:.2f}lv/piece"
