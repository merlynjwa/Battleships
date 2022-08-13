import re


def main():
    """
    The beginning of the program
    """
    print("Please select the co-ordinates for your ships\n"
          "Enter the co-ordinates in the following order:\n"
          "Carrier - 5, Battleship - 4, Cruiser - 3, Submarine - 3, Destroyer - 2\n\n"
          "Here's an example of how the input should be formatted:\n"
          "\"c4,up; a0,right; j9,down; e10,left; h7,down\"\n")
    input_string = input("Enter your ships' co-ordinates:\n")
    match = re.match(r"""([a-j](10|[0-9]),(up?|r(ight)?|d(own)?|l(eft)?);){5}\s*""",
                     input_string,
                     flags=re.I | re.M | re.X)


main()
