from minesweeper.utils import ANSI_RESET, COLORS
from .cellType import *
from ..utils import *

class Cell:
    def __init__(self, x, y):
        self.type = CellType.EMPTY
        self.x = x
        self.y = y

        self.is_flagged = False
        self.is_discovered = False
        self.is_marked = False
        self.bomb_index = 0

    def setType(self, type):
        '''Sets the cell's type'''
        assert(isinstance(type, CellType))
        self.type = type

    def setIsFlagged(self, flag):
        '''Defines the cell's flag'''
        self.is_flagged = flag

    def setIsMarked(self, mark):
        '''Defines the cell's mark'''
        self.is_marked = mark 

    def setIsDiscovered(self, discovered):
        '''Defines the cell's discovered state'''
        self.is_discovered = discovered

    def increaseBombIndex(self):
        '''Increases the bomb's index'''
        self.bomb_index = self.bomb_index + 1

    def __showDiscovered(self):
        '''Cell's representation when discovered'''
        if(self.getType() == CellType.BOMB):
            return COLORS['bomb'] + self.type.show()
        else:
            bomb_index_str = str(self.getBombIndex())
            if(self.getBombIndex() == 0):
                return self.type.show()
            else:
                return COLORS[bomb_index_str] + bomb_index_str

    def __showUndiscovered(self):
        '''Cell's representation when undiscovered'''
        if(self.is_flagged):
            return ANSI_RED_BOLD + '⚐'
        if(self.is_marked):
            return '?'

        return ' '

    def show(self):
        '''Cell's representation'''
        if self.is_discovered:
            return self.__showDiscovered()
        else:
            return self.__showUndiscovered()

    def getType(self):
        '''Defines the cell's type'''
        return self.type

    def getX(self):
        '''Returns the cell's x coordinate'''
        return self.x

    def getY(self):
        '''Returns the cell's y coordinate'''
        return self.y

    def isFlagged(self):
        '''Returns the cell's flag state'''
        return self.is_flagged

    def isMarked(self):
        '''Returns the cell's mark state'''
        return self.is_marked

    def isDiscovered(self):
        '''Returns the cell's discovered state'''
        return self.is_discovered

    def getBombIndex(self):
        '''Returns the bomb cell's bomb index'''
        return self.bomb_index