size = int(input())
commands = input().split(', ')

squirrel_position = []
field = []
collected_hazelnuts = 0

for row in range(size):
    field.append(list(input()))
    for col in range(size):
        if field[row][col] == 's':
            squirrel_position = [row, col]

directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
row, col = squirrel_position

for command in commands:
    row += directions_mapper[command][0]
    col += directions_mapper[command][1]

    if row not in range(size) or col not in range(size):
        print('The squirrel is out of the field.')
        break

    elif field[row][col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break

    elif field[row][col] == 'h':
        collected_hazelnuts += 1
        field[row][col] = '*'
        if collected_hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break

else:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {collected_hazelnuts}')
