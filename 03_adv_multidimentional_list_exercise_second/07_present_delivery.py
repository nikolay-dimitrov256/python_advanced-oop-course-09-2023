presents_count = int(input())
size = int(input())

matrix = []
santa = []
nice_kids_count = 0
nice_kids_with_present = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            santa = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids_count += 1

while True:
    if presents_count == 0:
        break

    command = input()
    if command == 'Christmas morning':
        break

    r, c = santa
    new_r = r + directions[command][0]
    new_c = c + directions[command][1]

    if new_r not in range(size) or new_c not in range(size):
        continue

    matrix[r][c] = '-'
    r, c = new_r, new_c
    santa = [r, c]
    field = matrix[r][c]

    if field == 'V':
        presents_count -= 1
        nice_kids_with_present += 1

    elif field == 'C':
        for move in directions.values():
            new_r = r + move[0]
            new_c = c + move[1]

            if matrix[new_r][new_c] == 'V':
                presents_count -= 1
                nice_kids_with_present += 1
            elif matrix[new_r][new_c] == 'X':
                presents_count -= 1

            matrix[new_r][new_c] = '-'
            if presents_count == 0:
                break

    matrix[r][c] = 'S'

if presents_count == 0 and nice_kids_with_present < nice_kids_count:
    print('Santa ran out of presents!')

[print(' '.join(row)) for row in matrix]

if nice_kids_with_present == nice_kids_count:
    print(f'Good job, Santa! {nice_kids_count} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_count - nice_kids_with_present} nice kid/s.')
