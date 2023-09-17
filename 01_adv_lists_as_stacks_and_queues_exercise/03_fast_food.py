from collections import deque

food = int(input())
orders = deque([int(num) for num in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order <= food:
        food -= orders.popleft()
    else:
        break

if not orders:
    print('Orders complete')
else:
    print('Orders left:', end='')
    while orders:
        print(f' {orders.popleft()}', end='')
