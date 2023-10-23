from collections import deque

males_stack = [int(el) for el in input().split()]
females_queue = deque(int(el) for el in input().split())

successful_matches = 0

while females_queue and males_stack:
    female = females_queue[0]
    male = males_stack[-1]

    if female <= 0:
        females_queue.popleft()
        continue

    if male <= 0:
        males_stack.pop()
        continue

    if male % 25 == 0:
        males_stack.pop()
        if males_stack:
            males_stack.pop()
        continue

    if female % 25 == 0:
        females_queue.popleft()
        if females_queue:
            females_queue.popleft()
        continue

    if female == male:
        females_queue.popleft()
        males_stack.pop()
        successful_matches += 1

    else:
        females_queue.popleft()
        males_stack[-1] -= 2

print(f'Matches: {successful_matches}')
print('Males left: ', end='')
if males_stack:
    while males_stack:
        end = ', ' if len(males_stack) > 1 else '\n'
        print(males_stack.pop(), end=end)
else:
    print('none')
print('Females left: ', end='')
if females_queue:
    print(*females_queue, sep=', ')
else:
    print('none')
