class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) in range(5, 16):
            self.__username = value

        else:
            raise ValueError('The username must be between 5 and 15 characters.')

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        valid_length = len(value) >= 8
        upper_present = any(ch.isupper() for ch in value)
        digit_present = any(ch.isdigit() for ch in value)

        if valid_length and upper_present and digit_present:
            self.__password = value

        else:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
