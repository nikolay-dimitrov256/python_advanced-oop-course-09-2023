from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    @property
    def valid_computers(self):
        return {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.valid_computers:
            raise ValueError(f'{type_computer} is not a valid type computer!')

        computer = self.valid_computers[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)

        # If we have not raised an error, building the computer:
        self.warehouse.append(computer)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((c for c in self.warehouse if c.price <= client_budget
                         and c.processor == wanted_processor
                         and c.ram >= wanted_ram), None)

        if computer is None:
            raise Exception('Sorry, we don\'t have a computer for you.')

        self.warehouse.remove(computer)
        self.profits += client_budget - computer.price

        return f'{repr(computer)} sold for {client_budget}$.'
