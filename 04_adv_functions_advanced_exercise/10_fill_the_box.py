def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    box_volume = height * length * width
    cubes_left = 0

    for i in range(3, len(args) - 1):
        cubes = args[i]
        if cubes == 'Finish':
            break

        if cubes < box_volume:
            box_volume -= cubes
        elif cubes == box_volume:
            box_volume -= cubes
            cubes_left = sum([args[j] for j in range(i+1, len(args)) if args[j] != 'Finish'])
            break
        else:
            cubes_left = (cubes - box_volume) + sum([args[j] for j in range(i+1, len(args)) if args[j] != 'Finish'])
            box_volume = 0
            break

    if box_volume == 0:
        return f'No more free space! You have {cubes_left} more cubes.'

    return f'There is free space in the box. You could put {box_volume} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
