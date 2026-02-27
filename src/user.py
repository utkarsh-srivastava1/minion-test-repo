class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f'Hello, {self.name}'
