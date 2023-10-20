from collections import deque

ramen_stack = [int(num) for num in input().split(', ')]
customers_queue = deque(int(num) for num in input().split(', '))

while ramen_stack and customers_queue:
    bowl_ramen = ramen_stack.pop()
    customer = customers_queue.popleft()

    if bowl_ramen < customer:
        customer -= bowl_ramen
        customers_queue.appendleft(customer)

    elif bowl_ramen > customer:
        bowl_ramen -= customer
        ramen_stack.append(bowl_ramen)

if customers_queue:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: ", end='')
    print(*customers_queue, sep=', ')

else:
    print("Great job! You served all the customers.")
    if ramen_stack:
        print("Bowls of ramen left: ", end='')
        print(*ramen_stack, sep=', ')
