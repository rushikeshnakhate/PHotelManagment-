import itertools
import string

from src.main.StateMachine import StateMachine


# This class can be singleton , For Simplicity creating a class now and
# User to create a single instance of this class
class Hotel:
    def __init__(self, floors, rooms_on_each_floor):
        self.hotel = []
        self.build_hotel(floors, rooms_on_each_floor)
        self.hotel = list(itertools.chain(*self.hotel))  # flatten
        self.set_status()

    def build_hotel(self, floors, rooms_on_each_floor):
        for floor in range(1, floors + 1):
            room_sequence = list(string.ascii_lowercase)[0: rooms_on_each_floor]
            if floor % 2 != 0:
                self.hotel.append([str(floor) + room for room in room_sequence])
            else:
                self.hotel.append([str(floor) + room for room in room_sequence[::-1]])

    def set_status(self):
        hotel = {}
        for room in self.hotel:
            hotel[room] = StateMachine()
        self.hotel = hotel

    def get_status(self, room):
        return self.hotel[room].state

    def get_room(self, room):
        return self.hotel[room]

    def print(self):
        for key, value in self.hotel.items():
            print(key, value.state)

    def get_room_for_status(self, States):
        for key, value in self.hotel.items():
            if value.state == States.name:
                return key , value
