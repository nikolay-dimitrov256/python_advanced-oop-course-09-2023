rows, columns = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

SEARCHED_MATRIX_SIZE = 3
max_sum = float('-inf')
max_start_row = 0
max_start_col = 0

for row in range(rows - SEARCHED_MATRIX_SIZE + 1):
    for col in range(columns - SEARCHED_MATRIX_SIZE + 1):

        for r in range(SEARCHED_MATRIX_SIZE):
            for c in range(SEARCHED_MATRIX_SIZE):
                pass