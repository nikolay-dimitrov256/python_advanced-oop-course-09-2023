SIZE = 6

board = [input().split() for _ in range(SIZE)]

total_points = 0

for _ in range(3):
    line = input().split(', ')
    row = int(line[0][1:])
    col = int(line[1][:-1])

    if row in range(SIZE) and col in range(SIZE) and board[row][col] == 'B':
        points = 0
        for i in range(SIZE):
            if board[i][col].isdigit():
                points += int(board[i][col])

        total_points += points
        board[row][col] = 'b'

if total_points >= 100:
    prize = ''
    if total_points in range(100, 200):
        prize = 'Football'
    elif total_points in range(200, 300):
        prize = 'Teddy Bear'
    else:
        prize = 'Lego Construction Set'

    print(f"Good job! You scored {total_points} points, and you've won {prize}.")

else:
    points_needed = 100 - total_points
    print(f"Sorry! You need {points_needed} points more to win a prize.")
