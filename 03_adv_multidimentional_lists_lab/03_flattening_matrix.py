rows = int(input())

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

flattened_matrix = [num for row in matrix for num in row]

# for row_i in range(rows):
#     row = matrix[row_i]
#     for col_i in range(len(row)):
#         flattened_matrix.append(matrix[row_i][col_i])

# for row in matrix:
#     for num in row:
#         flattened_matrix.append(num)

print(flattened_matrix)
