class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Cannot pop from an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Cannot peek an empty stack')

    def is_empty(self):
        return len(self.items) == 0