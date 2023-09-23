rows, columns = [int(num) for num in input().split()]
matrix = [input().split() for _ in range(rows)]

found_squares = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            found_squares += 1

print(found_squares)
