def start_spring(**kwargs):
    spring_types = {}
    result = []

    for spring_object, object_type in kwargs.items():
        if object_type not in spring_types:
            spring_types[object_type] = []
        spring_types[object_type].append(spring_object)

    spring_types = sorted(spring_types.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for key, value in spring_types:
        result.append(f'{key}:')
        for item in sorted(value):
            result.append(f'-{item}')

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
