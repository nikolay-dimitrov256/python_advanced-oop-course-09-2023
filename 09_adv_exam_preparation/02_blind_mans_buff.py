rows, columns = [int(num) for num in input().split()]

playground = []
staring_position = []

for row in range(rows):
    playground.append(input().split())
    for col in range(columns):
        if playground[row][col] == 'B':
            staring_position = [row, col]

touched_opponents = 0
moves = 0
current_row, current_col = staring_position
mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while touched_opponents < 3:
    command = input()
    if command == 'Finish':
        break

    next_row = current_row + mapper[command][0]
    next_col = current_col + mapper[command][1]

    if next_row not in range(rows) or next_col not in range(columns):
        continue

    elif playground[next_row][next_col] == 'O':
        continue

    current_row, current_col = next_row, next_col
    moves += 1

    if playground[current_row][current_col] == 'P':
        touched_opponents += 1

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves}')
