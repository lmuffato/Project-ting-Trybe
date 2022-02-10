class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if not (0 <= index <= len(self.queue)):
            raise IndexError()
        return self.queue[index]
