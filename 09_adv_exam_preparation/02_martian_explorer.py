SIZE = 6

field = []
starting_position = []

for r in range(SIZE):
    field.append(input().split())
    for c in range(SIZE):
        if field[r][c] == 'E':
            starting_position = [r, c]

directions = input().split(', ')

found_resources = {'W': ["Water", 0], 'M': ["Metal", 0], 'C': ["Concrete", 0]}
mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
row, col = starting_position

for command in directions:
    row += mapper[command][0]
    col += mapper[command][1]

    if row < 0:
        row = SIZE - 1
    elif row == SIZE:
        row = 0
    elif col < 0:
        col = SIZE - 1
    elif col == SIZE:
        col = 0

    position_value = field[row][col]

    if position_value == 'R':
        print(f'Rover got broken at ({row}, {col})')
        break

    elif position_value in found_resources:
        print(f'{found_resources[position_value][0]} deposit found at ({row}, {col})')
        found_resources[position_value][1] += 1

if all([value[1] > 0 for value in found_resources.values()]):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
