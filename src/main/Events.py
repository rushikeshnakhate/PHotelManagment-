from dataclasses import dataclass


@dataclass
class Events:
    CheckIn: str = "CheckIn"
    CheckOut: str = "CheckOut"
    Cleaning: str = "Cleaning"
    Repairing: str = "Repairing"
    Repaired: str = "Repaired"
