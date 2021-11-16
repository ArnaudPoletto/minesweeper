from .structure.grid import *
from .game.game import *

def startGame(grid_width,
              grid_height,
              n_bombs):
    '''Main method that starts the game'''
    grid = Grid(grid_width, grid_height, n_bombs)
    n_flags = n_bombs
    game = Game(grid, n_flags)
    game.start()
