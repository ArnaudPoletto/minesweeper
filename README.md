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

If you want to create a custom game without following the general grid rules (where the maximum number of bombs is calculated based on grid dimensions), you can add the parameter --ignore_rules=true.
