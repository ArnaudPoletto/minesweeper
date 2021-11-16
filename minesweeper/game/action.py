from enum import Enum

class Action(Enum):
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    FLAG = 5
    REVEAL = 6