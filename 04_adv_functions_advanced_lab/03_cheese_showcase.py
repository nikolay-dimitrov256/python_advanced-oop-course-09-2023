def sorting_cheeses(**kwargs):
    sorted_cheeses = dict(sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = ''

    for cheese, pieces in sorted_cheeses.items():
        sorted_pieces = sorted(pieces, reverse=True)
        sorted_pieces = [str(piece) for piece in sorted_pieces]
        sorted_pieces = '\n'.join(sorted_pieces)
        result += f'{cheese}\n{sorted_pieces}\n'

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print()
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)