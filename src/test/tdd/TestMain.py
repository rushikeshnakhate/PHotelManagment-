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
        actual = hotel.get_status("1a")
        assert actual, States.Available

    def test_checkOut_room_become_vacant(self):
        action(Events.CheckOut, "1a")
        actual = hotel.get_status("1a")
        assert actual, States.Vacant

    def test_vacant_room_after_cleaning_available(self):
        action(Events.Cleaning, "1a")
        actual = hotel.get_status("1a")
        assert actual, States.Available

    def test_vacant_room_for_repairing_become_repairing(self):
        action(Events.CheckIn)
        action(Events.CheckOut, "1a")
        action(Events.Repairing, "1a")
        actual = hotel.get_status("1a")
        assert actual, States.Repairing

    def test_repaired_room_become_vacant(self):
        action(Events.CheckIn)
        action(Events.CheckOut, "1b")
        action(Events.Repairing, "1b")
        action(Events.Repaired, "1b")
        actual = hotel.get_status("1b")
        assert actual, States.Vacant
