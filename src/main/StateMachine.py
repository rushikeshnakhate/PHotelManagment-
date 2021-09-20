from transitions import Machine
import enum

from src.main.Events import Events


class States(enum.Enum):
    Available = 1,
    Occupied = 2,
    Vacant = 3,
    Repairing = 4,
    Repaired = 5


class StateMachine(object):
    def __init__(self):
        self.machine = Machine(model=self, states=[e.name for e in States], initial=States.Available)
        self.machine.add_transition(trigger=Events.CheckIn, source=States.Available, dest=States.Occupied)
        self.machine.add_transition(trigger=Events.CheckOut, source=States.Occupied, dest=States.Vacant)
        self.machine.add_transition(trigger=Events.Cleaning, source=States.Vacant, dest=States.Available)
        self.machine.add_transition(trigger=Events.Repairing, source=States.Vacant, dest=States.Repairing)
        self.machine.add_transition(trigger=Events.Repaired, source=States.Repairing, dest=States.Vacant)
