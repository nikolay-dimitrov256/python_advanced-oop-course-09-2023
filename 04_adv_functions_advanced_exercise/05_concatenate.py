def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, kwargs[key])

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print()
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
