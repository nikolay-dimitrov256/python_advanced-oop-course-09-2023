from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        if price > self.__budget:
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        tending_costs = sum(a.money_for_care for a in self.animals)

        if tending_costs <= self.__budget:
            self.__budget -= tending_costs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal.__repr__())
            else:
                cheetahs.append(animal.__repr__())

        result = [f'You have {len(self.animals)} animals']
        result.append(f'----- {len(lions)} Lions:')
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)

        return '\n'.join(result)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker.__repr__())
            else:
                vets.append(worker.__repr__())

        result = [f'You have {len(self.workers)} workers']
        result.append(f'----- {len(keepers)} Keepers:')
        result.extend(keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)

        return '\n'.join(result)
