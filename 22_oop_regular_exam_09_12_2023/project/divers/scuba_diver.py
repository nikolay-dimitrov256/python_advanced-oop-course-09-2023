from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        oxygen_drain = round(time_to_catch * 0.3)

        if self.oxygen_level < oxygen_drain:
            self.oxygen_level = 0.0
        else:
            self.oxygen_level -= oxygen_drain

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN
