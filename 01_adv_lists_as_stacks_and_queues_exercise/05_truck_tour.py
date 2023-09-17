from collections import deque

number_of_pumps = int(input())

pumps = deque()
starting_position = 0
stops = 0

for _ in range(number_of_pumps):
    pump_data = dict()
    pump_data['fuel'], pump_data['distance'] = [int(num) for num in input().split()]
    pumps.append(pump_data)

while stops < number_of_pumps:
    truck_fuel = 0

    for i in range(number_of_pumps):
        fuel = pumps[i]['fuel']
        distance_to_next_pump = pumps[i]['distance']
        truck_fuel += fuel

        if truck_fuel < distance_to_next_pump:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        else:
            truck_fuel -= distance_to_next_pump
            stops += 1

print(starting_position)
