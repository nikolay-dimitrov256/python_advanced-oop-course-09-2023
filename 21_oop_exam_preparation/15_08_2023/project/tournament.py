from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    VALID_TEAMS = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception('Invalid equipment type!')

        equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)

        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception('Invalid team type!')

        if len(self.teams) == self.capacity:
            return 'Not enough tournament capacity.'

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f'{team_type} was successfully added.'

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        team = next((t for t in self.teams if t.name == team_name), None)

        if equipment.price > team.budget:
            raise Exception('Budget is not enough!')

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception('No such team!')

        if team.wins > 0:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')

        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1

        return f'Successfully changed {number_of_changed_equipment}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1))
        team2 = next((t for t in self.teams if t.name == team_name2))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception('Game cannot start! Team types mismatch!')

        team1_result = team1.advantage + team1.total_protection
        team2_result = team2.advantage + team2.total_protection

        winner = None
        if team1_result > team2_result:
            winner = team1
        elif team2_result > team1_result:
            winner = team2

        if winner is None:
            return 'No winner in this game.'

        winner.win()
        return f'The winner is {winner.name}.'

    def get_statistics(self):
        result = [f'Tournament: {self.name}', f'Number of Teams: {len(self.teams)}', 'Teams:']
        teams = sorted(self.teams, key=lambda t: -t.wins)

        for team in teams:
            result.append(team.get_statistics())

        return '\n'.join(result)
