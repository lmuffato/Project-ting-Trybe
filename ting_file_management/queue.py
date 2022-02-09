class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        return self.queue

    def dequeue(self):
        [first, *remainder] = self.queue
        self.queue = remainder
        return first

    def search(self, index):
        if (index < 0) or (index > len(self.queue) - 1):
            raise IndexError('list index out of range')
        else:
            return self.queue[index]
