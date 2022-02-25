import display
import utils


def main():
    player_1_board, player_2_board = utils.setup_game()
    utils.console_clear()
    display.print_board(player_1_board, player_2_board)
    player_1_ships, player_2_ships, p1_disallowed_fields, p2_disallowed_fields = utils.setup_ships()
    print("Player 1 ships:", player_1_ships)
    print("Player 1 disallowed fields:", p1_disallowed_fields)
    print("Player 2 ships:", player_2_ships)
    print("Player 2 disallowed fields:", p2_disallowed_fields)

if __name__ == "__main__":
    utils.console_clear()
    main()
