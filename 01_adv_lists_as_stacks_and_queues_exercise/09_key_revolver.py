from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = [int(num) for num in input().split()]
locks_queue = deque([int(num) for num in input().split()])
intelligence_value = int(input())

while bullets_stack and locks_queue:
    counter = 0

    while counter < barrel_size and bullets_stack and locks_queue:
        bullet = bullets_stack.pop()
        intelligence_value -= bullet_price

        if bullet <= locks_queue[0]:
            locks_queue.popleft()
            print('Bang!')
        else:
            print('Ping!')

        counter += 1

    if bullets_stack and counter == barrel_size:
        print('Reloading!')

if locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value}")
