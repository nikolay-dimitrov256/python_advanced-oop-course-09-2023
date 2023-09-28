size = 5

matrix = []
position = []
total_targets = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            position = [row, col]
            # matrix[row][col] = '.'
        elif matrix[row][col] == 'x':
            total_targets += 1

number_of_commands = int(input())
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
shot_targets = []

for _ in range(number_of_commands):
    command, *params = input().split()

    if command == 'move':
        direction = params[0]
        steps = int(params[1])
        current_row = position[0] + directions[direction][0] * steps
        current_col = position[1] + directions[direction][1] * steps

        if current_row not in range(size) or current_col not in range(size):
            continue
        elif matrix[current_row][current_col] != 'x':
            position = [current_row, current_col]

    elif command == 'shoot':
        direction = params[0]
        current_row = position[0]
        current_col = position[1]
        while True:
            current_row += directions[direction][0]
            current_col += directions[direction][1]

            if current_row not in range(size) or current_col not in range(size):
                break

            elif matrix[current_row][current_col] == 'x':
                matrix[current_row][current_col] = '.'
                shot_targets.append([current_row, current_col])
                break

    if len(shot_targets) == total_targets:
        break

if len(shot_targets) == total_targets:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {total_targets - len(shot_targets)} targets left.')
for target in shot_targets:
    print(target)
