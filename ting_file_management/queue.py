from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        self.__length = len(self.queue)
        return self.__length

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def search(self, index):
        if index >= 0:
            return self.queue[index]
        else:
            raise IndexError

# Source:
# https://pythontic.com/containers/deque/popleft
# https://pythontic.com/containers/deque/introduction
# https://www.geeksforgeeks.org/deque-in-python/
# https://docs.python.org/3/library/collections.html#collections.deque
