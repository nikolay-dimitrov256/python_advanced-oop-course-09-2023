from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ['Vegetable', 'Fruit']
    WEIGHT_GAIN = 0.10

    @staticmethod
    def make_sound():
        return 'Squeak'


class Dog(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_GAIN = 0.40

    @staticmethod
    def make_sound():
        return 'Woof!'


class Cat(Mammal):
    ALLOWED_FOOD = ['Meat', 'Vegetable']
    WEIGHT_GAIN = 0.30

    @staticmethod
    def make_sound():
        return 'Meow'


class Tiger(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_GAIN = 1.0

    @staticmethod
    def make_sound():
        return 'ROAR!!!'
