from collections import deque

eggs_queue = deque(int(num) for num in input().split(', '))
paper_stack = deque(int(num) for num in input().split(', '))

BOX_SIZE = 50

boxes_filled = 0

while eggs_queue and paper_stack:
    egg = eggs_queue.popleft()
    paper = paper_stack.pop()
    result = egg + paper

    if egg <= 0:
        paper_stack.append(paper)

    elif egg == 13:
        paper_stack.rotate(-1)
        paper_stack.appendleft(paper)

    elif result <= BOX_SIZE:
        boxes_filled += 1

if boxes_filled > 0:
    print(f'Great! You filled {boxes_filled} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_queue:
    print(f'Eggs left: {", ".join([str(num) for num in eggs_queue])}')
if paper_stack:
    print(f'Pieces of paper left: {", ".join([str(num) for num in paper_stack])}')
