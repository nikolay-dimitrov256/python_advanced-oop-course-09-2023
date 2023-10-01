rows, columns = [int(num) for num in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())

current_row = 0
current_col = 0
last_row = 0
last_col = 0
won = False
dead = False
move_character = {
    'L': lambda r, c: [r, c - 1],
    'R': lambda r, c: [r, c + 1],
    'U': lambda r, c: [r - 1, c],
    'D': lambda r, c: [r + 1, c]
}


def bunnies_positions():
    bunnies = []

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 'B':
                bunnies.append([r, c])

    return bunnies


def mutate_bunnies(bunnies: list):
    for r, c in bunnies:
        for direction, movement in move_character.items():
            new_r, new_c = movement(r, c)

            if new_r in range(rows) and new_c in range(columns):
                matrix[new_r][new_c] = 'B'


for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == 'P':
            current_row = row
            current_col = col
            matrix[row][col] = '.'
            break

for i in range(len(commands)):
    next_row, next_col = move_character[commands[i]](current_row, current_col)
    if next_row not in range(rows) or next_col not in range(columns):
        last_row = current_row
        last_col = current_col
        won = True

    current_row, current_col = next_row, next_col

    if not won and matrix[current_row][current_col] == 'B':
        dead = True

    mutate_bunnies(bunnies_positions())

    if not won and matrix[current_row][current_col] == 'B':
        dead = True

    if won or dead:
        break

[print(''.join(chars)) for chars in matrix]
if won:
    print(f'won: {last_row} {last_col}')
elif dead:
    print(f'dead: {current_row} {current_col}')
