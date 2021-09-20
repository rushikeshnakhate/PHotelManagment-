from src.main.Events import Events
from src.main.Hotel import Hotel
from src.main.StateMachine import States

hotel = Hotel(4, 5)


# creating this as raw example for now
def action(action, room=""):
    if action == Events.CheckIn:
        room, value = hotel.get_room_for_status(States.Available)
        value.CheckIn()
        print("room={} checked in".format(room))
    elif action == Events.CheckOut:
        value = hotel.get_room(room)
        value.CheckOut()
    elif action == Events.Cleaning:
        value = hotel.get_room(room)
        value.Cleaning()
    elif action == Events.Repairing:
        value = hotel.get_room(room)
        value.Repairing()
    elif action == Events.Repaired:
        value = hotel.get_room(room)
        value.Repaired()


if __name__ == "__main__":
    try:
        action(Events.CheckIn)
        action(Events.CheckOut, "1a")
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
