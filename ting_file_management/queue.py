class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        first_item = self.data[0]
        self.data.pop(0)
        return first_item

    def search(self, index):
        if index > len(self.data) or index < 0:
            raise IndexError
        return self.data[index]
