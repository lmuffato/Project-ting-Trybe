class Queue:
    def __init__(self):
        self.list = list()

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        return self.list.pop(0)

    def search(self, index):
        value = self.list[index]
        if not value or index < 0:
            raise IndexError
        return value
