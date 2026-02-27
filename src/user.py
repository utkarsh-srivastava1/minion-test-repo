import re

class User:
    def __init__(self, name, email):
        if not self.validate_email(email):
            raise ValueError('Invalid email address')
        self.name = name
        self.email = email

    def greet(self):
        return f'Hello, {self.name}'

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))
