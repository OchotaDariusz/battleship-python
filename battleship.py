from distutils.command.build import build
import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_boards(height: int, width: int) -> list:
    """Generates game board for each player"""
    first_board, second_board = list(), list()
    build_board(height, width, first_board)
    build_board(height, width, second_board)
    return first_board, second_board


def build_board(height: int, width: int, board: list) -> list:
    """Builds board based on height, width and empty list"""
    for i in range(height):
        board.append(['0'])
    for row in board:
        for i in range(width):
            row.append(['0'])
    return board


def print_header(player_board: list):
    print("Player 1", end=" ")
    print(" " * ((len(player_board[0]) * 2) - len("Player 1")), end=" ")
    print("Player 2")
    print(" " * 2, end="")
    for column in range(len(player_board[0]) - 1):
        print(column + 1, end=" ")
    if len(player_board[0]) < 10:
        print(" " * 4, end="")
    else:
        print(" " * 3, end="")
    for column in range(len(player_board[0]) - 1):
        if column != len(player_board) - 1:
            print(column + 1, end=" ")
        else:
            print(column + 1)


def print_board(player_1_board: list, player_2_board: list):
    print()
    print_header(player_1_board)
    for row in range(len(player_1_board)):
        print(chr(row+65), end=" ")
        for column in range(len(player_1_board[row]) - 1):
            print(player_1_board[row][column][0], end=" ")
        print(" ", end=" ")
        print(chr(row+65), end=" ")
        for column in range(len(player_1_board[row]) - 1):
            print(player_2_board[row][column][0], end=" ")
        print()


def main():
    height, width = get_size_from_input()
    player_1_board, player_2_board = generate_boards(height, width)
    console_clear()
    print_board(player_1_board, player_2_board)


def get_size_from_input() -> int:
    """Returns value for height and width based on user input"""
    while True:
        value = int(input("Choose board size (5-10): "))
        if 5 <= value <= 10:
            break
        else:
            print("Invalid input! (must be between 5-10)\n")
    return value, value


if __name__ == "__main__":
    console_clear()
    main()
