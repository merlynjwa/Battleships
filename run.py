import re


def main():
    """
    The beginning of the program
    """
    Game()


class Game:
    """
    The game's main engine.
    Containing all the main opperations and functions for Battleships.
    """
    def __init__(self):
        print("You will now need to enter the co-ordinates for your ships")
        print("The co-ordinates are written in the following format:")
        print()
        print("a10,up")
        print()
        print("The pattern starts with a letter (a - j) (case insensitive)")
        print("it is then followed by a number (1 - 10)")
        print("then an optional comma, with optional whitespace after it")
        print("followed by a direction (up,right,down,left),")
        print("which can be specified by the full word,")
        print("or just the first letter")
        print()
        input("Press enter to continue...\n")
        self.__player = PlayerGameBoard()


class PlayerGameBoard:
    """
    The player's game board.
    Containing all of their ships, where they've fired their missiles,
    and functions to act on the board.
    """
    def __init__(self):
        self.__board = []
        for _ in range(0, 10):
            self.__board.append([" "] * 10)
        self.print_shipboard()

    def print_shipboard(self):
        # Print the header of the board
        print()
        print("   A B C D E F G H I J ")
        print("-----------------------")
        # Use an iterator to print each row of the board
        n = 1
        for i in self.__board:
            print('{0:>2d}'.format(n), "|".join(i), sep="|", end="|\n")
            n = n + 1
        print("-----------------------")
        print()


main()
