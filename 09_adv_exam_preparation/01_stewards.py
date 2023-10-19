from collections import deque

seats = input().split(', ')
first_queue = deque(int(num) for num in input().split(', '))
second_queue = deque(int(num) for num in input().split(', '))

rotations = 0
matched_seats = []

while rotations < 10 and len(matched_seats) < 3:
    first_num = first_queue.popleft()
    second_num = second_queue.pop()
    character = chr(first_num + second_num)

    combination_1 = f'{first_num}{character}'
    combination_2 = f'{second_num}{character}'

    if combination_1 in seats:
        if combination_1 not in matched_seats:
            matched_seats.append(combination_1)

    elif combination_2 in seats:
        if combination_2 not in matched_seats:
            matched_seats.append(combination_2)

    else:
        first_queue.append(first_num)
        second_queue.appendleft(second_num)

    rotations += 1

print(f'Seat matches: {", ".join(matched_seats)}')
print(f'Rotations count: {rotations}')
