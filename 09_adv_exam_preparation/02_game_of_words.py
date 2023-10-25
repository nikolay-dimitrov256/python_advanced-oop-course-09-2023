string = list(input())
size = int(input())

field = []
player = []
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for r in range(size):
    field.append(list(input()))
    for c in range(size):
        if field[r][c] == 'P':
            player = [r, c]
            field[r][c] = '-'

commands_count = int(input())
row, col = player

for _ in range(commands_count):
    command = input()

    row, col = player

    new_row = row + directions_mapper[command][0]
    new_col = col + directions_mapper[command][1]

    if new_row not in range(size) or new_col not in range(size):
        if string:
            string.pop()

        continue

    row, col = new_row, new_col

    if field[row][col].isalpha():
        string.append(field[row][col])
        field[row][col] = '-'

    player = [row, col]

field[row][col] = 'P'

print(''.join(string))
[print(''.join(row)) for row in field]
