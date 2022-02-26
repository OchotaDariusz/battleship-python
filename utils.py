import os


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_size_from_input() -> int:
    """Returns value for height and width based on user input"""
    while True:
        value = input("Choose board size (5-10): ")
        if not(value.isdigit()):
            continue
        if 5 <= int(value) <= 10:
            break
        else:
            print("Invalid input! (must be between 5-10)\n")
    return int(value), int(value)


def generate_boards(height: int, width: int) -> list:
    """Generates game board for each player"""
    first_board, second_board = list(), list()
    build_board(height, width, first_board)
    build_board(height, width, second_board)
    return first_board, second_board


def build_board(height: int, width: int, board: list) -> list:
    """Builds board based on height, width and empty list"""
    # for i in range(height):
    #     board.append(['0'])
    # for row in board:
    #     for i in range(width):
    #         row.append(['0'])
    for i in range(height):
        board.append(['0'] * width)
    return board


def setup_game() -> list:
    height, width = get_size_from_input()
    player_1_board, player_2_board = generate_boards(height, width)
    return player_1_board, player_2_board


def setup_ships() -> list:
    ships = {"Big Boat": 3,
         "Medium boat": 2,
         "Small boat": 1}
    # ships = 3
    player_1_ships, player_2_ships = list(), list()
    p1_disallowed_fields, p2_disallowed_fields = list(), list()
    setup_complete = False
    players_done_setup = 0
    while setup_complete is not True:
        # console_clear()
        print("\nPlayer 1 turn")
        for ship in ships:
            player_setup(player_1_ships, p1_disallowed_fields, ships, ship)
        players_done_setup += 1
        # console_clear()
        print("\nPlayer 2 turn")
        # for i in range(ships):
            # player_setup(player_2_ships, p2_disallowed_fields)
        players_done_setup += 1
        if players_done_setup == 2:
            setup_complete = True
    return player_1_ships, player_2_ships, p1_disallowed_fields, p2_disallowed_fields


def player_setup(placed_ships: list, disallowed_fields: list, ships: dict, ship: str):
    if ships[ship] == 1:
        print("Place:", ship)
        while True:
            inputs = list()
            row, col = get_input()
            inputs.append(row)
            inputs.append(col)
            if inputs in disallowed_fields:
                print("Ships are too close!")
                continue
            if inputs in placed_ships:
                print("You've already placed ship on that field!")
                continue
            else:
                update_fields(placed_ships, disallowed_fields, inputs, row, col)
                break
    else:  # TODO: place ships bigger than Small Boat
        print("Place:", ship)


def update_fields(placed_ships, disallowed_fields, inputs, row, col):
    placed_ships.append(inputs)
    disallowed_ = [row + 1, col]
    disallowed_fields.append(disallowed_)
    disallowed_ = [row - 1, col]
    disallowed_fields.append(disallowed_)
    disallowed_ = [row, col + 1]
    disallowed_fields.append(disallowed_)
    disallowed_ = [row, col - 1]
    disallowed_fields.append(disallowed_)


def get_input():
    user_input = input("Select field (ex. B2)").upper()
    row = int(ord(user_input[:1])) - 65
    col = int(user_input[1:]) - 1
    return row, col
