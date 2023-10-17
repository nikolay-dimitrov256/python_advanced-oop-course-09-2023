from collections import deque

times_queue = deque(int(num) for num in input().split())
tasks_stack = [int(num) for num in input().split()]

duckies = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times_queue and tasks_stack:
    time = times_queue.popleft()
    task = tasks_stack.pop()
    result = time * task

    if result in range(0, 61):
        duckies['Darth Vader Ducky'] += 1
    elif result in range(61, 121):
        duckies['Thor Ducky'] += 1
    elif result in range(121, 181):
        duckies['Big Blue Rubber Ducky'] += 1
    elif result in range(181, 241):
        duckies['Small Yellow Rubber Ducky'] += 1
    else:
        task -= 2
        times_queue.append(time)
        tasks_stack.append(task)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for duck, count in duckies.items():
    print(f'{duck}: {count}')
