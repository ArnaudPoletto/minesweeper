from .cell import *
from ..utils import *

MAX_GRID_WIDTH = 40
MAX_GRID_HEIGHT = 26

class Grid:
    def __init__(self, width, height, n_bombs):
        self.width = width
        self.height = height
        self.n_bombs = n_bombs

        self.init = False
        # List of couples (x, y) representing the cell's location
        self.bomb_locations = []
        self.grid = [[Cell(x, y) for x in range(0, width)] for y in range(0, height)]

    def discoverAllBombs(self):
        '''Discovers all bombs'''
        for (x, y) in self.bomb_locations:
            cell = self.getCell(x, y)
            cell.setIsDiscovered(True)

    def __discoverNeigbour(self, x, y):
        '''Discovers a neighbour at a given location (x, y)'''
        if(not inGrid(x, y, self.width, self.height)):
            return
        
        self.setCellIsDiscovered(x, y)

    def __discoverNeigbours(self, cell):
        '''Discovers all neighbours from a cell'''
        (x, y) = (cell.getX(), cell.getY())
        self.__discoverNeigbour(x - 1, y + 1)
        self.__discoverNeigbour(x    , y + 1)
        self.__discoverNeigbour(x + 1, y + 1)
        self.__discoverNeigbour(x + 1, y    )
        self.__discoverNeigbour(x + 1, y - 1)
        self.__discoverNeigbour(x    , y - 1)
        self.__discoverNeigbour(x - 1, y - 1)
        self.__discoverNeigbour(x - 1, y    )

    def setCellIsDiscovered(self, x, y, computed_bomb_indexes=True):
        '''Discovers a cell, returns true if the cell is a bomb'''
        if(not computed_bomb_indexes):
            self.__computeBombIndexes()

        cell = self.getCell(x, y)
        if(cell.isFlagged() or cell.isDiscovered()):
            return False

        cell.setIsDiscovered(True)

        # Cell is bomb
        if(cell.getType() == CellType.BOMB):
            return True
            
        # Cell has bomb index 0
        if(cell.getBombIndex() == 0):
            self.__discoverNeigbours(cell)
        return False

    def setCellIsFlagged(self, x, y):
        '''Flags a cell, returns the flag's score to add'''
        cell = self.getCell(x, y)
        if(cell.isDiscovered()):
            return 0

        if(cell.isFlagged()):
            cell.setIsFlagged(False)
            cell.setIsMarked(True)
            score = 1
        else:
            if(cell.isMarked()):
                cell.setIsMarked(False)
                score = 0
            else:
                cell.setIsFlagged(True)
                score = -1

        return score

    def getNUndiscovered(self):
        '''Returns the number of undiscovered cells'''
        n = 0
        for xs in self.grid:
            for cell in xs:
                if not cell.isDiscovered():
                    n += 1

        return n

    def getWidth(self):
        '''Returns the width of the grid'''
        return self.width
    
    def getHeight(self):
        '''Returns the height of the grid'''
        return self.height

    def getNBombs(self):
        '''Returns the nomber of bombs'''
        return self.n_bombs

    def getCell(self, x, y):
        '''Returns the cell at a given location'''
        if(not inGrid(x, y, self.width, self.height)):
            exit_error('The cell specified is out of range.')
        
        return self.grid[y][x]

    def removeBomb(self, cell):
        '''Removes a bomb in a given cell'''
        if(cell.getType() is not CellType.BOMB):
            return

        cell.setType(CellType.EMPTY)
        self.bomb_locations.remove((cell.getX(), cell.getY()))

    def addBomb(self, cell):
        '''Adds a bomb in a given cell'''
        cell.setType(CellType.BOMB)
        self.bomb_locations.append((cell.getX(), cell.getY()))

    def __placeBombs(self):
        '''Places bombs in the grid'''
        rest_bombs = self.n_bombs
        while(rest_bombs > 0):
            x = rand(self.width)
            y = rand(self.height)
            cell = self.getCell(x, y)
            if(cell.getType() == CellType.EMPTY):
                self.addBomb(cell)
                rest_bombs -= 1

    def addCellBombIndex(self, x, y):
        '''Increases the bomb index given a cell'''
        if not inGrid(x, y, self.width, self.height):
            return

        cell = self.getCell(x, y)
        cell.increaseBombIndex()

    def __computeBombIndexes(self):
        '''Computes the bomb indexes of all cells in the grid'''
        for (x, y) in self.bomb_locations:
            self.addCellBombIndex(x - 1, y + 1)
            self.addCellBombIndex(x,     y + 1)
            self.addCellBombIndex(x + 1, y + 1)
            self.addCellBombIndex(x + 1, y    )
            self.addCellBombIndex(x + 1, y - 1)
            self.addCellBombIndex(x,     y - 1)
            self.addCellBombIndex(x - 1, y - 1)
            self.addCellBombIndex(x - 1, y    )

    def initGrid(self):
        '''Initializes the grid'''
        if(self.init):
            raise Exception("The grid can be initialized only one time.")
        self.init = True

        self.__placeBombs()

    def __showXAxis(self):
        '''Displays the x axis'''
        print('\t ', end='')
        for x_bar in range(ord('A'), ord('A') + self.getWidth()):
            print(chr(x_bar), ' ', end='')
    
    def __showYAxisAndGrid(self, select_x, select_y):
        '''Displays the y axis and the grid'''
        y_bar = 0

        print('\n')
        for xs in self.grid:
            print(y_bar, '\t', end='')
            y_bar += 1

            for cell in xs:
                is_selected_cell = (cell.getX(), cell.getY()) == (select_x, select_y)
                color = COLORS['select'] if is_selected_cell else COLORS['undiscovered'] if not cell.isDiscovered() else ''
                color_reset = COLORS['reset']
                print(color + ' ' + cell.show() + ' ' + color_reset, end = '')
            print('\n', end = '')

    def show(self, select_x, select_y):
        '''Print the grid'''
        self.__showXAxis()
        self.__showYAxisAndGrid(select_x, select_y)


        

        