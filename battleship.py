import display
import utils


def main():
    player_1_board, player_2_board, display_p1_board, display_p2_board = utils.setup_game()
    utils.console_clear()
    player_1_ships, player_2_ships, p1_disallowed_fields, p2_disallowed_fields = utils.setup_ships(player_1_board,
                                                                                                   display_p1_board,
                                                                                                   display_p2_board)
    player_1_hitboard = utils.create_hitboard(player_1_ships)  # if len hitboard == 0 loose / other player wins
    player_2_hitboard = utils.create_hitboard(player_2_ships)

    display.print_board(player_1_board, player_2_board)

    print("Player 1 ships:", player_1_ships)
    print("Player 1 disallowed fields:", p1_disallowed_fields)
    print("Player 1 hitboard:", player_1_hitboard)

    print("Player 2 ships:", player_2_ships)
    print("Player 2 disallowed fields:", p2_disallowed_fields)
    print("Player 2 hitboard:", player_2_hitboard)

    p1_sunken_ships, p2_sunken_ships = list(), list()
    p1_hits, p2_hits = list(), list()

    while len(player_1_hitboard) != 0 or len(player_2_hitboard) != 0:  # SHOOTING PHASE
        print("Player 2 hitboard:", player_2_hitboard)
        print("Player 1 shooting phase!")
        shooting_phase(player_2_board,
                       player_1_board,
                       player_2_board,
                       player_2_ships,
                       player_2_hitboard,
                       p2_sunken_ships,
                       p1_hits)

        if len(player_2_hitboard) == 0:
            print("Player 1 wins!")
            break

        print("Player 1 hitboard:", player_1_hitboard)
        print("Player 2 shooting phase!")
        shooting_phase(player_1_board,
                       player_1_board,
                       player_2_board,
                       player_1_ships,
                       player_1_hitboard,
                       p1_sunken_ships,
                       p2_hits)

        if len(player_1_hitboard) == 0:
            print("Player 2 wins!")
            break


def shooting_phase(board: list,
                   player_1_board: list,
                   player_2_board: list,
                   player_ships: list,
                   player_hitboard: list,
                   sunken_ships: list,
                   player_hits: list):
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
            player_hits.append(inputs)
            for index in range(len(player_hitboard)):
                if player_hitboard[index] == inputs:
                    player_hitboard.pop(index)
                    break
            utils.update_board(board, player_ships, "shooting", "H", inputs)
            utils.check_sunken_ships(board, player_ships, sunken_ships, player_hits)  # TODO: it shouldnt count hits but ships
            display.print_board(player_1_board, player_2_board)
            hit_combo = True
        else:
            print("You've missed!")
            utils.update_board(board, player_ships, "shooting", "M", inputs)
            display.print_board(player_1_board, player_2_board)
            hit_combo = False


if __name__ == "__main__":
    utils.console_clear()
    main()
