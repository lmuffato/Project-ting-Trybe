from collections import deque


class Queue:
    def __init__(self):
        self.fila = deque([])

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        return self.fila.append(value)

    def dequeue(self):
        return self.fila.popleft()

    def search(self, index):
        if index not in range(len(self.fila)):
            raise IndexError
        return self.fila[index]
