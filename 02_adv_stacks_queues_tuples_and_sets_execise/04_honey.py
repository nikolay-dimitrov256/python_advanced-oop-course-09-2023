from collections import deque

bees_queue = deque([int(num) for num in input().split()])
nectar_stack = [int(num) for num in input().split()]
operators_queue = deque(input().split())

total_honey = 0
mapper = {'+': lambda a, b: a + b, '-': lambda a, b: abs(a - b), '*': lambda a, b: a * b, '/': lambda a, b: a / b}

while bees_queue and nectar_stack:
    bee_capacity = bees_queue[0]
    nectar = nectar_stack.pop()

    if nectar < bee_capacity:
        continue

    operator = operators_queue.popleft()
    bee_capacity = bees_queue.popleft()

    if nectar == 0:
        continue

    total_honey += mapper[operator](bee_capacity, nectar)

print(f'Total honey made: {total_honey}')
if bees_queue:
    print('Bees left: ', end='')
    print(*bees_queue, sep=', ')
if nectar_stack:
    print('Nectar left: ', end='')
    print(*nectar_stack, sep=', ')
