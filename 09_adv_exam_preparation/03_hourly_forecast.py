def forecast(*args):
    locations = {}
    weather_types = {'Sunny': 1, 'Cloudy': 2, 'Rainy': 3}

    for location, weather in args:
        locations[location] = [weather, weather_types[weather]]

    locations = sorted(locations.items(), key=lambda kvp: (kvp[1][1], kvp[0]))
    result = []

    for city, data in locations:
        result.append(f'{city} - {data[0]}')

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
