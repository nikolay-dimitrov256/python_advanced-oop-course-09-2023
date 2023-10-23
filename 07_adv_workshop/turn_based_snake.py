from collections import deque
import random


def render_matrix():
    [print(f"| {' | '.join(r)} |") for r in matrix]


def render_snake():
    for r, c in snake_fields:
        matrix[r][c] = 'S'


def place_apple():
    r, c = random.choice(list(non_snake_fields))

    matrix[r][c] = 'A'


SIZE = 15

matrix = [[' '] * SIZE for _ in range(SIZE)]
snake = deque([(SIZE // 2 - 1, SIZE // 2), (SIZE // 2, SIZE // 2), (SIZE // 2 + 1, SIZE // 2)])
snake_fields = set(snake)
all_fields = set((r, c) for c in range(SIZE) for r in range(SIZE))
non_snake_fields = all_fields - snake_fields

render_snake()

place_apple()

directions_mapper = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
current_direction = 'u'
score = 0

while True:
    apple_eaten = False
    render_matrix()
    command = input('Enter a direction ["u", "d", "l", "r", or ""]: ')

    if command.lower() in directions_mapper:
        current_direction = command.lower()
    elif command != '':
        continue

    row, col = snake[0]
    row += directions_mapper[current_direction][0]
    col += directions_mapper[current_direction][1]

    # Check if the snake hit a wall
    if row not in range(SIZE) or col not in range(SIZE):
        print('Game Over!')
        break

    elif matrix[row][col] == 'A':
        score += 1
        apple_eaten = True

    # Move the tail of the snake
    if not apple_eaten:
        tail_row, tail_col = snake.pop()
        matrix[tail_row][tail_col] = ' '
        snake_fields.remove((tail_row, tail_col))

    # Check if the snake bit itself
    if (row, col) in snake_fields:
        print('Game Over!')
        break

    # Move the head of the snake
    snake.appendleft((row, col))
    snake_fields.add((row, col))

    render_snake()

    if apple_eaten:
        non_snake_fields = all_fields - snake_fields
        place_apple()

render_matrix()
print(f'Your score: {score}')
