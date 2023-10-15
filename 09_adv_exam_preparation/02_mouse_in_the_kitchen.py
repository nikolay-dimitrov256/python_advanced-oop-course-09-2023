def load_cupboard():
    matrix = []
    mouse_position = []
    cheese_pieces = 0
    for row in range(rows):
        matrix.append(list(input()))
        for col in range(columns):
            if matrix[row][col] == "M":
                mouse_position = [row, col]
                matrix[row][col] = '*'
            elif matrix[row][col] == 'C':
                cheese_pieces += 1

    return matrix, mouse_position, cheese_pieces


def move_mouse(matrix: list, starting_position: list, cheese_pieces: int):
    current_row, current_col = starting_position
    directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    while True:
        command = input()
        if command == 'danger':
            print('Mouse will come back later!')
            break

        next_row = current_row + directions_mapper[command][0]
        next_col = current_col + directions_mapper[command][1]

        if next_row not in range(rows) or next_col not in range(columns):
            print('No more cheese for tonight!')
            break

        elif matrix[next_row][next_col] == '@':
            continue

        current_row, current_col = next_row, next_col

        if matrix[current_row][current_col] == 'C':
            cheese_pieces -= 1
            matrix[current_row][current_col] = '*'

            if cheese_pieces == 0:
                print('Happy mouse! All the cheese is eaten, good night!')
                break

        elif matrix[current_row][current_col] == 'T':
            print('Mouse is trapped!')
            break

    matrix[current_row][current_col] = 'M'


rows, columns = [int(num) for num in input().split(',')]

cupboard, start_position, cheese = load_cupboard()

move_mouse(cupboard, start_position, cheese)

[print(''.join(row)) for row in cupboard]
