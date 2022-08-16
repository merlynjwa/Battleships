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
        while True:
            input_string = input("Please enter the co-ordinates "
                                 "for your carrier:\n")
            print()
            ship_dict = self.__check_input(input_string)
            if ship_dict:
                ship_dict.update({"size": 5})
                self.__normalise_coords(ship_dict)
                pass
            else:
                print("The input could not be parsed as co-ordinates")
                print("Please try entering the co-ordinates again")
                print()

    def print_shipboard(self):
        """
        Print the current state of the player's board to stdout
        """
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

    def __check_input(self, input_str):
        match = re.match(r"""# Match the letter of the co-ord
                             (?P<horizontal>[a-j])
                             # Match the digit of the co-ord
                             (?P<vertical>10|[1-9])
                             # Allow a comma and whitespace after
                             (,\s*|\s+)
                             # Match the direction of the ship
                             (?P<direction>up?|r(ight)?|d(own)?|l(eft)?)
                             # Allow extra input after the main pattern
                             .*""",
                         input_str, flags=re.I | re.M | re.X)
        if match:
            return match.groupdict()
        else:
            return None

    def __normalise_coords(self, ship_dict):
        ship_dict['horizontal'] = ord(ship_dict['horizontal'].upper()) - 65
        ship_dict['vertical'] = int(ship_dict['vertical']) - 1
        ship_dict['direction'] = ship_dict['direction'][0].upper()
        ship_status = []
        for i in range(0, ship_dict['size']):
            ship_status.append(True)
        ship_dict.update({'status': ship_status})
        ship_dict.update({'coords'}: self.__ship_to_coords(ship_dict))

    def __ship_to_coords(self, ship):
        size = ship['size']
        direction = ship['direction']
        ship_coords = []
        if direction == "U":
            direction_tuple = (0, 1)
        elif direction == "R":
            direction_tuple = (1, 0)
        elif direction == "D":
            direction_tuple = (0, -1)
        elif direction == "L":
            direction_tuple = (-1, 0)
        for i in range(0, size):
            ship_coords.append((ship['horizontal'] + i * direction_tuple[0],
                                ship['vertical'] + i * direction_tuple[1]))
        return ship_coords


main()
