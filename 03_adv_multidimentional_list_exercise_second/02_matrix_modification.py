rows = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(rows)]

while True:
    command, *params = input().split()
    if command == 'END':
        break

    row, col, value = [int(num) for num in params]

    if row not in range(rows) or col not in range(len(matrix[row])):
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

[print(*row) for row in matrix]
