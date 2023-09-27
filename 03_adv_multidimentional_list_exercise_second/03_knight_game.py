size = int(input())

matrix = []
knights = []
possible_attacks = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
removed_knights = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'K':
            knights.append([row, col])

while True:
    max_knight_attacks = 0
    max_knight_position = []

    for row, col in knights:
        current_knight_attacks = 0

        for attack in possible_attacks:
            new_row = row + attack[0]
            new_col = col + attack[1]

            if new_row in range(size) and new_col in range(size):
                if matrix[new_row][new_col] == 'K':
                    current_knight_attacks += 1

        if current_knight_attacks > max_knight_attacks:
            max_knight_attacks = current_knight_attacks
            max_knight_position = [row, col]

    if max_knight_attacks == 0:
        break

    matrix[max_knight_position[0]][max_knight_position[1]] = '0'
    knights.remove(max_knight_position)
    removed_knights += 1

print(removed_knights)
