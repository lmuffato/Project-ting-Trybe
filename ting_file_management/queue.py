class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        value = self.data[0]
        del self.data[0]
        return value

    def search(self, index):
        if (index < 0):
            raise(IndexError)
        return self.data[index]
