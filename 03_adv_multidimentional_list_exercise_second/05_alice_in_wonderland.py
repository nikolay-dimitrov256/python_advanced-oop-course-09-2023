size = int(input())

matrix = []
alice = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            alice = [row, col]
            matrix[row][col] = '*'

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
tea_bags = 0
party = False

while tea_bags < 10:
    command = input()  # 'up', 'down', 'left', or 'right'

    row = alice[0] + directions[command][0]
    col = alice[1] + directions[command][1]

    if row not in range(size) or col not in range(size):
        break
    elif matrix[row][col] == 'R':
        matrix[row][col] = '*'
        break
    elif matrix[row][col].isdigit():
        tea_bags += int(matrix[row][col])

    matrix[row][col] = '*'
    alice = [row, col]
else:
    party = True

if party:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
[print(' '.join(r)) for r in matrix]
