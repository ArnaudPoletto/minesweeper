# Minesweeper
Minesweeper game in Python.

## Start the game
Run
```
  python minesweeper.py --d=<difficulty>
```
, where difficulty in [easy, medium, hard].

Or run
```
  python minesweeper.py --c=w=<width>,h=<height>,b=<#bombs>
```
, which creates a grid of dimensions width x height, containing #bombs bombs.

The parameter ```--ignore_rules=true``` can be added to avoid generating a custom game with general grid rules.
