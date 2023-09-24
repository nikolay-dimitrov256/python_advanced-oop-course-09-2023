size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]
bombs = input().split()

for bomb in bombs:
    if not matrix:
        break
    bomb_row, bomb_col = [int(num) for num in bomb.split(',')]
    bomb_value = matrix[bomb_row][bomb_col]

    if bomb_value <= 0:
        continue

    start_row, start_col = bomb_row - 1, bomb_col -1
    if start_row < 0:
        start_row = 0
    if start_col < 0:
        start_col = 0

    for r in range(start_row, bomb_row + 2):
        for c in range(start_col, bomb_col + 2):
            if r in range(size) and c in range(size):
                if matrix[r][c] > 0:
                    matrix[r][c] -= bomb_value

alive_cells = 0
sum_cells = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_cells += matrix[row][col]

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_cells}')
[print(' '.join([str(num) for num in current_row])) for current_row in matrix]
