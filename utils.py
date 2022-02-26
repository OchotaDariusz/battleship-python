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
            correct_pos = True
            inputs = list()
            row, col = get_input()
            inputs.append(row)
            inputs.append(col)
            if inputs in placed_ships or inputs in disallowed_fields:
                print("Ships are too close!")
                correct_pos = False
                continue
            if correct_pos is True:
                update_fields(placed_ships, disallowed_fields, inputs)
                break
    else:
        print("Place:", ship)
        while True:
            correct_pos = True
            all_inputs = list()
            row, col = get_input()
            user_input = input("Horizontal(H) or Vertical(V)?: ").upper()
            if user_input.startswith("H"):
                for i in range(ships[ship]):
                    inputs = list()
                    inputs.append(row)
                    inputs.append(col + i)
                    all_inputs.append(inputs)
            if user_input.startswith("V"):
                for i in range(ships[ship]):
                    inputs = list()
                    inputs.append(row + i)
                    inputs.append(col)
                    all_inputs.append(inputs)
            for boat in range(len(all_inputs)):
                if all_inputs[boat] in placed_ships or all_inputs[boat] in disallowed_fields:
                    print("Ships are too close!")
                    correct_pos = False
                    continue
            if correct_pos is True:
                update_fields(placed_ships, disallowed_fields, all_inputs)
                break


def update_fields(placed_ships, disallowed_fields, inputs):
    placed_ships.append(inputs)
    for index in range(len(placed_ships)):
        if len(placed_ships) == 3:
            break
        else:
            for nested_index in range(len(placed_ships[index])):
                disallowed_ = list()
                disallowed_.append(placed_ships[index][nested_index][0])
                disallowed_.append(placed_ships[index][nested_index][1] + 1)
                if disallowed_ not in disallowed_fields:
                    disallowed_fields.append(disallowed_)
                disallowed_ = list()
                disallowed_.append(placed_ships[index][nested_index][0] + 1)
                disallowed_.append(placed_ships[index][nested_index][1])
                if disallowed_ not in disallowed_fields:
                    disallowed_fields.append(disallowed_)
                disallowed_ = list()
                disallowed_.append(placed_ships[index][nested_index][0])
                disallowed_.append(placed_ships[index][nested_index][1] - 1)
                if disallowed_ not in disallowed_fields:
                    disallowed_fields.append(disallowed_)
                disallowed_ = list()
                disallowed_.append(placed_ships[index][nested_index][0] - 1)
                disallowed_.append(placed_ships[index][nested_index][1])
                if disallowed_ not in disallowed_fields:
                    disallowed_fields.append(disallowed_)


def get_input():
    user_input = input("Select field (ex. B2)").upper()
    row = int(ord(user_input[:1])) - 65
    col = int(user_input[1:]) - 1
    return row, col
