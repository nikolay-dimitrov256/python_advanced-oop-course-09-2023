rows, columns = [int(num) for num in input().split(', ')]

matrix = [[int(num) for num in input().split()] for row in range(rows)]

for col_i in range(columns):
    sum_column = 0

    for row_i in range(rows):
        sum_column += matrix[row_i][col_i]

    print(sum_column)
