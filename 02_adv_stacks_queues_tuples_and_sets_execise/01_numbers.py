first_set = set([int(num) for num in input().split()])
second_set = set([int(num) for num in input().split()])
n = int(input())

for _ in range(n):
    line = input().split()
    command = f'{line[0]} {line[1]}'

    numbers = []
    if len(line) > 2:
        numbers = [int(num) for num in line[2:]]

    if command == 'Add First':
        first_set.update(numbers)

    elif command == 'Add Second':
        second_set.update(numbers)

    elif command == 'Remove First':
        first_set.difference_update(numbers)

    elif command == 'Remove Second':
        second_set.difference_update(numbers)

    elif command == 'Check Subset':
        is_subset = first_set > second_set or first_set < second_set
        print(is_subset)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
