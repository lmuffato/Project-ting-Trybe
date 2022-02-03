# https://www.tutorialspoint.com/python/python_deque.htm#:~:text=A%20double%2Dended%20queue%2C%20or,be%20invoked%20directly%20with%20arguments.
# https://www.youtube.com/watch?v=RHb-8hXs3HE

from collections import deque


class Queue:
    def __init__(self):
        self.head_value = deque()

    def __len__(self):
        return len(self.head_value)

    def enqueue(self, value):
        return self.head_value.append(value)

    def dequeue(self):
        return self.head_value.popleft()

    def search(self, index):
        if (0 > index or index > self.__len__()):
            raise IndexError
        return self.head_value[index]
