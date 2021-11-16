from enum import Enum

class CellType(Enum):
    EMPTY = 0
    BOMB = 1

    def show(self):
        '''Cell type's representation'''
        if(self == CellType.EMPTY):
            return ' '
        elif(self == CellType.BOMB):
            return '×'
        else:
            return '-'