class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data = [*self.data, value]

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if len(self) < abs(index) + 1:
            raise IndexError()

        return self.data[index]
