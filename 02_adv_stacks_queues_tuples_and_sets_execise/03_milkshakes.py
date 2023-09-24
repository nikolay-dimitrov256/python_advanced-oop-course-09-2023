from collections import deque

chocolates = deque([int(num) for num in input().split(', ')])
cups_of_milk = deque([int(num) for num in input().split(', ')])

milkshakes = 0

while True:
    chocolate = chocolates[-1]
    milk = cups_of_milk[0]

    if chocolate > 0 and milk > 0:
        if chocolate == milk:
            chocolates.pop()
            cups_of_milk.popleft()
            milkshakes += 1

        else:
            cups_of_milk.rotate(-1)
            chocolates[-1] -= 5

    else:
        if chocolate <= 0:
            chocolates.pop()
        if milk <= 0:
            cups_of_milk.popleft()

    if milkshakes == 5:
        break

    elif not chocolates or not cups_of_milk:
        break

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print('Chocolate: ', end='')
print(', '.join([str(num) for num in chocolates]) if chocolates else 'empty')

print('Milk: ', end='')
print(', '.join([str(num) for num in cups_of_milk]) if cups_of_milk else 'empty')
