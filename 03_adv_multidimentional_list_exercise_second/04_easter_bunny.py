size = int(input())

matrix = []
bunny = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
max_direction = ''
eggs_path = []

for direction, value in directions.items():
    current_eggs = 0
    current_path = []
    edge_position = False
    counter = 0
    row, col = bunny
    while True:
        row += directions[direction][0]
        col += directions[direction][1]
        if row not in range(size) or col not in range(size):
            edge_position = True
            break
        elif matrix[row][col] == 'X':
            break
        else:
            current_eggs += int(matrix[row][col])
            current_path.append([row, col])
            counter += 1

    if edge_position and counter == 0:  # the direction has no fields to collect
        continue

    if current_eggs > max_eggs:
        max_direction = direction
        max_eggs = current_eggs
        eggs_path = current_path

print(max_direction)
[print(place) for place in eggs_path]
print(max_eggs)
