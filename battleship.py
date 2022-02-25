import display
import os
import utils


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    player_1_board, player_2_board = utils.setup_game()
    console_clear()
    display.print_board(player_1_board, player_2_board)


if __name__ == "__main__":
    console_clear()
    main()
