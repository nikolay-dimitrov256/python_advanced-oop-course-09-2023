n = int(input())

stack = []

for _ in range(n):
    command = input()

    if command.startswith('1'):
        number = int(command.split()[1])
        stack.append(number)

    elif command.startswith('2'):
        if stack:
            stack.pop()

    elif command.startswith('3'):
        if stack:
            print(max(stack))

    elif command.startswith('4'):
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(*reversed_stack, sep=', ')
