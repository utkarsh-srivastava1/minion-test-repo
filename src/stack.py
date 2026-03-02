from src.logger import Logger

class Stack:
    def __init__(self):
        self.items = []
        self.logger = Logger(__name__)

    def push(self, item):
        self.logger.info(f'Pushing item: {item}')
        self.items.append(item)

    def pop(self):
        self.logger.info('Popping item')
        if not self.is_empty():
            item = self.items.pop()
            self.logger.info(f'Popped item: {item}')
            return item
        else:
            self.logger.error('Stack is empty')
            raise IndexError('Cannot pop from an empty stack')

    def peek(self):
        self.logger.info('Peeking item')
        if not self.is_empty():
            item = self.items[-1]
            self.logger.info(f'Peeked item: {item}')
            return item
        else:
            self.logger.error('Stack is empty')
            raise IndexError('Cannot peek an empty stack')

    def is_empty(self):
        self.logger.info('Checking if stack is empty')
        return len(self.items) == 0

    def clear(self):
        self.logger.info('Clearing stack')
        self.items = []
