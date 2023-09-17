from collections import deque

water = int(input())
people = deque()

while True:
    name = input()

    if name == 'Start':
        break
    else:
        people.append(name)

while True:
    command = input().split()

    if command[0] == 'End':
        break

    elif command[0] == 'refill':
        litres_to_fill = int(command[1])
        water += litres_to_fill

    else:
        litres_to_give = int(command[0])
        person_name = people.popleft()

        if litres_to_give <= water:
            print(f'{person_name} got water')
            water -= litres_to_give
        else:
            print(f'{person_name} must wait')

print(f"{water} liters left")
