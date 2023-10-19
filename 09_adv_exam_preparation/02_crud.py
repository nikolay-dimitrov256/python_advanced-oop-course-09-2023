def create(matrix_: list, parameters: list, row_: int, col_: int):
    direction, value = parameters
    row_ += directions_mapper[direction][0]
    col_ += directions_mapper[direction][1]

    if matrix_[row_][col_] == '.':
        matrix_[row_][col_] = value

    return row_, col_


def update(matrix_: list, parameters: list, row_: int, col_: int):
    direction, value = parameters
    row_ += directions_mapper[direction][0]
    col_ += directions_mapper[direction][1]

    if matrix_[row_][col_] != '.':
        matrix_[row_][col_] = value

    return row_, col_


def delete(matrix_: list, parameters: list, row_: int, col_: int):
    direction = parameters[0]
    row_ += directions_mapper[direction][0]
    col_ += directions_mapper[direction][1]

    matrix_[row_][col_] = '.'

    return row_, col_


def read(matrix_: list, parameters: list, row_: int, col_: int):
    direction = parameters[0]
    row_ += directions_mapper[direction][0]
    col_ += directions_mapper[direction][1]

    if matrix_[row_][col_] != '.':
        print(matrix_[row_][col_])

    return row_, col_


ROWS = 6
COLUMNS = 6


matrix = [input().split() for _ in range(ROWS)]
staring_position = input()

for bracket in '()':
    staring_position = staring_position.replace(bracket, '')

row, col = [int(num) for num in staring_position.split(', ')]

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
functions_mapper = {'Create': create, 'Update': update, 'Delete': delete, 'Read': read}

while True:
    command, *params = input().split(', ')

    if command == 'Stop':
        break

    row, col = functions_mapper[command](matrix, params, row, col)

[print(' '.join(row)) for row in matrix]
