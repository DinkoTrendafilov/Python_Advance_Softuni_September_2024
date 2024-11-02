def movie_organizer(*args):
    movie_info = {}
    result = ""

    for movie_name, genre in args:
        if genre not in movie_info:
            movie_info[genre] = []
        movie_info[genre].append(movie_name)

    sorted_movie_info = dict(sorted(movie_info.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for (genre, movies) in sorted_movie_info.items():
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result




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
print()