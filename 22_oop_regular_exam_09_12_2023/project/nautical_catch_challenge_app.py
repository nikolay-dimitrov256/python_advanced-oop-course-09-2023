from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    ALLOWED_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    @staticmethod
    def find_diver_by_name(diver_name, divers_list) -> BaseDiver:
        return next((d for d in divers_list if d.name == diver_name), None)

    @staticmethod
    def find_fish_by_name(fish_name, fish_list) -> BaseFish:
        return next((f for f in fish_list if f.name == fish_name), None)

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.ALLOWED_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        if self.find_diver_by_name(diver_name, self.divers):
            return f"{diver_name} is already a participant."

        diver = self.ALLOWED_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.find_fish_by_name(fish_name, self.fish_list):
            return f"{fish_name} is already permitted."

        fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.find_diver_by_name(diver_name, self.divers)

        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = self.find_fish_by_name(fish_name, self.fish_list)

        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                self.fish_list.remove(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        self.fish_list.remove(fish)
        if diver.oxygen_level == 0:
            diver.update_health_status()
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        fixed_divers = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                fixed_divers += 1

        return f"Divers recovered: {fixed_divers}"

    def diver_catch_report(self, diver_name: str):
        diver = self.find_diver_by_name(diver_name, self.divers)

        if diver is None:
            return None

        result = [f"**{diver_name} Catch Report**"]

        for fish in diver.catch:
            result.append(fish.fish_details())

        return "\n".join(result)

    def competition_statistics(self):
        divers = [d for d in self.divers if not d.has_health_issue]
        divers = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        for d in divers:
            result.append(str(d))

        return "\n".join(result)
