from collections import deque


def move_time(time: list) -> list:
    time[2] += 1
    if time[2] > 59:
        time[1] += 1
        time[2] = 0
    if time[1] > 59:
        time[0] += 1
        time[1] = 0
    if time[0] > 23:
        time[0] = 0

    return time


robots = {}
for r in input().split(';'):
    robot_name, time_needed = r.split('-')
    robots[robot_name] = [int(time_needed), 0]

current_time = [int(num) for num in input().split(':')]

products_queue = deque()

while True:
    product = input()
    if product == 'End':
        break
    products_queue.append(product)

while products_queue:
    current_time = move_time(current_time)
    available_robots_queue = deque()

    for name, data in robots.items():
        robots[name][1] -= 1

        if robots[name][1] <= 0:
            available_robots_queue.append(name)

    if available_robots_queue:
        robot_name = available_robots_queue.popleft()
        current_product = products_queue.popleft()
        print(f"{robot_name} - {current_product} [{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}]")

        robots[robot_name][1] = robots[robot_name][0]

    else:
        products_queue.rotate(-1)
