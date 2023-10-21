from collections import deque


def evaluate_result(number: int) -> str:
    if number < 100:
        return 'under'
    elif 100 <= number < 200:
        return 'Gemstone'
    elif 200 <= number < 300:
        return 'Porcelain Sculpture'
    elif 300 <= number < 400:
        return 'Gold'
    elif 400 <= number < 500:
        return 'Diamond Jewellery'
    else:
        return 'over'


def check_result(presents_dict: dict, product_: str):
    if product_ in presents_dict:
        presents_dict[product_] += 1

    return presents_dict


materials_stack = [int(num) for num in input().split()]
magic_queue = deque(int(num) for num in input().split())

presents_crafted = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials_stack and magic_queue:
    material = materials_stack.pop()
    magic = magic_queue.popleft()
    product = material + magic

    result = evaluate_result(product)

    if result in presents_crafted:
        presents_crafted[result] += 1

    elif result == 'under':
        if product % 2 == 0:
            material *= 2
            magic *= 3
            product = material + magic
            presents_crafted = check_result(presents_crafted, evaluate_result(product))

        else:
            material *= 2
            magic *= 2
            product = material + magic
            presents_crafted = check_result(presents_crafted, evaluate_result(product))

    elif result == 'over':
        material /= 2
        magic /= 2
        product = material + magic
        presents_crafted = check_result(presents_crafted, evaluate_result(product))

if (presents_crafted['Gemstone'] > 0 and presents_crafted['Porcelain Sculpture'] > 0) or \
        (presents_crafted['Gold'] > 0 and presents_crafted['Diamond Jewellery'] > 0):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials_stack:
    print('Materials left: ', end='')
    print(*materials_stack, sep=', ')
if magic_queue:
    print('Magic left: ', end='')
    print(*magic_queue, sep=', ')

for gift, count in sorted(presents_crafted.items()):
    if count > 0:
        print(f'{gift}: {count}')
