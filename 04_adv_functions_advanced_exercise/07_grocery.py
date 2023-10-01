def grocery_store(**kwargs):
    kwargs = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = ''

    for key, value in kwargs.items():
        result += f'{key}: {value}\n'

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))