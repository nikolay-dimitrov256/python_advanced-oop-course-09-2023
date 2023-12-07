from project.meals.meal import Meal


class Starter(Meal):
    TYPE = "Starter"

    def __init__(self, name: str, price: float, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"{self.TYPE} {self.name}: {self.price:.2f}lv/piece"
