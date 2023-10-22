SIZE = int(input())

matrix = []
ship_position = []

for row in range(SIZE):
    matrix.append(list(input()))
    for col in range(SIZE):
        if matrix[row][col] == 'S':
            ship_position = [row, col]
            matrix[row][col] = '-'

fish_cached = 0
whirlpool = False
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    current_row, current_col = ship_position

    command = input()
    if command == 'collect the nets':
        break

    current_row += directions_mapper[command][0]
    current_col += directions_mapper[command][1]

    if current_row < 0:
        current_row = SIZE - 1
    elif current_row == SIZE:
        current_row = 0
    elif current_col < 0:
        current_col = SIZE - 1
    elif current_col == SIZE:
        current_col = 0

    ship_position = [current_row, current_col]

    if matrix[current_row][current_col].isdigit():
        fish_cached += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '-'

    elif matrix[current_row][current_col] == 'W':
        fish_cached = 0
        whirlpool = True
        break

matrix[current_row][current_col] = 'S'

if whirlpool:
    print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
          f'Last coordinates of the ship: [{current_row},{current_col}]')
else:
    if fish_cached >= 20:
        print('Success! You managed to reach the quota!')
    else:
        needed_fish = 20 - fish_cached
        print(f"You didn't catch enough fish and didn't reach the quota! You need {needed_fish} tons of fish more.")

    if fish_cached > 0:
        print(f'Amount of fish caught: {fish_cached} tons.')

    [print(''.join(row)) for row in matrix]
