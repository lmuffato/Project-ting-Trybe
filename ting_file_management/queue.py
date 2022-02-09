# https://www.geeksforgeeks.org/deque-in-python/
from collections import deque


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = deque()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queue.popleft()

    def search(self, index):
        """Aqui irá sua implementação"""
        if index >= 0:
            return self.queue[index]
        else:
            raise IndexError
