"""
Exercise 24

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
"""


def print_horizontal_line(board_size):
    print(" --- " * board_size)


def print_vertical_line(board_size ):
    print("|    " * (board_size + 1))


if __name__ == "__main__":
    size = int(input("Enter number for a n x n board:  "))

    for index in range(size):
        print_horizontal_line(size)
        print_vertical_line(size)
    print_horizontal_line(size)
