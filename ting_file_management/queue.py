class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        deleted = self.data[0]
        self.data.pop(0)
        return deleted

    def search(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError
