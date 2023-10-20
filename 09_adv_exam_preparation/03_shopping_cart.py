def shopping_cart(*args):
    meals = {'Soup': [3, []], 'Pizza': [4, []], 'Dessert': [2, []]}
    result = []

    for index, element in enumerate(args):
        if element == 'Stop':
            if index == 0:
                return 'No products in the cart!'
            break

        meal, product = element

        if len(meals[meal][1]) < meals[meal][0] and product not in meals[meal][1]:
            meals[meal][1].append(product)

    meals = sorted(meals.items(), key=lambda kvp: (-len(kvp[1][1]), kvp[0]))

    for dish, data in meals:
        result.append(f'{dish}:')

        for item in sorted(data[1]):
            result.append(f' - {item}')

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
