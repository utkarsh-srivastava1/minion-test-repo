class HashMap:
    def __init__(self):
        self.map = {}

    def get(self, key):
        return self.map.get(key)

    def set(self, key, value):
        self.map[key] = value
