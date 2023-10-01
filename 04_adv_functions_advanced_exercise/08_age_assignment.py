def age_assignment(*args, **kwargs):
    names_ages = {}
    result = ''

    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            names_ages[name] = kwargs[first_letter]

    names_ages = dict(sorted(names_ages.items(), key=lambda kvp: kvp[0]))

    for name, age in names_ages.items():
        result += f'{name} is {age} years old.\n'

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
