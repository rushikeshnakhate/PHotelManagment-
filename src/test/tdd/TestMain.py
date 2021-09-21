import unittest

from src.main.Events import Events
from src.main.Hotel import Hotel
from src.main.Main import action, hotel
from src.main.StateMachine import States


class TestLinkList(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(4, 5)
        return

    def test_checkIn_room_become_available(self):
        action(Events.CheckIn)
        actual = hotel.get_status("1A")
        assert actual, States.Available

    def test_checkOut_room_become_vacant(self):
        action(Events.CheckOut, "1A")
        actual = hotel.get_status("1A")
        assert actual, States.Vacant

    def test_vacant_room_after_cleaning_available(self):
        action(Events.Cleaning, "1A")
        actual = hotel.get_status("1A")
        assert actual, States.Available

    def test_vacant_room_for_repairing_become_repairing(self):
        action(Events.CheckIn)
        action(Events.CheckOut, "1A")
        action(Events.Repairing, "1A")
        actual = hotel.get_status("1A")
        assert actual, States.Repairing

    def test_repaired_room_become_vacant(self):
        action(Events.CheckIn)
        action(Events.CheckOut, "1B")
        action(Events.Repairing, "1B")
        action(Events.Repaired, "1B")
        actual = hotel.get_status("1B")
        assert actual, States.Vacant
