from enum import Enum

class State(Enum):
    GOING_TO_SEAT = 1
    SEATING = 2
    SHUFFLING = 3
    WAITING_TO_COME_BACK = 4
    COMMING_BACK=5