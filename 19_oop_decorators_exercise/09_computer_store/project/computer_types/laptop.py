from project.computer_types.computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def max_ram(self):
        return 64

    @property
    def available_cpus(self):
        return {"AMD Ryzen 9 5950X": 900, 'Intel Core i9-11900H': 1050, "Apple M1 Pro": 1200}

    def __str__(self):
        return 'laptop'
