rows, columns = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

SEARCHED_MATRIX_SIZE = 3
max_sum = float('-inf')
max_start_row = 0
max_start_col = 0

for row in range(rows - SEARCHED_MATRIX_SIZE + 1):
    for col in range(columns - SEARCHED_MATRIX_SIZE + 1):

        current_sum = 0

        for r in range(row, SEARCHED_MATRIX_SIZE + row):
            for c in range(col, SEARCHED_MATRIX_SIZE + col):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_start_row = row
            max_start_col = col

max_matrix = [[str(matrix[r][c]) for c in range(max_start_col, max_start_col + SEARCHED_MATRIX_SIZE)] for r in range(max_start_row, max_start_row + SEARCHED_MATRIX_SIZE)]

print(f'Sum = {max_sum}')

# for r in range(max_start_row, max_start_row + SEARCHED_MATRIX_SIZE):
#     for c in range(max_start_col, max_start_col + SEARCHED_MATRIX_SIZE):
#         print(matrix[r][c], end=' ')
#     print()

[print(' '.join(row)) for row in max_matrix]
