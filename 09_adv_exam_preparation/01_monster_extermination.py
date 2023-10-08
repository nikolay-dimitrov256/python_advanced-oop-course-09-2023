from collections import deque

monsters_armor = deque([int(num) for num in input().split(',')])
soldier_strikes = [int(num) for num in input().split(',')]

killed_monsters = 0

while monsters_armor and soldier_strikes:
    strike_value = soldier_strikes.pop()

    if strike_value >= monsters_armor[0]:
        strike_value -= monsters_armor[0]
        monsters_armor.popleft()
        if soldier_strikes:
            soldier_strikes[-1] += strike_value
        elif strike_value > 0:
            soldier_strikes.append(strike_value)

        killed_monsters += 1

    else:
        monsters_armor[0] -= strike_value
        monsters_armor.rotate(-1)

if not monsters_armor:
    print('All monsters have been killed!')

if not soldier_strikes:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters}')
