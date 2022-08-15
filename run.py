import re


def main():
    """
    The beginning of the program
    """
    GameBoard()


class Game:
    def __init__(self):


class GameBoard:
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
