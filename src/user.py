from src.logger import Logger

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logger = Logger(__name__)

    def greet(self):
        self.logger.info('Greeting user')
        return f'Hello, {self.name}'
