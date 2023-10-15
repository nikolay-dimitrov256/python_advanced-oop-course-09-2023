def accommodate_new_pets(capacity: int, weight_limit: float, *pets):
    accommodated_pets = {}
    for pet_type, weight in pets:
        if capacity == 0:
            result = 'You did not manage to accommodate all pets!'
            break

        if weight > weight_limit:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1
    else:
        result = f'All pets are accommodated! Available capacity: {capacity}.'

    result += '\nAccommodated pets:'
    accommodated_pets = sorted(accommodated_pets.items())

    for pet_type, count in accommodated_pets:
        result += f'\n{pet_type}: {count}'

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
