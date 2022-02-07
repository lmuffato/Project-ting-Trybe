class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        current_out = self.queue[0]
        self.queue.pop(0)
        return current_out

    def search(self, index):
        """Aqui irá sua implementação"""
