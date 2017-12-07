"""
Exercise 26

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]] where a 0 means an empty square, a 1 means that player 1 put their token in
that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column,
or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be
one winner.
"""


def check_game(game_board):
    # row check
    x_win = [1, 1, 1]
    o_win = [2, 2, 2]
    for n in game_board:
        if n == x_win:
            return 1
        elif n == o_win:
            return 2

    # diagonal check
    left_right_d = set([game_board[0][0], game_board[1][1], game_board[2][2]])
    right_left_d = set([game_board[0][2], game_board[1][1], game_board[2][0]])
    if len(left_right_d) == 1 or len(right_left_d) == 1 and game_board[1][1] != 0:
        return game_board[1][1]

    # column check
    for i in range(len(game_board)):
        col = set([game_board[0][i], game_board[1][i], game_board[2][i]])
        if len(col) == 1 and game_board[0][i] != 0:
            return game_board[0][i]

    return 0


# checks
winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1_v2 = [[0, 1, 0],
                  [2, 1, 0],
                  [2, 1, 1]]
print(check_game(winner_is_1_v2))
