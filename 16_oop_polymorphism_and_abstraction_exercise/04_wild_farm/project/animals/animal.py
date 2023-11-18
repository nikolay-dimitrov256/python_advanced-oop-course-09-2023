from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    ALLOWED_FOOD = []
    WEIGHT_GAIN = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.ALLOWED_FOOD:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * self.WEIGHT_GAIN
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
