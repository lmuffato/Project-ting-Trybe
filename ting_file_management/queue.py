class Queue:
    FIRST = 0

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(self.FIRST)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.data[index]
