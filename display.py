def print_header(player_board: list):
    print("Player 1", end=" ")
    print(" " * ((len(player_board[0]) * 2) + 2 - len("Player 1")), end=" ")
    print("Player 2")
    print(" " * 2, end="")
    for column in range(len(player_board[0])):
        print(column + 1, end=" ")
    if len(player_board[0]) < 10:
        print(" " * 4, end="")
    else:
        print(" " * 3, end="")
    for column in range(len(player_board[0])):
        if column != len(player_board) - 1:
            print(column + 1, end=" ")
        else:
            print(column + 1)


def print_board(player_1_board: list, player_2_board: list):
    print()
    print_header(player_1_board)
    for row in range(len(player_1_board)):
        print(chr(row+65), end=" ")
        for column in range(len(player_1_board[row])):
            print(player_1_board[row][column][0], end=" ")
        print(" ", end=" ")
        print(chr(row+65), end=" ")
        for column in range(len(player_1_board[row])):
            print(player_2_board[row][column][0], end=" ")
        print()
