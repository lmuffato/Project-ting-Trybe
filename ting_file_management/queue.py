class Queue:
    def __init__(self):
        self.queueItems = []

    def __len__(self):
        return len(self.queueItems)

    def enqueue(self, value):
        self.queueItems.append(value)

    def dequeue(self):
        self.queueItems.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError()
        return self.queueItems[index]
