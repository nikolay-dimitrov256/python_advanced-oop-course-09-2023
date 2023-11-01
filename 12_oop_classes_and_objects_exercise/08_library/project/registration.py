from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        for u in library.user_records:
            if user.user_id == u.user_id:
                return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for u in library.user_records:
            if user.user_id == u.user_id:
                library.user_records.remove(u)

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for u in library.user_records:
            if u.user_id == user_id:
                if u.username != new_username:
                    if u.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(u.username)
                    u.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
