def naughty_or_nice_list(kids: list, *args, **kwargs):
    found_kids = {'Nice': [], 'Naughty': []}

    def search_from_args():
        for item in args:
            found = []
            item = item.split('-')
            num = int(item[0])
            command = item[1]

            for value, name in kids:
                if num == value:
                    found.append((value, name))

            if len(found) == 1:
                found_kids[command].append(found[0][1])
                kids.remove(found[0])

    def search_from_kwargs():
        for name, command in kwargs.items():
            found = []
            for value, kid in kids:
                if name == kid:
                    found.append((value, name))

            if len(found) == 1:
                found_kids[command].append(found[0][1])
                kids.remove(found[0])

    search_from_args()
    search_from_kwargs()

    not_found = [name for num, name in kids]
    result = []

    if found_kids["Nice"]:
        result.append(f'Nice: {", ".join(found_kids["Nice"])}')
    if found_kids["Naughty"]:
        result.append(f'Naughty: {", ".join(found_kids["Naughty"])}')
    if not_found:
        result.append(f'Not found: {", ".join(not_found)}')

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
