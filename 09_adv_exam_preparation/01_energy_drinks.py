from collections import deque

caffeine_stack = [int(num) for num in input().split(', ')]
drinks_queue = deque(int(num) for num in input().split(', '))

total_caffeine = 0

while caffeine_stack and drinks_queue:
    caffeine = caffeine_stack.pop()
    drink = drinks_queue.popleft()
    result = caffeine * drink

    if total_caffeine + result > 300:
        drinks_queue.append(drink)
        total_caffeine -= 30

        if total_caffeine < 0:
            total_caffeine = 0

    else:
        total_caffeine += result

if drinks_queue:
    print(f'Drinks left: {", ".join(str(x) for x in drinks_queue)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')
