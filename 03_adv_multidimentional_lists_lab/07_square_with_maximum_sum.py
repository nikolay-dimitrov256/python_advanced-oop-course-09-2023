rows, columns = [int(num) for num in input().split(', ')]
matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

max_sum = 0
max_matrix = []

for row in range(rows - 1):
    for col in range(columns - 1):

        first_num = matrix[row][col]
        right_num = matrix[row][col+1]
        below_num = matrix[row+1][col]
        diagonal_num = matrix[row+1][col+1]
        current_sum = first_num + right_num + below_num + diagonal_num

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = [[first_num, right_num], [below_num, diagonal_num]]

[print(*row) for row in max_matrix]
print(max_sum)
