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
    if len(left_right_d)==1 or len(right_left_d)==1 and game_board[1][1] != 0:
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
