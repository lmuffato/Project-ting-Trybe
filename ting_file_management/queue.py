class Queue:
    def __init__(self):
        self.queue_value = []

    def __len__(self):
        return len(self.queue_value)

    def enqueue(self, value):
        return self.queue_value.append(value)

    def dequeue(self):
        return self.queue_value.pop(0)

    def search(self, index):
        if index not in range(len(self.queue_value)):
            raise IndexError
        else:
            return self.queue_value[index]
