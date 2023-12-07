from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @staticmethod
    def find_horse_by_name(horse_name, horses_list):
        return next((h for h in horses_list if h.name == horse_name), None)

    @staticmethod
    def find_jockey_by_name(jockey_name, jockeys_list):
        return next((j for j in jockeys_list if j.name == jockey_name), None)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.find_horse_by_name(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        h_class = self.VALID_BREEDS.get(horse_type)

        if h_class:
            horse = h_class(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey_by_name(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey_by_name(jockey_name, self.jockeys)
        horse = next((h for h in reversed(self.horses) if h.__class__.__name__ == horse_type and not h.is_taken), None)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        jockey = self.find_jockey_by_name(jockey_name, self.jockeys)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey_name in [j.name for j in race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = race.jockeys[0]

        for jockey in race.jockeys:
            if jockey.horse.speed > winner.horse.speed:
                winner = jockey

        result = (f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! "
                  f"Winner's horse: {winner.horse.name}.")
        return result
