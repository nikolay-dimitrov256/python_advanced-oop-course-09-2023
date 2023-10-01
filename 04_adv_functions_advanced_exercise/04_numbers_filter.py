def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'even':
            kwargs['even'] = list(filter(lambda x: x % 2 == 0, value))
        elif key == 'odd':
            kwargs['odd'] = list(filter(lambda x: x % 2 != 0, value))

    kwargs = dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))

    return kwargs


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print()

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
