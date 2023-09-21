rows, columns = [int(num) for num in input().split(', ')]

matrix = []
sum_matrix = 0

for _ in range(rows):
    elements = [int(num) for num in input().split(', ')]
    sum_matrix += sum(elements)
    matrix.append(elements)

print(sum_matrix)
print(matrix)
