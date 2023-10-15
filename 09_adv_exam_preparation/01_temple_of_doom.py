from collections import deque

tools_queue = deque([int(num) for num in input().split()])
substance_stack = [int(num) for num in input().split()]
challenges = [int(num) for num in input().split()]

while substance_stack and challenges:
    tool = tools_queue.popleft()
    substance = substance_stack.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        tools_queue.append(tool)
        substance -= 1
        if substance > 0:
            substance_stack.append(substance)

if not challenges:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')
else:
    print('Harry is lost in the temple. Oblivion awaits him.')

if tools_queue:
    print('Tools: ', end='')
    print(*tools_queue, sep=', ')
if substance_stack:
    print('Substances: ', end='')
    print(*substance_stack, sep=', ')
if challenges:
    print('Challenges: ', end='')
    print(*challenges, sep=', ')
