# Minesweeper Game in Python

## Introduction

Minesweeper is a classic single-player puzzle game that requires strategic thinking and careful observation. The objective of the game is to clear a rectangular grid containing hidden mines, without detonating any of them. Players can reveal cells on the grid, and each revealed cell will display a number indicating the count of adjacent cells containing mines. By using these numbers as hints, players must deduce the locations of the mines and mark them with flags to ensure safe navigation.

## Getting Started

To start playing Minesweeper, follow these simple steps:

1. Clone the repository or download the minesweeper.py file to your local machine.
2. Open the terminal or command prompt.
3. Navigate to the directory containing minesweeper.py.
4. To play a pre-defined difficulty level, run the following command:
   ```
      python minesweeper.py --d=<difficulty>
   ```
   Replace `<difficulty>` with one of the following options: `easy`, `medium`, or `hard`.
   
   Alternatively, you can create a custom game grid with specific dimensions and a number of bombs using the following command:
   ```
   python minesweeper.py --c w=<width> h=<height> b=<#bombs>
   ```
   Replace `<width>` with the desired width of the grid, `<height>` with the desired height, and `<#bombs>` with the number of bombs you want to place on the grid.
   
   If you want to create a custom game without following the general grid rules (where the maximum number of bombs is calculated based on grid dimensions), you can add the parameter `--ignore_rules=true`.

## How to Play

The objective of Minesweeper is to uncover all the cells on the grid except for the ones containing bombs. Here's how to play:

1. The game begins with a grid of cells, some of which contain hidden bombs.
2. Use the hints provided by the numbers on the revealed cells to deduce the positions of the bombs.
3. Use the arrow keys on the keyboard and press space on the selected cell to reveal it.
4. If the revealed cell contains a bomb, the game is over, and you lose.
5. If the revealed cell is empty (i.e., has no adjacent bombs), all adjacent cells will automatically be revealed. This can trigger a chain reaction of empty cells being revealed.
6. If you believe a cell contains a bomb, you can mark it with a flag by pressing F. Pressing a second time on F will mark it with a question mark. Cells marked with a flag cannot be revealed.
7. Continue revealing cells and marking bombs until all non-bomb cells are uncovered, and you win the game!

## Difficulty Levels

Minesweeper offers three difficulty levels:

* Easy: A small grid with a few bombs, perfect for beginners or quick games.
* Medium: A moderately-sized grid with a moderate number of bombs, offering a balanced challenge.
* Hard: A large grid with a significant number of bombs, suitable for experienced players seeking a real challenge.

## Custom Game

If you want to create a custom game, you can specify the grid's dimensions and the number of bombs. This allows you to tailor the game to your preferences and skill level.

## General Grid Rules

By default, when creating a custom game, Minesweeper follows general grid rules to ensure an appropriate level of difficulty. The number of bombs is calculated based on the grid's dimensions, and it should not exceed the maximum allowed bombs for the given grid size. The minimum grid 
