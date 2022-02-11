class Queue:
    def __init__(self):
        self.queueFifo = list()

    def __len__(self):
        return len(self.queueFifo)

    def enqueue(self, value):
        self.queueFifo.append(value)

    def dequeue(self):
        return self.queueFifo.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.queueFifo[index]
