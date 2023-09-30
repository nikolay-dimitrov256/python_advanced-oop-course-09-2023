from collections import deque

green_light_seconds = int(input())
free_window_seconds = int(input())

cars_queue = deque()
total_cars_passed = 0
no_crash = True
car_name = ''
crash_letter = ''

while no_crash:
    line = input()

    if line == 'END':
        break

    elif line == 'green':
        green_time = green_light_seconds
        yellow_time = free_window_seconds
        car = deque()

        while cars_queue:
            car_name = cars_queue.popleft()
            car = deque(car_name)

            while car and green_time > 0:
                car.popleft()
                green_time -= 1

            if green_time > 0:
                total_cars_passed += 1
                continue

            while car and yellow_time > 0:
                car.popleft()
                yellow_time -= 1

            if car:
                crash_letter = car.popleft()
                no_crash = False
            else:
                total_cars_passed += 1

            break

    else:
        cars_queue.append(line)

if no_crash:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')
else:
    print('A crash happened!')
    print(f'{car_name} was hit at {crash_letter}.')
