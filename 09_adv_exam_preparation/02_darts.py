SIZE = 7

first_player, second_player = input().split(', ')
dartboard = [input().split() for _ in range(SIZE)]

data = {first_player: {'points': 501, 'turns': 0}, second_player: {'points': 501, 'turns': 0}}
player = 1

while True:
    winner = ''
    current_player = first_player if player % 2 == 1 else second_player

    line = input()
    for ch in '()':
        line = line.replace(ch, '')

    row, col = [int(num) for num in line.split(', ')]
    data[current_player]['turns'] += 1

    if row not in range(SIZE) or col not in range(SIZE):
        player += 1
        continue

    if dartboard[row][col].isdigit():
        data[current_player]['points'] -= int(dartboard[row][col])

    elif dartboard[row][col] == 'D':
        points = sum(int(x) for x in [dartboard[row][0], dartboard[row][-1], dartboard[0][col], dartboard[-1][col]]) * 2
        data[current_player]['points'] -= points

    elif dartboard[row][col] == 'T':
        points = sum(int(x) for x in [dartboard[row][0], dartboard[row][-1], dartboard[0][col], dartboard[-1][col]]) * 3
        data[current_player]['points'] -= points

    elif dartboard[row][col] == 'B':
        winner = current_player
        break

    if data[current_player]['points'] <= 0:
        winner = current_player
        break

    player += 1

print(f"{winner} won the game with {data[winner]['turns']} throws!")
