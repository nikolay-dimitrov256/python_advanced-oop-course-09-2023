def movie_organizer(*args):
    genres = {}

    for movie, genre in args:
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(movie)

    genres = dict(sorted(genres.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = []

    for key, value in genres.items():
        result.append(f'{key} - {len(value)}')
        for movie_name in sorted(value):
            result.append(f'* {movie_name}')

    return '\n'.join(result)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print()
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))