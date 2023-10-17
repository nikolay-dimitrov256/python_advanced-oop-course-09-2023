from collections import deque

textiles_queue = deque(int(num) for num in input().split())
medicaments_stack = [int(num) for num in input().split()]

healing_items = {30: ['Patch', 0], 40: ['Bandage', 0], 100: ['MedKit', 0]}

while textiles_queue and medicaments_stack:
    textile = textiles_queue.popleft()
    medicament = medicaments_stack.pop()
    result = textile + medicament

    if result in healing_items.keys():
        healing_items[result][1] += 1

    elif result > 100:
        healing_items[100][1] += 1
        result -= 100
        medicaments_stack[-1] += result

    else:
        medicament += 10
        medicaments_stack.append(medicament)

if not textiles_queue and not medicaments_stack:
    print('Textiles and medicaments are both empty.')
elif not textiles_queue:
    print('Textiles are empty.')
elif not medicaments_stack:
    print('Medicaments are empty.')

for item, count in sorted(healing_items.values(), key=lambda x: (-x[1], x[0])):
    if count == 0:
        break
    print(f'{item} - {count}')

if medicaments_stack:
    print('Medicaments left: ', end='')

    while medicaments_stack:
        ending = ', ' if len(medicaments_stack) > 1 else ''
        print(medicaments_stack.pop(), end=ending)
elif textiles_queue:
    print('Textiles left: ', end='')
    print(*textiles_queue, sep=', ')
