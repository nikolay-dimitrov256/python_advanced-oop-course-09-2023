data_stack = input().split('|')

matrix = []

while data_stack:
    row = data_stack.pop().split()
    if row:
        matrix.append(row)

[print(' '.join(row), end=' ') for row in matrix]
