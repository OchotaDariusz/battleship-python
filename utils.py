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
    for i in range(height):
        board.append(['0'])
    for row in board:
        for i in range(width):
            row.append(['0'])
    return board


def setup_game():
    height, width = get_size_from_input()
    player_1_board, player_2_board = generate_boards(height, width)
    return player_1_board, player_2_board


def setup_ships() -> list:
    ships = 3
    player_1_ships, player_2_ships = list(), list()
    setup_complete = False
    players_done_setup = 0
    while setup_complete is not True:
        print("Player 1 turn")
        for i in range(ships):
            player_setup(player_1_ships)
        players_done_setup += 1
        print("Player 2 turn")
        player_setup(player_2_ships)
        players_done_setup += 1
        if players_done_setup == 2:
            setup_complete = True
    return player_1_ships, player_2_ships


def player_setup(ships: list):
    inputs = list()
    user_input = input("Select field (ex. B2)").upper()
    row = int(ord(user_input[:1])) - 65
    col = int(user_input[1:]) - 1
    inputs.append(row)
    inputs.append(col)
    ships.append(inputs)
