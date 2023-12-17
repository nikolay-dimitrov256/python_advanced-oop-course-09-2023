from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    @staticmethod
    def find_user_by_name(username: str, collection: List[User]):
        return next((u for u in collection if u.username == username), None)

    @staticmethod
    def find_movie_by_title(title, collection: List[Movie]):
        return next((m for m in collection if m.title == title), None)

    def register_user(self, username: str, age: int):
        if self.find_user_by_name(username, self.users_collection):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username, self.users_collection)

        if user is None:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if self.find_movie_by_title(movie.title, self.movies_collection):
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.find_user_by_name(username, self.users_collection)

        if not self.find_movie_by_title(movie.title, self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, value in kwargs.items():
            setattr(movie, attribute, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username, self.users_collection)

        if not self.find_movie_by_title(movie.title, self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username, self.users_collection)

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if self.find_movie_by_title(movie.title, user.movies_liked):
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user_by_name(username, self.users_collection)

        if not self.find_movie_by_title(movie.title, user.movies_liked):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = [m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]

        return "\n".join(result)

    def __str__(self):
        users = ", ".join([u.username for u in self.users_collection]) if self.users_collection else "No users."
        movies = ", ".join([m.title for m in self.movies_collection]) if self.movies_collection else "No movies."
        result = f"All users: {users}\nAll movies: {movies}"

        return result
