size = int(input())
tracked_car = input()

race_route = []
tunnel = []
total_kilometers = 0
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
row, col = 0, 0

for row_i in range(size):
    race_route.append(input().split())
    for col_i in range(size):
        if race_route[row_i][col_i] == 'T':
            tunnel.append([row_i, col_i])

while True:
    command = input()
    if command == 'End':
        print(f'Racing car {tracked_car} DNF.')
        break

    row += directions_mapper[command][0]
    col += directions_mapper[command][1]

    if race_route[row][col] == '.':
        total_kilometers += 10

    elif race_route[row][col] == 'T':
        entrance_index = tunnel.index([row, col])
        end_index = 0 if entrance_index == 1 else 1
        row, col = tunnel[end_index]
        total_kilometers += 30

        for entrance in tunnel:
            tunnel_row, tunnel_col = entrance
            race_route[tunnel_row][tunnel_col] = '.'

    elif race_route[row][col] == 'F':
        total_kilometers += 10
        print(f'Racing car {tracked_car} finished the stage!')
        break

race_route[row][col] = 'C'

print(f'Distance covered {total_kilometers} km.')
[print(''.join(row)) for row in race_route]
