from collections import deque

cups_queue = deque([int(num) for num in input().split()])
bottles_stack = [int(num) for num in input().split()]

wasted_water = 0

while cups_queue and bottles_stack:
    cup_capacity = cups_queue.popleft()

    while cup_capacity > 0 and bottles_stack:
        bottle = bottles_stack.pop()
        cup_capacity -= bottle

        if cup_capacity < 0:
            wasted_water += abs(cup_capacity)

if cups_queue:
    print('Cups: ', end='')
    print(*cups_queue, sep=' ')
else:
    print('Bottles: ', end='')
    while bottles_stack:
        print(bottles_stack.pop(), end=' ')
    print()
print(f'Wasted litters of water: {wasted_water}')
