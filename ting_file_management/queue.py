class Queue:
    def __init__(self):
        self.len = 0
        self.list_fifo = []

    def __len__(self):
        return self.len

    def enqueue(self, value):
        self.list_fifo.append(value)
        self.len += 1

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
