from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError('Manufacturer name cannot be empty.')

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError('Model name cannot be empty.')

        self.__model = value

    @property
    @abstractmethod
    def available_cpus(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_cpus:
            raise ValueError(f'{processor} is not compatible with {self.__str__()} {self.manufacturer} {self.model}!')

        valid_rams = [2 ** i for i in range(1, int(log2(self.max_ram)) + 1)]

        if ram not in valid_rams:
            raise ValueError(f'{ram}GB RAM is not compatible with {self.__str__()} {self.manufacturer} {self.model}!')

        self.processor = processor
        self.ram = ram
        ram_price = int(100 * log2(ram))
        cpu_price = self.available_cpus[processor]
        self.price = ram_price + cpu_price

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'

    def __repr__(self):
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'
