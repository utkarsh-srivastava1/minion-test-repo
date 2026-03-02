from src.logger import Logger

class HashMap:
    def __init__(self):
        self.map = {}
        self.logger = Logger(__name__)

    def get(self, key):
        self.logger.info(f'Getting value for key: {key}')
        return self.map.get(key)

    def set(self, key, value):
        self.logger.info(f'Setting value for key: {key}')
        self.map[key] = value
