from abc import ABC, abstractmethod


class Animal(ABC):
    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Dog(Animal):
    @staticmethod
    def make_sound():
        return 'woof-woof'


class Cat(Animal):
    @staticmethod
    def make_sound():
        return 'meow'


class Pig(Animal):
    @staticmethod
    def make_sound():
        return 'oink'


class Lion(Animal):
    @staticmethod
    def make_sound():
        return 'ROAR!!!'


animals = [Cat(), Dog(), Pig(), Lion()]
for animal in animals:
    print(animal.make_sound())
