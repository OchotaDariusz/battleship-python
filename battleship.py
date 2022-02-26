import display
import utils


def main():
    player_1_board, player_2_board = utils.setup_game()
    utils.console_clear()
    display.print_board(player_1_board, player_2_board)
    player_1_ships, player_2_ships, p1_disallowed_fields, p2_disallowed_fields = utils.setup_ships()
    player_1_hitboard = utils.create_hitboard(player_1_ships)  # if len hitboard == 0 loose / other player wins
    player_2_hitboard = utils.create_hitboard(player_2_ships)
    print("Player 1 ships:", player_1_ships)
    print("Player 1 disallowed fields:", p1_disallowed_fields)
    print("Player 1 hitboard:", player_1_hitboard)

    print("Player 2 ships:", player_2_ships)
    print("Player 2 disallowed fields:", p2_disallowed_fields)
    print("Player 2 hitboard:", player_2_hitboard)

    while len(player_1_hitboard) != 0 or len(player_2_hitboard) != 0:
        print("Player 2 hitboard:", player_2_hitboard)
        print("Player 1 shooting phase!")
        shooting_phase(player_2_hitboard)

        if len(player_2_hitboard) == 0:
            print("Player 1 wins!")
            break

        print("Player 1 hitboard:", player_1_hitboard)
        print("Player 2 shooting phase!")
        shooting_phase(player_1_hitboard)

        if len(player_1_hitboard) == 0:
            print("Player 2 wins!")
            break


def shooting_phase(player_hitboard: list):
    hit_combo = True
    while hit_combo is True:
        if len(player_hitboard) == 0:
            break
        inputs = list()
        row, col = utils.get_input()
        inputs.append(row)
        inputs.append(col)
        if inputs in player_hitboard:
            print("You've hit a ship!")
            for index in range(len(player_hitboard)):
                if player_hitboard[index] == inputs:
                    player_hitboard.pop(index)
                    break
            hit_combo = True
        else:
            print("You've missed!")
            hit_combo = False


if __name__ == "__main__":
    utils.console_clear()
    main()
