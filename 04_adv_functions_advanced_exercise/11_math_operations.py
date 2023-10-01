def math_operations(*args, **kwargs):
    result = ''
    index = -1
    while index < len(args):
        for count in range(1, 5):
            index += 1
            if index not in range(len(args)):
                break

            if count == 1:
                kwargs['a'] += args[index]

            elif count == 2:
                kwargs['s'] -= args[index]

            elif count == 3:
                if args[index] == 0:
                    continue
                kwargs['d'] /= args[index]

            elif count == 4:
                kwargs['m'] *= args[index]

    kwargs = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])))

    for key, value in kwargs.items():
        result += f'{key}: {value:.1f}\n'

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
