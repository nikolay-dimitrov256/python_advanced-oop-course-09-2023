def shop_from_grocery_list(budget: int, grocery_list: list, *products):
    result = ''
    for product, price in products:
        if price > budget:
            break

        if product in grocery_list:
            budget -= price
            grocery_list.remove(product)

    if len(grocery_list) > 0:
        result = f'You did not buy all the products. Missing products: {", ".join(grocery_list)}.'
    else:
        result = f'Shopping is successful. Remaining budget: {budget:.2f}.'

    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))