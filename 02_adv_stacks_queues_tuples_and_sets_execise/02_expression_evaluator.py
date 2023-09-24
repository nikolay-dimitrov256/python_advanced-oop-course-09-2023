from collections import deque

line = deque(input().split())

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}
numbers_queue = deque()

while line:
    element = line.popleft()

    if element in '+-*/':
        while len(numbers_queue) > 1:
            first_num = numbers_queue.popleft()
            second_num = numbers_queue.popleft()
            result = operators[element](first_num, second_num)
            numbers_queue.appendleft(result)

    else:
        numbers_queue.append(int(element))

print(numbers_queue[0])
