size = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(size)]

sum_primary_diagonal = 0

for row_i in range(size):
    sum_primary_diagonal += matrix[row_i][row_i]

print(sum_primary_diagonal)
