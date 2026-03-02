from src.logger import Logger

class Queue:
    def __init__(self):
        self.queue = []
        self.logger = Logger(__name__)

    def enqueue(self, item):
        self.logger.info(f'Enqueuing item: {item}')
        self.queue.append(item)

    def dequeue(self):
        self.logger.info('Dequeueing item')
        if len(self.queue) < 1:
            self.logger.warning('Queue is empty')
            return None
        item = self.queue.pop(0)
        self.logger.info(f'Dequeued item: {item}')
        return item
