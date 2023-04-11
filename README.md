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

## Deployment

This application was deployed on Heroku

The steps for the deployment were as follows:
1. Sign up for Heroku
2. Create a new app from the dashboard
3. Fill in the inital details of the app - name, region
4. Move to the settings of the app and add a config variable key and value pair of: `PORT=8000`
5. From the settings page, add `heroku/python` and `heroku/nodejs` to the list of buildpacks; making sure that they are kept in that order
6. Move to the deployment page of the heroku app's settings, connect the app to my GitHub account and connect it to this repository
7. Make sure that the deployment is based on the `main` branch of the repository and manually deploy the app
8. Make sure that the application was deployed successfully and check and test the application performs as expected

I have chosen to keep the deployment manual
