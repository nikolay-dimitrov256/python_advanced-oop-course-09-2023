size = int(input())
commands = input().split()

matrix = []
total_coal = 0
collected_coal = 0
current_row = 0
current_col = 0
game_over = False

directions_validation = {
    'up': lambda r, c: r - 1 in range(size),
    'down': lambda r, c: r + 1 in range(size),
    'left': lambda r, c: c - 1 in range(size),
    'right': lambda r, c: c + 1 in range(size)
}
move_miner = {
    'up': lambda r, c: [r - 1, c],
    'down': lambda r, c: [r + 1, c],
    'left': lambda r, c: [r, c - 1],
    'right': lambda r, c: [r, c + 1]
}

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col
        elif matrix[row][col] == 'c':
            total_coal += 1

for command in commands:
    valid_direction = directions_validation[command](current_row, current_col)
    if valid_direction:
        current_row, current_col = move_miner[command](current_row, current_col)

    if matrix[current_row][current_col] == 'c':
        collected_coal += 1
        matrix[current_row][current_col] = '*'

    elif matrix[current_row][current_col] == 'e':
        game_over = True
        break

    if total_coal == collected_coal:
        break

if game_over:
    print(f'Game over! ({current_row}, {current_col})')
elif collected_coal < total_coal:
    print(f'{total_coal - collected_coal} pieces of coal left. ({current_row}, {current_col})')
else:
    print(f'You collected all coal! ({current_row}, {current_col})')
