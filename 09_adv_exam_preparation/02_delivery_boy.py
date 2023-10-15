def load_neighbourhood():
    matrix = []
    boy_position = []
    for row in range(rows):
        matrix.append(list(input()))
        for col in range(columns):
            if matrix[row][col] == 'B':
                boy_position = [row, col]

    return matrix, boy_position


def base_function():
    current_position = starting_position
    pizza_collected = False
    pizza_delivered = False

    while not pizza_delivered:
        current_row, current_col = current_position
        direction = input()
        next_row = current_row + directions_mapper[direction][0]
        next_col = current_col + directions_mapper[direction][1]

        if neighbourhood[current_row][current_col] == '-':
            neighbourhood[current_row][current_col] = '.'

        if next_row not in range(rows) or next_col not in range(columns):
            print('The delivery is late. Order is canceled.')
            neighbourhood[starting_position[0]][starting_position[1]] = ' '
            break

        elif neighbourhood[next_row][next_col] == '*':
            continue

        elif neighbourhood[next_row][next_col] == 'P':
            # if not pizza_collected:
            #     pizza_collected = True
            print('Pizza is collected. 10 minutes for delivery.')
            neighbourhood[next_row][next_col] = 'R'

        elif neighbourhood[next_row][next_col] == 'A':
            # if pizza_collected:
            print('Pizza is delivered on time! Next order...')
            neighbourhood[next_row][next_col] = 'P'
            pizza_delivered = True

        current_position = [next_row, next_col]


rows, columns = [int(num) for num in input().split()]

neighbourhood, starting_position = load_neighbourhood()
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

base_function()

[print(''.join(row)) for row in neighbourhood]
