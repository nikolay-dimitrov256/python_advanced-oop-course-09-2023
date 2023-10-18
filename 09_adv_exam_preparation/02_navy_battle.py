size = int(input())

field = []
starting_position = []

for row in range(size):
    field.append(list(input()))
    for col in range(size):
        if field[row][col] == 'S':
            starting_position = [row, col]
            field[row][col] = '-'

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
health = 3
BATTLE_CRUISERS = 3
sunken_ships = 0
current_row, current_col = starting_position
mission_accomplished = False

while True:
    command = input()

    current_row += directions_mapper[command][0]
    current_col += directions_mapper[command][1]

    if field[current_row][current_col] == '*':
        field[current_row][current_col] = '-'
        health -= 1

        if health == 0:
            break

    elif field[current_row][current_col] == 'C':
        field[current_row][current_col] = '-'
        sunken_ships += 1

        if sunken_ships == BATTLE_CRUISERS:
            mission_accomplished = True
            break

field[current_row][current_col] = 'S'

if mission_accomplished:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
else:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!')

[print(''.join(row)) for row in field]
