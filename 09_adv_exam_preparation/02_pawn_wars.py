SIZE = 8

board = []
positions = {'w': [], 'b': []}

for row in range(SIZE):
    board.append(input().split())
    for col in range(SIZE):
        if board[row][col] == 'w':
            positions['w'] = [row, col]
        elif board[row][col] == 'b':
            positions['b'] = [row, col]

directions_mapper = {'w': [-1, 0], 'b': [1, 0]}
capture_mapper = {'w': [[-1, -1], [-1, 1]], 'b': [[1, -1], [1, 1]]}
rows_mapper = {i: '87654321'[i] for i in range(8)}
columns_mapper = {i: 'abcdefgh'[i] for i in range(8)}

player = 1
game_over = False

while not game_over:
    pawn = 'w' if player % 2 == 1 else 'b'
    current_row, current_col = positions[pawn]

    for row_move, col_move in capture_mapper[pawn]:
        checked_row = current_row + row_move
        checked_col = current_col + col_move

        if checked_row in range(SIZE) and checked_col in range(SIZE) and board[checked_row][checked_col] != '-':
            winner = 'White' if pawn == 'w' else 'Black'
            square = f'{columns_mapper[checked_col]}{rows_mapper[checked_row]}'
            print(f'Game over! {winner} win, capture on {square}.')
            game_over = True
            break

    if game_over:
        break

    board[current_row][current_col] = '-'
    current_row += directions_mapper[pawn][0]
    current_col += directions_mapper[pawn][1]
    board[current_row][current_col] = pawn
    positions[pawn] = [current_row, current_col]

    if (pawn == 'w' and current_row == 0) or (pawn == 'b' and current_row == 7):
        winner = 'White' if pawn == 'w' else 'Black'
        square = f'{columns_mapper[current_col]}{rows_mapper[current_row]}'
        print(f'Game over! {winner} pawn is promoted to a queen at {square}.')
        game_over = True

    player += 1
