from collections import deque

sequence = deque(input())

opening_brackets = '([{'
closing_brackets = ')]}'
brackets_stack = []
balanced_brackets = True

while sequence:
    bracket = sequence.popleft()

    if bracket in opening_brackets:
        brackets_stack.append(bracket)

    elif bracket in closing_brackets:
        if not brackets_stack:
            balanced_brackets = False
            break

        opening_bracket = brackets_stack.pop()

        if opening_brackets.index(opening_bracket) != closing_brackets.index(bracket):
            balanced_brackets = False
            break

if balanced_brackets:
    print('YES')
else:
    print('NO')
