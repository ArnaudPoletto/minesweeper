from enum import Enum

class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

    def show(self):
        '''Difficulty's representation'''
        if(self.name == self.EASY):
            return 'easy'
        elif(self.name == self.MEDIUM):
            return 'medium'
        elif(self.name == self.HARD):
            return 'hard'
        else:
            return 'undefined'

    @staticmethod
    def getDifficultyFromStr(str):
        '''Retrieve difficulty from str representation'''
        if(str == 'easy'):
            return Difficulty.EASY
        elif(str == 'medium'):
            return Difficulty.MEDIUM
        elif(str == 'hard'):
            return Difficulty.HARD
        else:
            return None

# DIFFICULTY

DIFFICULTY_PARAMETERS = {
        Difficulty.EASY: {
            'type': 'easy',
            'grid_size': 10,
            'n_bombs': 10
        },
        Difficulty.MEDIUM: {
            'type': 'medium',
            'grid_size': 18,
            'n_bombs': 40
        },
        Difficulty.HARD: {
            'type': 'hard',
            'grid_size': 24,
            'n_bombs': 100
        }
    }