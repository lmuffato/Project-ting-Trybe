class Queue:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError()
        return self.storage[index]
