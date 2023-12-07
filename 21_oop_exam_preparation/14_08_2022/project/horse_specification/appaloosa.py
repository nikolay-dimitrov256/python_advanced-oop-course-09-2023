from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed_increase(self):
        return 2

    @property
    def max_speed(self):
        return 120
