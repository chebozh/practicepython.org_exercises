import sys


def new_game():
    global game, count, winner
    game = [["   ", "   ", "   "],
            ["   ", "   ", "   "],
            ["   ", "   ", "   "]]
    count = 0
    winner = None


def choose_player():
    if count % 2 == 0:
        print("It's your turn, Player 1!")
        return "Player 1"
    else:
        print("Now it's your turn, Player 2!")
        return "Player 2"


def ex(x):
    if x.lower() == "exit" or x == "q":
        sys.exit()


def get_input():
    move = input("Where would you like to place your piece? ")
    while True:
        try:
            ex(move)
            move = move.split(",")
            if len(move) != 2:
                print('Invalid move.')
            coordinates = [int(move[0]), int(move[1])]
            if 0 < coordinates[0] < 4 and 0 < coordinates[1] < 4:
                coordinates[0] -= 1
                coordinates[1] -= 1
                coordinates = tuple(coordinates)
                return coordinates
            else:
                int("error")
        except ValueError:
            print("")
            print("Choose a row number and a column number from 1 to 3.")
            move = input("Please input like so: 'Row , Column' ")


def check_legal(x):
    if game[x[0]][x[1]] == "   ":
        global count
        count += 1
        return True
    else:
        print("Please choose an empty spot. ")
        return False


def place_piece(tupl):
    if player_turn == "Player 1":
        game[tupl[0]][tupl[1]] = " x "
    else:
        game[tupl[0]][tupl[1]] = " O "


def draw_board():
    print("")
    for i in range(0, 3):
        print(" --- --- --- ")
        print('|%s|' % '|'.join(map(str, game[i])))
    print(" --- --- --- ")
    print("")


def check_who_won(board):
    if board[0][0] == board[1][1] == board[2][2] == " x " or board[0][-1] == board[1][-2] == board[2][-3] == " x ":
        return 1

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == " x ":
            return 1

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == " x ":
            return 1

    if board[0][0] == board[1][1] == board[2][2] == " O " or board[0][-1] == board[1][-2] == board[2][-3] == " O ":
        return 2

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == " O ":
            return 2

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == " O ":
            return 2


def revanche():
    print("")
    answer = input("Would you like to play again? ")
    ex(answer)
    while not (answer.lower() == "yes" or answer.lower() == "y" or answer.lower() == "no" or answer.lower() == "n"):
        answer = input("Please input 'yes' or 'no'. ")
        ex(answer)
    if "y" in answer.lower():
        return True
    else:
        return False


if __name__ == "__main__":

    running = True

    while running:                              # This while loop makes sure the program keeps running.
        new_game()
        draw_board()
        while count < 9 and winner is None:     # This while-loop covers up each match.
            player_turn = choose_player()
            legal = False
            while legal is False:               # This loop gets the user input for each move.
                global entry
                entry = get_input()
                legal = check_legal(entry)
            place_piece(entry)
            draw_board()
            winner = check_who_won(game)

        if winner is not None:
            input("The winner is Player %s!" % winner)
        else:
            input("It's a draw!")
        running = revanche() # either True or False
