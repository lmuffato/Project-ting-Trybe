class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if self.__len__() - 1 < index or index < 0:
          raise IndexError
        return self.queue[index]
