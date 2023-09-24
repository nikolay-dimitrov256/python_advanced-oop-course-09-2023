import re

rows, columns = [int(num) for num in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    line = input()
    if line == 'END':
        break

    correct_data = True

    pattern = r'(swap)\s(\d+)\s(\d+)\s(\d+)\s(\d+)'
    match = re.fullmatch(pattern, line)

    if match:
        command, row_1, col_1, row_2, col_2 = match.groups()
        row_1, col_1, row_2, col_2 = int(row_1), int(col_1), int(row_2), int(col_2)

        if row_1 in range(rows) and row_2 in range(rows) and col_1 in range(columns) and col_2 in range(columns):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

        else:
            correct_data = False
    else:
        correct_data = False

    if correct_data:
        [print(' '.join(row)) for row in matrix]
    else:
        print('Invalid input!')
