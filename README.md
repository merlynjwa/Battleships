# Battleships

Battleships is a classic boardgame played between two players,
involving each player taking turns to guess the position
of their opponents units.

This is a terminal based implementation of the game.
It is written in Python and runs through Heroku.

## Rules of the game

Battleships is typically played on a 10x10 grid, between two players.

Each player has a set of ships of different sizes available for them to place on this grid.

There are often 5 different classes of ships, with each player having one of each class available to place.
Each class has a distinct size, with each ship only able to be placed on the grid vertically or horizontally.

Each square on the grid can either be empty or occupied, and if occupied, can only be occupied by one ship.

For this game we will be using the following classes with the corresponding sizes:
| Ship Class | Size |
|------------|------|
| Carrier    |   5  |
| Battleship |   4  |
| Cruiser    |   3  |
| Submarine  |   3  |
| Destroyer  |   2  |

At the beginning of a game, each player places all of their ships in secret; each player is unable to view the positions of their opponent's ships.

Once all the ships have been placed, each player takes turns choosing squares on the grid.
When a player chooses a square they provide the coordinates for that square.
If there was a ship on the square chosen, the ship is hit.

If a player can hit all the squares of a ship, that ship is sunk.

If all of a player's ships are sunk, that player loses.

## Credits

### Python

This project makes use of Python.
Python software and documentation is licensed under the [PSF License Agreement](https://docs.python.org/3/license.html#psf-license)

### Code Institute

This project makes use of the Code Institute's Gitpod template.
This template is available [here](https://github.com/Code-Institute-Org/python-essentials-template)
