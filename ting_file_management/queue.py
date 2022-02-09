from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return (
            self.queue.popleft()
        )  # https://pythontic.com/containers/deque/popleft

    def search(self, index):
        if 0 <= index <= self.__len__() - 1:
            return self.queue[index]
        else:
            raise IndexError
