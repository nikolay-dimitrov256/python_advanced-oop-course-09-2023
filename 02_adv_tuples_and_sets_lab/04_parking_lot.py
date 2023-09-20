n = int(input())

car_numbers = set()

for _ in range(n):
    direction, number = input().split(', ')

    if direction == 'IN':
        car_numbers.add(number)
    elif direction == 'OUT':
        if number in car_numbers:
            car_numbers.remove(number)

if car_numbers:
    print('\n'.join(car_numbers))
else:
    print('Parking Lot is Empty')
