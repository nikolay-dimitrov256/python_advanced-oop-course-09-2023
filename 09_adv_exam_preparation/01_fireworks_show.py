from collections import deque

firework_effects_queue = deque(int(el) for el in input().split(', '))
explosive_powers_stack = [int(el) for el in input().split(', ')]

fireworks_made = {'Palm': 0, 'Willow': 0, 'Crossette': 0}

while firework_effects_queue and explosive_powers_stack:
    if firework_effects_queue[0] <= 0:
        firework_effects_queue.popleft()
        continue
    if explosive_powers_stack[-1] <= 0:
        explosive_powers_stack.pop()
        continue

    firework_effect = firework_effects_queue.popleft()
    explosive_power = explosive_powers_stack.pop()
    result = firework_effect + explosive_power

    if result % 3 == 0 and result % 5 == 0:
        fireworks_made['Crossette'] += 1

    elif result % 3 == 0:
        fireworks_made['Palm'] += 1

    elif result % 5 == 0:
        fireworks_made['Willow'] += 1

    else:
        firework_effect -= 1
        firework_effects_queue.append(firework_effect)
        explosive_powers_stack.append(explosive_power)

    if all(v >= 3 for v in fireworks_made.values()):
        print('Congrats! You made the perfect firework show!')
        break

else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects_queue:
    print('Firework Effects left: ', end='')
    print(*firework_effects_queue, sep=', ')
if explosive_powers_stack:
    print('Explosive Power left: ', end='')
    print(*explosive_powers_stack, sep=', ')

print(f'Palm Fireworks: {fireworks_made["Palm"]}')
print(f'Willow Fireworks: {fireworks_made["Willow"]}')
print(f'Crossette Fireworks: {fireworks_made["Crossette"]}')
