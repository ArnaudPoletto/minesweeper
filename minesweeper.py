import argparse
from minesweeper.utils import *
from minesweeper.globals import *
from minesweeper.main import startGame
from minesweeper.game.difficulty import *

#=== GLOBALS ================================

ARGS_DIFFICULTY = 'd'
ARGS_CUSTOM_GAME = 'c'
ARGS_CUSTOM_GAME_WIDTH = 'w'    
ARGS_CUSTOM_GAME_HEIGHT = 'h'
ARGS_CUSTOM_GAME_BOMBS = 'b'
ARGS_IGNORE_RULES = 'ignore_rules'

def __ERROR_INVALID_ARG(arg):
	return f'Custom game argument {arg} is not valid.'

def __ERROR_INVALID_IGNORE_RULES_ARG(arg):
	return f'Ignore rules argument {arg} is not valid.'

def __ERROR_INVALID_DIFFICULTY_ARG(arg):
	return f'Difficulty argument {arg} is not valid.'

def __ERROR_NOT_INTEGER(arg):
	return f'Custom game argument {arg} is not an integer.'

def __ERROR_DUPLICATE_ARG(arg):
	return f'Custom game argument {arg} has already been specified.'

ERROR_NOT_SPECIFIED_ARG = 'Not all custom game arguments have been specified.'

ERROR_ARGS_NOT_SPECIFIED = 'You must specify either the difficulty or a custom game.'

#=== MAIN ===================================

def __assertValidDifficulty(difficulty):
    '''Returns true if the given difficulty is valid, false otherwise'''

    isValidDifficulty = False
    for difficulty_data in DIFFICULTY_PARAMETERS:
        isValidDifficulty |= (difficulty == difficulty_data)
    
    return isValidDifficulty

def __getCustomGameParameters(custom_game_args):
    '''Returns the raw integer values for each arguments'''
    args = custom_game_args.split(',')
    grid_width, grid_height, n_bombs = -1, -1, -1
    for arg in args:
        arg_split = arg.split('=')
        if(len(arg_split) != 2):
            exit_error(__ERROR_INVALID_ARG(arg))

        arg_name = arg_split[0]
        arg_value = arg_split[1]
        # Get argument value
        if(not arg_value.isnumeric()):
            exit_error(__ERROR_NOT_INTEGER(arg))
        else:
            arg_value = int(arg_value)

        # Define parameters given argument
        if(arg_name == ARGS_CUSTOM_GAME_WIDTH):
            if(grid_width != -1):
                exit_error(__ERROR_DUPLICATE_ARG(ARGS_CUSTOM_GAME_WIDTH))
            grid_width = arg_value

        elif(arg_name == ARGS_CUSTOM_GAME_HEIGHT):
            if(grid_height != -1):
                exit_error(__ERROR_DUPLICATE_ARG(ARGS_CUSTOM_GAME_HEIGHT))
            grid_height = arg_value

        elif(arg_name == ARGS_CUSTOM_GAME_BOMBS):
            if(n_bombs != -1):
                exit_error(__ERROR_DUPLICATE_ARG(ARGS_CUSTOM_GAME_BOMBS))
            n_bombs = arg_value

        else:
            exit_error(__ERROR_INVALID_ARG(arg))

    if(grid_width == -1 or grid_height == -1 or n_bombs == -1):
        exit_error(ERROR_NOT_SPECIFIED_ARG)
    
    return grid_width, grid_height, n_bombs

def __getDifficultyParameters(difficulty):
    '''Returns the game parameters given a difficulty'''
    grid_width = DIFFICULTY_PARAMETERS[difficulty]['grid_size']
    grid_height = DIFFICULTY_PARAMETERS[difficulty]['grid_size']
    n_bombs = DIFFICULTY_PARAMETERS[difficulty]['n_bombs']

    return grid_width, grid_height, n_bombs


def main():
    '''Main method, parses the parameters and launches the game'''
    # Process each arguments given to the script
    parser = argparse.ArgumentParser()
    parser.add_argument('--' + ARGS_DIFFICULTY, help='int: Difficulty of the game (easy|medium|hard).')
    parser.add_argument('--' + ARGS_CUSTOM_GAME, help='w=int,h=int,b=int: Custom game with grid size (w, h) and b bombs.')
    parser.add_argument('--' + ARGS_IGNORE_RULES, help='Ignore parameters modifications to respect game rules.')
    args = parser.parse_args()

    # Get arguments, check that they are valid. Custom game is more powerful than difficulty when both specified
    difficulty_arg = vars(args)[ARGS_DIFFICULTY]
    difficulty = Difficulty.getDifficultyFromStr(difficulty_arg)
    custom_game = vars(args)[ARGS_CUSTOM_GAME]
    ignore_rules = vars(args)[ARGS_IGNORE_RULES]

    if(custom_game is not None):
        grid_width, grid_height, n_bombs = __getCustomGameParameters(custom_game)

        # Edit parameters according to the rules
        if(ignore_rules is None or ignore_rules == 'false'):
            grid_width = clamp(grid_width, MIN_GRID_WIDTH, MAX_GRID_WIDTH)
            grid_height = clamp(grid_height, MIN_GRID_HEIGHT, MAX_GRID_HEIGHT)
            n_bombs = clamp(n_bombs, 0, MAX_N_BOMBS(grid_width, grid_height))
        elif(ignore_rules == 'true'):
            # Still change number of bombs to avoid infinite loop
            n_bombs = clamp(n_bombs, 0, grid_width * grid_height)
        else:
        	exit_error(__ERROR_INVALID_IGNORE_RULES_ARG(ignore_rules))

    else:
        if(difficulty_arg is None):
            exit_error(ERROR_ARGS_NOT_SPECIFIED)
            
        # Check that the difficulty argument is valid
        if(not __assertValidDifficulty(difficulty)):
            exit_error(__ERROR_INVALID_DIFFICULTY_ARG(difficulty_arg))

        grid_width, grid_height, n_bombs = __getDifficultyParameters(difficulty)

    startGame(grid_width, grid_height, n_bombs)


if __name__ == '__main__':
    main()