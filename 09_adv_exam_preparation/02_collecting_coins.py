SIZE = int(input())

field = []
player_position = []

for row in range(SIZE):
    field.append(input().split())
    for col in range(SIZE):
        if field[row][col] == 'P':
            player_position = [row, col]

player_path = [player_position]
total_coins = 0
directions_mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()

    current_row, current_col = player_position
    current_row += directions_mapper[command][0]
    current_col += directions_mapper[command][1]

    if current_row < 0:
        current_row = SIZE - 1
    elif current_row == SIZE:
        current_row = 0
    elif current_col < 0:
        current_col = SIZE - 1
    elif current_col == SIZE:
        current_col = 0

    player_position = [current_row, current_col]
    player_path.append(player_position)

    if field[current_row][current_col].isdigit():
        total_coins += int(field[current_row][current_col])
        field[current_row][current_col] = '*'

        if total_coins >= 100:
            print(f"You won! You've collected {total_coins} coins.")
            break

    elif field[current_row][current_col] == 'X':
        total_coins = int(total_coins / 2)
        print(f"Game over! You've collected {total_coins} coins.")
        break

print("Your path:")
for element in player_path:
    print(element)
