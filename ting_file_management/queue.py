from collections import deque


class Queue:
    def __init__(self):
        self.list = deque()

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        return self.list.append(value)

    def dequeue(self):
        return self.list.popleft()

    def search(self, index):
        if index > self.__len__() or index < 0:
            raise IndexError
        return self.list[index]
