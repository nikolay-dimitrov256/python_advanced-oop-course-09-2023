class ColumnFullError(Exception):
    pass


def print_matrix():
    for row in matrix:
        print(row)


def check_direction(player: int, row: int, col: int, direction: tuple, opposite=False) -> int:
    for i in range(3):
        r_move = direction[0] if not opposite else -direction[0]
        c_move = direction[1] if not opposite else -direction[1]
        row += r_move
        col += c_move

        if not check_field_range(row, col):
            return i
        if matrix[row][col] != player:
            return i

    return 3


def check_field_range(row: int, col: int) -> bool:
    if row in range(ROWS) and col in range(COLUMNS):
        return True
    return False


def winner_check(player: int, row: int, col: int) -> bool:
    for direction in directions:
        line_length = 1
        line_length += check_direction(player, row, col, direction)
        line_length += check_direction(player, row, col, direction, opposite=True)

        if line_length >= 4:
            return True

    return False


def player_move(player: int, column: int):
    if column not in range(COLUMNS):
        raise ValueError

    for row in range(ROWS - 1, -1, -1):
        if matrix[row][column] == 0:
            matrix[row][column] = player
            return row

    else:
        raise ColumnFullError


def base_function():
    player = 1

    while True:
        print_matrix()
        print(f'Player {player}, please choose a column')

        try:
            column = int(input()) - 1
            row = player_move(player, column)
            winner = winner_check(player, row, column)
            if winner:
                print_matrix()
                print(f'The winner is player {player}')
                break

        except ValueError:
            print('Please enter a number 1-7')
            continue

        except ColumnFullError:
            print('This column is full. Please select one with empty slots.')
            continue

        player += 1
        if player % 2 != 0:
            player = 1


ROWS = 6
COLUMNS = 7
matrix = [[0] * COLUMNS for _ in range(ROWS)]
directions = (
    (-1, 0),  # UP
    (-1, -1),  # LEFT UPPER DIAGONAL
    (-1, 1),  # RIGHT UPPER DIAGONAL
    (0, -1)  # LEFT
)

base_function()
