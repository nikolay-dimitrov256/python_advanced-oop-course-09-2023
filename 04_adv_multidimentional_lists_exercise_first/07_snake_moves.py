from collections import deque

rows, columns = [int(num) for num in input().split()]
text = deque(input())
index = 0

matrix = []

for row in range(rows):
    current_row = []

    for col in range(columns):
        letter = text.popleft()
        current_row.append(letter)
        text.append(letter)

    if row % 2 != 0:
        current_row = current_row[::-1]

    matrix.append(current_row)

[print(''.join(row)) for row in matrix]
