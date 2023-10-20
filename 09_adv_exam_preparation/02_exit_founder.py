SIZE = 6

first, second = input().split(', ')
maze = [input().split() for _ in range(SIZE)]

player = 1
rest_players = {first: False, second: False}

while True:
    current_player = first if player % 2 == 1 else second
    coordinates = input()
    row = int(coordinates[1])
    col = int(coordinates[4])

    if rest_players[current_player]:
        rest_players[current_player] = False
        player += 1
        continue

    if maze[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif maze[row][col] == 'T':
        winner = first if current_player == second else second
        print(f"{current_player} is out of the game! The winner is {winner}.")
        break

    elif maze[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        rest_players[current_player] = True

    player += 1
