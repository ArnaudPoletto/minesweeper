import sys
import random

def rand(n):
    '''Returns a random number.'''
    return random.randrange(0, n)

def clamp(n, min_n, max_n):
    '''Clamps the value into a given interval.'''
    if(n < min_n):
        return min_n
    elif(n >= max_n):
        return max_n - 1
    else:
        return n

def sIfPlural(n):
    '''Returns s if n is not 1'''
    if n == 1:
        return ''
    else:
         return 's'

def inGrid(x, y, width, height):
    '''Checks if a coordinate is in a grid of dimension width x height'''
    return not ((0 > x or x >= width) or (0 > y or y >= height))

def print_info(message):
    '''Prints infos'''
    print('Info: ' + message)

def print_error(message):
    '''Prints error'''
    print('Error: ' + message)

def exit_error(message):
    '''Exits with error'''
    sys.exit('Error: ' + message)

ANSI_RESET = "\u001B[0m"
ANSI_BOLD = "\u001b[1m"
ANSI_RED = "\u001b[31m"
ANSI_RED_BOLD = "\u001b[1m\u001b[31m"
ANSI_1 = "\u001b[38;5;120m"
ANSI_2 = "\u001b[38;5;122m"
ANSI_3 = "\u001b[38;5;147m"
ANSI_4 = "\u001b[38;5;211m"
ANSI_5 = "\u001b[38;5;168m"
ANSI_6 = "\u001b[38;5;127m"
ANSI_7 = "\u001b[38;5;125m"
ANSI_8 = "\u001b[38;5;160m"
ANSI_GRAY_BACKGROUND = "\u001b[48;5;241m"
ANSI_DARK_BACKGROUND = "\u001b[48;5;235m"

COLORS = {
    'select': ANSI_GRAY_BACKGROUND,
    'undiscovered': ANSI_DARK_BACKGROUND,
    'bomb': ANSI_RED_BOLD,
    '1': ANSI_1,
    '2': ANSI_2,
    '3': ANSI_3,
    '4': ANSI_4,
    '5': ANSI_5,
    '6': ANSI_6,
    '7': ANSI_7,
    '8': ANSI_8,
    'reset': ANSI_RESET
}

def flush_input():
    '''Flushes input'''
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def secondsBetweenTimeStamps(ts1, ts2):
    '''Returns the number of seconds between 2 timestamps'''
    if ts1 > ts2:
        exit_error('Wrong timestamp ordering.')

    return int(ts2 - ts1)