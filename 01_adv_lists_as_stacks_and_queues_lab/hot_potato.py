from collections import deque

children = deque(input().split())
tosses_count = int(input()) - 1

while len(children) > 1:
    children.rotate(-tosses_count)
    removed_kid = children.popleft()
    print(f'Removed {removed_kid}')

last_kid = children.popleft()

print(f'Last is {last_kid}')
