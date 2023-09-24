size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_diagonal.append(matrix[row][row])

    col_i_secondary = size - row - 1
    secondary_diagonal.append(matrix[row][col_i_secondary])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)
