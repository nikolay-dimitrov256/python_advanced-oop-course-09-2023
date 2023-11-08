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

        return self.__print_status(self.animals, 'animals', 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self):

        return self.__print_status(self.workers, 'workers', 'Keeper', 'Caretaker', 'Vet')

    @staticmethod
    def __print_status(collection: List[Animal or Worker], collection_type: str, *types):
        result = [f'You have {len(collection)} {collection_type}']
        data = {}
        for item in types:
            data[item] = []

        for item in collection:
            data[item.__class__.__name__].append(item.__repr__())

        for key, value in data.items():
            result.append(f'----- {len(data[key])} {key}s:')
            result.extend(data[key])

        return '\n'.join(result)
