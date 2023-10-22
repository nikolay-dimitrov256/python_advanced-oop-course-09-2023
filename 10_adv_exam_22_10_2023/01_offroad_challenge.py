from collections import deque

fuel_stack = [int(el) for el in input().split()]
additional_consumption_queue = deque(int(el) for el in input().split())
needed_fuel_queue = deque(int(el) for el in input().split())

current_altitude = 0
reached_altitudes = []

while fuel_stack and additional_consumption_queue and needed_fuel_queue:
    current_altitude += 1
    current_fuel = fuel_stack.pop()
    additional_consumption = additional_consumption_queue.popleft()
    result = current_fuel - additional_consumption

    if result >= needed_fuel_queue[0]:
        needed_fuel_queue.popleft()
        reached_altitudes.append(f'Altitude {current_altitude}')
        print(f'John has reached: Altitude {current_altitude}')
    else:
        print(f'John did not reach: Altitude {current_altitude}')
        break

if needed_fuel_queue:
    print('John failed to reach the top.')
    if reached_altitudes:
        print(f'Reached altitudes: {", ".join(reached_altitudes)}')
    else:
        print("John didn't reach any altitude.")
else:
    print('John has reached all the altitudes and managed to reach the top!')
