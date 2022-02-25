import display
import utils


def main():
    player_1_board, player_2_board = utils.setup_game()
    utils.console_clear()
    display.print_board(player_1_board, player_2_board)
    player_1_ships, player_2_ships = utils.setup_ships()
    print(player_1_ships)
    print(player_2_ships)


if __name__ == "__main__":
    utils.console_clear()
    main()
