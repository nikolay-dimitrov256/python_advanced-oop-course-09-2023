from project.room import Room
from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f'{stars_count} stars Hotel'
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next((r for r in self.rooms if r.number == room_number), None)

        if room:
            return room.take_room(people)

    def free_room(self, room_number):
        room = next((r for r in self.rooms if r.number == room_number), None)

        if room:
            return room.free_room()

    def status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\nFree rooms: '
        result += ', '.join([str(r.number) for r in self.rooms if not r.is_taken])
        result += '\nTaken rooms: '
        result += ', '.join([str(r.number) for r in self.rooms if r.is_taken])

        return result
