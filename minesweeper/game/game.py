from minesweeper.game.difficulty import DIFFICULTY_PARAMETERS
from ..structure.grid import *
from .action import *
from ..utils import *
from ..globals import *
import keyboard
import threading
import time
import csv

# GLOBALS

KB_MOVE_UP = 'up'
KB_MOVE_DOWN = 'down'
KB_MOVE_LEFT = 'left'
KB_MOVE_RIGHT = 'right'
KB_FLAG = 'f'
KB_REVEAL = 'space'

# GAME

class Game:
    def __init__(self, 
                 grid,
                 n_flags):
        self.grid = grid
        self.n_flags = n_flags

        self.select_x = 0
        self.select_y = 0

        self.action_chosen = False
        self.perform_action = True
        self.action = None

        self.game_started = False
        self.start_time = None
        self.game_finished = False
        self.game_success = False

    def __getAction(self, key, action):
        '''Get keyboard action'''
        if(self.action_chosen):
            return

        if(keyboard.is_pressed(key)):
            self.perform_action = self.action is not action
            self.action = action
            self.action_chosen = True
        elif(self.action is action):
            self.action = None
            self.action_chosen = False
        
    def __catchAction(self):
        '''Updates the self.action argument given a key press action'''

        self.action_chosen = False
        self.__getAction(KB_MOVE_UP, Action.MOVE_UP)
        self.__getAction(KB_MOVE_DOWN, Action.MOVE_DOWN)
        self.__getAction(KB_MOVE_RIGHT, Action.MOVE_RIGHT)
        self.__getAction(KB_MOVE_LEFT, Action.MOVE_LEFT)
        self.__getAction(KB_FLAG, Action.FLAG)
        self.__getAction(KB_REVEAL, Action.REVEAL)

    def __performMove(self, diff_x, diff_y):
        '''Performs a movement action'''
        self.select_x = clamp(self.select_x + diff_x, 0, self.grid.getWidth())
        self.select_y = clamp(self.select_y + diff_y, 0, self.grid.getHeight())

    def __performFlag(self):
        '''Performs a flag action'''
        result = self.grid.setCellIsFlagged(self.select_x, self.select_y)
        self.n_flags += result

    def __avoidFirstRevealBomb(self):
        cell_d = self.grid.getCell(self.select_x, self.select_y)
        if(cell_d.getType() is CellType.EMPTY):
            return

        check_x, check_y = 0, 0
        is_bomb_placed = False
        while not is_bomb_placed:
            if(check_y >= self.grid.getHeight()):
                exit_error('Could not find a location to place the bomb.')

            cell_r = self.grid.getCell(check_x, check_y)
            if(cell_r.getType() == CellType.EMPTY):
                self.grid.addBomb(cell_r)
                is_bomb_placed = True

            check_y += (check_x == self.grid.getWidth() - 1)
            check_x = (check_x + 1) % self.grid.getWidth()
            
        self.grid.removeBomb(cell_d)

    def checkWinGame(self):
        '''Checks that the game is won'''
        n_undiscovered = self.grid.getNUndiscovered()
        return self.grid.getNBombs() == n_undiscovered

    def __performReveal(self):
        '''Performs a reveal action'''
        if(not self.game_started):
            self.__avoidFirstRevealBomb()
            self.start_time = time.time()

        discover_bomb = self.grid.setCellIsDiscovered(self.select_x, self.select_y, self.game_started)
        self.game_started = True

        # Finish game with failure
        if discover_bomb:
            self.game_finished = True
            self.game_success = False

        # Finish game with success
        if self.checkWinGame():
            self.game_finished = True
            self.game_success = True



    def __performAction(self):
        '''Performs the actions
         given by self.action'''
        if(not self.perform_action):
            return

        if(self.action == Action.MOVE_UP):
            self.__performMove(0, -1)
        elif(self.action == Action.MOVE_DOWN):
            self.__performMove(0, 1)
        elif(self.action == Action.MOVE_RIGHT):
            self.__performMove(1, 0)
        elif(self.action == Action.MOVE_LEFT):
            self.__performMove(-1, 0)
        elif(self.action == Action.FLAG):
            self.__performFlag()
        elif(self.action == Action.REVEAL):
            self.__performReveal()

        return self.action in [a for a in Action]

    def __update(self):
        '''Update the game periodically'''

        if self.game_finished:
            self.finish()

        timer = threading.Timer(0.01, self.__update)
        timer.start()

        self.__catchAction()
        updated = self.__performAction()
        if updated:
            self.show()

    def start(self):
        '''Start the game'''
        self.grid.initGrid()
        self.show()
        self.__update()

    def __showScore(self):
        '''Shows score'''
        end_time = time.time()
        seconds = secondsBetweenTimeStamps(self.start_time, end_time)
        if(seconds < 60):
            print(f'\t You completed the game in {seconds} second' + sIfPlural(seconds) + '!')
        else:
            minutes = seconds // 60
            seconds_re = int(((seconds / 60) - minutes) * 60)
            print(f'\t You completed the game in {minutes} minute' + sIfPlural(minutes) + f' and {seconds_re} second' + sIfPlural(seconds_re) + '!')

        return seconds

    def __checkBestScore(self, score):
        '''Checks that the current user score is the best'''
        is_best_score = True
        with open(DATA_FILE, newline='') as data_file:
            data_reader = csv.reader(data_file, delimiter=',')
            for row in data_reader:
                if(len(row) != 5):
                    continue

                if(row[1] == str(self.grid.getWidth())
                   and row[2] == str(self.grid.getHeight())
                   and row[3] == str(self.grid.getNBombs())):
                    is_best_score = is_best_score and (int(row[4]) > score)

        return is_best_score


    def __showBestScore(self):
        print(COLORS['1'] + '\n\t 🏆 This is a new best score!' + COLORS['reset'])

    def __enterUsername(self):
        name = None
        while(name == None or name == ''):
            name = input('Enter your username: ' + COLORS['1'])
            print(ANSI_RESET)

        return name

    def writeScore(self, name, score):
        with open(DATA_FILE, 'a') as data_file:
            new_row = name + ',' + str(self.grid.getWidth()) + ',' +  str(self.grid.getHeight()) + ',' + str(self.grid.getNBombs()) + ',' + str(score)
            data_file.write('\n' + new_row)

    def finish(self):
        '''Finishes the game, check if success or not'''
        if not self.game_success:
            self.grid.discoverAllBombs()

        self.show()

        flush_input()

        if self.game_success:
            print(ANSI_BOLD + '\n\t You won!' + COLORS['reset'])
            score = self.__showScore()
            is_best_score = self.__checkBestScore(score)
            if is_best_score:
                self.__showBestScore()
            name = self.__enterUsername()
            self.writeScore(name, score)
        else:
            print(ANSI_BOLD + '\n\t 💣💥 You lost!' + COLORS['reset'])

        exit()

    def show(self):
        '''Game's representation'''
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(ANSI_BOLD + str(self.n_flags) + ANSI_RESET + ' ⚐')
        self.grid.show(self.select_x, self.select_y)