from collections import deque

orders_queue = deque(int(num) for num in input().split(', '))
employees_stack = [int(num) for num in input().split(', ')]

total_pizza_made = 0

while orders_queue and employees_stack:
    order = orders_queue.popleft()

    if order <= 0 or order > 10:
        continue

    employee_capacity = employees_stack.pop()

    if employee_capacity >= order:
        total_pizza_made += order

    else:
        order -= employee_capacity
        total_pizza_made += employee_capacity
        orders_queue.appendleft(order)

if orders_queue:
    print('Not all orders are completed.')
    print('Orders left: ', end='')
    print(*orders_queue, sep=', ')

else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print('Employees: ', end='')
    print(*employees_stack, sep=', ')
