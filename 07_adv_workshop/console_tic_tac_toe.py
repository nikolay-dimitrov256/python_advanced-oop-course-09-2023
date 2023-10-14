size = 3
board = [[' '] * size for _ in range(size)]


class FieldTakenError(Exception):
    pass


def display_board():
    [print(f'| {" | ".join(row)} |') for row in board]


def numerated_board_display():
    counter = 1
    for row in range(size):
        print('| ', end='')
        for col in range(size):
            print(counter, end=' | ')
            counter += 1
        print()


def validate_choice(current_player_choice):
    current_player_choice = int(current_player_choice) - 1
    if current_player_choice not in range(size ** 2):
        raise ValueError
    row = current_player_choice // size
    col = current_player_choice % size

    if board[row][col] != ' ':
        raise FieldTakenError

    return row, col


def won_by_rows():
    return any([len(set(row)) == 1 and row[0] != ' ' for row in board])


def won_by_columns():
    return any([len(set(row)) == 1 and row[1] != ' ' for row in
                [[board[row_i][col_i] for row_i in range(size)] for col_i in range(size)]])


def won_by_diagonals():
    return any((len(set([board[i][i] for i in range(size)])) == 1 and board[0][0] != ' ',
                len(set([board[i][size - (i + 1)] for i in range(size)])) == 1 and board[0][-1] != ' '))


def game_won_check():
    return any([won_by_rows(), won_by_columns(), won_by_diagonals()])


def draw_by_rows():
    return all(['X' in row and 'O' in row for row in board])


def draw_by_columns():
    return all(['X' in row and 'O' in row for row in
                [[board[row_i][col_i] for row_i in range(size)] for col_i in range(size)]])


def draw_by_diagonals():
    primary_diagonal = [board[row][row] for row in range(size)]
    secondary_diagonal = [board[row][size - (row + 1)] for row in range(size)]
    return (('X' in primary_diagonal and 'O' in primary_diagonal)
            and ('X' in secondary_diagonal and 'O' in secondary_diagonal))


def draw_check():
    return all([draw_by_rows(), draw_by_columns(), draw_by_diagonals()])


player_one = input('Player one name: ')
player_two = input('Player two name: ')
while True:
    player_one_sign = input(f'{player_one}, would you like to play with "X" or "O"? ').upper()
    if player_one_sign in ['X', 'O']:
        break
    else:
        print(f'{player_one}, please chose between "X" and "O"!')

player_two_sign = 'X' if player_one_sign == 'O' else 'O'

print('This is the numeration of the board:')
numerated_board_display()

player = 1

while True:
    current_player = player_one if player % 2 == 1 else player_two
    current_player_sign = player_one_sign if current_player == player_one else player_two_sign

    player_choice = input(f'{current_player} chose a free position [1-{size ** 2}]: ')

    try:
        current_row, current_col = validate_choice(player_choice)
        board[current_row][current_col] = current_player_sign
    except ValueError:
        continue
    except FieldTakenError:
        print('The field is already taken!')
        continue

    display_board()

    if game_won_check():
        print(f'{current_player} won!')
        break

    if draw_check():
        print('Draw!')
        break

    player += 1
