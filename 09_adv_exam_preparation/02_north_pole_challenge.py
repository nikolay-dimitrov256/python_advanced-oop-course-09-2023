rows, columns = [int(num) for num in input().split(', ')]

workshop = []
starting_position = []
total_items = 0

for row in range(rows):
    workshop.append(input().split())
    for col in range(columns):
        if workshop[row][col] == 'Y':
            starting_position = [row, col]
        elif workshop[row][col] in 'DGC':
            total_items += 1

directions_mapper = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
collected_items = {'decorations': 0, 'gifts': 0, 'cookies': 0}
current_row, current_col = starting_position
merry_christmas = False

while not merry_christmas:
    command, *params = input().split('-')
    if command == 'End':
        break

    steps = int(params[0])

    for _ in range(steps):
        workshop[current_row][current_col] = 'x'
        current_row += directions_mapper[command][0]
        current_col += directions_mapper[command][1]

        if current_row < 0:
            current_row = rows - 1
        elif current_row == rows:
            current_row = 0
        elif current_col < 0:
            current_col = columns - 1
        elif current_col == columns:
            current_col = 0

        if workshop[current_row][current_col] == 'D':
            collected_items['decorations'] += 1

        elif workshop[current_row][current_col] == 'G':
            collected_items['gifts'] += 1

        elif workshop[current_row][current_col] == 'C':
            collected_items['cookies'] += 1

        workshop[current_row][current_col] = 'Y'

        if sum(collected_items.values()) == total_items:
            print('Merry Christmas!')
            merry_christmas = True
            break

print("You've collected:")
print(f"- {collected_items['decorations']} Christmas decorations")
print(f"- {collected_items['gifts']} Gifts")
print(f"- {collected_items['cookies']} Cookies")
[print(" ".join(row)) for row in workshop]
