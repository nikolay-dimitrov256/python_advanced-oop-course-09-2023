size = int(input())
matrix = [[int(num) for num in input().split(', ')] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_diagonal.append(matrix[row][row])

    col_i_secondary = size - row - 1
    secondary_diagonal.append(matrix[row][col_i_secondary])

print(f'Primary diagonal: {", ".join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
